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

"""controlled_noisy_web_labels dataset."""

from tensorflow_datasets.image_classification.controlled_noisy_web_labels import controlled_noisy_web_labels
import tensorflow_datasets.public_api as tfds


class ControlledNoisyWebLabelsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for controlled_noisy_web_labels dataset."""

  DATASET_CLASS = controlled_noisy_web_labels.ControlledNoisyWebLabels
  SPLITS = {
      'train_00': 3,  # Number of fake train examples
      'train_05': 6,  # Number of fake train examples
      'train_10': 6,  # Number of fake train examples
      'train_15': 6,  # Number of fake train examples
      'train_20': 6,  # Number of fake train examples
      'train_30': 6,  # Number of fake train examples
      'train_40': 6,  # Number of fake train examples
      'train_50': 6,  # Number of fake train examples
      'train_60': 6,  # Number of fake train examples
      'train_80': 6,  # Number of fake train examples
      'validation': 3,  # Number of fake test examples
  }

  DL_EXTRACT_RESULT = {
      'mini_train': 'train.csv',
      'mini_val': 'val.csv',
      'mini_test': 'test.csv',
  }

  OVERLAPPING_SPLITS = [
      'train_00',
      'train_05',
      'train_10',
      'train_15',
      'train_20',
      'train_30',
      'train_40',
      'train_50',
      'train_60',
      'train_80',
  ]

  SKIP_CHECKSUMS = True


if __name__ == '__main__':
  tfds.testing.test_main()
