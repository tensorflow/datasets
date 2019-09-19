<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="iris" />
  <meta itemprop="description" content="This is perhaps the best known database to be found in the pattern recognition&#10;literature. Fisher's paper is a classic in the field and is referenced&#10;frequently to this day. (See Duda &amp; Hart, for example.) The data set contains&#10;3 classes of 50 instances each, where each class refers to a type of iris&#10;plant. One class is linearly separable from the other 2; the latter are NOT&#10;linearly separable from each other.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/iris" />
  <meta itemprop="sameAs" content="https://archive.ics.uci.edu/ml/datasets/iris" />
</div>

# `iris`

This is perhaps the best known database to be found in the pattern recognition
literature. Fisher's paper is a classic in the field and is referenced
frequently to this day. (See Duda & Hart, for example.) The data set contains 3
classes of 50 instances each, where each class refers to a type of iris plant.
One class is linearly separable from the other 2; the latter are NOT linearly
separable from each other.

*   URL:
    [https://archive.ics.uci.edu/ml/datasets/iris](https://archive.ics.uci.edu/ml/datasets/iris)
*   `DatasetBuilder`:
    [`tfds.structured.iris.Iris`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/iris.py)
*   Version: `v1.0.0`
*   Size: `4.44 KiB`

## Features
```python
FeaturesDict({
    'features': Tensor(shape=(4,), dtype=tf.float32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 150
TRAIN | 150

## Urls

*   [https://archive.ics.uci.edu/ml/datasets/iris](https://archive.ics.uci.edu/ml/datasets/iris)

## Supervised keys (for `as_supervised=True`)
`(u'features', u'label')`

## Citation
```
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
}
```

--------------------------------------------------------------------------------
