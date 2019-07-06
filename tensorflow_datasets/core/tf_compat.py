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

"""TensorFlow compatibility utilities."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=g-import-not-at-top,g-direct-tensorflow-import

import types
import distutils.version

# Which patch function was called
# For debug only, not to be depended upon.
# Will be set to one of:
# * tf1_13
# * tf2
TF_PATCH = ""


# Ensure TensorFlow is importable and its version is sufficiently recent. This
# needs to happen before anything else, since the imports below will try to
# import tensorflow, too.
def ensure_tf_install():  # pylint: disable=g-statement-before-imports
  """Attempt to import tensorflow, and ensure its version is sufficient.

  Raises:
    ImportError: if either tensorflow is not importable or its version is
    inadequate.
  """
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

  tf_version = distutils.version.LooseVersion(tf.__version__)
  v_1_13 = distutils.version.LooseVersion("1.13.0")
  if tf_version < v_1_13:
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        "version >= {required}; Detected an installation of version {present}. "
        "Please upgrade TensorFlow to proceed.".format(
            required="1.13.0",
            present=tf.__version__))
  _patch_tf(tf)


def _patch_tf(tf):
  """Patch TF to maintain compatibility across versions."""
  global TF_PATCH
  if TF_PATCH:
    return

  v_1_13 = distutils.version.LooseVersion("1.13.0")
  v_2 = distutils.version.LooseVersion("2.0.0")
  tf_version = distutils.version.LooseVersion(tf.__version__)
  if v_1_13 <= tf_version < v_2:
    TF_PATCH = "tf1_13"
    _patch_for_tf1_13(tf)
  else:
    TF_PATCH = "tf2"
    _patch_for_tf2(tf)


def _patch_for_tf2(tf):
  if not hasattr(tf.data.Dataset, "output_shapes"):
    from tensorflow.python.data.ops import dataset_ops
    tf.data.Dataset.output_shapes = property(
        dataset_ops.get_legacy_output_shapes)
    tf.data.Dataset.output_types = property(dataset_ops.get_legacy_output_types)


def _patch_for_tf1_13(tf):
  """Monkey patch tf 1.13 so tfds can use it."""
  if not hasattr(tf.io.gfile, "GFile"):
    tf.io.gfile.GFile = tf.gfile.GFile
  if not hasattr(tf, "nest"):
    tf.nest = tf.contrib.framework.nest
  if not hasattr(tf.compat, "v2"):
    tf.compat.v2 = types.ModuleType("tf.compat.v2")
    tf.compat.v2.data = types.ModuleType("tf.compat.v2.data")
    from tensorflow.python.data.ops import dataset_ops
    tf.compat.v2.data.Dataset = dataset_ops.DatasetV2
  if not hasattr(tf.compat.v2.data.Dataset, "output_shapes"):
    from tensorflow.python.data.ops import dataset_ops
    if hasattr(dataset_ops, "get_legacy_output_shapes"):
      tf.compat.v2.data.Dataset.output_shapes = property(
          dataset_ops.get_legacy_output_shapes)
      tf.compat.v2.data.Dataset.output_types = property(
          dataset_ops.get_legacy_output_types)


def is_dataset(ds):
  """Whether ds is a Dataset. Compatible across TF versions."""
  import tensorflow as tf
  from tensorflow_datasets.core.utils import py_utils
  dataset_types = [tf.data.Dataset]
  v1_ds = py_utils.rgetattr(tf, "compat.v1.data.Dataset", None)
  v2_ds = py_utils.rgetattr(tf, "compat.v2.data.Dataset", None)
  if v1_ds is not None:
    dataset_types.append(v1_ds)
  if v2_ds is not None:
    dataset_types.append(v2_ds)
  return isinstance(ds, tuple(dataset_types))


