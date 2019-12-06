<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt18_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt18_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt18_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt18/translation-task.html" />
  <meta itemprop="citation" content="@InProceedings{bojar-EtAl:2018:WMT1,&#10;  author    = {Bojar, Ond{r}ej  and  Federmann, Christian  and  Fishel, Mark&#10;    and Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and&#10;    Koehn, Philipp  and  Monz, Christof},&#10;  title     = {Findings of the 2018 Conference on Machine Translation (WMT18)},&#10;  booktitle = {Proceedings of the Third Conference on Machine Translation,&#10;    Volume 2: Shared Task Papers},&#10;  month     = {October},&#10;  year      = {2018},&#10;  address   = {Belgium, Brussels},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {272--307},&#10;  url       = {http://www.aclweb.org/anthology/W18-6401}&#10;}&#10;" />
</div>
# `wmt18_translate` (Manual download)

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
    [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt18.Wmt18Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt18.py)

`wmt18_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.3`) (`Size: 1.89 GiB`): WMT 2018 cs-en translation task
    dataset.

*   `de-en` (`v0.0.3`) (`Size: 3.55 GiB`): WMT 2018 de-en translation task
    dataset.

*   `et-en` (`v0.0.3`) (`Size: 499.91 MiB`): WMT 2018 et-en translation task
    dataset.

*   `fi-en` (`v0.0.3`) (`Size: 468.76 MiB`): WMT 2018 fi-en translation task
    dataset.

*   `kk-en` (`v0.0.3`) (`Size: ?? GiB`): WMT 2018 kk-en translation task
    dataset.

*   `ru-en` (`v0.0.3`) (`Size: 3.91 GiB`): WMT 2018 ru-en translation task
    dataset.

*   `tr-en` (`v0.0.3`) (`Size: 59.32 MiB`): WMT 2018 tr-en translation task
    dataset.

*   `zh-en` (`v0.0.3`) (`Size: 2.10 GiB`): WMT 2018 zh-en translation task
    dataset.

## `wmt18_translate/cs-en`
WMT 2018 cs-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 68,117,370
TRAIN      | 68,111,382
VALIDATION | 3,005
TEST       | 2,983

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt18_translate/de-en`
WMT 2018 de-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 42,277,876
TRAIN      | 42,271,874
VALIDATION | 3,004
TEST       | 2,998

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt18_translate/et-en`
WMT 2018 et-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,179,873
TRAIN      | 2,175,873
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'et': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'et', u'en')`

## `wmt18_translate/fi-en`
WMT 2018 fi-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 3,289,604
TRAIN      | 3,280,600
VALIDATION | 6,004
TEST       | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt18_translate/kk-en`
WMT 2018 kk-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics
None computed

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'kk': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'kk', u'en')`

## `wmt18_translate/ru-en`
WMT 2018 ru-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 37,864,513
TRAIN      | 37,858,512
VALIDATION | 3,001
TEST       | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `wmt18_translate/tr-en`
WMT 2018 tr-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 211,763
TRAIN      | 205,756
VALIDATION | 3,007
TEST       | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'tr', u'en')`

## `wmt18_translate/zh-en`
WMT 2018 zh-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt18_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 25,168,191
TRAIN      | 25,162,209
TEST       | 3,981
VALIDATION | 2,001

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'zh': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'zh', u'en')`

## Citation
```
@InProceedings{bojar-EtAl:2018:WMT1,
  author    = {Bojar, Ond{r}ej  and  Federmann, Christian  and  Fishel, Mark
    and Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and
    Koehn, Philipp  and  Monz, Christof},
  title     = {Findings of the 2018 Conference on Machine Translation (WMT18)},
  booktitle = {Proceedings of the Third Conference on Machine Translation,
    Volume 2: Shared Task Papers},
  month     = {October},
  year      = {2018},
  address   = {Belgium, Brussels},
  publisher = {Association for Computational Linguistics},
  pages     = {272--307},
  url       = {http://www.aclweb.org/anthology/W18-6401}
}
```

--------------------------------------------------------------------------------
