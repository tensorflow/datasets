# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""wordnet dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import wordnet


class WordnetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Wordnet dataset."""
  DATASET_CLASS = wordnet.Wordnet
  SPLITS = {
      'train': 3,
      'validation': 2,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'WN18': '',
      'WN18RR': '',
  }

  def test_info(self):
    """Before download, there is no metadata."""
    super(WordnetTest, self).test_info()
    self.assertEmpty(self.builder.info.metadata)

  def test_info_after_download_and_prepare(self):
    """After downloading, metadata should be populated."""
    for config in self.builder.BUILDER_CONFIGS:
      with self._subTest(config.name):
        builder = self._make_builder(config=config)
        self._download_and_prepare_as_dataset(builder)
        self.assertEqual(builder.info.metadata['synsets']['07491708']['name'],
                         '__enjoyment_NN_1')
        self.assertEqual(
            builder.info.metadata['synsets']['08769179']['definition'],
            'an area in Germany around the upper Elbe river; '
            'the original home of the Saxons')


if __name__ == '__main__':
  tfds.testing.test_main()
