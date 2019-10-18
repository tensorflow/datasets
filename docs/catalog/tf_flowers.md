<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tf_flowers" />
  <meta itemprop="description" content="A large set of images of flowers&#10;&#10;To use this dataset:&#10;&#10;```&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('tf_flowers')&#10;```&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tf_flowers" />
  <meta itemprop="sameAs" content="http://download.tensorflow.org/example_images/flower_photos.tgz" />
  <meta itemprop="citation" content="@ONLINE {tfflowers,&#10;author = &quot;The TensorFlow Team&quot;,&#10;title = &quot;Flowers&quot;,&#10;month = &quot;jan&quot;,&#10;year = &quot;2019&quot;,&#10;url = &quot;http://download.tensorflow.org/example_images/flower_photos.tgz&quot; }&#10;" />
</div>
# `tf_flowers`

A large set of images of flowers

*   URL:
    [http://download.tensorflow.org/example_images/flower_photos.tgz](http://download.tensorflow.org/example_images/flower_photos.tgz)
*   `DatasetBuilder`:
    [`tfds.image.flowers.TFFlowers`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/flowers.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `218.21 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 3,670
TRAIN | 3,670

## Urls

*   [http://download.tensorflow.org/example_images/flower_photos.tgz](http://download.tensorflow.org/example_images/flower_photos.tgz)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }
```

--------------------------------------------------------------------------------
