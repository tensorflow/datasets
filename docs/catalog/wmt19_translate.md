<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt19_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt19_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt19_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt19/translation-task.html" />
  <meta itemprop="citation" content="&#10;@ONLINE {wmt19translate,&#10;    author = &quot;Wikimedia Foundation&quot;,&#10;    title  = &quot;ACL 2019 Fourth Conference on Machine Translation (WMT19), Shared Task: Machine Translation of News&quot;,&#10;    url    = &quot;http://www.statmt.org/wmt19/translation-task.html&quot;&#10;}&#10;" />
</div>
# `wmt19_translate` (Manual download)

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
    [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt19.Wmt19Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt19.py)

`wmt19_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.3`) (`Size: 1.88 GiB`): WMT 2019 cs-en translation task
    dataset.

*   `de-en` (`v0.0.3`) (`Size: 9.71 GiB`): WMT 2019 de-en translation task
    dataset.

*   `fi-en` (`v0.0.3`) (`Size: 959.46 MiB`): WMT 2019 fi-en translation task
    dataset.

*   `gu-en` (`v0.0.3`) (`Size: 37.03 MiB`): WMT 2019 gu-en translation task
    dataset.

*   `kk-en` (`v0.0.3`) (`Size: 39.58 MiB`): WMT 2019 kk-en translation task
    dataset.

*   `lt-en` (`v0.0.3`) (`Size: 392.20 MiB`): WMT 2019 lt-en translation task
    dataset.

*   `ru-en` (`v0.0.3`) (`Size: 3.86 GiB`): WMT 2019 ru-en translation task
    dataset.

*   `zh-en` (`v0.0.3`) (`Size: 2.04 GiB`): WMT 2019 zh-en translation task
    dataset.

*   `fr-de` (`v0.0.3`) (`Size: 722.20 MiB`): WMT 2019 fr-de translation task
    dataset.

## `wmt19_translate/cs-en`
WMT 2019 cs-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 64,339,036
TRAIN      | 64,336,053
VALIDATION | 2,983

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'cs', u'en')`

## `wmt19_translate/de-en`
WMT 2019 de-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 38,693,332
TRAIN      | 38,690,334
VALIDATION | 2,998

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

## `wmt19_translate/fi-en`
WMT 2019 fi-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 6,590,448
TRAIN      | 6,587,448
VALIDATION | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fi', u'en')`

## `wmt19_translate/gu-en`
WMT 2019 gu-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 13,668
TRAIN      | 11,670
VALIDATION | 1,998

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gu': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'gu', u'en')`

## `wmt19_translate/kk-en`
WMT 2019 kk-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 128,649
TRAIN      | 126,583
VALIDATION | 2,066

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'kk': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'kk', u'en')`

## `wmt19_translate/lt-en`
WMT 2019 lt-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,346,893
TRAIN      | 2,344,893
VALIDATION | 2,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'lt', u'en')`

## `wmt19_translate/ru-en`
WMT 2019 ru-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 38,495,126
TRAIN      | 38,492,126
VALIDATION | 3,000

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'ru', u'en')`

## `wmt19_translate/zh-en`
WMT 2019 zh-en translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 25,990,417
TRAIN      | 25,986,436
VALIDATION | 3,981

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'zh': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'zh', u'en')`

## `wmt19_translate/fr-de`
WMT 2019 fr-de translation task dataset.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt19_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 9,825,988
TRAIN      | 9,824,476
VALIDATION | 1,512

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://www.statmt.org/wmt19/translation-task.html](http://www.statmt.org/wmt19/translation-task.html)

### Supervised keys (for `as_supervised=True`)
`(u'fr', u'de')`

## Citation
```
@ONLINE {wmt19translate,
    author = "Wikimedia Foundation",
    title  = "ACL 2019 Fourth Conference on Machine Translation (WMT19), Shared Task: Machine Translation of News",
    url    = "http://www.statmt.org/wmt19/translation-task.html"
}
```

--------------------------------------------------------------------------------
