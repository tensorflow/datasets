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

"""Czech Restaurants dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.cs_restaurants import cs_restaurants


class CSRestaurantsTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = cs_restaurants.CSRestaurants
  SPLITS = {
      'train': 3,
      'validation': 2,
      'test': 2,
  }

  DL_EXTRACT_RESULT = {
      'train_path': 'train.json',
      'dev_path': 'dev.json',
      'test_path': 'test.json'
  }

  def test_get_table_from_da(self):
    da = 'inform(food=Mexican,kids_allowed=no,name=Ferdinanda)'
    self.assertCountEqual(
        cs_restaurants._get_table_from_da(da), [{
            'column_header': 'intent',
            'row_number': 1,
            'content': 'inform',
        }, {
            'column_header': 'food',
            'row_number': 1,
            'content': 'Mexican',
        }, {
            'column_header': 'kids_allowed',
            'row_number': 1,
            'content': 'no',
        }, {
            'column_header': 'name',
            'row_number': 1,
            'content': 'Ferdinanda',
        }])


if __name__ == '__main__':
  tfds.testing.test_main()
