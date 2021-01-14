# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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


from tensorflow_datasets.image_classification import stanford_online_products
import tensorflow_datasets.testing as tfds_test


class StanfordOnlineProductsTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = stanford_online_products.StanfordOnlineProducts
  SPLITS = {"train": 3, "test": 3}


if __name__ == "__main__":
  tfds_test.test_main()
