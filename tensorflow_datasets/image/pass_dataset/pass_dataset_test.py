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

"""pass dataset."""

from tensorflow_datasets.image.pass_dataset import pass_dataset
import tensorflow_datasets.public_api as tfds


class PASSTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for pass dataset."""
  DATASET_CLASS = pass_dataset.PASS
  SPLITS = {
      'train': 5,  # Number of fake train examples
  }

  DL_EXTRACT_RESULT = {
      'train_images': ['pass_dataset/dummy.0.tar', 'pass_dataset/dummy.1.tar'],
      'meta_data': 'dummy_meta.csv'
  }


if __name__ == '__main__':
  tfds.testing.test_main()
