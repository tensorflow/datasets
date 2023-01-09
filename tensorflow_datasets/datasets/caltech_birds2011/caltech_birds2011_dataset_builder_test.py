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

from tensorflow_datasets.datasets.caltech_birds2011 import caltech_birds2011_dataset_builder
import tensorflow_datasets.testing as tfds_test


class CaltechBirds2011Test(tfds_test.DatasetBuilderTestCase):

  DATASET_CLASS = caltech_birds2011_dataset_builder.Builder

  SPLITS = {  # No. of train and test samples
      'train': 6,
      'test': 4,
  }

  DL_EXTRACT_RESULT = [
      'extracted/TAR_GZ.CUB_200_2011.tar.gz', 'extracted/segmentations.tgz'
  ]

  DL_DOWNLOAD_RESULT = ['CUB_200_2011.tar.gz']


if __name__ == '__main__':
  tfds_test.test_main()
