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

"""TensorFlow compatibility utilities."""

# pylint: disable=g-import-not-at-top,g-direct-tensorflow-import

import distutils.version

from absl import logging
import six


_ensure_tf_install_called = False


# Ensure TensorFlow is importable and its version is sufficiently recent. This
# needs to happen before anything else, since the imports below will try to
# import tensorflow, too.
def ensure_tf_install():  # pylint: disable=g-statement-before-imports
  """Attempt to import tensorflow, and ensure its version is sufficient.

  Raises:
    ImportError: if either tensorflow is not importable or its version is
    inadequate.
  """
  # Only check the first time.
  global _ensure_tf_install_called
  if _ensure_tf_install_called:
    return
  _ensure_tf_install_called = True

  try:
    import tensorflow.compat.v2 as tf  # pylint: disable=import-outside-toplevel
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
  v_1_15 = distutils.version.LooseVersion("1.15.0")
  if tf_version < v_1_15:
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        "version >= {required}; Detected an installation of version {present}. "
        "Please upgrade TensorFlow to proceed.".format(
            required="1.15.0",
            present=tf.__version__))

  if six.PY2:
    logging.warning("TFDS is going to drop Python 2 support. Please "
                    "update to Python 3.")


def is_dataset(ds):
  """Whether ds is a Dataset. Compatible across TF versions."""
  import tensorflow.compat.v2 as tf  # pylint: disable=import-outside-toplevel
  return isinstance(ds, (tf.data.Dataset, tf.compat.v1.data.Dataset))
