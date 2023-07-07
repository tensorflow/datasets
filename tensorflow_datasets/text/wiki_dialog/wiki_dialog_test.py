# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""wiki_dialog dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.text.wiki_dialog import wiki_dialog


class WikiDialogTest(testing.DatasetBuilderTestCase):
  """Tests for wiki_dialog dataset."""

  DATASET_CLASS = wiki_dialog.WikiDialog
  BUILDER_CONFIG_NAMES_TO_TEST = ['OQ']
  DL_EXTRACT_RESULT = {
      'train': ['data_train.jsonl-00000-of-00001.gz'],
      'validation': ['data_validation.jsonl.gz'],
  }

  SPLITS = {
      'train': 3,  # Number of train pairs.
      'validation': 1,  # Number of validation pairs.
  }


if __name__ == '__main__':
  testing.test_main()
