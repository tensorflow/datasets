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

from tensorflow_datasets.image_classification import cars196
import tensorflow_datasets.testing as tfds_test


class Cars196Test(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = cars196.Cars196
  SPLITS = {'train': 2, 'test': 2}

  DL_EXTRACT_RESULT = {
      'train': 'train',
      'test': 'test',
      'extra': 'extra',
      'test_annos': 'cars_test_annos_withlabels.mat',
  }


if __name__ == '__main__':
  tfds_test.test_main()
