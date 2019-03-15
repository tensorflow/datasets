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

"""Tests for patchcamelyon dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import patchcamelyon

# testing/patchcamelyon.py generates fake input data

patchcamelyon._TRAIN_EXAMPLES = 32
patchcamelyon._VALIDATION_EXAMPLES = 4
patchcamelyon._TEST_EXAMPLES = 4


class PatchCAMELYONTest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = patchcamelyon.PatchCAMELYON
    SPLITS = {
        "train": 32,
        "validation": 4,
        "test": 4,
    }
    DL_EXTRACT_RESULT = {
        "train_data": "camelyonpatch_train_x.h5",
        "train_labels": "camelyonpatch_train_y.h5",
        "valid_data": "camelyonpatch_valid_x.h5",
        "valid_labels": "camelyonpatch_valid_y.h5",
        "test_data": "camelyonpatch_test_x.h5",
        "test_labels": "camelyonpatch_test_y.h5",
    }


if __name__ == "__main__":
    testing.test_main()
