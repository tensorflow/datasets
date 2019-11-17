<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="fashion_mnist" />
  <meta itemprop="description" content="Fashion-MNIST is a dataset of Zalando's article images consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('fashion_mnist', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/fashion_mnist" />
  <meta itemprop="sameAs" content="https://github.com/zalandoresearch/fashion-mnist" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1708-07747,&#10;  author    = {Han Xiao and&#10;               Kashif Rasul and&#10;               Roland Vollgraf},&#10;  title     = {Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning&#10;               Algorithms},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1708.07747},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1708.07747},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1708.07747},&#10;  timestamp = {Mon, 13 Aug 2018 16:47:27 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-07747},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
</div>
# `fashion_mnist`

Fashion-MNIST is a dataset of Zalando's article images consisting of a training
set of 60,000 examples and a test set of 10,000 examples. Each example is a
28x28 grayscale image, associated with a label from 10 classes.

*   URL:
    [https://github.com/zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)
*   `DatasetBuilder`:
    [`tfds.image.mnist.FashionMNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/mnist.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: S3: www.tensorflow.org/datasets/splits

*   Size: `29.45 MiB`

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

*   [https://github.com/zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{DBLP:journals/corr/abs-1708-07747,
  author    = {Han Xiao and
               Kashif Rasul and
               Roland Vollgraf},
  title     = {Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning
               Algorithms},
  journal   = {CoRR},
  volume    = {abs/1708.07747},
  year      = {2017},
  url       = {http://arxiv.org/abs/1708.07747},
  archivePrefix = {arXiv},
  eprint    = {1708.07747},
  timestamp = {Mon, 13 Aug 2018 16:47:27 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-07747},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
