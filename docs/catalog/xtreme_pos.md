<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xtreme_pos" />
  <meta itemprop="description" content="Universal Dependencies (UD) is a framework for consistent annotation of grammar&#10;(parts of speech, morphological features, and syntactic dependencies) across&#10;different human languages. UD is an open community effort with over 200&#10;contributors producing more than 100 treebanks in over 70 languages. If you’re&#10;new to UD, you should start by reading the first part of the Short Introduction&#10;and then browsing the annotation guidelines.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xtreme_pos&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xtreme_pos" />
  <meta itemprop="sameAs" content="https://universaldependencies.org/" />
  <meta itemprop="citation" content="" />
</div>

# `xtreme_pos`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Universal Dependencies (UD) is a framework for consistent annotation of grammar
(parts of speech, morphological features, and syntactic dependencies) across
different human languages. UD is an open community effort with over 200
contributors producing more than 100 treebanks in over 70 languages. If you’re
new to UD, you should start by reading the first part of the Short Introduction
and then browsing the annotation guidelines.

*   **Homepage**:
    [https://universaldependencies.org/](https://universaldependencies.org/)

*   **Source code**:
    [`tfds.text.xtreme_pos.XtremePos`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/xtreme_pos/xtreme_pos.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'tokens': Sequence(Text(shape=(), dtype=tf.string)),
    'upos': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=18)),
})
```

*   **Feature documentation**:

Feature | Class                | Shape   | Dtype     | Description
:------ | :------------------- | :------ | :-------- | :----------
        | FeaturesDict         |         |           |
tokens  | Sequence(Text)       | (None,) | tf.string |
upos    | Sequence(ClassLabel) | (None,) | tf.int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:


## xtreme_pos/xtreme_pos_af (default config)

## xtreme_pos/xtreme_pos_ar

## xtreme_pos/xtreme_pos_bg

## xtreme_pos/xtreme_pos_de

## xtreme_pos/xtreme_pos_el

## xtreme_pos/xtreme_pos_en

## xtreme_pos/xtreme_pos_es

## xtreme_pos/xtreme_pos_et

## xtreme_pos/xtreme_pos_eu

## xtreme_pos/xtreme_pos_fa

## xtreme_pos/xtreme_pos_fi

## xtreme_pos/xtreme_pos_fr

## xtreme_pos/xtreme_pos_he

## xtreme_pos/xtreme_pos_hi

## xtreme_pos/xtreme_pos_hu

## xtreme_pos/xtreme_pos_id

## xtreme_pos/xtreme_pos_it

## xtreme_pos/xtreme_pos_ja

## xtreme_pos/xtreme_pos_kk

## xtreme_pos/xtreme_pos_ko

## xtreme_pos/xtreme_pos_mr

## xtreme_pos/xtreme_pos_nl

## xtreme_pos/xtreme_pos_pt

## xtreme_pos/xtreme_pos_ru

## xtreme_pos/xtreme_pos_ta

## xtreme_pos/xtreme_pos_te

## xtreme_pos/xtreme_pos_th

## xtreme_pos/xtreme_pos_tl

## xtreme_pos/xtreme_pos_tr

## xtreme_pos/xtreme_pos_ur

## xtreme_pos/xtreme_pos_vi

## xtreme_pos/xtreme_pos_yo

## xtreme_pos/xtreme_pos_zh
