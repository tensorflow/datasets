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
# pylint: enable=line-too-long
import types



def _patch_for_tf1_12(tf):
  """Monkey patch tf 1.12 so tfds can use it."""
  tf.io.gfile = tf.gfile
  tf.io.gfile.copy = tf.gfile.Copy
  tf.io.gfile.exists = tf.gfile.Exists
  tf.io.gfile.glob = tf.gfile.Glob
  tf.io.gfile.isdir = tf.gfile.IsDirectory
  tf.io.gfile.listdir = tf.gfile.ListDirectory
  tf.io.gfile.makedirs = tf.gfile.MakeDirs
  tf.io.gfile.mkdir = tf.gfile.MkDir
  tf.io.gfile.remove = tf.gfile.Remove
  tf.io.gfile.rename = tf.gfile.Rename
  tf.io.gfile.rmtree = tf.gfile.DeleteRecursively
  tf.io.gfile.stat = tf.gfile.Stat
  tf.io.gfile.walk = tf.gfile.Walk
  tf.data.experimental = tf.contrib.data
  tf.data.Dataset.map_with_legacy_function = tf.data.Dataset.map
  tf.compat.v1 = types.ModuleType("tf.compat.v1")
  tf.compat.v1.assert_greater = tf.assert_greater
  tf.compat.v1.placeholder = tf.placeholder
  tf.compat.v1.ConfigProto = tf.ConfigProto
  tf.compat.v1.Session = tf.Session
  tf.compat.v1.enable_eager_execution = tf.enable_eager_execution
  tf.compat.v1.io = tf.io
  tf.compat.v1.data = tf.data
  tf.compat.v1.data.make_one_shot_iterator = (
      lambda ds: ds.make_one_shot_iterator())
  tf.compat.v1.train = tf.train
  tf.compat.v1.global_variables_initializer = tf.global_variables_initializer
  tf.compat.v1.test = tf.test
  tf.compat.v1.test.get_temp_dir = tf.test.get_temp_dir


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
    # Print more informative error message, then reraise.
    print("\n\nFailed to import TensorFlow. Please note that TensorFlow is not "
          "installed by default when you install TensorFlow Datasets. This is "
          "so that users can decide whether to install the GPU-enabled "
          "TensorFlow package. To use TensorFlow Datasets, please install the "
          "most recent version of TensorFlow, by following instructions at "
          "https://tensorflow.org/install.\n\n")
    raise

  import distutils.version

  v_1_12 = distutils.version.LooseVersion("1.12.0")
  v_1_13 = distutils.version.LooseVersion("1.13.0")
  tf_version = distutils.version.LooseVersion(tf.__version__)
  if v_1_12 <= tf_version < v_1_13:
    # TODO(b/123930850): remove when 1.13 is stable.
    _patch_for_tf1_12(tf)
  elif tf_version < v_1_12:
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        "version >= {required}; Detected an installation of version {present}. "
        "Please upgrade TensorFlow to proceed.".format(
            required="1.13.0",
            present=tf.__version__))
  # pylint: enable=g-import-not-at-top

  # Compat for TF > 1.13
  tf.data.Dataset.map_with_legacy_function = tf.data.Dataset.map
  if not hasattr(tf.io.gfile, "GFile"):
    tf.io.gfile.GFile = tf.gfile.GFile
  if not hasattr(tf, "nest"):
    tf.nest = tf.contrib.framework.nest


_ensure_tf_install()


# Imports for registration
# pylint: disable=g-import-not-at-top
from tensorflow_datasets import audio
from tensorflow_datasets import image
from tensorflow_datasets import text
from tensorflow_datasets import translate
from tensorflow_datasets import video


# Public API to create and generate a dataset
from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import

# __all__ for import * as well as documentation
from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
__all__ = public_api.__all__

