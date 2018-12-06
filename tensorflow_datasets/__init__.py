# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

Each dataset is defined as a `tfds.core.DatasetBuilder`.

See `tfds.builder`, `tfds.list_builders`, and `tfds.load` for the main
entrypoints into the library, or take a look at
[our dataset documentation](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md).
"""
# pylint: enable=line-too-long


# Copied from tensorflow/probability
# Ensure TensorFlow is importable and its version is sufficiently recent. This
# needs to happen before anything else, since the imports below will try to
# import tensorflow, too.
def _ensure_tf_install():  # pylint: disable=g-statement-before-imports
  """Attempt to import tensorflow, and ensure its version is sufficient.

  Raises:
    ImportError: if either tensorflow is not importable or its version is
    inadequate.
  """
  # pylint: disable=g-import-not-at-top
  try:
    import tensorflow as tf
  except ImportError:
    # Re-raise with more informative error message.
    raise ImportError(
        "Failed to import TensorFlow. Please note that TensorFlow is not "
        "installed by default when you install TensorFlow Datasets. This is "
        "so that users can decide whether to install the GPU-enabled "
        "TensorFlow package. To use TensorFlow Datasets, please install the "
        "most recent version of TensorFlow, by following instructions at "
        "https://tensorflow.org/install. Usually `pip install tensorflow` "
        "or `pip install tensorflow-gpu`.")

  import distutils.version

  #
  # Update this whenever we need to depend on a newer TensorFlow release.
  #
  required_tensorflow_version = "1.13.0"

  if (distutils.version.LooseVersion(tf.__version__) <
      distutils.version.LooseVersion(required_tensorflow_version)):
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        "version >= {required}; Detected an installation of version {present}. "
        "Please upgrade TensorFlow to proceed.".format(
            required=required_tensorflow_version,
            present=tf.__version__))
  # pylint: enable=g-import-not-at-top


_ensure_tf_install()


# Imports for registration
from tensorflow_datasets import image
from tensorflow_datasets import text
from tensorflow_datasets import video


# Public API to create and generate a dataset
from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import

# __all__ for import * as well as documentation
from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
__all__ = public_api.__all__
