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

"""BeeDataset dataset."""

from tensorflow_datasets.image_classification.bee_dataset import bee_dataset
import tensorflow_datasets.public_api as tfds


class BeeDatasetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for BeeDataset dataset."""
  DATASET_CLASS = bee_dataset.BeeDataset
  SPLITS = {'train': 3}

  DL_EXTRACT_RESULT = './'


if __name__ == '__main__':
  tfds.testing.test_main()
