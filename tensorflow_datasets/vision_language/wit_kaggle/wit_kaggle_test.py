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

"""Wikipedia-based Image Text (WIT) Dataset for the Kaggle competition."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.vision_language.wit_kaggle import wit_kaggle


class WitKaggleTestTrain(tfds.testing.DatasetBuilderTestCase):
  """Tests for wit_kaggle dataset train split."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['train_with_extended_features']
  DATASET_CLASS = wit_kaggle.WitKaggle
  SKIP_CHECKSUMS = True  # All data is manually downloaded.

  SPLITS = {'train_with_extended_features': 2}
  DL_EXTRACT_ONLY_RESULT = {
      'samples': ['wit_kaggle/train/ZIP.unzipped_train'],
      'images': 'wit_kaggle/train/image_data_train',
  }


class WitKaggleTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for wit_kaggle dataset test split."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['test_without_gold']
  DATASET_CLASS = wit_kaggle.WitKaggle
  SKIP_CHECKSUMS = True  # All data is manually downloaded.

  SPLITS = {'test_without_gold': 1}
  DL_EXTRACT_ONLY_RESULT = {
      'samples': ['wit_kaggle/test/ZIP.unzipped_test'],
      'images': 'wit_kaggle/test/image_data_test',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
