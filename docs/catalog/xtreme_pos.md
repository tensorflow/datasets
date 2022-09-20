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

*   **Download size**: `338.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

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

*   **Dataset size**: `445.94 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 194
`'test'`  | 425
`'train'` | 1,315

## xtreme_pos/xtreme_pos_ar

*   **Dataset size**: `3.35 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 909
`'test'`  | 1,680
`'train'` | 6,075

## xtreme_pos/xtreme_pos_bg

*   **Dataset size**: `2.14 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,115
`'test'`  | 1,116
`'train'` | 8,907

## xtreme_pos/xtreme_pos_de

*   **Dataset size**: `37.62 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 19,233
`'test'`  | 22,458
`'train'` | 166,849

## xtreme_pos/xtreme_pos_el

*   **Dataset size**: `7.17 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,559
`'test'`  | 2,809
`'train'` | 28,152

## xtreme_pos/xtreme_pos_en

*   **Dataset size**: `4.67 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 4,699
`'test'`  | 6,165
`'train'` | 26,825

## xtreme_pos/xtreme_pos_es

*   **Dataset size**: `8.26 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,054
`'test'`  | 3,147
`'train'` | 28,492

## xtreme_pos/xtreme_pos_et

*   **Dataset size**: `4.84 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,125
`'test'`  | 3,760
`'train'` | 25,749

## xtreme_pos/xtreme_pos_eu

*   **Dataset size**: `1.27 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,798
`'test'`  | 1,799
`'train'` | 5,396

## xtreme_pos/xtreme_pos_fa

*   **Dataset size**: `1.73 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 599
`'test'`  | 600
`'train'` | 4,798

## xtreme_pos/xtreme_pos_fi

*   **Dataset size**: `4.48 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,239
`'test'`  | 4,422
`'train'` | 27,198

## xtreme_pos/xtreme_pos_fr

*   **Dataset size**: `7.28 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 5,979
`'test'`  | 9,465
`'train'` | 47,308

## xtreme_pos/xtreme_pos_he

*   **Dataset size**: `1.57 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 484
`'test'`  | 491
`'train'` | 5,241

## xtreme_pos/xtreme_pos_hi

*   **Dataset size**: `5.78 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,884
`'test'`  | 2,909
`'train'` | 14,752

## xtreme_pos/xtreme_pos_hu

*   **Dataset size**: `438.07 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 441
`'test'`  | 449
`'train'` | 910

## xtreme_pos/xtreme_pos_id

*   **Dataset size**: `1.31 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 559
`'test'`  | 1,557
`'train'` | 4,477

## xtreme_pos/xtreme_pos_it

*   **Dataset size**: `6.85 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,278
`'test'`  | 3,518
`'train'` | 29,685

## xtreme_pos/xtreme_pos_ja

*   **Dataset size**: `3.57 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 8,938
`'test'`  | 10,253
`'train'` | 47,926

## xtreme_pos/xtreme_pos_kk

*   **Dataset size**: `167.15 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,047
`'train'` | 31

## xtreme_pos/xtreme_pos_ko

*   **Dataset size**: `5.82 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,016
`'test'`  | 4,276
`'train'` | 27,410

## xtreme_pos/xtreme_pos_mr

*   **Dataset size**: `56.14 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 46
`'test'`  | 47
`'train'` | 373

## xtreme_pos/xtreme_pos_nl

*   **Dataset size**: `2.90 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,394
`'test'`  | 1,471
`'train'` | 18,051

## xtreme_pos/xtreme_pos_pt

*   **Dataset size**: `4.65 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,770
`'test'`  | 2,681
`'train'` | 17,992

## xtreme_pos/xtreme_pos_ru

*   **Dataset size**: `20.25 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 9,960
`'test'`  | 11,336
`'train'` | 67,435

## xtreme_pos/xtreme_pos_ta

*   **Dataset size**: `3.65 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 55

## xtreme_pos/xtreme_pos_te

*   **Dataset size**: `143.77 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 131
`'test'`  | 146
`'train'` | 1,051

## xtreme_pos/xtreme_pos_th

*   **Dataset size**: `377.24 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

## xtreme_pos/xtreme_pos_tl

*   **Dataset size**: `228.78 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 80
`'test'`  | 120
`'train'` | 400

## xtreme_pos/xtreme_pos_tr

*   **Dataset size**: `1.06 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 988
`'test'`  | 4,785
`'train'` | 3,664

## xtreme_pos/xtreme_pos_ur

*   **Dataset size**: `1.50 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 552
`'test'`  | 535
`'train'` | 4,043

## xtreme_pos/xtreme_pos_vi

*   **Dataset size**: `454.32 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 800
`'test'`  | 800
`'train'` | 1,400

## xtreme_pos/xtreme_pos_yo

*   **Dataset size**: `22.65 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 100

## xtreme_pos/xtreme_pos_zh

*   **Dataset size**: `3.29 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,038
`'test'`  | 5,528
`'train'` | 18,998
