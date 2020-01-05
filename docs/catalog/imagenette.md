<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenette" />
  <meta itemprop="description" content="Imagenette is a subset of 10 easily classified classes from the Imagenet&#10;dataset. It was originally prepared by Jeremy Howard of FastAI. The objective&#10;behind putting together a small version of the Imagenet dataset was mainly&#10;because running new ideas/algorithms/experiments on the whole Imagenet take a&#10;lot of time.&#10;&#10;This version of the dataset allows researchers/practitioners to quickly try out&#10;ideas and share with others. The dataset comes in three variants:&#10;&#10;  * Full size&#10;  * 320 px&#10;  * 160 px&#10;This dataset consists of the Imagenette dataset {size} variant.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('imagenette', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenette" />
  <meta itemprop="sameAs" content="https://github.com/fastai/imagenette" />
  <meta itemprop="citation" content="&#10;" />
</div>
# `imagenette`

Imagenette is a subset of 10 easily classified classes from the Imagenet
dataset. It was originally prepared by Jeremy Howard of FastAI. The objective
behind putting together a small version of the Imagenet dataset was mainly
because running new ideas/algorithms/experiments on the whole Imagenet take a
lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset {size} variant.

*   URL:
    [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

*   `DatasetBuilder`:
    [`tfds.image.imagenette.Imagenette`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/imagenette.py)

`imagenette` is configured with `tfds.image.imagenette.ImagenetteConfig` and has
the following configurations predefined (defaults to the first one):

*   `full-size` (`v0.1.0`) (`Size: 1.45 GiB`): Imagenette is a subset of 10
    easily classified classes from the Imagenet dataset. It was originally
    prepared by Jeremy Howard of FastAI. The objective behind putting together a
    small version of the Imagenet dataset was mainly because running new
    ideas/algorithms/experiments on the whole Imagenet take a lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset full-size variant.

*   `320px` (`v0.1.0`) (`Size: 325.48 MiB`): Imagenette is a subset of 10 easily
    classified classes from the Imagenet dataset. It was originally prepared by
    Jeremy Howard of FastAI. The objective behind putting together a small
    version of the Imagenet dataset was mainly because running new
    ideas/algorithms/experiments on the whole Imagenet take a lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset 320px variant.

*   `160px` (`v0.1.0`) (`Size: 94.18 MiB`): Imagenette is a subset of 10 easily
    classified classes from the Imagenet dataset. It was originally prepared by
    Jeremy Howard of FastAI. The objective behind putting together a small
    version of the Imagenet dataset was mainly because running new
    ideas/algorithms/experiments on the whole Imagenet take a lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset 160px variant.

## `imagenette/full-size`
Imagenette is a subset of 10 easily classified classes from the Imagenet
dataset. It was originally prepared by Jeremy Howard of FastAI. The objective
behind putting together a small version of the Imagenet dataset was mainly
because running new ideas/algorithms/experiments on the whole Imagenet take a
lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset full-size variant.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 13,394
TRAIN      | 12,894
VALIDATION | 500

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `imagenette/320px`
Imagenette is a subset of 10 easily classified classes from the Imagenet
dataset. It was originally prepared by Jeremy Howard of FastAI. The objective
behind putting together a small version of the Imagenet dataset was mainly
because running new ideas/algorithms/experiments on the whole Imagenet take a
lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset 320px variant.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 13,394
TRAIN      | 12,894
VALIDATION | 500

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `imagenette/160px`
Imagenette is a subset of 10 easily classified classes from the Imagenet
dataset. It was originally prepared by Jeremy Howard of FastAI. The objective
behind putting together a small version of the Imagenet dataset was mainly
because running new ideas/algorithms/experiments on the whole Imagenet take a
lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

*   Full size
*   320 px
*   160 px This dataset consists of the Imagenette dataset 160px variant.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 13,394
TRAIN      | 12,894
VALIDATION | 500

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation

```

```

--------------------------------------------------------------------------------
