#!/usr/bin/env python3
"""Build the processed Lucene dataset used by the Midas experiments.

This script reads the raw Apache Lucene mailing-list archives (``.mbox`` files),
extracts the ``text/plain`` bodies, tokenizes and stems the text, selects the
top-n keywords by document frequency, performs a random split in half into
indexed and non-indexed documents, and writes the four-element dataset consumed
by the experiment scripts.

Use ``--nr-keywords 3000`` for ``Datasets/Lucene_3000.pkl`` and
``--nr-keywords 6000`` for ``Datasets/Lucene_6000.pkl``.

Without ``--seed``, the split uses ``np.random.permutation`` and is therefore
not fixed; re-running this script produces a different (but statistically
equivalent) split.  Pass ``--seed`` to make it reproducible.

The output is a list of four elements:
    [0] dict: keyword -> list of document ids in the indexed half
    [1] dict: keyword -> list of document ids in the non-indexed half
    [2] numpy array: document ids of the indexed half
    [3] numpy array: document ids of the non-indexed half
"""

import argparse
import glob
import mailbox
import multiprocessing
import os
import pickle
from collections import Counter

import numpy as np
import tqdm
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

# Email-header labels that leak into the bodies of quoted or forwarded
# messages; they are structural markers rather than query content.
FIXED_STOPWORDS = {"subject", "cc", "from", "to", "forward"}

_STOPWORDS = None
_STEMMER = None


def get_body(msg):
    """Return the concatenated text/plain body of a mailing-list message."""
    parts = []
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            parts.append(part.get_payload())
    body = "".join(parts)
    # Drop the mailing-list footer.
    body = body.split("To unsubscribe")[0]
    return body


def read_emails(mbox_dir, limit=None):
    """Read all messages from the ``.mbox`` files and return ``{doc_id: body}``."""
    paths = glob.glob(os.path.join(mbox_dir, "*"))
    paths = sorted(p.replace("\\", "/") for p in paths)
    docs = {}
    doc_id = 0
    for path in paths:
        for msg in tqdm.tqdm(mailbox.mbox(path), desc="reading {}".format(os.path.basename(path))):
            docs[doc_id] = get_body(msg)
            doc_id += 1
            if limit is not None and doc_id >= limit:
                return docs
    return docs


def _init_worker():
    global _STOPWORDS, _STEMMER
    from nltk.corpus import stopwords

    _STOPWORDS = set(stopwords.words("english"))
    _STOPWORDS.update(FIXED_STOPWORDS)
    _STEMMER = PorterStemmer()


def _extract_one(item):
    doc_id, text = item
    stems = set()
    for sentence in sent_tokenize(text):
        for word in word_tokenize(sentence):
            lowered = word.lower()
            if lowered not in _STOPWORDS and word.isalpha():
                stems.add(_STEMMER.stem(lowered))
    return doc_id, stems


def extract_stems(docs, workers):
    """Return ``{doc_id: set(stems)}``."""
    items = list(docs.items())
    if workers <= 1:
        _init_worker()
        results = [
            _extract_one(item)
            for item in tqdm.tqdm(items, desc="extracting keywords")
        ]
    else:
        with multiprocessing.Pool(processes=workers, initializer=_init_worker) as pool:
            results = list(tqdm.tqdm(
                pool.imap_unordered(_extract_one, items, chunksize=64),
                total=len(items),
                desc="extracting keywords",
            ))
    return dict(results)


def build_dataset(docs, nr_keywords, seed, workers):
    doc_stems = extract_stems(docs, workers)

    freq = Counter()
    for stems in doc_stems.values():
        freq.update(stems)
    keywords = [word for word, _ in freq.most_common(nr_keywords)]

    rng = np.random.RandomState(seed) if seed is not None else np.random
    n_docs = len(docs)
    perm = rng.permutation(n_docs)
    half = n_docs // 2
    indexed_ids = perm[half:]
    nonindexed_ids = perm[:half]

    indexed = {word: [] for word in keywords}
    nonindexed = {word: [] for word in keywords}

    # Append documents in the order in which they appear in the split.
    for doc_id in indexed_ids:
        for word in doc_stems[doc_id]:
            if word in indexed:
                indexed[word].append(int(doc_id))
    for doc_id in nonindexed_ids:
        for word in doc_stems[doc_id]:
            if word in nonindexed:
                nonindexed[word].append(int(doc_id))

    return [indexed, nonindexed, indexed_ids, nonindexed_ids]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mbox-dir", required=True,
                        help="directory containing the Lucene .mbox files")
    parser.add_argument("--nr-keywords", type=int, default=3000,
                        help="number of keywords to keep (default: 3000)")
    parser.add_argument("--out", default=None,
                        help="output pickle (default: Datasets/Lucene_<n>.pkl)")
    parser.add_argument("--seed", type=int, default=None,
                        help="random seed for the split")
    parser.add_argument("--limit", type=int, default=None,
                        help="use only the first N emails (for quick tests)")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 1,
                        help="number of worker processes (default: CPU count)")
    return parser.parse_args()


def main():
    args = parse_args()
    out = args.out or os.path.join("Datasets", "Lucene_{}.pkl".format(args.nr_keywords))

    docs = read_emails(args.mbox_dir, limit=args.limit)
    dataset = build_dataset(docs, args.nr_keywords, args.seed, args.workers)

    out_dir = os.path.dirname(out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out, "wb") as fh:
        pickle.dump(dataset, fh)
    print("wrote {} ({} documents, {} keywords)".format(out, len(docs), args.nr_keywords))


if __name__ == "__main__":
    main()
