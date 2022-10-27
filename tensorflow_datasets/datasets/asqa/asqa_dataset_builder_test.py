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

"""asqa dataset."""

from tensorflow_datasets.datasets.asqa import asqa_dataset_builder
import tensorflow_datasets.public_api as tfds


class AsqaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for asqa dataset."""
  DATASET_CLASS = asqa_dataset_builder.Builder
  SPLITS = {
      'train': 2,
      'dev': 1,
  }

  DL_EXTRACT_RESULT = 'ASQA.json'


if __name__ == '__main__':
  tfds.testing.test_main()
