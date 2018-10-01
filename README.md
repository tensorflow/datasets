# TensorFlow Datasets

**Note: `tensorflow_datasets` is not yet released. Follow the [release tracking
issue](https://github.com/tensorflow/datasets/issues/5) to be notified
of release.**

TensorFlow Datasets provides many public datasets as `tf.data.Dataset`s.

[![Travis](https://img.shields.io/travis/tensorflow/datasets.svg)](https://travis-ci.org/tensorflow/datasets)

### Installation

```
pip install tensorflow-datasets

# Requires tensorflow or tensorflow-gpu to be installed
# Some datasets require additional libraries; see setup.py extras_require
```

### Usage

```python
import tensorflow_datasets as datasets

# See available datasets
print(datasets.registered())

# Construct a tf.data.Dataset
dataset = datasets.load(name="mnist",
                        split=datasets.Split.TRAIN,
                        data_dir="~/tfdata",
                        download=True)

# Build your input pipeline
dataset = dataset.shuffle(1000).batch(128).prefetch(1)
features = dataset.make_oneshot_iterator().get_next()
image, label = features["input"], features["target"]
```

### `DatasetBuilder`

All datasets are implemented as subclasses of `DatasetBuilder`.

```python
import tensorflow_datasets as datasets

# The following is the equivalent of the `load` call above.

# You can fetch the DatasetBuilder class by string
mnist_builder = datasets.builder("mnist")(data_dir="~/tfdata")

# Download the dataset
mnist_builder.download_and_prepare()
# Construct a tf.data.Dataset
dataset = mnist_builder.as_dataset(split=datasets.Split.TRAIN)
```

### Non-TensorFlow Usage

All datasets are usable outside of TensorFlow with the `numpy_iterator`
method, which takes the same arguments as `as_dataset`.

```python
import tensorflow_datasets as datasets

mnist_builder = datasets.builder("mnist")(data_dir="~/tfdata")
mnist_builder.download_and_prepare()
for element in mnist_builder.numpy_iterator(split=datasets.Split.TRAIN):
  numpy_image, numpy_label = element["input"], element["target"]
```

Note that the library still requires `tensorflow` as an internal dependency.

## Contributing a dataset

Thanks for considering a contribution. See the
[doc on adding a new dataset](https://github.com/tensorflow/datasets/tree/master/docs/new_dataset.md)
