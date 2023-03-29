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

"""efron_morris_75 dataset."""

from tensorflow_datasets.datasets.efron_morris75 import efron_morris75_dataset_builder
import tensorflow_datasets.public_api as tfds


class EfronMorris75Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for efron_morris_75 dataset."""

  DATASET_CLASS = efron_morris75_dataset_builder.Builder
  SPLITS = {'train': 4}

  DL_EXTRACT_RESULT = 'efron-morris-75-data.tsv'


if __name__ == '__main__':
  tfds.testing.test_main()
