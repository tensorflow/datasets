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

"""e2e_cleaned dataset."""

from tensorflow_datasets.datasets.e2e_cleaned import e2e_cleaned_dataset_builder
import tensorflow_datasets.public_api as tfds


class E2eCleanedTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = e2e_cleaned_dataset_builder.Builder
  SPLITS = {
      'train': 3,
      'validation': 2,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'train_path': 'train.csv',
      'dev_path': 'dev.csv',
      'test_path': 'test.csv',
  }

  def test_get_table_from_mr(self):
    mr = 'name[Blue Spice], eatType[coffee shop], area[city centre]'
    self.assertCountEqual(
        e2e_cleaned_dataset_builder._get_table_from_mr(mr),
        [
            {
                'column_header': 'name',
                'row_number': 1,
                'content': 'Blue Spice',
            },
            {
                'column_header': 'eatType',
                'row_number': 1,
                'content': 'coffee shop',
            },
            {
                'column_header': 'area',
                'row_number': 1,
                'content': 'city centre',
            },
        ],
    )


if __name__ == '__main__':
  tfds.testing.test_main()
