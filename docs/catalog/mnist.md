<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mnist" />
  <meta itemprop="description" content="The MNIST database of handwritten digits.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('mnist', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mnist" />
  <meta itemprop="sameAs" content="http://yann.lecun.com/exdb/mnist/" />
  <meta itemprop="citation" content="@article{lecun2010mnist,&#10;  title={MNIST handwritten digit database},&#10;  author={LeCun, Yann and Cortes, Corinna and Burges, CJ},&#10;  journal={ATT Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},&#10;  volume={2},&#10;  year={2010}&#10;}&#10;" />
</div>
# `mnist`

The MNIST database of handwritten digits.

*   URL: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
*   `DatasetBuilder`:
    [`tfds.image.mnist.MNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/mnist.py)
*   Version: `v1.0.0`
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

## Homepage

*   [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

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
