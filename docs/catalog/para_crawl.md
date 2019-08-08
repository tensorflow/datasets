<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="para_crawl" />
  <meta itemprop="description" content="Web-Scale Parallel Corpora for Official European Languages. English-Swedish." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/para_crawl" />
  <meta itemprop="sameAs" content="https://paracrawl.eu/releases.html" />
</div>

# `para_crawl`

Web-Scale Parallel Corpora for Official European Languages. English-Swedish.

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

```python
Translation({
    'bg': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/encs_plain_text`

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enda_plain_text`

```python
Translation({
    'da': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/ende_plain_text`

```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enel_plain_text`

```python
Translation({
    'el': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enes_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'es': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enet_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'et': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enfi_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enfr_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enga_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ga': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enhr_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'hr': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enhu_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'hu': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enit_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'it': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enlt_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lt': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enlv_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lv': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enmt_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'mt': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/ennl_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'nl': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enpl_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pl': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enpt_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/enro_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ro': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/ensk_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sk': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/ensl_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sl': Text(shape=(), dtype=tf.string),
})
```

## `para_crawl/ensv_plain_text`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'sv': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split | Examples
:---- | --------:
TRAIN | 3,476,729
ALL   | 3,476,729

## Urls

*   [https://paracrawl.eu/releases.html](https://paracrawl.eu/releases.html)
*   [https://s3.amazonaws.com/web-language-models/paracrawl/release4/en-sv.bicleaner07.txt.gz](https://s3.amazonaws.com/web-language-models/paracrawl/release4/en-sv.bicleaner07.txt.gz)

## Supervised keys (for `as_supervised=True`)

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
