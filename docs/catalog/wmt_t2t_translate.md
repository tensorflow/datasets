<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt_t2t_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wmt_t2t_translate', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt_t2t_translate" />
  <meta itemprop="sameAs" content="https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/translate_ende.py" />
  <meta itemprop="citation" content="&#10;@InProceedings{bojar-EtAl:2014:W14-33,&#10;  author    = {Bojar, Ondrej  and  Buck, Christian  and  Federmann, Christian  and  Haddow, Barry  and  Koehn, Philipp  and  Leveling, Johannes  and  Monz, Christof  and  Pecina, Pavel  and  Post, Matt  and  Saint-Amand, Herve  and  Soricut, Radu  and  Specia, Lucia  and  Tamchyna, Ale{s}},&#10;  title     = {Findings of the 2014 Workshop on Statistical Machine Translation},&#10;  booktitle = {Proceedings of the Ninth Workshop on Statistical Machine Translation},&#10;  month     = {June},&#10;  year      = {2014},&#10;  address   = {Baltimore, Maryland, USA},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {12--58},&#10;  url       = {http://www.aclweb.org/anthology/W/W14/W14-3302}&#10;}&#10;" />
</div>
# `wmt_t2t_translate` (Manual download)

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
    [https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/translate_ende.py](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/translate_ende.py)
*   `DatasetBuilder`:
    [`tfds.translate.wmt_t2t.WmtT2tTranslate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt_t2t.py)

`wmt_t2t_translate` is configured with `tfds.translate.wmt.WmtConfig` and has
the following configurations predefined (defaults to the first one):

*   `de-en` (`v0.0.1`) (`Size: 1.61 GiB`): WMT T2T EnDe translation task
    dataset.

## `wmt_t2t_translate/de-en`
WMT T2T EnDe translation task dataset.

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: None

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/wmt_t2t_translate/`): Some
of the wmt configs here, require a manual download. Please look into wmt.py to
see the exact path (and file name) that has to be downloaded.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 4,598,292
TRAIN      | 4,592,289
TEST       | 3,003
VALIDATION | 3,000

### Features
```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/translate_ende.py](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/translate_ende.py)

### Supervised keys (for `as_supervised=True`)
`(u'de', u'en')`

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
