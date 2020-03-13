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

# Lint as: python3
"""TEST FOR QMNIST DATASET"""

from tensorflow_datasets import testing
from tensorflow_datasets.image import qmnist

# testing/qmnist.py generates fake input data

qmnist._TRAIN_EXAMPLES = 10  # pylint: disable=protected-access
qmnist._TEST_EXAMPLES = 2  # pylint: disable=protected-access

class QmnistTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = qmnist.QMNIST
  SPLITS = {
      "train": 10,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "train-image",
      "train_labels": "train-label",
      "test_data": "test-image",
      "test_labels": "test-label",
  }

if __name__ == "__main__":
  testing.test_main()
