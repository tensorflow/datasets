<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt15_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt15_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt15_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt15/translation-task.html" />
  <meta itemprop="citation" content="&#10;@InProceedings{bojar-EtAl:2015:WMT,&#10;  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Haddow, Barry  and  Huck, Matthias  and  Hokamp, Chris  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco},&#10;  title     = {Findings of the 2015 Workshop on Statistical Machine Translation},&#10;  booktitle = {Proceedings of the Tenth Workshop on Statistical Machine Translation},&#10;  month     = {September},&#10;  year      = {2015},&#10;  address   = {Lisbon, Portugal},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {1--46},&#10;  url       = {http://aclweb.org/anthology/W15-3001}&#10;}&#10;" />
</div>
# `wmt15_translate` (Manual download)

Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.

```
config = tfds.translate.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        tfds.Split.TRAIN: ["commoncrawl_frde"],
        tfds.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = tfds.builder("wmt_translate", config=config)
```

*   URL:
    [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt15.Wmt15Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt15.py)

`wmt15_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.4`) (`Size: 1.62 GiB`): WMT 2015 cs-en translation task
    dataset.

*   `de-en` (`v0.0.4`) (`Size: 1.62 GiB`): WMT 2015 de-en translation task
    dataset.

*   `fi-en` (`v0.0.4`) (`Size: 260.51 MiB`): WMT 2015 fi-en translation task
    dataset.

*   `fr-en` (`v0.0.4`) (`Size: 6.24 GiB`): WMT 2015 fr-en translation task
    dataset.

*   `ru-en` (`v0.0.4`) (`Size: 1.02 GiB`): WMT 2015 ru-en translation task
    dataset.

*   `cs-en.subwords8k` (`v0.0.4`) (`Size: 1.62 GiB`): WMT 2015 cs-en translation
    task dataset with subword encoding.

*   `de-en.subwords8k` (`v0.0.4`) (`Size: 1.62 GiB`): WMT 2015 de-en translation
    task dataset with subword encoding.

*   `fi-en.subwords8k` (`v0.0.4`) (`Size: 260.51 MiB`): WMT 2015 fi-en
    translation task dataset with subword encoding.

*   `fr-en.subwords8k` (`v0.0.4`) (`Size: 6.24 GiB`): WMT 2015 fr-en translation
    task dataset with subword encoding.

*   `ru-en.subwords8k` (`v0.0.4`) (`Size: 1.02 GiB`): WMT 2015 ru-en translation
    task dataset with subword encoding.

## `wmt15_translate/cs-en`
WMT 2015 cs-en translation task dataset.

Versions:

*   **`0.0.4`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 62,208,679
TRAIN      | 62,203,020
VALIDATION | 3,003
TEST       | 2,656

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt15_translate/de-en`
WMT 2015 de-en translation task dataset.

Versions:

*   **`0.0.4`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 4,528,170
TRAIN      | 4,522,998
VALIDATION | 3,003
TEST       | 2,169

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt15_translate/fi-en`
WMT 2015 fi-en translation task dataset.

Versions:

*   **`0.0.4`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,076,264
TRAIN      | 2,073,394
VALIDATION | 1,500
TEST       | 1,370

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt15_translate/fr-en`
WMT 2015 fr-en translation task dataset.

Versions:

*   **`0.0.4`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 40,859,301
TRAIN      | 40,853,298
VALIDATION | 4,503
TEST       | 1,500

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fr', u'en')`

## `wmt15_translate/ru-en`
WMT 2015 ru-en translation task dataset.

Versions:

*   **`0.0.4`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,500,902
TRAIN      | 2,495,081
VALIDATION | 3,003
TEST       | 2,818

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `wmt15_translate/cs-en.subwords8k`
WMT 2015 cs-en translation task dataset with subword encoding.

Versions:

*   **`0.0.4`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 62,208,679
TRAIN      | 62,203,020
VALIDATION | 3,003
TEST       | 2,656

### Features
```python
Translation({
    'cs': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8193>),
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8155>),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt15_translate/de-en.subwords8k`
WMT 2015 de-en translation task dataset with subword encoding.

Versions:

*   **`0.0.4`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 4,528,170
TRAIN      | 4,522,998
VALIDATION | 3,003
TEST       | 2,169

### Features
```python
Translation({
    'de': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8270>),
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8212>),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt15_translate/fi-en.subwords8k`
WMT 2015 fi-en translation task dataset with subword encoding.

Versions:

*   **`0.0.4`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,076,264
TRAIN      | 2,073,394
VALIDATION | 1,500
TEST       | 1,370

### Features
```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8217>),
    'fi': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8113>),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt15_translate/fr-en.subwords8k`
WMT 2015 fr-en translation task dataset with subword encoding.

Versions:

*   **`0.0.4`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 40,859,301
TRAIN      | 40,853,298
VALIDATION | 4,503
TEST       | 1,500

### Features
```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8183>),
    'fr': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8133>),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fr', u'en')`

## `wmt15_translate/ru-en.subwords8k`
WMT 2015 ru-en translation task dataset with subword encoding.

Versions:

*   **`0.0.4`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt15_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,500,902
TRAIN      | 2,495,081
VALIDATION | 3,003
TEST       | 2,818

### Features
```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8194>),
    'ru': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8180>),
})
```

### Homepage

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## Citation
```
@InProceedings{bojar-EtAl:2015:WMT,
  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Haddow, Barry  and  Huck, Matthias  and  Hokamp, Chris  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco},
  title     = {Findings of the 2015 Workshop on Statistical Machine Translation},
  booktitle = {Proceedings of the Tenth Workshop on Statistical Machine Translation},
  month     = {September},
  year      = {2015},
  address   = {Lisbon, Portugal},
  publisher = {Association for Computational Linguistics},
  pages     = {1--46},
  url       = {http://aclweb.org/anthology/W15-3001}
}
```

--------------------------------------------------------------------------------
