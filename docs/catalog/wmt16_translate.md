<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt16_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt16_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt16_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt16/translation-task.html" />
  <meta itemprop="citation" content="&#10;@InProceedings{bojar-EtAl:2016:WMT1,&#10;  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and  Jimeno Yepes, Antonio  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Neveol, Aurelie  and  Neves, Mariana  and  Popel, Martin  and  Post, Matt  and  Rubino, Raphael  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco  and  Verspoor, Karin  and  Zampieri, Marcos},&#10;  title     = {Findings of the 2016 Conference on Machine Translation},&#10;  booktitle = {Proceedings of the First Conference on Machine Translation},&#10;  month     = {August},&#10;  year      = {2016},&#10;  address   = {Berlin, Germany},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {131--198},&#10;  url       = {http://www.aclweb.org/anthology/W/W16/W16-2301}&#10;}&#10;" />
</div>
# `wmt16_translate` (Manual download)

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
    [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt16.Wmt16Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt16.py)

`wmt16_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.3`) (`Size: 1.57 GiB`): WMT 2016 cs-en translation task
    dataset.

*   `de-en` (`v0.0.3`) (`Size: 1.57 GiB`): WMT 2016 de-en translation task
    dataset.

*   `fi-en` (`v0.0.3`) (`Size: 260.51 MiB`): WMT 2016 fi-en translation task
    dataset.

*   `ro-en` (`v0.0.3`) (`Size: 273.83 MiB`): WMT 2016 ro-en translation task
    dataset.

*   `ru-en` (`v0.0.3`) (`Size: 993.38 MiB`): WMT 2016 ru-en translation task
    dataset.

*   `tr-en` (`v0.0.3`) (`Size: 59.32 MiB`): WMT 2016 tr-en translation task
    dataset.

## `wmt16_translate/cs-en`
WMT 2016 cs-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 52,341,306
TRAIN      | 52,335,651
TEST       | 2,999
VALIDATION | 2,656

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt16_translate/de-en`
WMT 2016 de-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 4,554,053
TRAIN      | 4,548,885
TEST       | 2,999
VALIDATION | 2,169

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt16_translate/fi-en`
WMT 2016 fi-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,080,764
TRAIN      | 2,073,394
TEST       | 6,000
VALIDATION | 1,370

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt16_translate/ro-en`
WMT 2016 ro-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 614,318
TRAIN      | 610,320
TEST       | 1,999
VALIDATION | 1,999

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ro': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ro', u'en')`

## `wmt16_translate/ru-en`
WMT 2016 ru-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,521,978
TRAIN      | 2,516,162
TEST       | 2,998
VALIDATION | 2,818

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `wmt16_translate/tr-en`
WMT 2016 tr-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt16_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 209,757
TRAIN      | 205,756
TEST       | 3,000
VALIDATION | 1,001

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt16/translation-task.html](http://www.statmt.org/wmt16/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'tr', u'en')`

## Citation
```
@InProceedings{bojar-EtAl:2016:WMT1,
  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and  Jimeno Yepes, Antonio  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Neveol, Aurelie  and  Neves, Mariana  and  Popel, Martin  and  Post, Matt  and  Rubino, Raphael  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco  and  Verspoor, Karin  and  Zampieri, Marcos},
  title     = {Findings of the 2016 Conference on Machine Translation},
  booktitle = {Proceedings of the First Conference on Machine Translation},
  month     = {August},
  year      = {2016},
  address   = {Berlin, Germany},
  publisher = {Association for Computational Linguistics},
  pages     = {131--198},
  url       = {http://www.aclweb.org/anthology/W/W16/W16-2301}
}
```

--------------------------------------------------------------------------------
