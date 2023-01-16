# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""beir dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.beir import beir_dataset_builder


class BeirTest(testing.DatasetBuilderTestCase):
  """Tests for beir dataset."""

  DATASET_CLASS = beir_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ['msmarco']
  SPLITS = {
      'query': 2,  # Number of fake queries
      'passage': 3,  # Number of fake passages
      'train': 1,  # Number of train pairs
      'validation': 1,  # Number of validation pairs
      'test': 1,  # Number of test pairs
  }


if __name__ == '__main__':
  testing.test_main()
