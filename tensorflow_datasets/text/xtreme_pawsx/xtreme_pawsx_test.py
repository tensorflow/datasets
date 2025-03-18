# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""paws_x_wiki dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.text.xtreme_pawsx import xtreme_pawsx


class XtremePawsxTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["es"]
  DATASET_CLASS = xtreme_pawsx.XtremePawsx
  SPLITS = {
      "train": 2,  # Number of fake train examples
  }
  DL_EXTRACT_RESULT = "en-es.translated.tsv"


if __name__ == "__main__":
  testing.test_main()
