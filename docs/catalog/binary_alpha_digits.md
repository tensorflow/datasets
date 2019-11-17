<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="binary_alpha_digits" />
  <meta itemprop="description" content="Binary 20x16 digits of '0' through '9' and capital 'A' through 'Z'. 39 examples of each class.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('binary_alpha_digits', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/binary_alpha_digits" />
  <meta itemprop="sameAs" content="https://cs.nyu.edu/~roweis/data/" />
  <meta itemprop="citation" content="&#10;" />
</div>
# `binary_alpha_digits`

Binary 20x16 digits of '0' through '9' and capital 'A' through 'Z'. 39 examples
of each class.

*   URL: [https://cs.nyu.edu/~roweis/data/](https://cs.nyu.edu/~roweis/data/)
*   `DatasetBuilder`:
    [`tfds.image.binary_alpha_digits.BinaryAlphaDigits`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/binary_alpha_digits.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

*   Size: `519.83 KiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(20, 16, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=36),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 1,404
TRAIN | 1,404

## Homepage

*   [https://cs.nyu.edu/~roweis/data/](https://cs.nyu.edu/~roweis/data/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```

```

--------------------------------------------------------------------------------
