# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Smallnorb dataset test."""

from tensorflow_datasets.image import smallnorb
import tensorflow_datasets.testing as tfds_test


class SmallnorbTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = smallnorb.Smallnorb
  SPLITS = {"train": 5, "test": 5}
  DL_EXTRACT_RESULT = {
      "training_dat": "smallnorb-5x46789x9x18x6x2x96x96-training-dat.mat",
      "training_cat": "smallnorb-5x46789x9x18x6x2x96x96-training-cat.mat",
      "training_info": "smallnorb-5x46789x9x18x6x2x96x96-training-info.mat",
      "testing_dat": "smallnorb-5x01235x9x18x6x2x96x96-testing-dat.mat",
      "testing_cat": "smallnorb-5x01235x9x18x6x2x96x96-testing-cat.mat",
      "testing_info": "smallnorb-5x01235x9x18x6x2x96x96-testing-info.mat",
  }


if __name__ == "__main__":
  tfds_test.test_main()
