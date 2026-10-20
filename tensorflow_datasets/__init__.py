# coding=utf-8
# Copyright 2026 The TensorFlow Datasets Authors.
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
* [Colab
tutorial](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
* [Add a dataset](https://www.tensorflow.org/datasets/add_dataset)
"""
# pylint: enable=line-too-long
# pylint: disable=g-import-not-at-top,g-bad-import-order,wrong-import-position,unused-import

from __future__ import annotations

import os

if os.environ.get('GCS_PREFER_FSSPEC') == 'true':
  os.environ['EPATH_PREFER_FSSPEC'] = 'true'

from absl import logging
from etils import epy as _epy


try:
  # pylint: disable=g-import-not-at-top
  # For builds that don't include all dataset builders, we don't want to fail on
  # import errors of dataset builders.
  with _epy.lazy_imports(
      error_callback='Could not import TFDS dataset builders.'
  ):
    from tensorflow_datasets import audio  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import graphs  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import image  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import image_classification  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import object_detection  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import nearest_neighbors  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import question_answering  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import d4rl  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import ranking  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import recommendation  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import rl_unplugged  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets.rlds import datasets  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import robotics  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import robomimic  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import structured  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import summarization  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import text  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import text_simplification  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import time_series  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import translate  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import video  # pyrefly: ignore[missing-module-attribute]
    from tensorflow_datasets import vision_language  # pyrefly: ignore[missing-module-attribute]


  from tensorflow_datasets import rlds  # pylint: disable=g-bad-import-order

  # Public API to create and generate a dataset
  from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import
  from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
  # pylint: enable=g-import-not-at-top
  # __all__ for import * as well as documentation
  __all__ = public_api.__all__

except Exception as exception:  # pylint: disable=broad-except
  logging.exception(exception)

del _epy
