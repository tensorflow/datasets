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

"""Default values for some parameters of the API when no values are passed."""

# IMPORTANT: when changing values here, update docstrings.

import os

# Github base URL
SRC_BASE_URL = 'https://github.com/tensorflow/datasets/tree/master/'

# Directory where to store processed datasets.
DATA_DIR = os.environ.get('TFDS_DATA_DIR',
                          os.path.join('~', 'tensorflow_datasets'))

# Suffix of files / directories which aren't finished downloading / extracting.
INCOMPLETE_SUFFIX = '.incomplete'

# Note: GCS constants are defined in `core/utils/gcs_utils.py`


_registered_data_dir = set()


def add_data_dir(data_dir):
  """Registers a new default `data_dir` to search for datasets.

  When a `tfds.core.DatasetBuilder` is created with `data_dir=None`, TFDS
  will look in all registered `data_dir` (including the default one) to
  load existing datasets.

  * An error is raised if a dataset can be loaded from more than 1 registered
    data_dir.
  * This only affects reading datasets. Generation always uses the
    `data_dir` kwargs when specified or `tfds.core.constant.DATA_DIR` otherwise.

  Args:
    data_dir: New data_dir to register.
  """
  _registered_data_dir.add(data_dir)


def list_data_dirs():
  """Return the list of all registered `data_dir`."""
  all_data_dirs = _registered_data_dir | {DATA_DIR}
  return sorted(os.path.expanduser(d) for d in all_data_dirs)


