# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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
* [Available datasets](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md)
* [Colab tutorial](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
* [Add a dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: enable=line-too-long
# pylint: disable=g-import-not-at-top,g-bad-import-order

# Ensure TensorFlow is importable and its version is sufficiently recent. This
# needs to happen before anything else, since the imports below will try to
# import tensorflow, too.
from tensorflow_datasets.core import tf_compat
tf_compat.ensure_tf_install()

# Imports for registration
# pylint: disable=g-import-not-at-top
from tensorflow_datasets import audio
from tensorflow_datasets import image
from tensorflow_datasets import structured
from tensorflow_datasets import text
from tensorflow_datasets import translate
from tensorflow_datasets import video


# Public API to create and generate a dataset
from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import

# __all__ for import * as well as documentation
from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
__all__ = public_api.__all__

