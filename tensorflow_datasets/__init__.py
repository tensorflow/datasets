# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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
# pylint: enable=line-too-long
# pylint: disable=g-import-not-at-top,g-bad-import-order,wrong-import-position,unused-import

import time
_TIMESTAMP_IMPORT_STARTS = time.time()
import tensorflow_datasets.core.logging as _tfds_logging
from tensorflow_datasets.core.logging import call_metadata as _call_metadata

_metadata = _call_metadata.CallMetadata()
_metadata.start_time_micros = int(_TIMESTAMP_IMPORT_STARTS * 1E6)
_import_time_ms_tensorflow = 0
_import_time_ms_dataset_builders = 0

try:
  _before_tf_inport = time.time()
  import tensorflow
  _import_time_ms_tensorflow = int((time.time() - _before_tf_inport) * 1000)

  # Ensure TensorFlow is importable and its version is sufficiently recent. This
  # needs to happen before anything else, since the imports below will try to
  # import tensorflow, too.
  from tensorflow_datasets.core import tf_compat
  tf_compat.ensure_tf_install()

  # Imports for registration
  _before_dataset_imports = time.time()
  from tensorflow_datasets import audio
  from tensorflow_datasets import graphs
  from tensorflow_datasets import image
  from tensorflow_datasets import image_classification
  from tensorflow_datasets import object_detection
  from tensorflow_datasets import nearest_neighbors
  from tensorflow_datasets import question_answering
  from tensorflow_datasets import d4rl
  from tensorflow_datasets import ranking
  from tensorflow_datasets import recommendation
  from tensorflow_datasets import rl_unplugged
  from tensorflow_datasets import rlds
  from tensorflow_datasets import robotics
  from tensorflow_datasets import robomimic
  from tensorflow_datasets import structured
  from tensorflow_datasets import summarization
  from tensorflow_datasets import text
  from tensorflow_datasets import text_simplification
  from tensorflow_datasets import time_series
  from tensorflow_datasets import translate
  from tensorflow_datasets import video
  from tensorflow_datasets import vision_language


  _import_time_ms_dataset_builders = int(
      (time.time() - _before_dataset_imports) * 1000)

  # Public API to create and generate a dataset
  from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import
  from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
  # __all__ for import * as well as documentation
  __all__ = public_api.__all__

except Exception:  # pylint: disable=broad-except
  _metadata.mark_error()
finally:
  _metadata.mark_end()
  _tfds_logging.tfds_import(
      metadata=_metadata,
      import_time_ms_tensorflow=_import_time_ms_tensorflow,
      import_time_ms_dataset_builders=_import_time_ms_dataset_builders)
