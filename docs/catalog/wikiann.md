<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikiann" />
  <meta itemprop="description" content="WikiANN (sometimes called PAN-X) is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format. This version corresponds to the balanced train, dev, and test splits of Rahimi et al. (2019), which supports 176 of the 282 languages from the original WikiANN corpus.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikiann&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikiann" />
  <meta itemprop="sameAs" content="https://github.com/afshinrahimi/mmner" />
  <meta itemprop="citation" content="@inproceedings{rahimi-etal-2019-massively,&#10;    title = &quot;Massively Multilingual Transfer for {NER}&quot;,&#10;    author = &quot;Rahimi, Afshin  and&#10;      Li, Yuan  and&#10;      Cohn, Trevor&quot;,&#10;    booktitle = &quot;Proceedings of the 57th Annual Meeting of the Association     for Computational Linguistics&quot;,&#10;    month = jul,&#10;    year = &quot;2019&quot;,&#10;    address = &quot;Florence, Italy&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/P19-1015&quot;,&#10;    pages = &quot;151--164&quot;,&#10;}" />
</div>

# `wikiann`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

WikiANN (sometimes called PAN-X) is a multilingual named entity recognition
dataset consisting of Wikipedia articles annotated with LOC (location), PER
(person), and ORG (organisation) tags in the IOB2 format. This version
corresponds to the balanced train, dev, and test splits of Rahimi et al. (2019),
which supports 176 of the 282 languages from the original WikiANN corpus.

