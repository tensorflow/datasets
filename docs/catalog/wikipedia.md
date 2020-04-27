<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia" />
  <meta itemprop="description" content="Wikipedia dataset containing cleaned articles of all languages.&#10;The datasets are built from the Wikipedia dump&#10;(https://dumps.wikimedia.org/) with one split per language. Each example&#10;contains the content of one full Wikipedia article with cleaning to strip&#10;markdown and unwanted sections (references, etc.).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikipedia&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia" />
  <meta itemprop="sameAs" content="https://dumps.wikimedia.org" />
  <meta itemprop="citation" content="@ONLINE {wikidump,&#10;    author = &quot;Wikimedia Foundation&quot;,&#10;    title  = &quot;Wikimedia Downloads&quot;,&#10;    url    = &quot;https://dumps.wikimedia.org&quot;&#10;}" />
</div>
# `wikipedia`

*   **Description**:

Wikipedia dataset containing cleaned articles of all languages. The datasets are
built from the Wikipedia dump (https://dumps.wikimedia.org/) with one split per
language. Each example contains the content of one full Wikipedia article with
cleaning to strip markdown and unwanted sections (references, etc.).

*   **Homepage**: [https://dumps.wikimedia.org](https://dumps.wikimedia.org)
*   **Source code**:
    [`tfds.text.wikipedia.Wikipedia`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia.py)
*   **Versions**:
    *   **`1.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)
*   **Features**:

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```
@ONLINE {wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## wikipedia/20200301.aa (default config)

*   **Config description**: Wikipedia dataset for aa, parsed from 20200301 dump.

*   **Download size**: `44.96 KiB`
*   **Dataset size**: `3.46 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1

## wikipedia/20200301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20200301 dump.

*   **Download size**: `1.74 MiB`
*   **Dataset size**: `2.79 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,108

## wikipedia/20200301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20200301
    dump.

*   **Download size**: `2.93 MiB`

*   **Dataset size**: `3.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,501

## wikipedia/20200301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20200301
    dump.

*   **Download size**: `394.09 KiB`

*   **Dataset size**: `505.97 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 553

## wikipedia/20200301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20200301 dump.

*   **Download size**: `99.17 MiB`
*   **Dataset size**: `179.95 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 110,483

## wikipedia/20200301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20200301 dump.

*   **Download size**: `462.66 KiB`
*   **Dataset size**: `247.24 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 993

## wikipedia/20200301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20200301
    dump.

*   **Download size**: `51.03 MiB`

*   **Dataset size**: `68.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 29,318

## wikipedia/20200301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20200301 dump.

*   **Download size**: `6.82 MiB`
*   **Dataset size**: `16.64 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,400

## wikipedia/20200301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20200301 dump.

*   **Download size**: `32.94 MiB`
*   **Dataset size**: `46.63 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 50,774

## wikipedia/20200301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20200301
    dump.

*   **Download size**: `4.13 MiB`

*   **Dataset size**: `2.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,249

## wikipedia/20200301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20200301 dump.

*   **Download size**: `1.08 GiB`
*   **Dataset size**: `2.09 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,972,799

## wikipedia/20200301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20200301
    dump.

*   **Download size**: `1.03 MiB`

*   **Dataset size**: `778.26 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,305

## wikipedia/20200301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20200301
    dump.

*   **Download size**: `36.61 MiB`

*   **Dataset size**: `115.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 157,001

## wikipedia/20200301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20200301 dump.

*   **Download size**: `21.48 MiB`
*   **Dataset size**: `40.49 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,509

## wikipedia/20200301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20200301
    dump.

*   **Download size**: `217.68 MiB`

*   **Dataset size**: `445.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 108,220

## wikipedia/20200301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20200301
    dump.

*   **Download size**: `546.89 KiB`

*   **Dataset size**: `664.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,175

## wikipedia/20200301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20200301 dump.

*   **Download size**: `4.47 MiB`
*   **Dataset size**: `3.23 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,075

## wikipedia/20200301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20200301 dump.

*   **Download size**: `2.19 MiB`
*   **Dataset size**: `4.04 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,039

## wikipedia/20200301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20200301 dump.

*   **Download size**: `181.30 MiB`
*   **Dataset size**: `317.17 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 175,038

## wikipedia/20200301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20200301
    dump.

*   **Download size**: `76.38 MiB`

*   **Dataset size**: `131.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 208,456

## wikipedia/20200301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20200301 dump.

*   **Download size**: `64.46 MiB`
*   **Dataset size**: `181.18 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 56,822

## wikipedia/20200301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20200301
    dump.

*   **Download size**: `32.17 MiB`

*   **Dataset size**: `40.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 46,363

## wikipedia/20200301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20200301
    dump.

*   **Download size**: `4.82 MiB`

*   **Dataset size**: `6.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 19,665

## wikipedia/20200301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20200301
    dump.

*   **Download size**: `7.59 MiB`

*   **Dataset size**: `8.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,581

## wikipedia/20200301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20200301 dump.

*   **Download size**: `208.69 MiB`
*   **Dataset size**: `433.16 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 185,758

## wikipedia/20200301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20200301
    dump.

*   **Download size**: `79.73 MiB`

*   **Dataset size**: `178.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 99,513

## wikipedia/20200301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20200301 dump.

*   **Download size**: `344.69 MiB`
*   **Dataset size**: `866.33 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 377,391

## wikipedia/20200301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20200301 dump.

*   **Download size**: `13.79 MiB`
*   **Dataset size**: `10.36 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,035

## wikipedia/20200301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20200301 dump.

*   **Download size**: `444.50 KiB`
*   **Dataset size**: `298.56 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,392

## wikipedia/20200301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20200301
    dump.

*   **Download size**: `2.68 MiB`

*   **Dataset size**: `2.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,431

## wikipedia/20200301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20200301 dump.

*   **Download size**: `464.48 KiB`
*   **Dataset size**: `351.32 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 745

## wikipedia/20200301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20200301 dump.

*   **Download size**: `183.92 MiB`
*   **Dataset size**: `482.94 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 119,216

## wikipedia/20200301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20200301 dump.

*   **Download size**: `13.17 MiB`
*   **Dataset size**: `116.42 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,575

## wikipedia/20200301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20200301
    dump.

*   **Download size**: `5.11 MiB`

*   **Dataset size**: `39.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 25,416

## wikipedia/20200301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20200301 dump.

*   **Download size**: `50.39 MiB`
*   **Dataset size**: `72.08 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 77,940

## wikipedia/20200301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20200301 dump.

*   **Download size**: `110.31 MiB`
*   **Dataset size**: `150.33 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 185,885

## wikipedia/20200301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20200301
    dump.

*   **Download size**: `1.82 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,411

## wikipedia/20200301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20200301
    dump.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `5.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,653

## wikipedia/20200301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20200301 dump.

*   **Download size**: `899.00 MiB`
*   **Dataset size**: `1.50 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 698,894

## wikipedia/20200301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20200301
    dump.

*   **Download size**: `1.86 MiB`

*   **Dataset size**: `2.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,366

## wikipedia/20200301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20200301
    dump.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `3.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 16,785

## wikipedia/20200301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20200301 dump.

*   **Download size**: `49.70 MiB`
*   **Dataset size**: `254.09 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 259,152

## wikipedia/20200301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20200301
    dump.

*   **Download size**: `1.84 GiB`

*   **Dataset size**: `3.68 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 5,378,741

## wikipedia/20200301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20200301 dump.

*   **Download size**: `707.12 KiB`
*   **Dataset size**: `167.80 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 541

## wikipedia/20200301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20200301
    dump.

*   **Download size**: `26.88 KiB`

*   **Dataset size**: `7.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14

## wikipedia/20200301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20200301
    dump.

*   **Download size**: `644.28 KiB`

*   **Dataset size**: `629.37 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 962

## wikipedia/20200301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20200301
    dump.

*   **Download size**: `340.35 KiB`

*   **Dataset size**: `116.39 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 780

## wikipedia/20200301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20200301
    dump.

*   **Download size**: `26.96 MiB`

*   **Dataset size**: `46.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 25,695

## wikipedia/20200301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20200301 dump.

*   **Download size**: `3.54 MiB`
*   **Dataset size**: `5.85 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,465

## wikipedia/20200301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20200301 dump.

*   **Download size**: `271.60 KiB`
*   **Dataset size**: `31.60 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 120

## wikipedia/20200301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20200301
    dump.

*   **Download size**: `4.38 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,093

## wikipedia/20200301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20200301 dump.

*   **Download size**: `825.14 MiB`
*   **Dataset size**: `1.15 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 574,136

## wikipedia/20200301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20200301
    dump.

*   **Download size**: `2.13 MiB`

*   **Dataset size**: `3.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,696

## wikipedia/20200301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20200301 dump.

*   **Download size**: `665.69 KiB`
*   **Dataset size**: `672.01 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,520

## wikipedia/20200301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20200301 dump.

*   **Download size**: `23.37 MiB`
*   **Dataset size**: `59.96 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 45,907

## wikipedia/20200301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20200301 dump.

*   **Download size**: `69.14 MiB`
*   **Dataset size**: `100.36 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 147,899

## wikipedia/20200301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20200301 dump.

*   **Download size**: `341.55 MiB`
*   **Dataset size**: `457.15 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 257,349

## wikipedia/20200301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20200301 dump.

*   **Download size**: `5.32 GiB`
*   **Dataset size**: `7.52 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,104,703

## wikipedia/20200301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20200301
    dump.

*   **Download size**: `490.49 KiB`

*   **Dataset size**: `462.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 284

## wikipedia/20200301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20200301
    dump.

*   **Download size**: `8.36 MiB`

*   **Dataset size**: `7.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 16,255

## wikipedia/20200301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20200301
    dump.

*   **Download size**: `3.73 MiB`

*   **Dataset size**: `3.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,495

## wikipedia/20200301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20200301
    dump.

*   **Download size**: `6.52 MiB`

*   **Dataset size**: `5.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,559

## wikipedia/20200301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20200301 dump.

*   **Download size**: `4.35 MiB`
*   **Dataset size**: `12.40 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,262

## wikipedia/20200301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20200301 dump.

*   **Download size**: `377.61 KiB`
*   **Dataset size**: `799.74 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 294

## wikipedia/20200301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20200301 dump.

*   **Download size**: `460.80 KiB`
*   **Dataset size**: `207.60 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 381

## wikipedia/20200301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20200301 dump.

*   **Download size**: `359.36 MiB`
*   **Dataset size**: `937.56 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 244,313

## wikipedia/20200301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20200301
    dump.

*   **Download size**: `8.14 MiB`

*   **Dataset size**: `3.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,208

## wikipedia/20200301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20200301 dump.

*   **Download size**: `16.73 GiB`
*   **Dataset size**: `17.05 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 6,033,151

## wikipedia/20200301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20200301 dump.

*   **Download size**: `264.90 MiB`
*   **Dataset size**: `405.95 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 379,859

## wikipedia/20200301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20200301 dump.

*   **Download size**: `3.16 GiB`
*   **Dataset size**: `4.58 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,837,472

## wikipedia/20200301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20200301 dump.

*   **Download size**: `211.83 MiB`
*   **Dataset size**: `352.11 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 317,330

## wikipedia/20200301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20200301 dump.

*   **Download size**: `195.51 MiB`
*   **Dataset size**: `386.22 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 437,022

## wikipedia/20200301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20200301
    dump.

*   **Download size**: `2.50 MiB`

*   **Dataset size**: `3.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,486

## wikipedia/20200301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20200301 dump.

*   **Download size**: `769.97 MiB`
*   **Dataset size**: `1.33 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,316,555

## wikipedia/20200301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20200301 dump.

*   **Download size**: `417.26 KiB`
*   **Dataset size**: `280.51 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 313

## wikipedia/20200301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20200301 dump.

*   **Download size**: `703.73 MiB`
*   **Dataset size**: `923.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 656,462

## wikipedia/20200301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20200301
    dump.

*   **Download size**: `2.06 MiB`

*   **Dataset size**: `3.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,132

## wikipedia/20200301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20200301 dump.

*   **Download size**: `400.67 KiB`
*   **Dataset size**: `278.31 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 853

## wikipedia/20200301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20200301 dump.

*   **Download size**: `14.07 MiB`
*   **Dataset size**: `13.50 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,325

## wikipedia/20200301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20200301 dump.

*   **Download size**: `4.46 GiB`
*   **Dataset size**: `6.00 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,186,354

## wikipedia/20200301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20200301
    dump.

*   **Download size**: `2.19 MiB`

*   **Dataset size**: `1.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,937

## wikipedia/20200301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20200301
    dump.

*   **Download size**: `8.73 MiB`

*   **Dataset size**: `5.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,448

## wikipedia/20200301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20200301
    dump.

*   **Download size**: `2.33 MiB`

*   **Dataset size**: `3.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,563

## wikipedia/20200301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20200301 dump.

*   **Download size**: `49.88 MiB`
*   **Dataset size**: `94.24 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 43,510

## wikipedia/20200301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20200301 dump.

*   **Download size**: `27.12 MiB`
*   **Dataset size**: `43.30 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 58,490

## wikipedia/20200301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20200301
    dump.

*   **Download size**: `2.04 MiB`

*   **Dataset size**: `2.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,011

## wikipedia/20200301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20200301
    dump.

*   **Download size**: `3.85 MiB`

*   **Dataset size**: `2.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,513

## wikipedia/20200301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20200301 dump.

*   **Download size**: `8.72 MiB`
*   **Dataset size**: `12.45 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,158

## wikipedia/20200301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20200301 dump.

*   **Download size**: `254.09 MiB`
*   **Dataset size**: `376.97 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 215,685

## wikipedia/20200301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20200301
    dump.

*   **Download size**: `2.02 MiB`

*   **Dataset size**: `4.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,784

## wikipedia/20200301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20200301 dump.

*   **Download size**: `3.50 MiB`
*   **Dataset size**: `5.27 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,493

## wikipedia/20200301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20200301
    dump.

*   **Download size**: `6.24 MiB`

*   **Dataset size**: `29.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,436

## wikipedia/20200301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20200301
    dump.

*   **Download size**: `1.67 MiB`

*   **Dataset size**: `2.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,006

## wikipedia/20200301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20200301
    dump.

*   **Download size**: `673.14 KiB`

*   **Dataset size**: `1.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 940

## wikipedia/20200301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20200301 dump.

*   **Download size**: `28.55 MiB`
*   **Dataset size**: `106.99 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 29,103

## wikipedia/20200301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20200301 dump.

*   **Download size**: `5.36 MiB`
*   **Dataset size**: `4.38 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,020

## wikipedia/20200301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20200301 dump.

*   **Download size**: `2.54 MiB`
*   **Dataset size**: `3.01 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,856

## wikipedia/20200301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20200301
    dump.

*   **Download size**: `3.74 MiB`

*   **Dataset size**: `3.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,894

## wikipedia/20200301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20200301
    dump.

*   **Download size**: `1.50 MiB`

*   **Dataset size**: `2.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,308

## wikipedia/20200301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20200301 dump.

*   **Download size**: `626.91 MiB`
*   **Dataset size**: `1.36 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 424,381

## wikipedia/20200301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20200301 dump.

*   **Download size**: `151.17 MiB`
*   **Dataset size**: `520.31 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 168,552

## wikipedia/20200301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20200301
    dump.

*   **Download size**: `4.62 MiB`

*   **Dataset size**: `4.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,054

## wikipedia/20200301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20200301 dump.

*   **Download size**: `19.24 KiB`
*   **Dataset size**: `3.27 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3

## wikipedia/20200301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20200301 dump.

*   **Download size**: `261.83 MiB`
*   **Dataset size**: `389.49 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 243,050

## wikipedia/20200301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20200301
    dump.

*   **Download size**: `10.63 MiB`

*   **Dataset size**: `14.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,878

## wikipedia/20200301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20200301 dump.

*   **Download size**: `13.19 MiB`
*   **Dataset size**: `38.84 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 59,271

## wikipedia/20200301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20200301 dump.

*   **Download size**: `863.44 MiB`
*   **Dataset size**: `1.19 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 654,141

## wikipedia/20200301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20200301 dump.

*   **Download size**: `309.20 MiB`
*   **Dataset size**: `846.57 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 589,352

## wikipedia/20200301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20200301 dump.

*   **Download size**: `8.64 MiB`
*   **Dataset size**: `11.52 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 19,556

## wikipedia/20200301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20200301 dump.

*   **Download size**: `595.70 MiB`
*   **Dataset size**: `809.23 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,033,265

## wikipedia/20200301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20200301 dump.

*   **Download size**: `1.85 MiB`
*   **Dataset size**: `2.82 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,766

## wikipedia/20200301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20200301 dump.

*   **Download size**: `1.13 MiB`
*   **Dataset size**: `1.18 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,797

## wikipedia/20200301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20200301 dump.

*   **Download size**: `31.73 KiB`
*   **Dataset size**: `8.31 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14

## wikipedia/20200301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20200301 dump.

*   **Download size**: `251.48 KiB`
*   **Dataset size**: `94.27 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 669

## wikipedia/20200301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20200301
    dump.

*   **Download size**: `16.98 MiB`

*   **Dataset size**: `14.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,221

## wikipedia/20200301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20200301
    dump.

*   **Download size**: `2.15 MiB`

*   **Dataset size**: `1.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,597

## wikipedia/20200301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20200301 dump.

*   **Download size**: `13.17 MiB`
*   **Dataset size**: `29.29 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 30,720

## wikipedia/20200301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20200301 dump.

*   **Download size**: `44.88 MiB`
*   **Dataset size**: `70.66 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 70,348

## wikipedia/20200301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20200301 dump.

*   **Download size**: `2.85 GiB`
*   **Dataset size**: `3.72 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,907,437

## wikipedia/20200301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20200301 dump.

*   **Download size**: `292.01 KiB`
*   **Dataset size**: `153.39 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 512

## wikipedia/20200301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20200301 dump.

*   **Download size**: `2.95 GiB`
*   **Dataset size**: `5.33 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,459,322

## wikipedia/20200301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20200301
    dump.

*   **Download size**: `908.86 KiB`

*   **Dataset size**: `1.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,708

## wikipedia/20200301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20200301
    dump.

*   **Download size**: `1.09 MiB`

*   **Dataset size**: `2.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,320

## wikipedia/20200301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20200301 dump.

*   **Download size**: `42.41 MiB`
*   **Dataset size**: `54.26 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 75,864

## wikipedia/20200301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20200301 dump.

*   **Download size**: `142.65 MiB`
*   **Dataset size**: `480.54 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 170,803

## wikipedia/20200301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20200301
    dump.

*   **Download size**: `1.38 MiB`

*   **Dataset size**: `1.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,183

## wikipedia/20200301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20200301
    dump.

*   **Download size**: `2.99 MiB`

*   **Dataset size**: `2.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,612

## wikipedia/20200301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20200301
    dump.

*   **Download size**: `1.67 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,611

## wikipedia/20200301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20200301
    dump.

*   **Download size**: `1.33 MiB`

*   **Dataset size**: `3.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,797

## wikipedia/20200301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20200301 dump.

*   **Download size**: `452.75 KiB`
*   **Dataset size**: `255.06 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,242

## wikipedia/20200301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20200301 dump.

*   **Download size**: `377.70 KiB`
*   **Dataset size**: `310.31 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,486

## wikipedia/20200301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20200301 dump.

*   **Download size**: `17.46 KiB`
*   **Dataset size**: `4.93 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5

## wikipedia/20200301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20200301 dump.

*   **Download size**: `116.81 MiB`
*   **Dataset size**: `417.74 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 269,235

## wikipedia/20200301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20200301 dump.

*   **Download size**: `874.37 KiB`
*   **Dataset size**: `574.59 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,708

## wikipedia/20200301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20200301 dump.

*   **Download size**: `23.63 MiB`
*   **Dataset size**: `132.41 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,773

## wikipedia/20200301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20200301 dump.

*   **Download size**: `73.08 MiB`
*   **Dataset size**: `323.92 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 26,349

## wikipedia/20200301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20200301 dump.

*   **Download size**: `685.64 MiB`
*   **Dataset size**: `1.02 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,053,176

## wikipedia/20200301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20200301
    dump.

*   **Download size**: `2.18 MiB`

*   **Dataset size**: `4.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,968

## wikipedia/20200301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20200301
    dump.

*   **Download size**: `3.20 MiB`

*   **Dataset size**: `4.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,329

## wikipedia/20200301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20200301 dump.

*   **Download size**: `331.45 KiB`
*   **Dataset size**: `153.64 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 443

## wikipedia/20200301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20200301
    dump.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `2.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,375

## wikipedia/20200301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20200301 dump.

*   **Download size**: `18.20 MiB`
*   **Dataset size**: `24.55 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 34,513

## wikipedia/20200301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20200301 dump.

*   **Download size**: `3.46 MiB`
*   **Dataset size**: `8.16 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,759

## wikipedia/20200301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20200301 dump.

*   **Download size**: `1.92 MiB`
*   **Dataset size**: `1.76 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,027

## wikipedia/20200301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20200301 dump.

*   **Download size**: `33.38 MiB`
*   **Dataset size**: `146.62 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 79,687

## wikipedia/20200301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20200301 dump.

*   **Download size**: `85.88 MiB`
*   **Dataset size**: `123.90 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 132,256

## wikipedia/20200301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20200301
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `4.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,943

## wikipedia/20200301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20200301 dump.

*   **Download size**: `47.48 MiB`
*   **Dataset size**: `75.73 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 63,849

## wikipedia/20200301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20200301
    dump.

*   **Download size**: `1.30 MiB`

*   **Dataset size**: `643.83 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,549

## wikipedia/20200301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20200301
    dump.

*   **Download size**: `4.42 MiB`

*   **Dataset size**: `8.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,448

## wikipedia/20200301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20200301
    dump.

*   **Download size**: `3.65 MiB`

*   **Dataset size**: `7.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,308

## wikipedia/20200301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20200301 dump.

*   **Download size**: `1.59 MiB`
*   **Dataset size**: `3.69 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,365

## wikipedia/20200301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20200301 dump.

*   **Download size**: `14.58 MiB`
*   **Dataset size**: `25.08 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,721

## wikipedia/20200301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20200301
    dump.

*   **Download size**: `3.02 MiB`

*   **Dataset size**: `4.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,543

## wikipedia/20200301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20200301
    dump.

*   **Download size**: `21.87 MiB`

*   **Dataset size**: `28.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 45,704

## wikipedia/20200301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20200301 dump.

*   **Download size**: `1.89 MiB`
*   **Dataset size**: `1.67 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,265

## wikipedia/20200301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20200301 dump.

*   **Download size**: `4.24 MiB`
*   **Dataset size**: `11.47 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,463

## wikipedia/20200301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20200301
    dump.

*   **Download size**: `5.55 MiB`

*   **Dataset size**: `3.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,953

## wikipedia/20200301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20200301 dump.

*   **Download size**: `182.22 MiB`
*   **Dataset size**: `286.61 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 223,184

## wikipedia/20200301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20200301
    dump.

*   **Download size**: `878.96 KiB`

*   **Dataset size**: `860.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,002

## wikipedia/20200301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20200301 dump.

*   **Download size**: `137.56 MiB`
*   **Dataset size**: `170.66 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 100,641

## wikipedia/20200301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20200301
    dump.

*   **Download size**: `11.43 MiB`

*   **Dataset size**: `18.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,774

## wikipedia/20200301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20200301
    dump.

*   **Download size**: `4.55 MiB`

*   **Dataset size**: `4.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,680

## wikipedia/20200301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20200301
    dump.

*   **Download size**: `1.14 MiB`

*   **Dataset size**: `1.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,354

## wikipedia/20200301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20200301 dump.

*   **Download size**: `26.66 MiB`
*   **Dataset size**: `61.98 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 128,813

## wikipedia/20200301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20200301 dump.

*   **Download size**: `28.59 KiB`
*   **Dataset size**: `11.04 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8

## wikipedia/20200301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20200301
    dump.

*   **Download size**: `5.90 MiB`

*   **Dataset size**: `16.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 12,302

## wikipedia/20200301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20200301 dump.

*   **Download size**: `1.99 MiB`
*   **Dataset size**: `3.50 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,187

## wikipedia/20200301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20200301
    dump.

*   **Download size**: `27.69 MiB`

*   **Dataset size**: `98.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 227,688

## wikipedia/20200301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20200301 dump.

*   **Download size**: `152.75 MiB`
*   **Dataset size**: `432.82 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 145,820

## wikipedia/20200301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20200301 dump.

*   **Download size**: `130.77 MiB`
*   **Dataset size**: `340.30 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 123,672

## wikipedia/20200301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20200301 dump.

*   **Download size**: `30.40 MiB`
*   **Dataset size**: `71.21 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 24,252

## wikipedia/20200301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20200301 dump.

*   **Download size**: `53.71 MiB`
*   **Dataset size**: `149.28 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 101,310

## wikipedia/20200301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20200301
    dump.

*   **Download size**: `3.10 MiB`

*   **Dataset size**: `8.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,831

## wikipedia/20200301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20200301 dump.

*   **Download size**: `228.62 MiB`
*   **Dataset size**: `318.42 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 373,578

## wikipedia/20200301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20200301 dump.

*   **Download size**: `8.53 MiB`
*   **Dataset size**: `12.70 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,748

## wikipedia/20200301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20200301
    dump.

*   **Download size**: `15.08 KiB`

*   **Dataset size**: `875 bytes`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2

## wikipedia/20200301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20200301
    dump.

*   **Download size**: `9.09 MiB`

*   **Dataset size**: `18.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,332

## wikipedia/20200301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20200301 dump.

*   **Download size**: `37.69 MiB`
*   **Dataset size**: `177.44 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 48,451

## wikipedia/20200301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20200301
    dump.

*   **Download size**: `8.87 MiB`

*   **Dataset size**: `7.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,566

## wikipedia/20200301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20200301
    dump.

*   **Download size**: `6.63 MiB`

*   **Dataset size**: `11.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 18,486

## wikipedia/20200301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20200301 dump.

*   **Download size**: `495.83 KiB`
*   **Dataset size**: `334.74 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,319

## wikipedia/20200301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20200301
    dump.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `7.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,672

## wikipedia/20200301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20200301
    dump.

*   **Download size**: `5.15 MiB`

*   **Dataset size**: `5.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,191

## wikipedia/20200301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20200301
    dump.

*   **Download size**: `37.74 MiB`

*   **Dataset size**: `75.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 65,024

## wikipedia/20200301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20200301
    dump.

*   **Download size**: `6.92 MiB`

*   **Dataset size**: `10.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,976

## wikipedia/20200301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20200301 dump.

*   **Download size**: `32.89 MiB`
*   **Dataset size**: `86.01 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 34,609

## wikipedia/20200301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20200301
    dump.

*   **Download size**: `16.96 MiB`

*   **Dataset size**: `140.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 72,895

## wikipedia/20200301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20200301 dump.

*   **Download size**: `91.98 KiB`
*   **Dataset size**: `66.12 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 21

## wikipedia/20200301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20200301 dump.

*   **Download size**: `1.45 GiB`
*   **Dataset size**: `2.13 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,464,920

## wikipedia/20200301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20200301 dump.

*   **Download size**: `132.55 MiB`
*   **Dataset size**: `200.31 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 225,543

## wikipedia/20200301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20200301 dump.

*   **Download size**: `619.74 MiB`
*   **Dataset size**: `861.07 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 822,320

## wikipedia/20200301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20200301
    dump.

*   **Download size**: `1.14 MiB`

*   **Dataset size**: `810.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,790

## wikipedia/20200301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20200301
    dump.

*   **Download size**: `1.74 MiB`

*   **Dataset size**: `2.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,356

## wikipedia/20200301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20200301
    dump.

*   **Download size**: `2.26 MiB`

*   **Dataset size**: `2.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,248

## wikipedia/20200301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20200301 dump.

*   **Download size**: `3.48 MiB`
*   **Dataset size**: `8.00 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 12,199

## wikipedia/20200301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20200301 dump.

*   **Download size**: `1.29 MiB`
*   **Dataset size**: `752.91 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 630

## wikipedia/20200301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20200301 dump.

*   **Download size**: `73.98 MiB`
*   **Dataset size**: `110.92 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 95,125

## wikipedia/20200301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20200301
    dump.

*   **Download size**: `1.80 MiB`

*   **Dataset size**: `2.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,278

## wikipedia/20200301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20200301 dump.

*   **Download size**: `1.10 MiB`
*   **Dataset size**: `1.59 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,099

## wikipedia/20200301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20200301 dump.

*   **Download size**: `26.72 MiB`
*   **Dataset size**: `55.44 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 30,267

## wikipedia/20200301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20200301 dump.

*   **Download size**: `7.76 MiB`
*   **Dataset size**: `9.04 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,078

## wikipedia/20200301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20200301 dump.

*   **Download size**: `45.93 MiB`
*   **Dataset size**: `118.68 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 43,772

## wikipedia/20200301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20200301
    dump.

*   **Download size**: `1.32 MiB`

*   **Dataset size**: `2.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,052

## wikipedia/20200301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20200301
    dump.

*   **Download size**: `8.19 MiB`

*   **Dataset size**: `7.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,729

## wikipedia/20200301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20200301
    dump.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `1.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,116

## wikipedia/20200301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20200301
    dump.

*   **Download size**: `4.54 MiB`

*   **Dataset size**: `4.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,839

## wikipedia/20200301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20200301
    dump.

*   **Download size**: `1.12 MiB`

*   **Dataset size**: `1.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,354

## wikipedia/20200301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20200301
    dump.

*   **Download size**: `3.39 MiB`

*   **Dataset size**: `3.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,886

## wikipedia/20200301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20200301 dump.

*   **Download size**: `606.15 KiB`
*   **Dataset size**: `2.03 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,068

## wikipedia/20200301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20200301
    dump.

*   **Download size**: `726.58 KiB`

*   **Dataset size**: `213.73 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 834

## wikipedia/20200301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20200301 dump.

*   **Download size**: `1.87 GiB`
*   **Dataset size**: `2.35 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,694,759

## wikipedia/20200301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20200301
    dump.

*   **Download size**: `13.59 MiB`

*   **Dataset size**: `30.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 65,817

## wikipedia/20200301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20200301
    dump.

*   **Download size**: `38.95 MiB`

*   **Dataset size**: `97.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 57,145

## wikipedia/20200301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20200301
    dump.

*   **Download size**: `536.03 KiB`

*   **Dataset size**: `588.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 527

## wikipedia/20200301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20200301 dump.

*   **Download size**: `16.28 MiB`
*   **Dataset size**: `36.91 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 12,100

## wikipedia/20200301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20200301 dump.

*   **Download size**: `1.69 GiB`
*   **Dataset size**: `2.13 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,451,953

## wikipedia/20200301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20200301 dump.

*   **Download size**: `11.85 MiB`
*   **Dataset size**: `15.12 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 30,353

## wikipedia/20200301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20200301 dump.

*   **Download size**: `6.50 MiB`
*   **Dataset size**: `15.51 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,796

## wikipedia/20200301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20200301
    dump.

*   **Download size**: `530.59 KiB`

*   **Dataset size**: `367.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 709

## wikipedia/20200301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20200301 dump.

*   **Download size**: `796.83 KiB`
*   **Dataset size**: `347.72 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 701

## wikipedia/20200301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20200301 dump.

*   **Download size**: `478.19 MiB`
*   **Dataset size**: `661.55 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 405,150

## wikipedia/20200301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20200301
    dump.

*   **Download size**: `963.66 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,253

## wikipedia/20200301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20200301
    dump.

*   **Download size**: `5.98 MiB`

*   **Dataset size**: `6.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,297

## wikipedia/20200301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20200301 dump.

*   **Download size**: `3.77 GiB`
*   **Dataset size**: `7.62 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,592,128

## wikipedia/20200301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20200301
    dump.

*   **Download size**: `4.78 MiB`

*   **Dataset size**: `8.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,035

## wikipedia/20200301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20200301 dump.

*   **Download size**: `908.39 KiB`
*   **Dataset size**: `977.34 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,961

## wikipedia/20200301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20200301 dump.

*   **Download size**: `14.82 MiB`
*   **Dataset size**: `56.70 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 21,969

## wikipedia/20200301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20200301
    dump.

*   **Download size**: `12.32 MiB`

*   **Dataset size**: `32.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,941

## wikipedia/20200301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20200301
    dump.

*   **Download size**: `6.21 MiB`

*   **Dataset size**: `13.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,060

## wikipedia/20200301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20200301 dump.

*   **Download size**: `5.01 MiB`
*   **Dataset size**: `7.90 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,567

## wikipedia/20200301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20200301
    dump.

*   **Download size**: `11.88 MiB`

*   **Dataset size**: `16.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 31,362

## wikipedia/20200301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20200301
    dump.

*   **Download size**: `61.94 MiB`

*   **Dataset size**: `54.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 56,522

## wikipedia/20200301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20200301 dump.

*   **Download size**: `15.68 MiB`
*   **Dataset size**: `28.68 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 18,865

## wikipedia/20200301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20200301 dump.

*   **Download size**: `3.66 MiB`
*   **Dataset size**: `3.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,374

## wikipedia/20200301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20200301 dump.

*   **Download size**: `299.28 KiB`
*   **Dataset size**: `95.17 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 290

## wikipedia/20200301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20200301 dump.

*   **Download size**: `412.87 MiB`
*   **Dataset size**: `814.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,930,504

## wikipedia/20200301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20200301 dump.

*   **Download size**: `38.91 MiB`
*   **Dataset size**: `106.82 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 26,983

## wikipedia/20200301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20200301
    dump.

*   **Download size**: `172.58 MiB`

*   **Dataset size**: `181.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 155,877

## wikipedia/20200301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20200301 dump.

*   **Download size**: `265.58 MiB`
*   **Dataset size**: `345.16 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 249,815

## wikipedia/20200301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20200301 dump.

*   **Download size**: `214.19 MiB`
*   **Dataset size**: `341.62 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 197,474

## wikipedia/20200301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20200301 dump.

*   **Download size**: `723.35 KiB`
*   **Dataset size**: `677.25 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 976

## wikipedia/20200301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20200301 dump.

*   **Download size**: `2.43 MiB`
*   **Dataset size**: `3.66 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,381

## wikipedia/20200301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20200301 dump.

*   **Download size**: `8.45 MiB`
*   **Dataset size**: `9.53 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,987

## wikipedia/20200301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20200301 dump.

*   **Download size**: `83.93 MiB`
*   **Dataset size**: `140.82 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 106,777

## wikipedia/20200301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20200301 dump.

*   **Download size**: `778.54 MiB`
*   **Dataset size**: `1.51 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,091,798

## wikipedia/20200301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20200301
    dump.

*   **Download size**: `644.18 KiB`

*   **Dataset size**: `620.41 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,249

## wikipedia/20200301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20200301 dump.

*   **Download size**: `795.23 KiB`
*   **Dataset size**: `469.17 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 533

## wikipedia/20200301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20200301 dump.

*   **Download size**: `558.97 KiB`
*   **Dataset size**: `332.01 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 753

## wikipedia/20200301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20200301
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `4.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,500

## wikipedia/20200301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20200301 dump.

*   **Download size**: `24.10 MiB`
*   **Dataset size**: `39.52 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 65,709

## wikipedia/20200301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20200301 dump.

*   **Download size**: `1.68 GiB`
*   **Dataset size**: `2.93 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 5,993,395

## wikipedia/20200301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20200301 dump.

*   **Download size**: `30.67 MiB`
*   **Dataset size**: `48.36 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 55,913

## wikipedia/20200301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20200301
    dump.

*   **Download size**: `11.53 MiB`

*   **Dataset size**: `17.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 52,672

## wikipedia/20200301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20200301 dump.

*   **Download size**: `154.80 MiB`
*   **Dataset size**: `604.28 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 161,622

## wikipedia/20200301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20200301
    dump.

*   **Download size**: `2.81 MiB`

*   **Dataset size**: `6.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,536

## wikipedia/20200301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20200301 dump.

*   **Download size**: `102.37 MiB`
*   **Dataset size**: `556.43 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 93,223

## wikipedia/20200301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20200301
    dump.

*   **Download size**: `1.25 MiB`

*   **Dataset size**: `1.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,600

## wikipedia/20200301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20200301 dump.

*   **Download size**: `39.93 MiB`
*   **Dataset size**: `106.84 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 101,637

## wikipedia/20200301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20200301 dump.

*   **Download size**: `271.37 MiB`
*   **Dataset size**: `789.74 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 235,109

## wikipedia/20200301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20200301 dump.

*   **Download size**: `365.94 KiB`
*   **Dataset size**: `369.20 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 347

## wikipedia/20200301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20200301 dump.

*   **Download size**: `4.61 MiB`
*   **Dataset size**: `9.94 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,869

## wikipedia/20200301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20200301 dump.

*   **Download size**: `54.88 MiB`
*   **Dataset size**: `61.05 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 75,676

## wikipedia/20200301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20200301 dump.

*   **Download size**: `1.40 MiB`
*   **Dataset size**: `1.45 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 828

## wikipedia/20200301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20200301 dump.

*   **Download size**: `797.75 KiB`
*   **Dataset size**: `911.82 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,623

## wikipedia/20200301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20200301
    dump.

*   **Download size**: `1.43 MiB`

*   **Dataset size**: `399.11 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,639

## wikipedia/20200301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20200301 dump.

*   **Download size**: `534.01 MiB`
*   **Dataset size**: `662.27 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 575,697

## wikipedia/20200301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20200301 dump.

*   **Download size**: `1.43 MiB`
*   **Dataset size**: `701.00 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 697

## wikipedia/20200301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20200301 dump.

*   **Download size**: `58.06 MiB`
*   **Dataset size**: `134.13 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 130,169

## wikipedia/20200301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20200301
    dump.

*   **Download size**: `333.38 KiB`

*   **Dataset size**: `212.55 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 708

## wikipedia/20200301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20200301 dump.

*   **Download size**: `413.61 KiB`
*   **Dataset size**: `290.86 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 766

## wikipedia/20200301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20200301 dump.

*   **Download size**: `502.60 KiB`
*   **Dataset size**: `249.88 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,285

## wikipedia/20200301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20200301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `7.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,879

## wikipedia/20200301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20200301
    dump.

*   **Download size**: `3.21 MiB`

*   **Dataset size**: `5.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,067

## wikipedia/20200301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20200301 dump.

*   **Download size**: `5.94 MiB`
*   **Dataset size**: `27.87 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,247

## wikipedia/20200301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20200301 dump.

*   **Download size**: `1.45 GiB`
*   **Dataset size**: `3.35 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,347,474

## wikipedia/20200301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20200301 dump.

*   **Download size**: `143.42 MiB`
*   **Dataset size**: `222.05 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 342,368

## wikipedia/20200301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20200301 dump.

*   **Download size**: `62.85 MiB`
*   **Dataset size**: `94.39 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 154,674

## wikipedia/20200301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20200301 dump.

*   **Download size**: `278.29 KiB`
*   **Dataset size**: `210.46 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 450

## wikipedia/20200301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20200301
    dump.

*   **Download size**: `11.77 MiB`

*   **Dataset size**: `14.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 22,587

## wikipedia/20200301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20200301
    dump.

*   **Download size**: `5.58 MiB`

*   **Dataset size**: `8.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,767

## wikipedia/20200301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20200301 dump.

*   **Download size**: `708.12 MiB`
*   **Dataset size**: `1.22 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,435,673

## wikipedia/20200301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20200301
    dump.

*   **Download size**: `6.85 MiB`

*   **Dataset size**: `10.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,564

## wikipedia/20200301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20200301 dump.

*   **Download size**: `24.16 MiB`
*   **Dataset size**: `80.36 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 124,186

## wikipedia/20200301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20200301 dump.

*   **Download size**: `9.23 MiB`
*   **Dataset size**: `14.37 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 16,047

## wikipedia/20200301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20200301
    dump.

*   **Download size**: `257.48 MiB`

*   **Dataset size**: `412.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,264,120

## wikipedia/20200301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20200301 dump.

*   **Download size**: `1.84 MiB`
*   **Dataset size**: `3.06 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,604

## wikipedia/20200301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20200301
    dump.

*   **Download size**: `12.24 MiB`

*   **Dataset size**: `16.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 30,773

## wikipedia/20200301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20200301
    dump.

*   **Download size**: `1.66 MiB`

*   **Dataset size**: `1.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,797

## wikipedia/20200301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20200301 dump.

*   **Download size**: `1.38 MiB`
*   **Dataset size**: `1.65 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,342

## wikipedia/20200301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20200301
    dump.

*   **Download size**: `10.50 MiB`

*   **Dataset size**: `25.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,349

## wikipedia/20200301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20200301 dump.

*   **Download size**: `12.02 MiB`
*   **Dataset size**: `32.21 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 24,376

## wikipedia/20200301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20200301 dump.

*   **Download size**: `12.32 MiB`
*   **Dataset size**: `10.02 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 32,530

## wikipedia/20200301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20200301 dump.

*   **Download size**: `772.04 KiB`
*   **Dataset size**: `708.21 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,491

## wikipedia/20200301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20200301
    dump.

*   **Download size**: `2.52 MiB`

*   **Dataset size**: `4.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,575

## wikipedia/20200301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20200301 dump.

*   **Download size**: `1.87 GiB`
*   **Dataset size**: `1.94 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,577,556

## wikipedia/20200301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20200301 dump.

*   **Download size**: `14.44 MiB`

*   **Dataset size**: `9.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,897

## wikipedia/20200301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20200301 dump.

*   **Download size**: `55.69 MiB`

*   **Dataset size**: `79.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 280,886

## wikipedia/20200301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20200301
    dump.

*   **Download size**: `57.83 MiB`

*   **Dataset size**: `61.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 77,025

## wikipedia/20200301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20200301 dump.

*   **Download size**: `1.81 MiB`
*   **Dataset size**: `1.28 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,562

## wikipedia/20190301.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20190301 dump.

*   **Download size**: `44.09 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1

## wikipedia/20190301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20190301 dump.

*   **Download size**: `1.31 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,053

## wikipedia/20190301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20190301
    dump.

*   **Download size**: `2.66 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,264

## wikipedia/20190301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20190301
    dump.

*   **Download size**: `349.43 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 547

## wikipedia/20190301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20190301 dump.

*   **Download size**: `84.13 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 92,366

## wikipedia/20190301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20190301 dump.

*   **Download size**: `377.84 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 628

## wikipedia/20190301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20190301
    dump.

*   **Download size**: `46.90 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 27,705

## wikipedia/20190301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20190301 dump.

*   **Download size**: `6.54 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,231

## wikipedia/20190301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20190301 dump.

*   **Download size**: `31.39 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 47,536

## wikipedia/20190301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20190301
    dump.

*   **Download size**: `3.77 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,135

## wikipedia/20190301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20190301 dump.

*   **Download size**: `805.82 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,272,226

## wikipedia/20190301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20190301
    dump.

*   **Download size**: `952.49 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,272

## wikipedia/20190301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20190301
    dump.

*   **Download size**: `20.32 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 28,136

## wikipedia/20190301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20190301 dump.

*   **Download size**: `19.06 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,435

## wikipedia/20190301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20190301
    dump.

*   **Download size**: `216.68 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 106,275

## wikipedia/20190301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20190301
    dump.

*   **Download size**: `467.05 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,005

## wikipedia/20190301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20190301 dump.

*   **Download size**: `3.61 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,918

## wikipedia/20190301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20190301 dump.

*   **Download size**: `2.06 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,773

## wikipedia/20190301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20190301 dump.

*   **Download size**: `163.04 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 161,901

## wikipedia/20190301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20190301
    dump.

*   **Download size**: `50.59 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 159,459

## wikipedia/20190301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20190301 dump.

*   **Download size**: `55.04 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 51,934

## wikipedia/20190301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20190301
    dump.

*   **Download size**: `30.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 42,237

## wikipedia/20190301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20190301
    dump.

*   **Download size**: `4.61 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 19,344

## wikipedia/20190301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20190301
    dump.

*   **Download size**: `6.18 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,025

## wikipedia/20190301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20190301 dump.

*   **Download size**: `192.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 164,589

## wikipedia/20190301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20190301
    dump.

*   **Download size**: `74.77 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 93,527

## wikipedia/20190301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20190301 dump.

*   **Download size**: `326.20 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 362,723

## wikipedia/20190301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20190301 dump.

*   **Download size**: `13.28 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,725

## wikipedia/20190301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20190301 dump.

*   **Download size**: `424.88 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,352

## wikipedia/20190301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20190301
    dump.

*   **Download size**: `2.09 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,476

## wikipedia/20190301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20190301 dump.

*   **Download size**: `447.98 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 729

## wikipedia/20190301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20190301 dump.

*   **Download size**: `145.04 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 87,566

## wikipedia/20190301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20190301 dump.

*   **Download size**: `12.41 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,301

## wikipedia/20190301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20190301
    dump.

*   **Download size**: `5.05 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 25,360

## wikipedia/20190301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20190301 dump.

*   **Download size**: `49.14 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 76,055

## wikipedia/20190301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20190301 dump.

*   **Download size**: `103.26 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 181,802

## wikipedia/20190301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20190301
    dump.

*   **Download size**: `1.76 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,378

## wikipedia/20190301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20190301
    dump.

*   **Download size**: `3.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,594

## wikipedia/20190301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20190301 dump.

*   **Download size**: `849.65 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 650,189

## wikipedia/20190301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20190301
    dump.

*   **Download size**: `1.84 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,289

## wikipedia/20190301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20190301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,422

## wikipedia/20190301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20190301 dump.

*   **Download size**: `43.89 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 213,978

## wikipedia/20190301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20190301
    dump.

*   **Download size**: `1.79 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 5,379,484

## wikipedia/20190301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20190301 dump.

*   **Download size**: `684.97 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 496

## wikipedia/20190301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20190301
    dump.

*   **Download size**: `25.99 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14

## wikipedia/20190301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20190301
    dump.

*   **Download size**: `651.25 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 947

## wikipedia/20190301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20190301
    dump.

*   **Download size**: `325.90 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 773

## wikipedia/20190301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20190301
    dump.

*   **Download size**: `22.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 23,099

## wikipedia/20190301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20190301 dump.

*   **Download size**: `3.38 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,232

## wikipedia/20190301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20190301 dump.

*   **Download size**: `259.71 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 118

## wikipedia/20190301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20190301
    dump.

*   **Download size**: `4.01 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,341

## wikipedia/20190301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20190301 dump.

*   **Download size**: `759.21 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 539,754

## wikipedia/20190301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20190301
    dump.

*   **Download size**: `2.03 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,620

## wikipedia/20190301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20190301 dump.

*   **Download size**: `631.49 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,463

## wikipedia/20190301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20190301 dump.

*   **Download size**: `22.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 44,865

## wikipedia/20190301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20190301 dump.

*   **Download size**: `64.37 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 142,397

## wikipedia/20190301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20190301 dump.

*   **Download size**: `323.53 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 244,767

## wikipedia/20190301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20190301 dump.

*   **Download size**: `4.97 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,925,588

## wikipedia/20190301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20190301
    dump.

*   **Download size**: `457.06 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 228

## wikipedia/20190301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20190301
    dump.

*   **Download size**: `7.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,948

## wikipedia/20190301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20190301
    dump.

*   **Download size**: `3.54 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,438

## wikipedia/20190301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20190301
    dump.

*   **Download size**: `4.95 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,323

## wikipedia/20190301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20190301 dump.

*   **Download size**: `4.24 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,156

## wikipedia/20190301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20190301 dump.

*   **Download size**: `360.01 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 286

## wikipedia/20190301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20190301 dump.

*   **Download size**: `434.14 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 368

## wikipedia/20190301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20190301 dump.

*   **Download size**: `324.40 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 224,159

## wikipedia/20190301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20190301
    dump.

*   **Download size**: `7.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,957

## wikipedia/20190301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20190301 dump.

*   **Download size**: `15.72 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 5,824,596

## wikipedia/20190301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20190301 dump.

*   **Download size**: `245.73 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 353,663

## wikipedia/20190301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20190301 dump.

*   **Download size**: `2.93 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,728,167

## wikipedia/20190301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20190301 dump.

*   **Download size**: `196.03 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 288,641

## wikipedia/20190301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20190301 dump.

*   **Download size**: `180.35 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 400,162

## wikipedia/20190301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20190301
    dump.

*   **Download size**: `2.40 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,278

## wikipedia/20190301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20190301 dump.

*   **Download size**: `693.84 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,201,990

## wikipedia/20190301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20190301 dump.

*   **Download size**: `387.75 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 298

## wikipedia/20190301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20190301 dump.

*   **Download size**: `656.44 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 619,207

## wikipedia/20190301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20190301
    dump.

*   **Download size**: `2.00 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,050

## wikipedia/20190301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20190301 dump.

*   **Download size**: `262.98 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 507

## wikipedia/20190301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20190301 dump.

*   **Download size**: `13.67 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 12,935

## wikipedia/20190301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20190301 dump.

*   **Download size**: `4.14 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,087,215

## wikipedia/20190301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20190301
    dump.

*   **Download size**: `2.03 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,262

## wikipedia/20190301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20190301
    dump.

*   **Download size**: `7.88 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,706

## wikipedia/20190301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20190301
    dump.

*   **Download size**: `2.29 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,508

## wikipedia/20190301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20190301 dump.

*   **Download size**: `45.52 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 41,573

## wikipedia/20190301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20190301 dump.

*   **Download size**: `24.78 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 56,252

## wikipedia/20190301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20190301
    dump.

*   **Download size**: `2.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,034

## wikipedia/20190301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20190301
    dump.

*   **Download size**: `3.82 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,503

## wikipedia/20190301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20190301 dump.

*   **Download size**: `8.51 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,891

## wikipedia/20190301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20190301 dump.

*   **Download size**: `235.07 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 203,961

## wikipedia/20190301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20190301
    dump.

*   **Download size**: `1.91 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,432

## wikipedia/20190301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20190301 dump.

*   **Download size**: `3.37 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,337

## wikipedia/20190301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20190301
    dump.

*   **Download size**: `6.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,259

## wikipedia/20190301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20190301
    dump.

*   **Download size**: `1.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,467

## wikipedia/20190301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20190301
    dump.

*   **Download size**: `604.10 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 715

## wikipedia/20190301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20190301 dump.

*   **Download size**: `27.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 28,607

## wikipedia/20190301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20190301 dump.

*   **Download size**: `5.32 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,996

## wikipedia/20190301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20190301 dump.

*   **Download size**: `1.62 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,795

## wikipedia/20190301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20190301
    dump.

*   **Download size**: `3.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,445

## wikipedia/20190301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20190301
    dump.

*   **Download size**: `1017.76 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,935

## wikipedia/20190301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20190301 dump.

*   **Download size**: `572.30 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 393,436

## wikipedia/20190301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20190301 dump.

*   **Download size**: `137.86 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 156,142

## wikipedia/20190301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20190301
    dump.

*   **Download size**: `4.57 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,036

## wikipedia/20190301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20190301 dump.

*   **Download size**: `18.37 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3

## wikipedia/20190301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20190301 dump.

*   **Download size**: `246.05 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 228,044

## wikipedia/20190301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20190301
    dump.

*   **Download size**: `10.38 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,693

## wikipedia/20190301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20190301 dump.

*   **Download size**: `10.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 56,093

## wikipedia/20190301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20190301 dump.

*   **Download size**: `810.17 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 625,614

## wikipedia/20190301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20190301 dump.

*   **Download size**: `277.53 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 575,357

## wikipedia/20190301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20190301 dump.

*   **Download size**: `7.85 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 18,780

## wikipedia/20190301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20190301 dump.

*   **Download size**: `523.94 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 947,627

## wikipedia/20190301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20190301 dump.

*   **Download size**: `1.70 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,403

## wikipedia/20190301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20190301 dump.

*   **Download size**: `1.00 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,710

## wikipedia/20190301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20190301 dump.

*   **Download size**: `30.88 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14

## wikipedia/20190301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20190301 dump.

*   **Download size**: `238.12 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 647

## wikipedia/20190301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20190301
    dump.

*   **Download size**: `15.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 11,808

## wikipedia/20190301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20190301
    dump.

*   **Download size**: `1.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 932

## wikipedia/20190301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20190301 dump.

*   **Download size**: `12.56 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 29,629

## wikipedia/20190301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20190301 dump.

*   **Download size**: `41.86 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 66,219

## wikipedia/20190301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20190301 dump.

*   **Download size**: `2.66 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,800,218

## wikipedia/20190301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20190301 dump.

*   **Download size**: `284.06 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 510

## wikipedia/20190301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20190301 dump.

*   **Download size**: `2.74 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,382,683

## wikipedia/20190301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20190301
    dump.

*   **Download size**: `895.29 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,692

## wikipedia/20190301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20190301
    dump.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,301

## wikipedia/20190301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20190301 dump.

*   **Download size**: `39.32 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 72,893

## wikipedia/20190301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20190301 dump.

*   **Download size**: `131.78 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 161,290

## wikipedia/20190301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20190301
    dump.

*   **Download size**: `1.35 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,192

## wikipedia/20190301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20190301
    dump.

*   **Download size**: `3.62 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,415

## wikipedia/20190301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20190301
    dump.

*   **Download size**: `1.65 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,608

## wikipedia/20190301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20190301
    dump.

*   **Download size**: `1.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,706

## wikipedia/20190301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20190301 dump.

*   **Download size**: `439.26 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,240

## wikipedia/20190301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20190301 dump.

*   **Download size**: `370.78 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,482

## wikipedia/20190301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20190301 dump.

*   **Download size**: `16.58 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5

## wikipedia/20190301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20190301 dump.

*   **Download size**: `113.46 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 266,609

## wikipedia/20190301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20190301 dump.

*   **Download size**: `862.51 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,713

## wikipedia/20190301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20190301 dump.

*   **Download size**: `21.92 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,889

## wikipedia/20190301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20190301 dump.

*   **Download size**: `69.62 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 24,679

## wikipedia/20190301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20190301 dump.

*   **Download size**: `625.16 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 980,493

## wikipedia/20190301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20190301
    dump.

*   **Download size**: `2.12 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,964

## wikipedia/20190301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20190301
    dump.

*   **Download size**: `3.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,317

## wikipedia/20190301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20190301 dump.

*   **Download size**: `309.15 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 399

## wikipedia/20190301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20190301
    dump.

*   **Download size**: `3.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,356

## wikipedia/20190301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20190301 dump.

*   **Download size**: `17.09 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 30,811

## wikipedia/20190301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20190301 dump.

*   **Download size**: `3.36 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,733

## wikipedia/20190301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20190301 dump.

*   **Download size**: `1.71 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,913

## wikipedia/20190301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20190301 dump.

*   **Download size**: `33.13 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 79,311

## wikipedia/20190301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20190301 dump.

*   **Download size**: `82.72 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 130,161

## wikipedia/20190301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20190301
    dump.

*   **Download size**: `3.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,261

## wikipedia/20190301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20190301 dump.

*   **Download size**: `45.70 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 61,607

## wikipedia/20190301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20190301
    dump.

*   **Download size**: `1.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,545

## wikipedia/20190301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20190301
    dump.

*   **Download size**: `4.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,348

## wikipedia/20190301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20190301
    dump.

*   **Download size**: `2.81 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,741

## wikipedia/20190301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20190301 dump.

*   **Download size**: `1.58 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,359

## wikipedia/20190301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20190301 dump.

*   **Download size**: `13.86 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,155

## wikipedia/20190301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20190301
    dump.

*   **Download size**: `2.73 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,281

## wikipedia/20190301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20190301
    dump.

*   **Download size**: `21.34 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 43,911

## wikipedia/20190301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20190301 dump.

*   **Download size**: `1.83 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,192

## wikipedia/20190301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20190301 dump.

*   **Download size**: `3.44 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,074

## wikipedia/20190301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20190301
    dump.

*   **Download size**: `4.71 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,774

## wikipedia/20190301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20190301 dump.

*   **Download size**: `174.73 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 217,121

## wikipedia/20190301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20190301
    dump.

*   **Download size**: `798.18 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 920

## wikipedia/20190301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20190301 dump.

*   **Download size**: `127.47 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 91,567

## wikipedia/20190301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20190301
    dump.

*   **Download size**: `10.80 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,523

## wikipedia/20190301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20190301
    dump.

*   **Download size**: `4.49 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,710

## wikipedia/20190301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20190301
    dump.

*   **Download size**: `1.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,344

## wikipedia/20190301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20190301 dump.

*   **Download size**: `25.64 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 126,066

## wikipedia/20190301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20190301 dump.

*   **Download size**: `27.71 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8

## wikipedia/20190301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20190301
    dump.

*   **Download size**: `5.69 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 12,204

## wikipedia/20190301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20190301 dump.

*   **Download size**: `1.96 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,174

## wikipedia/20190301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20190301
    dump.

*   **Download size**: `25.05 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 226,002

## wikipedia/20190301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20190301 dump.

*   **Download size**: `140.69 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 138,779

## wikipedia/20190301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20190301 dump.

*   **Download size**: `117.24 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 112,979

## wikipedia/20190301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20190301 dump.

*   **Download size**: `28.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 23,195

## wikipedia/20190301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20190301 dump.

*   **Download size**: `49.58 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 95,825

## wikipedia/20190301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20190301
    dump.

*   **Download size**: `3.01 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,826

## wikipedia/20190301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20190301 dump.

*   **Download size**: `205.79 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 357,957

## wikipedia/20190301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20190301 dump.

*   **Download size**: `8.21 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,610

## wikipedia/20190301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20190301
    dump.

*   **Download size**: `14.20 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2

## wikipedia/20190301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20190301
    dump.

*   **Download size**: `8.95 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,279

## wikipedia/20190301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20190301 dump.

*   **Download size**: `34.60 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 46,348

## wikipedia/20190301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20190301
    dump.

*   **Download size**: `7.79 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,077

## wikipedia/20190301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20190301
    dump.

*   **Download size**: `6.47 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 18,184

## wikipedia/20190301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20190301 dump.

*   **Download size**: `480.57 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,316

## wikipedia/20190301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20190301
    dump.

*   **Download size**: `4.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,613

## wikipedia/20190301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20190301
    dump.

*   **Download size**: `5.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,167

## wikipedia/20190301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20190301
    dump.

*   **Download size**: `33.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 45,754

## wikipedia/20190301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20190301
    dump.

*   **Download size**: `6.67 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,644

## wikipedia/20190301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20190301 dump.

*   **Download size**: `29.26 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 33,465

## wikipedia/20190301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20190301
    dump.

*   **Download size**: `16.91 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 72,872

## wikipedia/20190301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20190301 dump.

*   **Download size**: `91.11 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 21

## wikipedia/20190301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20190301 dump.

*   **Download size**: `1.38 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,409,491

## wikipedia/20190301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20190301 dump.

*   **Download size**: `126.01 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 213,859

## wikipedia/20190301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20190301 dump.

*   **Download size**: `610.74 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 783,420

## wikipedia/20190301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20190301
    dump.

*   **Download size**: `1.12 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,780

## wikipedia/20190301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20190301
    dump.

*   **Download size**: `1.56 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,048

## wikipedia/20190301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20190301
    dump.

*   **Download size**: `2.20 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,075

## wikipedia/20190301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20190301 dump.

*   **Download size**: `2.52 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,105

## wikipedia/20190301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20190301 dump.

*   **Download size**: `1.18 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 566

## wikipedia/20190301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20190301 dump.

*   **Download size**: `70.97 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 91,840

## wikipedia/20190301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20190301
    dump.

*   **Download size**: `1.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,348

## wikipedia/20190301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20190301 dump.

*   **Download size**: `1.06 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,054

## wikipedia/20190301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20190301 dump.

*   **Download size**: `24.90 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 28,368

## wikipedia/20190301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20190301 dump.

*   **Download size**: `7.31 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,490

## wikipedia/20190301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20190301 dump.

*   **Download size**: `40.39 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 40,578

## wikipedia/20190301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20190301
    dump.

*   **Download size**: `1.29 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,042

## wikipedia/20190301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20190301
    dump.

*   **Download size**: `8.17 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,721

## wikipedia/20190301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20190301
    dump.

*   **Download size**: `1.33 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,126

## wikipedia/20190301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20190301
    dump.

*   **Download size**: `4.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,485

## wikipedia/20190301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20190301
    dump.

*   **Download size**: `1.10 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,331

## wikipedia/20190301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20190301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,744

## wikipedia/20190301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20190301 dump.

*   **Download size**: `586.77 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,057

## wikipedia/20190301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20190301
    dump.

*   **Download size**: `654.11 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 748

## wikipedia/20190301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20190301 dump.

*   **Download size**: `1.76 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,610,189

## wikipedia/20190301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20190301
    dump.

*   **Download size**: `13.42 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 65,551

## wikipedia/20190301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20190301
    dump.

*   **Download size**: `24.31 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 50,764

## wikipedia/20190301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20190301
    dump.

*   **Download size**: `533.84 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 521

## wikipedia/20190301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20190301 dump.

*   **Download size**: `14.09 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,554

## wikipedia/20190301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20190301 dump.

*   **Download size**: `1.58 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,393,069

## wikipedia/20190301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20190301 dump.

*   **Download size**: `11.42 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 29,495

## wikipedia/20190301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20190301 dump.

*   **Download size**: `5.85 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 3,710

## wikipedia/20190301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20190301
    dump.

*   **Download size**: `509.61 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 693

## wikipedia/20190301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20190301 dump.

*   **Download size**: `779.25 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 696

## wikipedia/20190301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20190301 dump.

*   **Download size**: `449.49 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 393,012

## wikipedia/20190301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20190301
    dump.

*   **Download size**: `931.23 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,245

## wikipedia/20190301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20190301
    dump.

*   **Download size**: `5.98 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 9,288

## wikipedia/20190301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20190301 dump.

*   **Download size**: `3.51 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 2,449,364

## wikipedia/20190301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20190301
    dump.

*   **Download size**: `4.11 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,526

## wikipedia/20190301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20190301 dump.

*   **Download size**: `904.81 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,950

## wikipedia/20190301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20190301 dump.

*   **Download size**: `14.29 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 21,846

## wikipedia/20190301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20190301
    dump.

*   **Download size**: `11.88 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,504

## wikipedia/20190301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20190301
    dump.

*   **Download size**: `2.36 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,036

## wikipedia/20190301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20190301 dump.

*   **Download size**: `4.39 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,214

## wikipedia/20190301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20190301
    dump.

*   **Download size**: `11.83 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 31,330

## wikipedia/20190301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20190301
    dump.

*   **Download size**: `57.80 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 53,525

## wikipedia/20190301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20190301 dump.

*   **Download size**: `12.62 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 16,930

## wikipedia/20190301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20190301 dump.

*   **Download size**: `3.30 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,127

## wikipedia/20190301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20190301 dump.

*   **Download size**: `286.02 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 281

## wikipedia/20190301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20190301 dump.

*   **Download size**: `406.72 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,923,606

## wikipedia/20190301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20190301 dump.

*   **Download size**: `36.84 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 25,922

## wikipedia/20190301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20190301
    dump.

*   **Download size**: `156.11 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 143,427

## wikipedia/20190301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20190301 dump.

*   **Download size**: `254.37 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 244,877

## wikipedia/20190301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20190301 dump.

*   **Download size**: `201.41 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 191,938

## wikipedia/20190301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20190301 dump.

*   **Download size**: `678.46 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 957

## wikipedia/20190301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20190301 dump.

*   **Download size**: `2.02 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,656

## wikipedia/20190301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20190301 dump.

*   **Download size**: `8.17 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,587

## wikipedia/20190301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20190301 dump.

*   **Download size**: `77.55 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 102,156

## wikipedia/20190301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20190301 dump.

*   **Download size**: `725.30 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,043,191

## wikipedia/20190301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20190301
    dump.

*   **Download size**: `634.21 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,234

## wikipedia/20190301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20190301 dump.

*   **Download size**: `737.58 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 495

## wikipedia/20190301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20190301 dump.

*   **Download size**: `482.27 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 605

## wikipedia/20190301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20190301
    dump.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 4,477

## wikipedia/20190301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20190301 dump.

*   **Download size**: `20.52 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 43,393

## wikipedia/20190301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20190301 dump.

*   **Download size**: `1.64 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 5,950,503

## wikipedia/20190301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20190301 dump.

*   **Download size**: `27.60 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 48,434

## wikipedia/20190301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20190301
    dump.

*   **Download size**: `4.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 8,603

## wikipedia/20190301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20190301 dump.

*   **Download size**: `141.07 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 154,505

## wikipedia/20190301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20190301
    dump.

*   **Download size**: `2.33 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,267

## wikipedia/20190301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20190301 dump.

*   **Download size**: `113.16 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 91,857

## wikipedia/20190301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20190301
    dump.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,556

## wikipedia/20190301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20190301 dump.

*   **Download size**: `36.95 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 96,808

## wikipedia/20190301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20190301 dump.

*   **Download size**: `254.00 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 224,144

## wikipedia/20190301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20190301 dump.

*   **Download size**: `309.72 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 304

## wikipedia/20190301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20190301 dump.

*   **Download size**: `4.50 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 6,743

## wikipedia/20190301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20190301 dump.

*   **Download size**: `50.85 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 76,905

## wikipedia/20190301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20190301 dump.

*   **Download size**: `1.21 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 751

## wikipedia/20190301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20190301 dump.

*   **Download size**: `775.10 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,577

## wikipedia/20190301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20190301
    dump.

*   **Download size**: `1.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,523

## wikipedia/20190301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20190301 dump.

*   **Download size**: `497.19 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 548,768

## wikipedia/20190301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20190301 dump.

*   **Download size**: `1.39 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 665

## wikipedia/20190301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20190301 dump.

*   **Download size**: `53.23 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 120,720

## wikipedia/20190301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20190301
    dump.

*   **Download size**: `309.58 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 638

## wikipedia/20190301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20190301 dump.

*   **Download size**: `345.96 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 697

## wikipedia/20190301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20190301 dump.

*   **Download size**: `485.56 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,279

## wikipedia/20190301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20190301
    dump.

*   **Download size**: `2.60 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,563

## wikipedia/20190301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20190301
    dump.

*   **Download size**: `2.94 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,768

## wikipedia/20190301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20190301 dump.

*   **Download size**: `5.64 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,908

## wikipedia/20190301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20190301 dump.

*   **Download size**: `1.28 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,131,279

## wikipedia/20190301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20190301 dump.

*   **Download size**: `129.57 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 330,776

## wikipedia/20190301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20190301 dump.

*   **Download size**: `60.85 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 149,537

## wikipedia/20190301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20190301 dump.

*   **Download size**: `257.59 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 337

## wikipedia/20190301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20190301
    dump.

*   **Download size**: `10.65 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 13,433

## wikipedia/20190301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20190301
    dump.

*   **Download size**: `4.59 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,230

## wikipedia/20190301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20190301 dump.

*   **Download size**: `623.74 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,377,623

## wikipedia/20190301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20190301
    dump.

*   **Download size**: `6.58 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 7,233

## wikipedia/20190301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20190301 dump.

*   **Download size**: `23.80 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 122,640

## wikipedia/20190301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20190301 dump.

*   **Download size**: `8.75 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 15,283

## wikipedia/20190301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20190301
    dump.

*   **Download size**: `256.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,263,705

## wikipedia/20190301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20190301 dump.

*   **Download size**: `1.54 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,336

## wikipedia/20190301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20190301
    dump.

*   **Download size**: `9.08 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 19,269

## wikipedia/20190301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20190301
    dump.

*   **Download size**: `1.64 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,794

## wikipedia/20190301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20190301 dump.

*   **Download size**: `1.26 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,004

## wikipedia/20190301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20190301
    dump.

*   **Download size**: `9.40 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 14,297

## wikipedia/20190301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20190301 dump.

*   **Download size**: `11.56 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 23,430

## wikipedia/20190301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20190301 dump.

*   **Download size**: `11.55 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 31,968

## wikipedia/20190301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20190301 dump.

*   **Download size**: `735.93 KiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 2,404

## wikipedia/20190301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20190301
    dump.

*   **Download size**: `2.47 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,408

## wikipedia/20190301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20190301 dump.

*   **Download size**: `1.71 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,482,100

## wikipedia/20190301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20190301 dump.

*   **Download size**: `13.37 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 10,173

## wikipedia/20190301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20190301 dump.

*   **Download size**: `50.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 233,720

## wikipedia/20190301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20190301
    dump.

*   **Download size**: `52.41 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 70,666

## wikipedia/20190301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20190301 dump.

*   **Download size**: `1.50 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 1,184
