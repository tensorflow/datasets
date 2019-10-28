<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="image_label_folder" />
  <meta itemprop="description" content="Generic image classification dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('image_label_folder', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/image_label_folder" />
  <meta itemprop="sameAs" content="" />
  <meta itemprop="citation" content="" />
</div>

# `image_label_folder`

Generic image classification dataset.

*   URL:
    [https://www.tensorflow.org/datasets](https://www.tensorflow.org/datasets)
*   `DatasetBuilder`:
    [`tfds.image.image_folder.ImageLabelFolder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/image_folder.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):
    *   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `?? GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=None),
})
```

## Statistics
None computed

## Urls

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

--------------------------------------------------------------------------------
