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

# Lint as: python3
"""Tests for `tensorflow_datasets.core.visualization.as_dataframe`."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import visualization

# Import for registration
from tensorflow_datasets.text import anli  # pylint: disable=unused-import,g-bad-import-order
from tensorflow_datasets.structured import higgs  # pylint: disable=unused-import,g-bad-import-order
from tensorflow_datasets.image_classification import imagenet  # pylint: disable=unused-import,g-bad-import-order


class AsDataframeTest(testing.TestCase):

  def test_text_dataset(self):
    with testing.mock_data(num_examples=20):
      ds, ds_info = registered.load(
          'anli', split='train', with_info=True)
    visualization.as_dataframe(ds, ds_info)

  def test_structured_dataset(self):
    with testing.mock_data(num_examples=20):
      ds, ds_info = registered.load(
          'higgs', split='train', with_info=True)
    visualization.as_dataframe(ds, ds_info)

  def test_image_dataset(self):
    with testing.mock_data(num_examples=20):
      ds, ds_info = registered.load(
          'imagenet2012', split='train', with_info=True)
    visualization.as_dataframe(ds, ds_info)


if __name__ == '__main__':
  testing.test_main()
