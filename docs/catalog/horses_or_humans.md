<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="horses_or_humans" />
  <meta itemprop="description" content="A large set of images of horses and humans." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/horses_or_humans" />
  <meta itemprop="sameAs" content="http://laurencemoroney.com/horses-or-humans-dataset" />
</div>

# `horses_or_humans`

A large set of images of horses and humans.

*   URL:
    [http://laurencemoroney.com/horses-or-humans-dataset](http://laurencemoroney.com/horses-or-humans-dataset)
*   `DatasetBuilder`:
    [`tfds.image.horses_or_humans.HorsesOrHumans`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/horses_or_humans.py)
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `153.59 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(300, 300, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 1,283
TRAIN | 1,027
TEST  | 256

## Urls

*   [http://laurencemoroney.com/horses-or-humans-dataset](http://laurencemoroney.com/horses-or-humans-dataset)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@ONLINE {horses_or_humans,
author = "Laurence Moroney",
title = "Horses or Humans Dataset",
month = "feb",
year = "2019",
url = "http://laurencemoroney.com/horses-or-humans-dataset"
}
```

--------------------------------------------------------------------------------
