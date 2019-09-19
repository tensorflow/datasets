<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="titanic" />
  <meta itemprop="description" content="Dataset describing the survival status of individual passengers on the Titanic. Missing values in the original dataset are represented using ?. Float and int missing values are replaced with -1, string missing values are replaced with 'Unknown'." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/titanic" />
  <meta itemprop="sameAs" content="https://www.openml.org/d/40945" />
</div>

# `titanic`

Dataset describing the survival status of individual passengers on the Titanic.
Missing values in the original dataset are represented using ?. Float and int
missing values are replaced with -1, string missing values are replaced with
'Unknown'.

*   URL: [https://www.openml.org/d/40945](https://www.openml.org/d/40945)
*   `DatasetBuilder`:
    [`tfds.structured.titanic.Titanic`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/titanic.py)
*   Version: `v1.0.0`
*   Size: `114.98 KiB`

## Features
```python
FeaturesDict({
    'features': FeaturesDict({
        'age': Tensor(shape=(), dtype=tf.float32),
        'boat': Tensor(shape=(), dtype=tf.string),
        'body': Tensor(shape=(), dtype=tf.int32),
        'cabin': Tensor(shape=(), dtype=tf.string),
        'embarked': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
        'fare': Tensor(shape=(), dtype=tf.float32),
        'home.dest': Tensor(shape=(), dtype=tf.string),
        'name': Tensor(shape=(), dtype=tf.string),
        'parch': Tensor(shape=(), dtype=tf.int32),
        'pclass': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
        'sex': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'sibsp': Tensor(shape=(), dtype=tf.int32),
        'ticket': Tensor(shape=(), dtype=tf.string),
    }),
    'survived': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 1,309
TRAIN | 1,309

## Urls

*   [https://www.openml.org/d/40945](https://www.openml.org/d/40945)

## Supervised keys (for `as_supervised=True`)
`(u'features', u'survived')`

## Citation
```
@ONLINE {titanic,
author = "Frank E. Harrell Jr., Thomas Cason",
title  = "Titanic dataset",
month  = "oct",
year   = "2017",
url    = "https://www.openml.org/d/40945"
}
```

--------------------------------------------------------------------------------
