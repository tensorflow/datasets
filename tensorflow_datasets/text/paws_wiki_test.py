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


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.text import paws_wiki


class PawsWikiTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = paws_wiki.PawsWiki
  SPLITS = {
      "train": 2,  # Number of fake train examples
      "validation": 2,  # Number of fake validation examples
      "test": 3,  # Number of fake test examples
  }
  DL_EXTRACT_RESULT = {"paws_wiki": ""}


if __name__ == "__main__":
  testing.test_main()
