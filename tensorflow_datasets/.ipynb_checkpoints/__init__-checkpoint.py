# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=line-too-long
"""`tensorflow_datasets` (`tfds`) defines a collection of datasets ready-to-use with TensorFlow.

Each dataset is defined as a `tfds.core.DatasetBuilder`, which encapsulates
the logic to download the dataset and construct an input pipeline, as well as
contains the dataset documentation (version, splits, number of examples, etc.).

The main library entrypoints are:

* `tfds.builder`: fetch a `tfds.core.DatasetBuilder` by name
* `tfds.load`: convenience method to construct a builder, download the data, and
  create an input pipeline, returning a `tf.data.Dataset`.

Documentation:

* These API docs
* [Available datasets](https://www.tensorflow.org/datasets/catalog/overview)
* [Colab tutorial](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
* [Add a dataset](https://www.tensorflow.org/datasets/add_dataset)
"""

import sys

# pylint: disable=g-import-not-at-top

# TODO(py2): Cleanup once Py2 support is dropped entirely
if sys.version_info[0] < 3:
  print("""
  ************************************************
  *   WARNING: TFDS IS UNSUPORTED FOR PYTHON 2   *
  ************************************************
  """)
  from tensorflow_datasets import __init__py2 as api
  from tensorflow_datasets.__init__py2 import *
else:
  from tensorflow_datasets import __init__py3 as api
  from tensorflow_datasets.__init__py3 import *

__all__ = api.__all__
