# Output files and figure mapping

Every file in this directory is generated at runtime by the experiment
scripts; nothing here is shipped in the repository. Run the experiment
commands from the repository root and the plotting commands from `pic/`.

The output file names below are the exact strings written by the
`pickle.dump` calls in each `*Test.py`.

## Figure 2 — PR

| Run | Output | Plot |
| --- | --- | --- |
| `python3 PRTest.py -d Enron` | `PREnron.pkl` | `python3 PRaPlot.py -d Enron`; `python3 PRbPlot.py -d Enron` |

## Figure 3 — RR

| Run | Output | Plot |
| --- | --- | --- |
| `python3 RRTest.py -d Enron` | `RREnron.pkl` | `python3 RRPlot.py -d Enron` |

## Figure 4 — CR

| Run | Output | Plot |
| --- | --- | --- |
| `python3 CRTest.py -d Enron` | `CRTest_Dsim_5000_count_30_Enron.pkl` | `python3 CRPlot.py -d Enron` |

## Figure 5 — IHOP^M

| Run | Output | Plot |
| --- | --- | --- |
| `python3 ihopMTest.py -d Enron` | `ihopMEnron.pkl` | `python3 ihopMPlot.py -d Enron` |

## Figure 6 — co-absence leakage ablation

| Run | Output | Plot |
| --- | --- | --- |
| `python3 ablationLeakageTest.py -s S1` | `ablationLeakageS1Enron.pkl` | `python3 ablationLeakagePlot.py -s S1` |
| `python3 ablationLeakageTest.py -s S2` | `ablationLeakageS2Enron.pkl` | `python3 ablationLeakagePlot.py -s S2` |

## Figure 7 — iterative refinement ablation

| Run | Output | Plot |
| --- | --- | --- |
| `python3 ablationRRTest.py -s S1` | `ablationRRS1Enron.pkl` | `python3 ablationRRPlot.py -s S1` |
| `python3 ablationRRTest.py -s S2` | `ablationRRS2Enron.pkl` | `python3 ablationRRPlot.py -s S2` |

## Figure 8 — incremental computation

| Run | Output | Plot |
| --- | --- | --- |
| `python3 ablationOptimizeMTest.py` | `ablationOptimizeS1MEnron.pkl` | `python3 ablationOptimizeMPlot.py` |
| `python3 ablationOptimizeNTest.py` | `ablationOptimizeS1NEnron.pkl` | `python3 ablationOptimizeNPlot.py` |

## Figure 9 — auxiliary knowledge

| Run | Output | Plot |
| --- | --- | --- |
| `python3 auxTest.py -d Enron -s S1` | `AuxS1Enron.pkl` | `python3 auxPlot.py -d Enron -s S1` |
| `python3 auxTest.py -d Enron -s S2` | `AuxS2Enron.pkl` | `python3 auxPlot.py -d Enron -s S2` |
| `python3 auxTest.py -d Enron -s S3` | `AuxS3Enron.pkl` | `python3 auxPlot.py -d Enron -s S3` |
| `python3 auxTest.py -d Lucene -s S1` | `AuxS1Lucene.pkl` | `python3 auxPlot.py -d Lucene -s S1` |
| `python3 auxTest.py -d Lucene -s S2` | `AuxS2Lucene.pkl` | `python3 auxPlot.py -d Lucene -s S2` |
| `python3 auxTest.py -d Lucene -s S3` | `AuxS3Lucene.pkl` | `python3 auxPlot.py -d Lucene -s S3` |

## Figure 10 — keyword universe n

| Run | Output | Plot |
| --- | --- | --- |
| `python3 nTest.py -d Enron -s S1` | `nS1Enron.pkl` | `python3 nPlot.py -d Enron -s S1`; `python3 nTimePlot.py -d Enron -s S1` |
| `python3 nTest.py -d Enron -s S2` | `nS2Enron.pkl` | `python3 nPlot.py -d Enron -s S2`; `python3 nTimePlot.py -d Enron -s S2` |
| `python3 nTest.py -d Enron -s S3` | `nS3Enron.pkl` | `python3 nPlot.py -d Enron -s S3`; `python3 nTimePlot.py -d Enron -s S3` |

## Figure 11 — similar runtime on n

