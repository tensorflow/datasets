<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt18_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt18_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt18/translation-task.html" />
</div>

# `wmt18_translate`

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

`wmt18_translate` is configured with `tfds.translate.wmt18.WmtConfig` and has
the following configurations predefined (defaults to the first one):

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

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/de-en`

```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/et-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'et': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/fi-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/kk-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'kk': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/ru-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/tr-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

## `wmt18_translate/zh-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'zh': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | ---------:
ALL        | 25,168,191
TRAIN      | 25,162,209
TEST       | 3,981
VALIDATION | 2,001

## Urls

*   [http://www.statmt.org/wmt18/translation-task.html](http://www.statmt.org/wmt18/translation-task.html)

## Supervised keys (for `as_supervised=True`)
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
