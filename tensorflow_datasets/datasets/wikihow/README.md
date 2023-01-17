WikiHow is a new large-scale dataset using the online WikiHow
(http://www.wikihow.com/) knowledge base.

There are two features: - text: wikihow answers texts. - headline: bold lines as
summary.

There are two separate versions: - all: consisting of the concatenation of all
paragraphs as the articles and the bold lines as the reference summaries. - sep:
consisting of each paragraph and its summary.

Download "wikihowAll.csv" and "wikihowSep.csv" from
https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder
https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.
Train/validation/test splits are provided by the authors. Preprocessing is
applied to remove short articles (abstract length < 0.75 article length) and
clean up extra commas.
