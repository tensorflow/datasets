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

"""TODO(so2sat): Add a description here."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import so2sat


class So2satTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = so2sat.So2sat
  SPLITS = {
      "train": 5,  # Number of fake train example
      "validation": 3,  # Number of fake validation example
  }
  DL_EXTRACT_RESULT = {
      "train": "./training.h5",
      "val": "./validation.h5",
  }


if __name__ == "__main__":
  testing.test_main()
