<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="para_crawl" />
  <meta itemprop="description" content="Web-Scale Parallel Corpora for Official European Languages.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('para_crawl', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/para_crawl" />
  <meta itemprop="sameAs" content="https://paracrawl.eu/releases.html" />
  <meta itemprop="citation" content="@misc {paracrawl,&#10;    title  = &quot;ParaCrawl&quot;,&#10;    year   = &quot;2018&quot;,&#10;    url    = &quot;http://paracrawl.eu/download.html.&quot;&#10;}&#10;" />
</div>
# `para_crawl`

Web-Scale Parallel Corpora for Official European Languages.

*   URL:
    [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)
*   `DatasetBuilder`:
    [`tfds.translate.para_crawl.ParaCrawl`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/para_crawl.py)

`para_crawl` is configured with `tfds.translate.para_crawl.ParaCrawlConfig` and
has the following configurations predefined (defaults to the first one):

*   `enbg_plain_text` (`v0.1.0`) (`Size: 98.94 MiB`): Translation dataset from
    English to bg, uses encoder plain_text.

*   `encs_plain_text` (`v0.1.0`) (`Size: 187.31 MiB`): Translation dataset from
    English to cs, uses encoder plain_text.

*   `enda_plain_text` (`v0.1.0`) (`Size: 174.34 MiB`): Translation dataset from
    English to da, uses encoder plain_text.

*   `ende_plain_text` (`v0.1.0`) (`Size: 1.22 GiB`): Translation dataset from
    English to de, uses encoder plain_text.

*   `enel_plain_text` (`v0.1.0`) (`Size: 184.59 MiB`): Translation dataset from
    English to el, uses encoder plain_text.

*   `enes_plain_text` (`v0.1.0`) (`Size: 1.82 GiB`): Translation dataset from
    English to es, uses encoder plain_text.

*   `enet_plain_text` (`v0.1.0`) (`Size: 66.91 MiB`): Translation dataset from
    English to et, uses encoder plain_text.

*   `enfi_plain_text` (`v0.1.0`) (`Size: 151.83 MiB`): Translation dataset from
    English to fi, uses encoder plain_text.

*   `enfr_plain_text` (`v0.1.0`) (`Size: 2.63 GiB`): Translation dataset from
    English to fr, uses encoder plain_text.

*   `enga_plain_text` (`v0.1.0`) (`Size: 28.03 MiB`): Translation dataset from
    English to ga, uses encoder plain_text.

*   `enhr_plain_text` (`v0.1.0`) (`Size: 80.97 MiB`): Translation dataset from
    English to hr, uses encoder plain_text.

*   `enhu_plain_text` (`v0.1.0`) (`Size: 114.24 MiB`): Translation dataset from
    English to hu, uses encoder plain_text.

*   `enit_plain_text` (`v0.1.0`) (`Size: 1017.30 MiB`): Translation dataset from
    English to it, uses encoder plain_text.

*   `enlt_plain_text` (`v0.1.0`) (`Size: 63.28 MiB`): Translation dataset from
    English to lt, uses encoder plain_text.

*   `enlv_plain_text` (`v0.1.0`) (`Size: 45.17 MiB`): Translation dataset from
    English to lv, uses encoder plain_text.

*   `enmt_plain_text` (`v0.1.0`) (`Size: 18.15 MiB`): Translation dataset from
    English to mt, uses encoder plain_text.

*   `ennl_plain_text` (`v0.1.0`) (`Size: 400.63 MiB`): Translation dataset from
    English to nl, uses encoder plain_text.

*   `enpl_plain_text` (`v0.1.0`) (`Size: 257.90 MiB`): Translation dataset from
    English to pl, uses encoder plain_text.

*   `enpt_plain_text` (`v0.1.0`) (`Size: 608.62 MiB`): Translation dataset from
    English to pt, uses encoder plain_text.

*   `enro_plain_text` (`v0.1.0`) (`Size: 153.24 MiB`): Translation dataset from
    English to ro, uses encoder plain_text.

*   `ensk_plain_text` (`v0.1.0`) (`Size: 96.61 MiB`): Translation dataset from
    English to sk, uses encoder plain_text.

