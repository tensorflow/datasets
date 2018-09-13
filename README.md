# TensorFlow Datasets

**Note: `tensorflow_datasets` is not yet functional and is under active
development. API unstable.**

TensorFlow Datasets provides many public datasets as `tf.data.Dataset`s.

[![Travis](https://img.shields.io/travis/tensorflow/datasets.svg)](https://travis-ci.org/tensorflow/datasets)

Installation:

```
pip install tensorflow-datasets
# Also requires tensorflow or tensorflow-gpu to be installed
```

Usage:

```python
import tensorflow_datasets as datasets

# Construct a tf.data.Dataset
dataset = datasets.load("mnist",
                        split="train",
                        data_dir="~/tfdata",
                        download=True)

# Build your input pipeline
dataset = dataset.shuffle(1000).batch(128).prefetch(1)
features = dataset.make_oneshot_iterator().get_next()
image, label = features["input"], features["output"]
```
