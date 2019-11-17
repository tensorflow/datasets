<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ted_hrlr_translate" />
  <meta itemprop="description" content="Data sets derived from TED talk transcripts for comparing similar language pairs&#10;where one is high resource and the other is low resource.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('ted_hrlr_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ted_hrlr_translate" />
  <meta itemprop="sameAs" content="https://github.com/neulab/word-embeddings-for-nmt" />
  <meta itemprop="citation" content="@inproceedings{Ye2018WordEmbeddings,&#10;  author  = {Ye, Qi and Devendra, Sachan and Matthieu, Felix and Sarguna, Padmanabhan and Graham, Neubig},&#10;  title   = {When and Why are pre-trained word embeddings useful for Neural Machine Translation},&#10;  booktitle = {HLT-NAACL},&#10;  year    = {2018},&#10;  }&#10;" />
</div>
# `ted_hrlr_translate`

Data sets derived from TED talk transcripts for comparing similar language pairs
where one is high resource and the other is low resource.

*   URL:
    [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)
*   `DatasetBuilder`:
    [`tfds.translate.ted_hrlr.TedHrlrTranslate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/ted_hrlr.py)

`ted_hrlr_translate` is configured with `tfds.translate.ted_hrlr.TedHrlrConfig`
and has the following configurations predefined (defaults to the first one):

*   `az_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from az to
    en in plain text.

*   `aztr_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from az_tr
    to en in plain text.

*   `be_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from be to
    en in plain text.

*   `beru_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from be_ru
    to en in plain text.

*   `es_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from es to
    pt in plain text.

*   `fr_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from fr to
    pt in plain text.

*   `gl_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from gl to
    en in plain text.

*   `glpt_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from gl_pt
    to en in plain text.

*   `he_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from he to
    pt in plain text.

*   `it_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from it to
    pt in plain text.

*   `pt_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from pt to
    en in plain text.

*   `ru_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from ru to
    en in plain text.

*   `ru_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from ru to
    pt in plain text.

*   `tr_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from tr to
    en in plain text.

## `ted_hrlr_translate/az_to_en`
Translation dataset from az to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 7,520
TRAIN      | 5,946
TEST       | 903
VALIDATION | 671

### Features
```python
Translation({
    'az': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'az', u'en')`

## `ted_hrlr_translate/aztr_to_en`
Translation dataset from az_tr to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 189,970
TRAIN      | 188,396
TEST       | 903
VALIDATION | 671

### Features
```python
Translation({
    'az_tr': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'az_tr', u'en')`

## `ted_hrlr_translate/be_to_en`
Translation dataset from be to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,421
TRAIN      | 4,509
TEST       | 664
VALIDATION | 248

### Features
```python
Translation({
    'be': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'be', u'en')`

## `ted_hrlr_translate/beru_to_en`
Translation dataset from be_ru to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 213,526
TRAIN      | 212,614
TEST       | 664
VALIDATION | 248

### Features
```python
Translation({
    'be_ru': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'be_ru', u'en')`

## `ted_hrlr_translate/es_to_pt`
Translation dataset from es to pt in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 47,717
TRAIN      | 44,938
TEST       | 1,763
VALIDATION | 1,016

### Features
```python
Translation({
    'es': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'es', u'pt')`

## `ted_hrlr_translate/fr_to_pt`
Translation dataset from fr to pt in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 46,498
TRAIN      | 43,873
TEST       | 1,494
VALIDATION | 1,131

### Features
```python
Translation({
    'fr': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'fr', u'pt')`

## `ted_hrlr_translate/gl_to_en`
Translation dataset from gl to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 11,706
TRAIN      | 10,017
TEST       | 1,007
VALIDATION | 682

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'gl', u'en')`

## `ted_hrlr_translate/glpt_to_en`
Translation dataset from gl_pt to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 63,491
TRAIN      | 61,802
TEST       | 1,007
VALIDATION | 682

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl_pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'gl_pt', u'en')`

## `ted_hrlr_translate/he_to_pt`
Translation dataset from he to pt in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 51,279
TRAIN      | 48,511
TEST       | 1,623
VALIDATION | 1,145

### Features
```python
Translation({
    'he': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'he', u'pt')`

## `ted_hrlr_translate/it_to_pt`
Translation dataset from it to pt in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 49,090
TRAIN      | 46,259
TEST       | 1,669
VALIDATION | 1,162

### Features
```python
Translation({
    'it': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'it', u'pt')`

## `ted_hrlr_translate/pt_to_en`
Translation dataset from pt to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 54,781
TRAIN      | 51,785
TEST       | 1,803
VALIDATION | 1,193

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'pt', u'en')`

## `ted_hrlr_translate/ru_to_en`
Translation dataset from ru to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 218,387
TRAIN      | 208,106
TEST       | 5,476
VALIDATION | 4,805

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `ted_hrlr_translate/ru_to_pt`
Translation dataset from ru to pt in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 50,050
TRAIN      | 47,278
TEST       | 1,588
VALIDATION | 1,184

### Features
```python
Translation({
    'pt': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'pt')`

## `ted_hrlr_translate/tr_to_en`
Translation dataset from tr to en in plain text.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 191,524
TRAIN      | 182,450
TEST       | 5,029
VALIDATION | 4,045

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

### Supervised keys (for `as_supervised=True`)
`(u'tr', u'en')`

## Citation
```
@inproceedings{Ye2018WordEmbeddings,
  author  = {Ye, Qi and Devendra, Sachan and Matthieu, Felix and Sarguna, Padmanabhan and Graham, Neubig},
  title   = {When and Why are pre-trained word embeddings useful for Neural Machine Translation},
  booktitle = {HLT-NAACL},
  year    = {2018},
  }
```

--------------------------------------------------------------------------------