*   `ensl_plain_text` (`v0.1.0`) (`Size: 62.02 MiB`): Translation dataset from
    English to sl, uses encoder plain_text.

*   `ensv_plain_text` (`v0.1.0`) (`Size: 262.76 MiB`): Translation dataset from
    English to sv, uses encoder plain_text.

## `para_crawl/enbg_plain_text`
Translation dataset from English to bg, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,039,885
TRAIN | 1,039,885

### Features
```python
Translation({
    'bg': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'bg')`

## `para_crawl/encs_plain_text`
Translation dataset from English to cs, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,981,949
TRAIN | 2,981,949

### Features
```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'cs')`

## `para_crawl/enda_plain_text`
Translation dataset from English to da, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,414,895
TRAIN | 2,414,895

### Features
```python
Translation({
    'da': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'da')`

## `para_crawl/ende_plain_text`
Translation dataset from English to de, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | ---------:
ALL   | 16,264,448
TRAIN | 16,264,448

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'de')`

## `para_crawl/enel_plain_text`
Translation dataset from English to el, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,985,233
TRAIN | 1,985,233

### Features
```python
Translation({
    'el': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'el')`

## `para_crawl/enes_plain_text`
Translation dataset from English to es, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | ---------:
ALL   | 21,987,267
TRAIN | 21,987,267

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'es': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'es')`

## `para_crawl/enet_plain_text`
Translation dataset from English to et, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 853,422
TRAIN | 853,422

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'et': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'et')`

## `para_crawl/enfi_plain_text`
Translation dataset from English to fi, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,156,069
TRAIN | 2,156,069

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'fi')`

## `para_crawl/enfr_plain_text`
Translation dataset from English to fr, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | ---------:
ALL   | 31,374,161
TRAIN | 31,374,161

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'fr')`

## `para_crawl/enga_plain_text`
Translation dataset from English to ga, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 357,399
TRAIN | 357,399

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ga': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'ga')`

## `para_crawl/enhr_plain_text`
Translation dataset from English to hr, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,002,053
TRAIN | 1,002,053

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'hr': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'hr')`

## `para_crawl/enhu_plain_text`
Translation dataset from English to hu, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,901,342
TRAIN | 1,901,342

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'hu': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'hu')`

## `para_crawl/enit_plain_text`
Translation dataset from English to it, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | ---------:
ALL   | 12,162,239
TRAIN | 12,162,239

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'it': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'it')`

## `para_crawl/enlt_plain_text`
Translation dataset from English to lt, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 844,643
TRAIN | 844,643

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'lt')`

## `para_crawl/enlv_plain_text`
Translation dataset from English to lv, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 553,060
TRAIN | 553,060

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lv': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'lv')`

## `para_crawl/enmt_plain_text`
Translation dataset from English to mt, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 195,502
TRAIN | 195,502

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'mt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'mt')`

## `para_crawl/ennl_plain_text`
Translation dataset from English to nl, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,659,268
TRAIN | 5,659,268

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'nl': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'nl')`

## `para_crawl/enpl_plain_text`
Translation dataset from English to pl, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,503,276
TRAIN | 3,503,276

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pl': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'pl')`

## `para_crawl/enpt_plain_text`
Translation dataset from English to pt, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 8,141,940
TRAIN | 8,141,940

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'pt')`

## `para_crawl/enro_plain_text`
Translation dataset from English to ro, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,952,043
TRAIN | 1,952,043

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ro': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'ro')`

## `para_crawl/ensk_plain_text`
Translation dataset from English to sk, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,591,831
TRAIN | 1,591,831

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sk': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'sk')`

## `para_crawl/ensl_plain_text`
Translation dataset from English to sl, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 660,161
TRAIN | 660,161

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sl': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'sl')`

## `para_crawl/ensv_plain_text`
Translation dataset from English to sv, uses encoder plain_text.

Versions:

*   **`0.1.0`** (default):
*   `1.0.0`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,476,729
TRAIN | 3,476,729

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sv': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)

### Supervised keys (for `as_supervised=True`)
`(u'en', u'sv')`

## Citation
```
@misc {paracrawl,
    title  = "ParaCrawl",
    year   = "2018",
    url    = "http://paracrawl.eu/download.html."
}
```

--------------------------------------------------------------------------------
