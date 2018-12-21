# TensorFlow Datasets

**Note: `tensorflow_datasets` is not yet released. Follow the [release tracking
issue](https://github.com/tensorflow/datasets/issues/5) to be notified
of release.**

TensorFlow Datasets provides many public datasets as `tf.data.Dataset`s.

[![Travis](https://img.shields.io/travis/tensorflow/datasets.svg)](https://travis-ci.org/tensorflow/datasets)

Try it in a [Colab notebook](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb).

See all our datasets on our
[datasets documentation page](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md).

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
          'label': ClassLabel(shape=(), dtype=tf.int64)
      }),
      num_examples=70000,
      splits=[u'test', u'train'],
      examples_per_split=[10000L, 60000L],
      supervised_keys=(u'image', u'label'),
      citation='Y. Lecun and C. Cortes, "The MNIST database of handwritten digits," 1998.
  [Online]. Available: http://yann.lecun.com/exdb/mnist/',
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

#### Disclaimers

This is a utility library that downloads and prepares public datasets. We do
not host or distribute these datasets, vouch for their quality or fairness, or
claim that you have license to use the dataset. It is your responsibility to
determine whether you have permission to use the dataset under the dataset's
license.

If you're a dataset owner and wish to update any part of it (description,
citation, etc.), or do not want your dataset to be included in this
library, please get in touch through a GitHub issue. Thanks for your
contribution to the ML community!

If you're interested in learning more about responsible AI practices, including
fairness, please see https://ai.google/education/responsible-ai-practices.

`tensorflow/datasets` is Apache 2.0 licensed. See the `LICENSE` file.
