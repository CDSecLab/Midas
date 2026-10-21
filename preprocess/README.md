# Building the processed datasets

This directory contains the scripts that convert the raw Enron and Lucene data into the processed datasets used by the experiments (`Datasets/*.pkl`).

## Scripts

| Script | Input | Default output |
| --- | --- | --- |
| `build_enron_dataset.py` | raw Enron `maildir` | `Datasets/Enron_3000.pkl` |
| `build_lucene_dataset.py` | directory of Lucene `.mbox` files | `Datasets/Lucene_3000.pkl` (or `Lucene_6000.pkl`) |

## Requirements

Besides the main `requirements.txt`, the preprocessing needs NLTK and its tokenizer/stop-word data:

```sh
pip install nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

## Raw data

- **Enron**: the CMU Enron email corpus (<https://www.cs.cmu.edu/~enron/>), extracted so that each user directory contains a `_sent_mail` folder.
- **Lucene**: the Apache Lucene mailing-list archives (<http://mail-archives.apache.org/mod_mbox/lucene-java-user>). The root `README.md` shows how to mirror them with `wget`.

## Usage

```sh
# Enron (3000 keywords)
python preprocess/build_enron_dataset.py --maildir /path/to/maildir --nr-keywords 3000

# Lucene (3000 keywords)
python preprocess/build_lucene_dataset.py --mbox-dir /path/to/apache_ml --nr-keywords 3000

# Lucene with a larger keyword universe
python preprocess/build_lucene_dataset.py --mbox-dir /path/to/apache_ml --nr-keywords 6000
```

Both scripts accept `--out` to override the output path and `--seed` to make the split reproducible.

## Pipeline

The scripts read the raw messages, extract the `text/plain` bodies, tokenize and stem the text, keep the top `--nr-keywords` keywords by document frequency, split the documents in half into an indexed and a non-indexed set, and write the four-element dataset.

## Output format

Each dataset pickle is a list of four elements:

1. `dict`: keyword -> list of document ids in the indexed half
2. `dict`: keyword -> list of document ids in the non-indexed half
3. `numpy.ndarray`: document ids of the indexed half
4. `numpy.ndarray`: document ids of the non-indexed half

The experiment scripts read these files directly; files under `pic_pkl/` are generated at runtime.

## Reproducibility note

Without `--seed`, the split uses `np.random.permutation` and is not fixed, so a regenerated dataset may differ slightly from the provided one. The provided datasets were generated with such a random split, i.e., without a fixed seed. This does not affect the attack's effectiveness, and the provided `Datasets/*.pkl` are the exact inputs used in the paper. Use `--seed` for reproducible future runs.

> **Caution.** By default the scripts write to `Datasets/<name>.pkl`; use `--out` to write elsewhere if you do not want to overwrite the provided datasets.
