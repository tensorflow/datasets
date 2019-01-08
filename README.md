# TensorFlow Datasets

**Note: `tensorflow_datasets` is not yet released. Follow the [release tracking
issue](https://github.com/tensorflow/datasets/issues/5) to be notified
of release.**

TensorFlow Datasets provides many public datasets as `tf.data.Dataset`s.

[![Travis](https://img.shields.io/travis/tensorflow/datasets.svg)](https://travis-ci.org/tensorflow/datasets)

Try it in a [Colab notebook](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb).

See all our datasets on our
[datasets documentation page](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md)
or see our [API docs](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds.md)

### Installation

```
pip install tensorflow-datasets

# Currently requires TF 1.13+, i.e. tf-nightly or tf-nightly-gpu to be installed
# Some datasets require additional libraries; see setup.py extras_require

# To use our nightly release
pip install tfds-nightly
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
datasets = tfds.load(name="mnist")
train_dataset, test_dataset = datasets["train"], datasets["test"]

# Build your input pipeline
train_dataset = train_dataset.shuffle(1000).batch(128).prefetch(10)
for features in train_dataset.take(1):
  image, label = features["image"], features["label"]
```

### `DatasetBuilder`

All datasets are implemented as subclasses of `DatasetBuilder` and `tfds.load`
is a thin convenience wrapper.

```python
import tensorflow_datasets as tfds

# The following is the equivalent of the `load` call above.

# You can fetch the DatasetBuilder class by string
mnist_builder = tfds.builder("mnist")

# Download the dataset
mnist_builder.download_and_prepare()

# Construct a tf.data.Dataset
dataset = mnist_builder.as_dataset(split=tfds.Split.TRAIN)

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
        num_examples=70000,
        splits={
            u'test': <tfds.core.SplitInfo num_examples=10000>,
            u'train': <tfds.core.SplitInfo num_examples=60000>
        },
        supervised_keys=(u'image', u'label'),
        citation='"""
            @article{lecun2010mnist,
              title={MNIST handwritten digit database},
              author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
              journal={AT\&T Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},
              volume={2},
              year={2010}
            }
      """',
  )
```

### NumPy Usage with `tfds.dataset_as_numpy`

As a convenience for users that want simple NumPy arrays in their programs, you
can use `tfds.dataset_as_numpy` to return a generator that yields NumPy array
records out of a `tf.data.Dataset`. This allows you to build high-performance
input pipelines with `tf.data` but use whatever you'd like for your model
components.

```
train_ds = tfds.load("mnist", split=tfds.Split.TRAIN)
train_ds = train_ds.shuffle(1024).batch(128).repeat(5).prefetch(10)
for example in tfds.dataset_as_numpy(train_ds):
  numpy_images, numpy_labels = example["image"], example["label"]
```

You can also use `tfds.dataset_as_numpy` in conjunction with `batch_size=-1` to
get the full dataset in NumPy arrays from the returned `tf.Tensor` object:

```
train_data = tfds.load("mnist", split=tfds.Split.TRAIN, batch_size=-1)
numpy_data = tfds.dataset_as_numpy(train_data)
numpy_images, numpy_labels = numpy_dataset["image"], numpy_dataset["label"]
```

Note that the library still requires `tensorflow` as an internal dependency.

## Contributing a dataset

Thanks for considering a contribution! We're eager to grow the available set of
datasets. See the
[doc on adding a new dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md).

## Want a certain dataset?

Consider contributing (see above). But if you'd just like to request a dataset,
open a
[Dataset request GitHub issue](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=dataset+request&template=dataset-request.md&title=%5Bdata+request%5D+%3Cdataset+name%3E)
and the community can vote on which datasets they'd like most by adding
+1/thumbs-up to the issue.

Vote on the current
[set of requests](https://github.com/tensorflow/datasets/labels/dataset%20request).

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
