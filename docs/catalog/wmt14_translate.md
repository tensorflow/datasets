<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt14_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt14_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt14/translation-task.html" />
</div>

# `wmt14_translate`

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
    [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)
*   `DatasetBuilder`:
    [`tfds.translate.wmt14.Wmt14Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt14.py)

`wmt14_translate` is configured with `tfds.translate.wmt.WmtConfig` and has the
following configurations predefined (defaults to the first one):

*   `cs-en` (`v0.0.3`) (`Size: 1.58 GiB`): WMT 2014 cs-en translation task
    dataset.

*   `de-en` (`v0.0.3`) (`Size: 1.58 GiB`): WMT 2014 de-en translation task
    dataset.

*   `fr-en` (`v0.0.3`) (`Size: 6.20 GiB`): WMT 2014 fr-en translation task
    dataset.

*   `hi-en` (`v0.0.3`) (`Size: 44.65 MiB`): WMT 2014 hi-en translation task
    dataset.

*   `ru-en` (`v0.0.3`) (`Size: 998.38 MiB`): WMT 2014 ru-en translation task
    dataset.

## `wmt14_translate/cs-en`

WMT 2014 cs-en translation task dataset.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 62,202,876
TRAIN      | 62,196,873
TEST       | 3,003
VALIDATION | 3,000

### Features

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)

### Supervised keys (for `as_supervised=True`)

`(u'cs', u'en')`

## `wmt14_translate/de-en`

WMT 2014 de-en translation task dataset.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 4,514,788
TRAIN      | 4,508,785
TEST       | 3,003
VALIDATION | 3,000

### Features

```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)

### Supervised keys (for `as_supervised=True`)

`(u'de', u'en')`

## `wmt14_translate/fr-en`

WMT 2014 fr-en translation task dataset.

### Statistics

Split      | Examples
:--------- | ---------:
ALL        | 40,842,879
TRAIN      | 40,836,876
TEST       | 3,003
VALIDATION | 3,000

### Features

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)

### Supervised keys (for `as_supervised=True`)

`(u'fr', u'en')`

## `wmt14_translate/hi-en`

WMT 2014 hi-en translation task dataset.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 316,775
TRAIN      | 313,748
TEST       | 2,507
VALIDATION | 520

### Features

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'hi': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)

### Supervised keys (for `as_supervised=True`)

`(u'hi', u'en')`

## `wmt14_translate/ru-en`

WMT 2014 ru-en translation task dataset.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,492,968
TRAIN      | 2,486,965
TEST       | 3,003
VALIDATION | 3,000

### Features

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.statmt.org/wmt14/translation-task.html](http://www.statmt.org/wmt14/translation-task.html)

### Supervised keys (for `as_supervised=True`)

`(u'ru', u'en')`

## Citation
```
@InProceedings{bojar-EtAl:2014:W14-33,
  author    = {Bojar, Ondrej  and  Buck, Christian  and  Federmann, Christian  and  Haddow, Barry  and  Koehn, Philipp  and  Leveling, Johannes  and  Monz, Christof  and  Pecina, Pavel  and  Post, Matt  and  Saint-Amand, Herve  and  Soricut, Radu  and  Specia, Lucia  and  Tamchyna, Ale{s}},
  title     = {Findings of the 2014 Workshop on Statistical Machine Translation},
  booktitle = {Proceedings of the Ninth Workshop on Statistical Machine Translation},
  month     = {June},
  year      = {2014},
  address   = {Baltimore, Maryland, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {12--58},
  url       = {http://www.aclweb.org/anthology/W/W14/W14-3302}
}
```

--------------------------------------------------------------------------------
