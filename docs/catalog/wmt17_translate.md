<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt17_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt17_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt17_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt17/translation-task.html" />
  <meta itemprop="citation" content="&#10;@InProceedings{bojar-EtAl:2017:WMT1,&#10;  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huang, Shujian  and  Huck, Matthias  and  Koehn, Philipp  and  Liu, Qun  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Rubino, Raphael  and  Specia, Lucia  and  Turchi, Marco},&#10;  title     = {Findings of the 2017 Conference on Machine Translation (WMT17)},&#10;  booktitle = {Proceedings of the Second Conference on Machine Translation, Volume 2: Shared Task Papers},&#10;  month     = {September},&#10;  year      = {2017},&#10;  address   = {Copenhagen, Denmark},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {169--214},&#10;  url       = {http://www.aclweb.org/anthology/W17-4717}&#10;}&#10;" />
</div>
# `wmt17_translate` (Manual download)

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
    [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt17.Wmt17Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt17.py)

`wmt17_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.3`) (`Size: 1.66 GiB`): WMT 2017 cs-en translation task
    dataset.

*   `de-en` (`v0.0.3`) (`Size: 1.81 GiB`): WMT 2017 de-en translation task
    dataset.

*   `fi-en` (`v0.0.3`) (`Size: 414.10 MiB`): WMT 2017 fi-en translation task
    dataset.

*   `lv-en` (`v0.0.3`) (`Size: 161.69 MiB`): WMT 2017 lv-en translation task
    dataset.

*   `ru-en` (`v0.0.3`) (`Size: 3.34 GiB`): WMT 2017 ru-en translation task
    dataset.

*   `tr-en` (`v0.0.3`) (`Size: 59.32 MiB`): WMT 2017 tr-en translation task
    dataset.

*   `zh-en` (`v0.0.3`) (`Size: 2.16 GiB`): WMT 2017 zh-en translation task
    dataset.

## `wmt17_translate/cs-en`
WMT 2017 cs-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 62,267,547
TRAIN      | 62,261,543
TEST       | 3,005
VALIDATION | 2,999

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt17_translate/de-en`
WMT 2017 de-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 5,912,187
TRAIN      | 5,906,184
TEST       | 3,004
VALIDATION | 2,999

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt17_translate/fi-en`
WMT 2017 fi-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,668,546
TRAIN      | 2,656,542
TEST       | 6,004
VALIDATION | 6,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt17_translate/lv-en`
WMT 2017 lv-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 3,571,532
TRAIN      | 3,567,528
VALIDATION | 2,003
TEST       | 2,001

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lv': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'lv', u'en')`

## `wmt17_translate/ru-en`
WMT 2017 ru-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 25,788,719
TRAIN      | 25,782,720
TEST       | 3,001
VALIDATION | 2,998

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `wmt17_translate/tr-en`
WMT 2017 tr-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 211,763
TRAIN      | 205,756
TEST       | 3,007
VALIDATION | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'tr', u'en')`

## `wmt17_translate/zh-en`
WMT 2017 zh-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt17_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 25,140,612
TRAIN      | 25,136,609
VALIDATION | 2,002
TEST       | 2,001

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'zh': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'zh', u'en')`

## Citation
```
@InProceedings{bojar-EtAl:2017:WMT1,
  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huang, Shujian  and  Huck, Matthias  and  Koehn, Philipp  and  Liu, Qun  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Rubino, Raphael  and  Specia, Lucia  and  Turchi, Marco},
  title     = {Findings of the 2017 Conference on Machine Translation (WMT17)},
  booktitle = {Proceedings of the Second Conference on Machine Translation, Volume 2: Shared Task Papers},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {169--214},
  url       = {http://www.aclweb.org/anthology/W17-4717}
}
```

--------------------------------------------------------------------------------