| Run | Output | Plot |
| --- | --- | --- |
| `python3 nTestLimitedTime.py -d Enron -s S1` | `nS1EnronLimitedTime.pkl` | `python3 limitedTimeNPlot.py -d Enron -s S1` |
| `python3 nTestLimitedTime.py -d Enron -s S2` | `nS2EnronLimitedTime.pkl` | `python3 limitedTimeNPlot.py -d Enron -s S2` |
| `python3 nTestLimitedTime.py -d Lucene -s S1` | `nS1LuceneLimitedTime.pkl` | `python3 limitedTimeNPlot.py -d Lucene -s S1` |
| `python3 nTestLimitedTime.py -d Lucene -s S2` | `nS2LuceneLimitedTime.pkl` | `python3 limitedTimeNPlot.py -d Lucene -s S2` |

## Figure 12 — number of observed queries m

| Run | Output | Plot |
| --- | --- | --- |
| `python3 mTest.py -d Enron -s S1` | `mS1Enron.pkl` | `python3 mPlot.py -d Enron -s S1`; `python3 mTimePlot.py -d Enron -s S1` |
| `python3 mTest.py -d Enron -s S2` | `mS2Enron.pkl` | `python3 mPlot.py -d Enron -s S2`; `python3 mTimePlot.py -d Enron -s S2` |
| `python3 mTest.py -d Enron -s S3` | `mS3Enron.pkl` | `python3 mPlot.py -d Enron -s S3`; `python3 mTimePlot.py -d Enron -s S3` |

## Figure 13 — similar runtime on m

| Run | Output | Plot |
| --- | --- | --- |
| `python3 mTestLimitedTime.py -d Enron -s S1` | `mS1EnronLimitedTime.pkl` | `python3 limitedTimeMPlot.py -d Enron -s S1` |
| `python3 mTestLimitedTime.py -d Enron -s S2` | `mS2EnronLimitedTime.pkl` | `python3 limitedTimeMPlot.py -d Enron -s S2` |
| `python3 mTestLimitedTime.py -d Lucene -s S1` | `mS1LuceneLimitedTime.pkl` | `python3 limitedTimeMPlot.py -d Lucene -s S1` |
| `python3 mTestLimitedTime.py -d Lucene -s S2` | `mS2LuceneLimitedTime.pkl` | `python3 limitedTimeMPlot.py -d Lucene -s S2` |

## Figure 14 — CLRZ defense

| Run | Output | Plot |
| --- | --- | --- |
| `python3 clrzTest.py -d Enron -s S1` | `CLRZS1Enron.pkl` | `python3 clrzPlot.py -d Enron -s S1` |
| `python3 clrzTest.py -d Enron -s S2` | `CLRZS2Enron.pkl` | `python3 clrzPlot.py -d Enron -s S2` |
| `python3 clrzTest.py -d Enron -s S3` | `CLRZS3Enron.pkl` | `python3 clrzPlot.py -d Enron -s S3` |
| `python3 clrzTest.py -d Lucene -s S1` | `CLRZS1Lucene.pkl` | `python3 clrzPlot.py -d Lucene -s S1` |
| `python3 clrzTest.py -d Lucene -s S2` | `CLRZS2Lucene.pkl` | `python3 clrzPlot.py -d Lucene -s S2` |
| `python3 clrzTest.py -d Lucene -s S3` | `CLRZS3Lucene.pkl` | `python3 clrzPlot.py -d Lucene -s S3` |

## Figure 15 — OSSE defense

| Run | Output | Plot |
| --- | --- | --- |
| `python3 osseTest.py -d Enron -s S1` | `osseS1Enron.pkl` | `python3 ossePlot.py -d Enron -s S1` |
| `python3 osseTest.py -d Enron -s S2` | `osseS2Enron.pkl` | `python3 ossePlot.py -d Enron -s S2` |
| `python3 osseTest.py -d Enron -s S3` | `osseS3Enron.pkl` | `python3 ossePlot.py -d Enron -s S3` |
| `python3 osseTest.py -d Lucene -s S1` | `osseS1Lucene.pkl` | `python3 ossePlot.py -d Lucene -s S1` |
| `python3 osseTest.py -d Lucene -s S2` | `osseS2Lucene.pkl` | `python3 ossePlot.py -d Lucene -s S2` |
| `python3 osseTest.py -d Lucene -s S3` | `osseS3Lucene.pkl` | `python3 ossePlot.py -d Lucene -s S3` |
