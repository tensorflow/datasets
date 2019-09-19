<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="emnist" />
  <meta itemprop="description" content="The EMNIST dataset is a set of handwritten character digits derived from the NIST Special Database 19 and converted to a 28x28 pixel image format and dataset structure that directly matches the MNIST dataset.&#10;&#10;Note: Like the original EMNIST data, images provided here are inverted horizontally and rotated 90 anti-clockwise. You can use `tf.transpose` within `ds.map` to convert the images to a human-friendlier format." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/emnist" />
  <meta itemprop="sameAs" content="https://www.nist.gov/node/1298471/emnist-dataset" />
</div>

# `emnist`

The EMNIST dataset is a set of handwritten character digits derived from the
NIST Special Database 19 and converted to a 28x28 pixel image format and dataset
structure that directly matches the MNIST dataset.

Note: Like the original EMNIST data, images provided here are inverted
horizontally and rotated 90 anti-clockwise. You can use `tf.transpose` within
`ds.map` to convert the images to a human-friendlier format.

*   URL:
    [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)
*   `DatasetBuilder`:
    [`tfds.image.mnist.EMNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/mnist.py)

`emnist` is configured with `tfds.image.mnist.EMNISTConfig` and has the
following configurations predefined (defaults to the first one):

*   `byclass` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST ByClass

*   `bymerge` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST ByMerge

*   `balanced` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST Balanced

*   `letters` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST Letters

*   `digits` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST Digits

*   `mnist` (`v1.0.1`) (`Size: 535.73 MiB`): EMNIST MNIST

## `emnist/byclass`

EMNIST ByClass

### Statistics

Split | Examples
:---- | -------:
ALL   | 814,255
TRAIN | 697,932
TEST  | 116,323

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=62),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `emnist/bymerge`

EMNIST ByMerge

### Statistics

Split | Examples
:---- | -------:
ALL   | 814,255
TRAIN | 697,932
TEST  | 116,323

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `emnist/balanced`

EMNIST Balanced

### Statistics

Split | Examples
:---- | -------:
ALL   | 131,600
TRAIN | 112,800
TEST  | 18,800

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `emnist/letters`

EMNIST Letters

### Statistics

Split | Examples
:---- | -------:
ALL   | 103,600
TRAIN | 88,800
TEST  | 14,800

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=37),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `emnist/digits`

EMNIST Digits

### Statistics

Split | Examples
:---- | -------:
ALL   | 280,000
TRAIN | 240,000
TEST  | 40,000

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `emnist/mnist`

EMNIST MNIST

### Statistics

Split | Examples
:---- | -------:
ALL   | 70,000
TRAIN | 60,000
TEST  | 10,000

### Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://www.nist.gov/node/1298471/emnist-dataset](https://www.nist.gov/node/1298471/emnist-dataset)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## Citation
```
@article{cohen_afshar_tapson_schaik_2017,
    title={EMNIST: Extending MNIST to handwritten letters},
    DOI={10.1109/ijcnn.2017.7966217},
    journal={2017 International Joint Conference on Neural Networks (IJCNN)},
    author={Cohen, Gregory and Afshar, Saeed and Tapson, Jonathan and Schaik, Andre Van},
    year={2017}
}
```

--------------------------------------------------------------------------------