*   **Homepage**:
    [https://github.com/afshinrahimi/mmner](https://github.com/afshinrahimi/mmner)

*   **Source code**:
    [`tfds.text.wikiann.Wikiann`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikiann/wikiann.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `223.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'langs': Sequence(Text(shape=(), dtype=tf.string)),
    'spans': Sequence(Text(shape=(), dtype=tf.string)),
    'tags': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=7)),
    'tokens': Sequence(Text(shape=(), dtype=tf.string)),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@inproceedings{rahimi-etal-2019-massively,
    title = "Massively Multilingual Transfer for {NER}",
    author = "Rahimi, Afshin  and
      Li, Yuan  and
      Cohn, Trevor",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association     for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1015",
    pages = "151--164",
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

## wikiann/ace (default config)

*   **Config description**: Wikiann ace train/dev/test splits

*   **Dataset size**: `54.10 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/af

*   **Config description**: Wikiann af train/dev/test splits

*   **Dataset size**: `1.46 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/als

*   **Config description**: Wikiann als train/dev/test splits

*   **Dataset size**: `72.71 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/am

*   **Config description**: Wikiann am train/dev/test splits

*   **Dataset size**: `57.45 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ang

*   **Config description**: Wikiann ang train/dev/test splits

*   **Dataset size**: `54.09 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/an

*   **Config description**: Wikiann an train/dev/test splits

*   **Dataset size**: `453.48 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/arc

*   **Config description**: Wikiann arc train/dev/test splits

*   **Dataset size**: `46.72 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ar

*   **Config description**: Wikiann ar train/dev/test splits

*   **Dataset size**: `7.68 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/arz

*   **Config description**: Wikiann arz train/dev/test splits

*   **Dataset size**: `63.88 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/as

*   **Config description**: Wikiann as train/dev/test splits

*   **Dataset size**: `67.52 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ast

*   **Config description**: Wikiann ast train/dev/test splits

*   **Dataset size**: `530.44 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/ay

*   **Config description**: Wikiann ay train/dev/test splits

*   **Dataset size**: `35.33 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/az

*   **Config description**: Wikiann az train/dev/test splits

*   **Dataset size**: `2.39 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/bar

*   **Config description**: Wikiann bar train/dev/test splits

*   **Dataset size**: `43.94 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ba

*   **Config description**: Wikiann ba train/dev/test splits

*   **Dataset size**: `72.95 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/bat-smg

*   **Config description**: Wikiann bat-smg train/dev/test splits

*   **Dataset size**: `63.67 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/be

*   **Config description**: Wikiann be train/dev/test splits

*   **Dataset size**: `3.63 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 15,000
`'validation'` | 1,000

## wikiann/be-x-old

*   **Config description**: Wikiann be-x-old train/dev/test splits

*   **Dataset size**: `1.95 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/bg

*   **Config description**: Wikiann bg train/dev/test splits

*   **Dataset size**: `8.79 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/bh

*   **Config description**: Wikiann bh train/dev/test splits

*   **Dataset size**: `80.45 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/bn

*   **Config description**: Wikiann bn train/dev/test splits

*   **Dataset size**: `2.60 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/bo

*   **Config description**: Wikiann bo train/dev/test splits

*   **Dataset size**: `55.98 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/br

*   **Config description**: Wikiann br train/dev/test splits

*   **Dataset size**: `504.28 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/bs

*   **Config description**: Wikiann bs train/dev/test splits

*   **Dataset size**: `3.05 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 15,000
`'validation'` | 1,000

## wikiann/ca

*   **Config description**: Wikiann ca train/dev/test splits

*   **Dataset size**: `5.95 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/cbk-zam

*   **Config description**: Wikiann cbk-zam train/dev/test splits

*   **Dataset size**: `102.73 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/cdo

*   **Config description**: Wikiann cdo train/dev/test splits

*   **Dataset size**: `76.46 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ceb

*   **Config description**: Wikiann ceb train/dev/test splits

*   **Dataset size**: `54.40 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ce

*   **Config description**: Wikiann ce train/dev/test splits

*   **Dataset size**: `90.21 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ckb

*   **Config description**: Wikiann ckb train/dev/test splits

*   **Dataset size**: `579.97 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/co

*   **Config description**: Wikiann co train/dev/test splits

*   **Dataset size**: `41.70 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/crh

*   **Config description**: Wikiann crh train/dev/test splits

*   **Dataset size**: `53.30 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/csb

*   **Config description**: Wikiann csb train/dev/test splits

*   **Dataset size**: `64.54 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/cs

*   **Config description**: Wikiann cs train/dev/test splits

*   **Dataset size**: `7.22 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/cv

*   **Config description**: Wikiann cv train/dev/test splits

*   **Dataset size**: `66.00 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/cy

*   **Config description**: Wikiann cy train/dev/test splits

*   **Dataset size**: `2.08 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/da

*   **Config description**: Wikiann da train/dev/test splits

*   **Dataset size**: `7.14 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/de

*   **Config description**: Wikiann de train/dev/test splits

*   **Dataset size**: `7.88 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/diq

*   **Config description**: Wikiann diq train/dev/test splits

*   **Dataset size**: `53.87 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/dv

*   **Config description**: Wikiann dv train/dev/test splits

*   **Dataset size**: `73.24 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/el

*   **Config description**: Wikiann el train/dev/test splits

*   **Dataset size**: `9.26 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/eml

*   **Config description**: Wikiann eml train/dev/test splits

*   **Dataset size**: `67.16 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/en

*   **Config description**: Wikiann en train/dev/test splits

*   **Dataset size**: `6.97 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/eo

*   **Config description**: Wikiann eo train/dev/test splits

*   **Dataset size**: `5.46 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 15,000
`'validation'` | 10,000

## wikiann/es

*   **Config description**: Wikiann es train/dev/test splits

*   **Dataset size**: `6.33 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/et

*   **Config description**: Wikiann et train/dev/test splits

*   **Dataset size**: `6.31 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 15,000
`'validation'` | 10,000

## wikiann/eu

*   **Config description**: Wikiann eu train/dev/test splits

*   **Dataset size**: `5.82 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 10,000
`'validation'` | 10,000

## wikiann/ext

*   **Config description**: Wikiann ext train/dev/test splits

*   **Dataset size**: `59.86 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/fa

*   **Config description**: Wikiann fa train/dev/test splits

*   **Dataset size**: `7.82 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/fi

*   **Config description**: Wikiann fi train/dev/test splits

*   **Dataset size**: `7.51 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/fiu-vro

*   **Config description**: Wikiann fiu-vro train/dev/test splits

*   **Dataset size**: `65.91 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/fo

*   **Config description**: Wikiann fo train/dev/test splits

*   **Dataset size**: `55.92 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/frr

*   **Config description**: Wikiann frr train/dev/test splits

*   **Dataset size**: `41.98 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/fr

*   **Config description**: Wikiann fr train/dev/test splits

*   **Dataset size**: `6.46 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/fur

*   **Config description**: Wikiann fur train/dev/test splits

*   **Dataset size**: `62.83 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/fy

*   **Config description**: Wikiann fy train/dev/test splits

*   **Dataset size**: `521.68 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/gan

*   **Config description**: Wikiann gan train/dev/test splits

*   **Dataset size**: `45.24 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ga

*   **Config description**: Wikiann ga train/dev/test splits

*   **Dataset size**: `544.53 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/gd

*   **Config description**: Wikiann gd train/dev/test splits

*   **Dataset size**: `50.07 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/gl

*   **Config description**: Wikiann gl train/dev/test splits

*   **Dataset size**: `5.48 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 15,000
`'validation'` | 10,000

## wikiann/gn

*   **Config description**: Wikiann gn train/dev/test splits

*   **Dataset size**: `59.81 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/gu

*   **Config description**: Wikiann gu train/dev/test splits

*   **Dataset size**: `105.52 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/hak

*   **Config description**: Wikiann hak train/dev/test splits

*   **Dataset size**: `46.47 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/he

*   **Config description**: Wikiann he train/dev/test splits

*   **Dataset size**: `8.55 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/hi

*   **Config description**: Wikiann hi train/dev/test splits

*   **Dataset size**: `1.59 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/hr

*   **Config description**: Wikiann hr train/dev/test splits

*   **Dataset size**: `7.12 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/hsb

*   **Config description**: Wikiann hsb train/dev/test splits

*   **Dataset size**: `57.13 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/hu

*   **Config description**: Wikiann hu train/dev/test splits

*   **Dataset size**: `7.69 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/hy

*   **Config description**: Wikiann hy train/dev/test splits

*   **Dataset size**: `3.42 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 15,000
`'validation'` | 1,000

## wikiann/ia

*   **Config description**: Wikiann ia train/dev/test splits

*   **Dataset size**: `69.12 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/id

*   **Config description**: Wikiann id train/dev/test splits

*   **Dataset size**: `6.14 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/ig

*   **Config description**: Wikiann ig train/dev/test splits

*   **Dataset size**: `42.87 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ilo

*   **Config description**: Wikiann ilo train/dev/test splits

*   **Dataset size**: `44.54 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/io

*   **Config description**: Wikiann io train/dev/test splits

*   **Dataset size**: `46.46 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/is

*   **Config description**: Wikiann is train/dev/test splits

*   **Dataset size**: `552.81 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/it

*   **Config description**: Wikiann it train/dev/test splits

*   **Dataset size**: `6.86 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/ja

*   **Config description**: Wikiann ja train/dev/test splits

*   **Dataset size**: `14.80 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/jbo

*   **Config description**: Wikiann jbo train/dev/test splits

*   **Dataset size**: `42.70 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/jv

*   **Config description**: Wikiann jv train/dev/test splits

*   **Dataset size**: `46.62 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ka

*   **Config description**: Wikiann ka train/dev/test splits

*   **Dataset size**: `8.47 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 10,000
`'validation'` | 10,000

## wikiann/kk

*   **Config description**: Wikiann kk train/dev/test splits

*   **Dataset size**: `696.23 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/km

*   **Config description**: Wikiann km train/dev/test splits

*   **Dataset size**: `90.85 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/kn

*   **Config description**: Wikiann kn train/dev/test splits

*   **Dataset size**: `87.73 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ko

*   **Config description**: Wikiann ko train/dev/test splits

*   **Dataset size**: `7.81 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/ksh

*   **Config description**: Wikiann ksh train/dev/test splits

*   **Dataset size**: `57.31 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ku

*   **Config description**: Wikiann ku train/dev/test splits

*   **Dataset size**: `51.26 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ky

*   **Config description**: Wikiann ky train/dev/test splits

*   **Dataset size**: `75.74 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/la

*   **Config description**: Wikiann la train/dev/test splits

*   **Dataset size**: `1.15 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/lb

*   **Config description**: Wikiann lb train/dev/test splits

*   **Dataset size**: `1.28 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/lij

*   **Config description**: Wikiann lij train/dev/test splits

*   **Dataset size**: `61.82 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/li

*   **Config description**: Wikiann li train/dev/test splits

*   **Dataset size**: `47.45 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/lmo

*   **Config description**: Wikiann lmo train/dev/test splits

*   **Dataset size**: `60.66 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ln

*   **Config description**: Wikiann ln train/dev/test splits

*   **Dataset size**: `53.14 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/lt

*   **Config description**: Wikiann lt train/dev/test splits

*   **Dataset size**: `5.09 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 10,000
`'validation'` | 10,000

## wikiann/lv

*   **Config description**: Wikiann lv train/dev/test splits

*   **Dataset size**: `5.07 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 10,000
`'validation'` | 10,000

## wikiann/map-bms

*   **Config description**: Wikiann map-bms train/dev/test splits

*   **Dataset size**: `53.08 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mg

*   **Config description**: Wikiann mg train/dev/test splits

*   **Dataset size**: `54.92 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mhr

*   **Config description**: Wikiann mhr train/dev/test splits

*   **Dataset size**: `57.46 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/min

*   **Config description**: Wikiann min train/dev/test splits

*   **Dataset size**: `59.47 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mi

*   **Config description**: Wikiann mi train/dev/test splits

*   **Dataset size**: `75.39 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mk

*   **Config description**: Wikiann mk train/dev/test splits

*   **Dataset size**: `3.03 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/ml

*   **Config description**: Wikiann ml train/dev/test splits

*   **Dataset size**: `3.68 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/mn

*   **Config description**: Wikiann mn train/dev/test splits

*   **Dataset size**: `57.44 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mr

*   **Config description**: Wikiann mr train/dev/test splits

*   **Dataset size**: `1.88 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/ms

*   **Config description**: Wikiann ms train/dev/test splits

*   **Dataset size**: `3.33 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 20,000
`'validation'` | 1,000

## wikiann/mt

*   **Config description**: Wikiann mt train/dev/test splits

*   **Dataset size**: `56.14 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mwl

*   **Config description**: Wikiann mwl train/dev/test splits

*   **Dataset size**: `90.71 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/my

*   **Config description**: Wikiann my train/dev/test splits

*   **Dataset size**: `120.06 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/mzn

*   **Config description**: Wikiann mzn train/dev/test splits

*   **Dataset size**: `60.55 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/nap

*   **Config description**: Wikiann nap train/dev/test splits

*   **Dataset size**: `54.66 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/nds

*   **Config description**: Wikiann nds train/dev/test splits

*   **Dataset size**: `59.27 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ne

*   **Config description**: Wikiann ne train/dev/test splits

*   **Dataset size**: `86.38 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/nl

*   **Config description**: Wikiann nl train/dev/test splits

*   **Dataset size**: `7.03 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/nn

*   **Config description**: Wikiann nn train/dev/test splits

*   **Dataset size**: `4.23 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 20,000
`'validation'` | 1,000

## wikiann/no

*   **Config description**: Wikiann no train/dev/test splits

*   **Dataset size**: `7.45 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/nov

*   **Config description**: Wikiann nov train/dev/test splits

*   **Dataset size**: `41.55 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/oc

*   **Config description**: Wikiann oc train/dev/test splits

*   **Dataset size**: `47.08 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/or

*   **Config description**: Wikiann or train/dev/test splits

*   **Dataset size**: `78.96 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/os

*   **Config description**: Wikiann os train/dev/test splits

*   **Dataset size**: `64.83 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/pa

*   **Config description**: Wikiann pa train/dev/test splits

*   **Dataset size**: `65.44 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/pdc

*   **Config description**: Wikiann pdc train/dev/test splits

*   **Dataset size**: `54.89 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/pl

*   **Config description**: Wikiann pl train/dev/test splits

*   **Dataset size**: `7.25 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/pms

*   **Config description**: Wikiann pms train/dev/test splits

*   **Dataset size**: `60.25 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/pnb

*   **Config description**: Wikiann pnb train/dev/test splits

*   **Dataset size**: `51.34 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ps

*   **Config description**: Wikiann ps train/dev/test splits

*   **Dataset size**: `102.92 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/pt

*   **Config description**: Wikiann pt train/dev/test splits

*   **Dataset size**: `6.24 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/qu

*   **Config description**: Wikiann qu train/dev/test splits

*   **Dataset size**: `44.98 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/rm

*   **Config description**: Wikiann rm train/dev/test splits

*   **Dataset size**: `67.64 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ro

*   **Config description**: Wikiann ro train/dev/test splits

*   **Dataset size**: `6.57 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/ru

*   **Config description**: Wikiann ru train/dev/test splits

*   **Dataset size**: `8.39 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/rw

*   **Config description**: Wikiann rw train/dev/test splits

*   **Dataset size**: `42.88 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sah

*   **Config description**: Wikiann sah train/dev/test splits

*   **Dataset size**: `68.91 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sa

*   **Config description**: Wikiann sa train/dev/test splits

*   **Dataset size**: `120.55 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/scn

*   **Config description**: Wikiann scn train/dev/test splits

*   **Dataset size**: `47.93 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sco

*   **Config description**: Wikiann sco train/dev/test splits

*   **Dataset size**: `50.61 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sd

*   **Config description**: Wikiann sd train/dev/test splits

*   **Dataset size**: `98.67 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sh

*   **Config description**: Wikiann sh train/dev/test splits

*   **Dataset size**: `5.86 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/simple

*   **Config description**: Wikiann simple train/dev/test splits

*   **Dataset size**: `4.23 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 20,000
`'validation'` | 1,000

## wikiann/si

*   **Config description**: Wikiann si train/dev/test splits

*   **Dataset size**: `80.41 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sk

*   **Config description**: Wikiann sk train/dev/test splits

*   **Dataset size**: `7.01 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/sl

*   **Config description**: Wikiann sl train/dev/test splits

*   **Dataset size**: `5.61 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 15,000
`'validation'` | 10,000

## wikiann/so

*   **Config description**: Wikiann so train/dev/test splits

*   **Dataset size**: `48.82 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sq

*   **Config description**: Wikiann sq train/dev/test splits

*   **Dataset size**: `1.11 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 5,000
`'validation'` | 1,000

## wikiann/sr

*   **Config description**: Wikiann sr train/dev/test splits

*   **Dataset size**: `8.22 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/su

*   **Config description**: Wikiann su train/dev/test splits

*   **Dataset size**: `51.14 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/sv

*   **Config description**: Wikiann sv train/dev/test splits

*   **Dataset size**: `7.70 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/sw

*   **Config description**: Wikiann sw train/dev/test splits

*   **Dataset size**: `427.56 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/szl

*   **Config description**: Wikiann szl train/dev/test splits

*   **Dataset size**: `46.39 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/ta

*   **Config description**: Wikiann ta train/dev/test splits

*   **Dataset size**: `5.08 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 15,000
`'validation'` | 1,000

## wikiann/te

*   **Config description**: Wikiann te train/dev/test splits

*   **Dataset size**: `906.64 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/tg

*   **Config description**: Wikiann tg train/dev/test splits

*   **Dataset size**: `67.61 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/th

*   **Config description**: Wikiann th train/dev/test splits

*   **Dataset size**: `29.46 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/tk

*   **Config description**: Wikiann tk train/dev/test splits

*   **Dataset size**: `49.70 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/tl

*   **Config description**: Wikiann tl train/dev/test splits

*   **Dataset size**: `1.60 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 10,000
`'validation'` | 1,000

## wikiann/tr

*   **Config description**: Wikiann tr train/dev/test splits

*   **Dataset size**: `6.94 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/tt

*   **Config description**: Wikiann tt train/dev/test splits

*   **Dataset size**: `684.14 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/ug

*   **Config description**: Wikiann ug train/dev/test splits

*   **Dataset size**: `75.12 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/uk

*   **Config description**: Wikiann uk train/dev/test splits

*   **Dataset size**: `9.39 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/ur

*   **Config description**: Wikiann ur train/dev/test splits

*   **Dataset size**: `3.95 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 20,000
`'validation'` | 1,000

## wikiann/uz

*   **Config description**: Wikiann uz train/dev/test splits

*   **Dataset size**: `469.58 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 1,000
`'validation'` | 1,000

## wikiann/vec

*   **Config description**: Wikiann vec train/dev/test splits

*   **Dataset size**: `48.79 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/vep

*   **Config description**: Wikiann vep train/dev/test splits

*   **Dataset size**: `51.53 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/vi

*   **Config description**: Wikiann vi train/dev/test splits

*   **Dataset size**: `6.22 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/vls

*   **Config description**: Wikiann vls train/dev/test splits

*   **Dataset size**: `59.63 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/vo

*   **Config description**: Wikiann vo train/dev/test splits

*   **Dataset size**: `38.88 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/war

*   **Config description**: Wikiann war train/dev/test splits

*   **Dataset size**: `47.04 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/wa

*   **Config description**: Wikiann wa train/dev/test splits

*   **Dataset size**: `50.23 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/wuu

*   **Config description**: Wikiann wuu train/dev/test splits

*   **Dataset size**: `48.28 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/xmf

*   **Config description**: Wikiann xmf train/dev/test splits

*   **Dataset size**: `92.71 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/yi

*   **Config description**: Wikiann yi train/dev/test splits

*   **Dataset size**: `63.57 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/yo

*   **Config description**: Wikiann yo train/dev/test splits

*   **Dataset size**: `47.97 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/zea

*   **Config description**: Wikiann zea train/dev/test splits

*   **Dataset size**: `53.35 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/zh-classical

*   **Config description**: Wikiann zh-classical train/dev/test splits

*   **Dataset size**: `129.73 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/zh-min-nan

*   **Config description**: Wikiann zh-min-nan train/dev/test splits

*   **Dataset size**: `59.82 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 100
`'train'`      | 100
`'validation'` | 100

## wikiann/zh

*   **Config description**: Wikiann zh train/dev/test splits

*   **Dataset size**: `10.87 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000

## wikiann/zh-yue

*   **Config description**: Wikiann zh-yue train/dev/test splits

*   **Dataset size**: `12.62 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 20,000
`'validation'` | 10,000
