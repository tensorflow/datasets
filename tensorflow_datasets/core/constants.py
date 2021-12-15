# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
# If modifying this, should also update `scripts/cli/build.py` `--data_dir`
DATA_DIR = os.environ.get('TFDS_DATA_DIR',
                          os.path.join('~', 'tensorflow_datasets'))

# Suffix of files / directories which aren't finished downloading / extracting.
INCOMPLETE_SUFFIX = '.incomplete'

# Note: GCS constants are defined in `core/utils/gcs_utils.py`
