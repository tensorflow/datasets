<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wiki40b" />
  <meta itemprop="description" content="Clean-up text for 40+ Wikipedia languages editions of pages&#10;correspond to entities. The datasets have train/dev/test splits per language.&#10;The dataset is cleaned up by page filtering to remove disambiguation pages,&#10;redirect pages, deleted pages, and non-entity pages. Each example contains the&#10;wikidata id of the entity, and the full Wikipedia article after page processing&#10;that removes non-content sections and structured objects.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wiki40b&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wiki40b" />
  <meta itemprop="sameAs" content="https://research.google/pubs/pub49029/" />
  <meta itemprop="citation" content="&#10;" />
</div>
# `wiki40b`

*   **Description**:

Clean-up text for 40+ Wikipedia languages editions of pages correspond to
entities. The datasets have train/dev/test splits per language. The dataset is
cleaned up by page filtering to remove disambiguation pages, redirect pages,
deleted pages, and non-entity pages. Each example contains the wikidata id of
the entity, and the full Wikipedia article after page processing that removes
non-content sections and structured objects.

*   **Homepage**:
    [https://research.google/pubs/pub49029/](https://research.google/pubs/pub49029/)
*   **Source code**:
    [`tfds.text.wiki40b.Wiki40b`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wiki40b.py)
*   **Versions**:
    *   **`1.1.0`** (default): No release notes.
*   **Download size**: `Unknown size`
*   **Features**:

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'version_id': Text(shape=(), dtype=tf.string),
    'wikidata_id': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```

```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## wiki40b/Wiki40B.en (default config)

*   **Config description**: Wiki40B dataset for en.

*   **Dataset size**: `9.91 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | --------:
'test'       | 162,274
'train'      | 2,926,536
'validation' | 163,597

## wiki40b/Wiki40B.ar

*   **Config description**: Wiki40B dataset for ar.

*   **Dataset size**: `833.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 12,271
'train'      | 220,885
'validation' | 12,198

## wiki40b/Wiki40B.zh-cn

*   **Config description**: Wiki40B dataset for zh-cn.

*   **Dataset size**: `985.53 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 30,355
'train'      | 549,672
'validation' | 30,299

## wiki40b/Wiki40B.zh-tw

*   **Config description**: Wiki40B dataset for zh-tw.

*   **Dataset size**: `986.45 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 30,670
'train'      | 552,031
'validation' | 30,739

## wiki40b/Wiki40B.nl

*   **Config description**: Wiki40B dataset for nl.

*   **Dataset size**: `961.82 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 24,776
'train'      | 447,555
'validation' | 25,201

## wiki40b/Wiki40B.fr

*   **Config description**: Wiki40B dataset for fr.

*   **Dataset size**: `3.37 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | --------:
'test'       | 68,004
'train'      | 1,227,206
'validation' | 68,655

## wiki40b/Wiki40B.de

*   **Config description**: Wiki40B dataset for de.

*   **Dataset size**: `4.78 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | --------:
'test'       | 86,594
'train'      | 1,554,910
'validation' | 86,068

## wiki40b/Wiki40B.it

*   **Config description**: Wiki40B dataset for it.

*   **Dataset size**: `2.00 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 40,443
'train'      | 732,609
'validation' | 40,684

## wiki40b/Wiki40B.ja

*   **Config description**: Wiki40B dataset for ja.

*   **Dataset size**: `2.19 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 41,268
'train'      | 745,392
'validation' | 41,576

## wiki40b/Wiki40B.ko

*   **Config description**: Wiki40B dataset for ko.

*   **Dataset size**: `453.98 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 10,802
'train'      | 194,977
'validation' | 10,805

## wiki40b/Wiki40B.pl

*   **Config description**: Wiki40B dataset for pl.

*   **Dataset size**: `1.03 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 27,987
'train'      | 505,191
'validation' | 28,310

## wiki40b/Wiki40B.pt

*   **Config description**: Wiki40B dataset for pt.

*   **Dataset size**: `1.08 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 22,693
'train'      | 406,507
'validation' | 22,301

## wiki40b/Wiki40B.ru

*   **Config description**: Wiki40B dataset for ru.

*   **Dataset size**: `4.13 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 51,885
'train'      | 926,037
'validation' | 51,287

## wiki40b/Wiki40B.es

*   **Config description**: Wiki40B dataset for es.

*   **Dataset size**: `2.70 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 48,764
'train'      | 872,541
'validation' | 48,592

## wiki40b/Wiki40B.th

*   **Config description**: Wiki40B dataset for th.

*   **Dataset size**: `326.29 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 3,114
'train'      | 56,798
'validation' | 3,093

## wiki40b/Wiki40B.tr

*   **Config description**: Wiki40B dataset for tr.

*   **Dataset size**: `308.87 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 7,890
'train'      | 142,576
'validation' | 7,845

## wiki40b/Wiki40B.bg

*   **Config description**: Wiki40B dataset for bg.

*   **Dataset size**: `433.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 7,289
'train'      | 130,670
'validation' | 7,259

## wiki40b/Wiki40B.ca

*   **Config description**: Wiki40B dataset for ca.

*   **Dataset size**: `753.00 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 15,568
'train'      | 277,313
'validation' | 15,362

## wiki40b/Wiki40B.cs

*   **Config description**: Wiki40B dataset for cs.

*   **Dataset size**: `631.84 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 12,984
'train'      | 235,971
'validation' | 13,096

## wiki40b/Wiki40B.da

*   **Config description**: Wiki40B dataset for da.

*   **Dataset size**: `240.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 6,219
'train'      | 109,486
'validation' | 6,173

## wiki40b/Wiki40B.el

*   **Config description**: Wiki40B dataset for el.

*   **Dataset size**: `524.77 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 5,261
'train'      | 93,596
'validation' | 5,130

## wiki40b/Wiki40B.et

*   **Config description**: Wiki40B dataset for et.

*   **Dataset size**: `184.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 6,205
'train'      | 114,464
'validation' | 6,351

## wiki40b/Wiki40B.fa

*   **Config description**: Wiki40B dataset for fa.

*   **Dataset size**: `482.55 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,262
'train'      | 203,145
'validation' | 11,180

## wiki40b/Wiki40B.fi

*   **Config description**: Wiki40B dataset for fi.

*   **Dataset size**: `534.13 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 14,179
'train'      | 255,822
'validation' | 13,962

## wiki40b/Wiki40B.he

*   **Config description**: Wiki40B dataset for he.

*   **Dataset size**: `869.51 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 9,344
'train'      | 165,359
'validation' | 9,231

## wiki40b/Wiki40B.hi

*   **Config description**: Wiki40B dataset for hi.

*   **Dataset size**: `277.56 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 2,643
'train'      | 45,737
'validation' | 2,596

## wiki40b/Wiki40B.hr

*   **Config description**: Wiki40B dataset for hr.

*   **Dataset size**: `235.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 5,724
'train'      | 103,857
'validation' | 5,792

## wiki40b/Wiki40B.hu

*   **Config description**: Wiki40B dataset for hu.

*   **Dataset size**: `634.25 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 15,258
'train'      | 273,248
'validation' | 15,208

## wiki40b/Wiki40B.id

*   **Config description**: Wiki40B dataset for id.

*   **Dataset size**: `334.06 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 8,598
'train'      | 156,255
'validation' | 8,714

## wiki40b/Wiki40B.lt

*   **Config description**: Wiki40B dataset for lt.

*   **Dataset size**: `140.46 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 4,683
'train'      | 84,854
'validation' | 4,754

## wiki40b/Wiki40B.lv

*   **Config description**: Wiki40B dataset for lv.

*   **Dataset size**: `80.07 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,932
'train'      | 33,064
'validation' | 1,857

## wiki40b/Wiki40B.ms

*   **Config description**: Wiki40B dataset for ms.

*   **Dataset size**: `142.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 5,235
'train'      | 97,509
'validation' | 5,357

## wiki40b/Wiki40B.no

*   **Config description**: Wiki40B dataset for no.

*   **Dataset size**: `382.03 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 10,588
'train'      | 190,588
'validation' | 10,547

## wiki40b/Wiki40B.ro

*   **Config description**: Wiki40B dataset for ro.

*   **Dataset size**: `319.68 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 7,870
'train'      | 139,615
'validation' | 7,624

## wiki40b/Wiki40B.sk

*   **Config description**: Wiki40B dataset for sk.

*   **Dataset size**: `170.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 5,741
'train'      | 103,095
'validation' | 5,604

## wiki40b/Wiki40B.sl

*   **Config description**: Wiki40B dataset for sl.

*   **Dataset size**: `157.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 3,341
'train'      | 60,927
'validation' | 3,287

## wiki40b/Wiki40B.sr

*   **Config description**: Wiki40B dataset for sr.

*   **Dataset size**: `582.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 17,997
'train'      | 327,313
'validation' | 18,100

## wiki40b/Wiki40B.sv

*   **Config description**: Wiki40B dataset for sv.

*   **Dataset size**: `613.62 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 22,291
'train'      | 400,742
'validation' | 22,263

## wiki40b/Wiki40B.tl

*   **Config description**: Wiki40B dataset for tl.

*   **Dataset size**: `29.04 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,446
'train'      | 25,940
'validation' | 1,472

## wiki40b/Wiki40B.uk

*   **Config description**: Wiki40B dataset for uk.

*   **Dataset size**: `1.67 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 26,581
'train'      | 477,618
'validation' | 26,324

## wiki40b/Wiki40B.vi

*   **Config description**: Wiki40B dataset for vi.

*   **Dataset size**: `497.70 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 7,942
'train'      | 146,255
'validation' | 8,195
