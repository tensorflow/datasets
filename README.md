# TensorFlow Datasets

TensorFlow Datasets provides many public datasets as `tf.data.Datasets`.

[![Kokoro](https://storage.googleapis.com/tfds-kokoro-public/kokoro-build.svg)](https://storage.googleapis.com/tfds-kokoro-public/kokoro-build.html)
[![PyPI version](https://badge.fury.io/py/tensorflow-datasets.svg)](https://badge.fury.io/py/tensorflow-datasets)
[![Tutorial](https://img.shields.io/badge/doc-tutorial-blue.svg)](https://www.tensorflow.org/datasets/overview)
[![API](https://img.shields.io/badge/doc-api-blue.svg)](https://www.tensorflow.org/datasets/api_docs/python/tfds)
[![Catalog](https://img.shields.io/badge/doc-datasets-blue.svg)](https://www.tensorflow.org/datasets/catalog/overview#all_datasets)

## Documentation

To install and use TFDS, we strongly encourage to start with our
[**getting started guide**](https://www.tensorflow.org/datasets/overview). Try
it interactively in a
[Colab notebook](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb).

Our documentation contains:

* [Tutorials and guides](https://www.tensorflow.org/datasets/overview)
* List of all [available datasets](https://www.tensorflow.org/datasets/catalog/overview#all_datasets)
* The [API reference](https://www.tensorflow.org/datasets/api_docs/python/tfds)

```python
# !pip install tensorflow-datasets
import tensorflow_datasets as tfds
import tensorflow as tf

# Construct a tf.data.Dataset
ds = tfds.load('mnist', split='train', as_supervised=True, shuffle_files=True)

# Build your input pipeline
ds = ds.shuffle(1000).batch(128).prefetch(10).take(5)
for image, label in ds:
  pass
```

## Want a certain dataset?

Adding a dataset is really straightforward by following
[our guide](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md).

Request a dataset by opening a
[Dataset request GitHub issue](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=dataset+request&template=dataset-request.md&title=%5Bdata+request%5D+%3Cdataset+name%3E).

And vote on the current
[set of requests](https://github.com/tensorflow/datasets/labels/dataset%20request)
by adding a thumbs-up reaction to the issue.


### Citation

Please include the following citation when using `tensorflow-datasets` for a
paper, in addition to any citation specific to the used datasets.

```
@misc{TFDS,
  title = {{TensorFlow Datasets}, A collection of ready-to-use datasets},
  howpublished = {\url{https://www.tensorflow.org/datasets}},
}
```

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

*`tensorflow/datasets` is Apache 2.0 licensed. See the
[`LICENSE`](LICENSE) file.*
