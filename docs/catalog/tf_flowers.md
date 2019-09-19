<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tf_flowers" />
  <meta itemprop="description" content="A large set of images of flowers" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tf_flowers" />
  <meta itemprop="sameAs" content="http://download.tensorflow.org/example_images/flower_photos.tgz" />
</div>

# `tf_flowers`

A large set of images of flowers

*   URL:
    [http://download.tensorflow.org/example_images/flower_photos.tgz](http://download.tensorflow.org/example_images/flower_photos.tgz)
*   `DatasetBuilder`:
    [`tfds.image.flowers.TFFlowers`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/flowers.py)
*   Version: `v1.0.0`
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
