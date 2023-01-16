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

"""wiki_bio dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.structured import wiki_bio

# pyformat: disable
_INFO_BOX_TEST = 'name_1:akoo	name_2:nana	image_size:<none>	background_1:solo_singer	origin_1:ghanaian	occupation_1:singer	occupation_2:,	occupation_3:songwriter	occupation_4:,	occupation_5:rapper	years_active_1:2012	years_active_2:--	years_active_3:present'
# pyformat: enable


class WikiBioTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = wiki_bio.WikiBio
  SPLITS = {
      'train': 3,
      'validation': 3,
      'test': 3,
  }

  def test_get_table(self):
    self.assertCountEqual(
        wiki_bio._get_table(_INFO_BOX_TEST),
        [
            {
                'column_header': 'name',
                'row_number': 1,
                'content': 'akoo nana',
            },
            {
                'column_header': 'background',
                'row_number': 1,
                'content': 'solo_singer',
            },
            {
                'column_header': 'occupation',
                'row_number': 1,
                'content': 'singer , songwriter , rapper',
            },
            {
                'column_header': 'origin',
                'row_number': 1,
                'content': 'ghanaian',
            },
            {
                'column_header': 'years_active',
                'row_number': 1,
                'content': '2012 -- present',
            },
        ],
    )


if __name__ == '__main__':
  testing.test_main()
