<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikihow" />
  <meta itemprop="description" content="&#10;WikiHow is a new large-scale dataset using the online WikiHow&#10;(http://www.wikihow.com/) knowledge base.&#10;&#10;There are two features:&#10;  - text: wikihow answers texts.&#10;  - headline: bold lines as summary.&#10;&#10;There are two separate versions:&#10;  - all: consisting of the concatenation of all paragraphs as the articles and&#10;         the bold lines as the reference summaries.&#10;  - sep: consisting of each paragraph and its summary.&#10;&#10;Download &quot;wikihowAll.csv&quot; and &quot;wikihowSep.csv&quot; from&#10;https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder&#10;https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.&#10;Train/validation/test splits are provided by the authors.&#10;Preprocessing is applied to remove short articles&#10;(abstract length &lt; 0.75 article length) and clean up extra commas.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wikihow', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikihow" />
  <meta itemprop="sameAs" content="https://github.com/mahnazkoupaee/WikiHow-Dataset" />
  <meta itemprop="citation" content="&#10;@misc{koupaee2018wikihow,&#10;    title={WikiHow: A Large Scale Text Summarization Dataset},&#10;    author={Mahnaz Koupaee and William Yang Wang},&#10;    year={2018},&#10;    eprint={1810.09305},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `wikihow` (Manual download)

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

*   URL:
    [https://github.com/mahnazkoupaee/WikiHow-Dataset](https://github.com/mahnazkoupaee/WikiHow-Dataset)
*   `DatasetBuilder`:
    [`tfds.summarization.wikihow.Wikihow`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/wikihow.py)

`wikihow` is configured with `tfds.summarization.wikihow.WikihowConfig` and has
the following configurations predefined (defaults to the first one):

*   `all` (`v1.2.0`) (`Size: 5.21 MiB`): Use the concatenation of all paragraphs
    as the articles and the bold lines as the reference summaries

*   `sep` (`v1.2.0`) (`Size: 5.21 MiB`): use each paragraph and its summary.

## `wikihow/all`

Use the concatenation of all paragraphs as the articles and the bold lines as
the reference summaries

Versions:

*   **`1.2.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wikihow/`): Links to files
can be found on https://github.com/mahnazkoupaee/WikiHow-Dataset Please download
both wikihowAll.csv and wikihowSep.csv.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 168,428
TRAIN      | 157,252
VALIDATION | 5,599
TEST       | 5,577

### Features
```python
FeaturesDict({
    'headline': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/mahnazkoupaee/WikiHow-Dataset](https://github.com/mahnazkoupaee/WikiHow-Dataset)

### Supervised keys (for `as_supervised=True`)
`(u'text', u'headline')`

## `wikihow/sep`
use each paragraph and its summary.

Versions:

*   **`1.2.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wikihow/`): Links to files
can be found on https://github.com/mahnazkoupaee/WikiHow-Dataset Please download
both wikihowAll.csv and wikihowSep.csv.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,136,464
TRAIN      | 1,060,732
VALIDATION | 37,932
TEST       | 37,800

### Features
```python
FeaturesDict({
    'headline': Text(shape=(), dtype=tf.string),
    'overview': Text(shape=(), dtype=tf.string),
    'sectionLabel': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/mahnazkoupaee/WikiHow-Dataset](https://github.com/mahnazkoupaee/WikiHow-Dataset)

### Supervised keys (for `as_supervised=True`)
`(u'text', u'headline')`

## Citation
```
@misc{koupaee2018wikihow,
    title={WikiHow: A Large Scale Text Summarization Dataset},
    author={Mahnaz Koupaee and William Yang Wang},
    year={2018},
    eprint={1810.09305},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
