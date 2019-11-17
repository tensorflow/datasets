<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cats_vs_dogs" />
  <meta itemprop="description" content="A large set of images of cats and dogs.There are 1738 corrupted images that are dropped.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('cats_vs_dogs', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cats_vs_dogs" />
  <meta itemprop="sameAs" content="https://www.microsoft.com/en-us/download/details.aspx?id=54765" />
  <meta itemprop="citation" content="@Inproceedings (Conference){asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization,&#10;author = {Elson, Jeremy and Douceur, John (JD) and Howell, Jon and Saul, Jared},&#10;title = {Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization},&#10;booktitle = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},&#10;year = {2007},&#10;month = {October},&#10;publisher = {Association for Computing Machinery, Inc.},&#10;url = {https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/},&#10;edition = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},&#10;}&#10;" />
</div>
# `cats_vs_dogs`

A large set of images of cats and dogs.There are 1738 corrupted images that are
dropped.

*   URL:
    [https://www.microsoft.com/en-us/download/details.aspx?id=54765](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
*   `DatasetBuilder`:
    [`tfds.image.cats_vs_dogs.CatsVsDogs`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cats_vs_dogs.py)
*   Version: `v2.0.1`
*   Versions:

    *   **`2.0.1`** (default):
    *   `4.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `786.68 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 23,262
TRAIN | 23,262

## Homepage

*   [https://www.microsoft.com/en-us/download/details.aspx?id=54765](https://www.microsoft.com/en-us/download/details.aspx?id=54765)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@Inproceedings (Conference){asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization,
author = {Elson, Jeremy and Douceur, John (JD) and Howell, Jon and Saul, Jared},
title = {Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization},
booktitle = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
year = {2007},
month = {October},
publisher = {Association for Computing Machinery, Inc.},
url = {https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/},
edition = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
}
```

--------------------------------------------------------------------------------
