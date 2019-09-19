<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lm1b" />
  <meta itemprop="description" content="A benchmark corpus to be used for measuring progress in statistical language modeling. This has almost one billion words in the training data.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lm1b" />
  <meta itemprop="sameAs" content="http://www.statmt.org/lm-benchmark/" />
</div>

# `lm1b`

A benchmark corpus to be used for measuring progress in statistical language
modeling. This has almost one billion words in the training data.

*   URL:
    [http://www.statmt.org/lm-benchmark/](http://www.statmt.org/lm-benchmark/)
*   `DatasetBuilder`:
    [`tfds.text.lm1b.Lm1b`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/lm1b.py)

`lm1b` is configured with `tfds.text.lm1b.Lm1bConfig` and has the following
configurations predefined (defaults to the first one):

*   `plain_text` (`v0.0.1`) (`Size: 1.67 GiB`): Plain text

*   `bytes` (`v0.0.1`) (`Size: 1.67 GiB`): Uses byte-level text encoding with
    `tfds.features.text.ByteTextEncoder`

*   `subwords8k` (`v0.0.2`) (`Size: 1.67 GiB`): Uses
    `tfds.features.text.SubwordTextEncoder` with 8k vocab size

*   `subwords32k` (`v0.0.2`) (`Size: 1.67 GiB`): Uses
    `tfds.features.text.SubwordTextEncoder` with 32k vocab size

## `lm1b/plain_text`

Plain text

### Statistics

Split | Examples
:---- | ---------:
ALL   | 30,607,716
TRAIN | 30,301,028
TEST  | 306,688

### Features

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/lm-benchmark/](http://www.statmt.org/lm-benchmark/)

### Supervised keys (for `as_supervised=True`)

`(u'text', u'text')`

## `lm1b/bytes`

Uses byte-level text encoding with `tfds.features.text.ByteTextEncoder`

### Statistics

Split | Examples
:---- | ---------:
ALL   | 30,607,716
TRAIN | 30,301,028
TEST  | 306,688

### Features

```python
FeaturesDict({
    'text': Text(shape=(None,), dtype=tf.int64, encoder=<ByteTextEncoder vocab_size=257>),
})
```

### Urls

*   [http://www.statmt.org/lm-benchmark/](http://www.statmt.org/lm-benchmark/)

### Supervised keys (for `as_supervised=True`)

`(u'text', u'text')`

## `lm1b/subwords8k`

Uses `tfds.features.text.SubwordTextEncoder` with 8k vocab size

### Statistics

Split | Examples
:---- | ---------:
ALL   | 30,607,716
TRAIN | 30,301,028
TEST  | 306,688

### Features

```python
FeaturesDict({
    'text': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8189>),
})
```

### Urls

*   [http://www.statmt.org/lm-benchmark/](http://www.statmt.org/lm-benchmark/)

### Supervised keys (for `as_supervised=True`)

`(u'text', u'text')`

## `lm1b/subwords32k`

Uses `tfds.features.text.SubwordTextEncoder` with 32k vocab size

### Statistics

Split | Examples
:---- | ---------:
ALL   | 30,607,716
TRAIN | 30,301,028
TEST  | 306,688

### Features

```python
FeaturesDict({
    'text': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=32711>),
})
```

### Urls

*   [http://www.statmt.org/lm-benchmark/](http://www.statmt.org/lm-benchmark/)

### Supervised keys (for `as_supervised=True`)

`(u'text', u'text')`

## Citation
```
@article{DBLP:journals/corr/ChelbaMSGBK13,
  author    = {Ciprian Chelba and
               Tomas Mikolov and
               Mike Schuster and
               Qi Ge and
               Thorsten Brants and
               Phillipp Koehn},
  title     = {One Billion Word Benchmark for Measuring Progress in Statistical Language
               Modeling},
  journal   = {CoRR},
  volume    = {abs/1312.3005},
  year      = {2013},
  url       = {http://arxiv.org/abs/1312.3005},
  archivePrefix = {arXiv},
  eprint    = {1312.3005},
  timestamp = {Mon, 13 Aug 2018 16:46:16 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ChelbaMSGBK13},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
