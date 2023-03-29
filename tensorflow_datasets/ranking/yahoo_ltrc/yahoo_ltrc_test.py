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

"""yahoo_ltrc dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.ranking.yahoo_ltrc import yahoo_ltrc


class YahooLTRCTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for yahoo_ltrc dataset."""

  DATASET_CLASS = yahoo_ltrc.YahooLTRC
  SPLITS = {
      "train": 6,
      "vali": 2,
      "test": 2,
  }
  DL_EXTRACT_ONLY_RESULT = "extracted"
  SKIP_CHECKSUMS = True
  BUILDER_CONFIG_NAMES_TO_TEST = ["set1"]


if __name__ == "__main__":
  tfds.testing.test_main()
