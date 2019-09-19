<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cats_vs_dogs" />
  <meta itemprop="description" content="A large set of images of cats and dogs.There are 1738 corrupted images that are dropped." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cats_vs_dogs" />
  <meta itemprop="sameAs" content="https://www.microsoft.com/en-us/download/details.aspx?id=54765" />
</div>

# `cats_vs_dogs`

A large set of images of cats and dogs.There are 1738 corrupted images that are
dropped.

*   URL:
    [https://www.microsoft.com/en-us/download/details.aspx?id=54765](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
*   `DatasetBuilder`:
    [`tfds.image.cats_vs_dogs.CatsVsDogs`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cats_vs_dogs.py)
*   Version: `v2.0.1`
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

## Urls

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
