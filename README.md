# TensorFlow Datasets

**Note: `tensorflow_datasets` is not yet released. Follow the [release tracking
issue](https://github.com/tensorflow/datasets/issues/5) to be notified
of release.**

TensorFlow Datasets provides many public datasets as `tf.data.Dataset`s.

[![Travis](https://img.shields.io/travis/tensorflow/datasets.svg)](https://travis-ci.org/tensorflow/datasets)

Try it in a [Colab notebook](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb).

### Installation

```
pip install tensorflow-datasets

# Currently requires tf-nightly or tf-nightly-gpu to be installed
# Some datasets require additional libraries; see setup.py extras_require
```

### Usage

```python
import tensorflow_datasets as tfds

# See available datasets
print(tfds.list_builders())

# Construct a tf.data.Dataset
dataset = tfds.load(name="mnist", split=tfds.Split.TRAIN)

# Build your input pipeline
dataset = dataset.shuffle(1000).batch(128).prefetch(tf.data.experimental.AUTOTUNE)
features = dataset.make_oneshot_iterator().get_next()
image, label = features["image"], features["label"]
```

### `DatasetBuilder`

All datasets are implemented as subclasses of `DatasetBuilder`.

```python
import tensorflow_datasets as tfds

# The following is the equivalent of the `load` call above.

# You can fetch the DatasetBuilder class by string
mnist_builder = tfds.builder("mnist")

# Download the dataset
mnist_builder.download_and_prepare()
# Construct a tf.data.Dataset
dataset = mnist_builder.as_dataset(split=tfds.Split.TRAIN)
```

### Non-TensorFlow Usage

All datasets are usable outside of TensorFlow with the `numpy_iterator`
method, which takes the same arguments as `as_dataset`.

```python
import tensorflow_datasets as tfds

mnist_builder = tfds.builder("mnist")
mnist_builder.download_and_prepare()
for element in mnist_builder.numpy_iterator(split=tfds.Split.TRAIN):
  numpy_image, numpy_label = element["image"], element["label"]
```

Note that the library still requires `tensorflow` as an internal dependency.

## Contributing a dataset

Thanks for considering a contribution. See the
[doc on adding a new dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)
