<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="div2k" />
  <meta itemprop="description" content="&#10;DIV2K dataset: DIVerse 2K resolution high quality images as used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;div2k&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/div2k" />
  <meta itemprop="sameAs" content="https://data.vision.ee.ethz.ch/cvl/DIV2K/" />
  <meta itemprop="citation" content="@InProceedings{Ignatov_2018_ECCV_Workshops,&#10;author = {Ignatov, Andrey and Timofte, Radu and others},&#10;title = {PIRM challenge on perceptual image enhancement on smartphones: report},&#10;booktitle = {European Conference on Computer Vision (ECCV) Workshops},&#10;url = &quot;http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf&quot;,&#10;month = {January},&#10;year = {2019}&#10;}&#10;" />
</div>

# `div2k`

DIV2K dataset: DIVerse 2K resolution high quality images as used for the
challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)

*   URL:
    [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
*   `DatasetBuilder`:
    [`tfds.image.div2k.Div2k`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/div2k.py)

`div2k` is configured with `tfds.image.div2k.Div2kConfig` and has the following
configurations predefined (defaults to the first one):

*   `bicubic_x2` (`v2.0.0`) (`Size: 4.68 GiB`): Uses bicubic_x2 data.

*   `bicubic_x3` (`v2.0.0`) (`Size: 4.16 GiB`): Uses bicubic_x3 data.

*   `bicubic_x4` (`v2.0.0`) (`Size: 3.97 GiB`): Uses bicubic_x4 data.

*   `bicubic_x8` (`v2.0.0`) (`Size: 3.78 GiB`): Uses bicubic_x8 data.

*   `unknown_x2` (`v2.0.0`) (`Size: 4.48 GiB`): Uses unknown_x2 data.

*   `unknown_x3` (`v2.0.0`) (`Size: 4.10 GiB`): Uses unknown_x3 data.

*   `unknown_x4` (`v2.0.0`) (`Size: 3.93 GiB`): Uses unknown_x4 data.

*   `realistic_mild_x4` (`v2.0.0`) (`Size: 4.00 GiB`): Uses realistic_mild_x4
    data.

*   `realistic_difficult_x4` (`v2.0.0`) (`Size: 3.98 GiB`): Uses
    realistic_difficult_x4 data.

*   `realistic_wild_x4` (`v2.0.0`) (`Size: 4.74 GiB`): Uses realistic_wild_x4
    data.

## `div2k/bicubic_x2`

Uses bicubic_x2 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/bicubic_x3`

Uses bicubic_x3 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/bicubic_x4`

Uses bicubic_x4 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/bicubic_x8`

Uses bicubic_x8 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/unknown_x2`

Uses unknown_x2 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/unknown_x3`

Uses unknown_x3 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/unknown_x4`

Uses unknown_x4 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/realistic_mild_x4`

Uses realistic_mild_x4 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/realistic_difficult_x4`

Uses realistic_difficult_x4 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 900
TRAIN      | 800
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## `div2k/realistic_wild_x4`

Uses realistic_wild_x4 data.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 3,300
TRAIN      | 3,200
VALIDATION | 100

### Features

```python
FeaturesDict({
    'hr': Image(shape=(None, None, 3), dtype=tf.uint8),
    'lr': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

### Supervised keys (for `as_supervised=True`)

`('lr', 'hr')`

## Citation

```
@InProceedings{Ignatov_2018_ECCV_Workshops,
author = {Ignatov, Andrey and Timofte, Radu and others},
title = {PIRM challenge on perceptual image enhancement on smartphones: report},
booktitle = {European Conference on Computer Vision (ECCV) Workshops},
url = "http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf",
month = {January},
year = {2019}
}
```

--------------------------------------------------------------------------------
