<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mnist" />
  <meta itemprop="description" content="The MNIST database of handwritten digits." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mnist" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/cvdf-datasets/mnist/" />
</div>

# `mnist`

The MNIST database of handwritten digits.

*   URL:
    [https://storage.googleapis.com/cvdf-datasets/mnist/](https://storage.googleapis.com/cvdf-datasets/mnist/)
*   `DatasetBuilder`:
    [`tfds.image.mnist.MNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/mnist.py)
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: S3: www.tensorflow.org/datasets/splits

*   Size: `11.06 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 70,000
TRAIN | 60,000
TEST  | 10,000

## Urls

*   [https://storage.googleapis.com/cvdf-datasets/mnist/](https://storage.googleapis.com/cvdf-datasets/mnist/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{lecun2010mnist,
  title={MNIST handwritten digit database},
  author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
  journal={ATT Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},
  volume={2},
  year={2010}
}
```

--------------------------------------------------------------------------------
