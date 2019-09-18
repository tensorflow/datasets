<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt15_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt15_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt15/translation-task.html" />
</div>

# `wmt15_translate`

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

`wmt15_translate` is configured with `tfds.translate.wmt15.WmtConfig` and has
the following configurations predefined (defaults to the first one):

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

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `wmt15_translate/de-en`

```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `wmt15_translate/fi-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```

## `wmt15_translate/fr-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

## `wmt15_translate/ru-en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

## `wmt15_translate/cs-en.subwords8k`

```python
Translation({
    'cs': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8193>),
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8155>),
})
```

## `wmt15_translate/de-en.subwords8k`

```python
Translation({
    'de': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8270>),
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8212>),
})
```

## `wmt15_translate/fi-en.subwords8k`

```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8217>),
    'fi': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8113>),
})
```

## `wmt15_translate/fr-en.subwords8k`

```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8183>),
    'fr': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8133>),
})
```

## `wmt15_translate/ru-en.subwords8k`

```python
Translation({
    'en': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8194>),
    'ru': Text(shape=(None,), dtype=tf.int64, encoder=<SubwordTextEncoder vocab_size=8180>),
})
```

## Statistics

Split      | Examples
:--------- | --------:
ALL        | 2,500,902
TRAIN      | 2,495,081
VALIDATION | 3,003
TEST       | 2,818

## Urls

*   [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

## Supervised keys (for `as_supervised=True`)
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
