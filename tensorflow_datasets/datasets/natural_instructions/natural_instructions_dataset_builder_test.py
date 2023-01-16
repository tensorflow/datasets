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

"""natural_instructions dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.natural_instructions import natural_instructions_dataset_builder


class NaturalInstructionsTest(testing.DatasetBuilderTestCase):
  """Tests for natural_instructions dataset."""

  DATASET_CLASS = natural_instructions_dataset_builder.Builder
  SPLITS = {
      'train': 3,  # Number of fake train example
  }

  DL_EXTRACT_RESULT = {'train': 'natural_instructions_train.json'}

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == '__main__':
  testing.test_main()
