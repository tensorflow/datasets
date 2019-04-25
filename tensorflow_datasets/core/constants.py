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

"""Default values for some parameters of the API when no values are passed."""
# IMPORTANT: when changing values here, update docstrings.

import os

# Directory where to store processed datasets.
DATA_DIR = os.path.join("~", "tensorflow_datasets")

GCS_DATA_DIR = "gs://tfds-data/datasets"

# Suffix of files / directories which aren't finished downloading / extracting.
INCOMPLETE_SUFFIX = ".incomplete"

