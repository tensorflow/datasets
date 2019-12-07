<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="svhn_cropped" />
  <meta itemprop="description" content="The Street View House Numbers (SVHN) Dataset is an image digit recognition dataset of over 600,000 digit images coming from real world data. Images are cropped to 32x32.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('svhn_cropped', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/svhn_cropped" />
  <meta itemprop="sameAs" content="http://ufldl.stanford.edu/housenumbers/" />
  <meta itemprop="citation" content="@article{Netzer2011,&#10;author = {Netzer, Yuval and Wang, Tao and Coates, Adam and Bissacco, Alessandro and Wu, Bo and Ng, Andrew Y},&#10;booktitle = {Advances in Neural Information Processing Systems ({NIPS})},&#10;title = {Reading Digits in Natural Images with Unsupervised Feature Learning},&#10;year = {2011}&#10;}&#10;" />
</div>
# `svhn_cropped`

The Street View House Numbers (SVHN) Dataset is an image digit recognition
dataset of over 600,000 digit images coming from real world data. Images are
cropped to 32x32.

*   URL:
    [http://ufldl.stanford.edu/housenumbers/](http://ufldl.stanford.edu/housenumbers/)
*   `DatasetBuilder`:
    [`tfds.image.svhn.SvhnCropped`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/svhn.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `1.47 GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 630,420
EXTRA | 531,131
TRAIN | 73,257
TEST  | 26,032

## Homepage

*   [http://ufldl.stanford.edu/housenumbers/](http://ufldl.stanford.edu/housenumbers/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{Netzer2011,
author = {Netzer, Yuval and Wang, Tao and Coates, Adam and Bissacco, Alessandro and Wu, Bo and Ng, Andrew Y},
booktitle = {Advances in Neural Information Processing Systems ({NIPS})},
title = {Reading Digits in Natural Images with Unsupervised Feature Learning},
year = {2011}
}
```

--------------------------------------------------------------------------------
