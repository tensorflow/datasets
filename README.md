# TensorFlow Datasets

TensorFlow Datasets provides many public datasets as `tf.data.Datasets`.

[![Kokoro](https://storage.googleapis.com/tfds-kokoro-public/kokoro-build.svg)](https://storage.googleapis.com/tfds-kokoro-public/kokoro-build.html)
[![PyPI version](https://badge.fury.io/py/tensorflow-datasets.svg)](https://badge.fury.io/py/tensorflow-datasets)

* [List of datasets](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md)
* [Try it in Colab](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
* [API docs](https://www.tensorflow.org/datasets/api_docs/python/tfds)
* [Add a dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)

**Table of Contents**

* [Installation](#installation)
* [Usage](#usage)
* [`DatasetBuilder`](#datasetbuilder)
* [NumPy usage](#numpy-usage-with-tfdsas-numpy)
* [Want a certain dataset?](#want-a-certain-dataset)
* [Disclaimers](#disclaimers)

### Installation

```sh
pip install tensorflow-datasets

# Requires TF 1.12+ to be installed.
# Some datasets require additional libraries; see setup.py extras_require
pip install tensorflow
# or:
pip install tensorflow-gpu
```

### Usage

```python
import tensorflow_datasets as tfds
import tensorflow as tf

# tfds works in both Eager and Graph modes
tf.enable_eager_execution()

# See available datasets
print(tfds.list_builders())

# Construct a tf.data.Dataset
ds_train, ds_test = tfds.load(name="mnist", split=["train", "test"])

# Build your input pipeline
ds_train = ds_train.shuffle(1000).batch(128).prefetch(10)
for features in ds_train.take(1):
  image, label = features["image"], features["label"]
```

Try it interactively in a
[Colab notebook](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb).

### `DatasetBuilder`

All datasets are implemented as subclasses of
[`DatasetBuilder`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/DatasetBuilder.md)
and
[`tfds.load`](https://www.tensorflow.org/datasets/api_docs/python/tfds/load.md)
is a thin convenience wrapper.
[`DatasetInfo`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/DatasetInfo.md)
documents the dataset.

```python
import tensorflow_datasets as tfds

# The following is the equivalent of the `load` call above.

# You can fetch the DatasetBuilder class by string
mnist_builder = tfds.builder("mnist")

# Download the dataset
mnist_builder.download_and_prepare()

# Construct a tf.data.Dataset
ds = mnist_builder.as_dataset(split=tfds.Split.TRAIN)

# Get the `DatasetInfo` object, which contains useful information about the
# dataset and its features
info = mnist_builder.info
print(info)

    tfds.core.DatasetInfo(
        name='mnist',
        version=1.0.0,
        description='The MNIST database of handwritten digits.',
        urls=[u'http://yann.lecun.com/exdb/mnist/'],
        features=FeaturesDict({
            'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
            'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10)
        },
        total_num_examples=70000,
        splits={
            u'test': <tfds.core.SplitInfo num_examples=10000>,
            u'train': <tfds.core.SplitInfo num_examples=60000>
        },
        supervised_keys=(u'image', u'label'),
        citation='"""
            @article{lecun2010mnist,
              title={MNIST handwritten digit database},
              author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
              journal={ATT Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},
              volume={2},
              year={2010}
            }
      """',
  )
```

### NumPy Usage with `tfds.as_numpy`

As a convenience for users that want simple NumPy arrays in their programs, you
can use
[`tfds.as_numpy`](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_numpy.md)
to return a generator that yields NumPy array
records out of a `tf.data.Dataset`. This allows you to build high-performance
input pipelines with `tf.data` but use whatever you'd like for your model
components.

```python
train_ds = tfds.load("mnist", split=tfds.Split.TRAIN)
train_ds = train_ds.shuffle(1024).batch(128).repeat(5).prefetch(10)
for example in tfds.as_numpy(train_ds):
  numpy_images, numpy_labels = example["image"], example["label"]
```

You can also use `tfds.as_numpy` in conjunction with `batch_size=-1` to
get the full dataset in NumPy arrays from the returned `tf.Tensor` object:

```python
train_ds = tfds.load("mnist", split=tfds.Split.TRAIN, batch_size=-1)
numpy_ds = tfds.as_numpy(train_ds)
numpy_images, numpy_labels = numpy_ds["image"], numpy_ds["label"]
```

Note that the library still requires `tensorflow` as an internal dependency.

## Want a certain dataset?

Adding a dataset is really straightforward by following
[our guide](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md).

Request a dataset by opening a
[Dataset request GitHub issue](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=dataset+request&template=dataset-request.md&title=%5Bdata+request%5D+%3Cdataset+name%3E).

And vote on the current
[set of requests](https://github.com/tensorflow/datasets/labels/dataset%20request)
by adding a thumbs-up reaction to the issue.

#### *Disclaimers*

*This is a utility library that downloads and prepares public datasets. We do*
*not host or distribute these datasets, vouch for their quality or fairness, or*
*claim that you have license to use the dataset. It is your responsibility to*
*determine whether you have permission to use the dataset under the dataset's*
*license.*

*If you're a dataset owner and wish to update any part of it (description,*
*citation, etc.), or do not want your dataset to be included in this*
*library, please get in touch through a GitHub issue. Thanks for your*
*contribution to the ML community!*

*If you're interested in learning more about responsible AI practices, including*
*fairness, please see Google AI's [Responsible AI Practices](https://ai.google/education/responsible-ai-practices).*

*`tensorflow/datasets` is Apache 2.0 licensed. See the `LICENSE` file.*
