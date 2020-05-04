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
"""Tests for `tensorflow_datasets.core.visualization.show_examples`."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import mock

from tensorflow_datasets import testing
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import visualization

# Import for registration
from tensorflow_datasets.image_classification import imagenet  # pylint: disable=unused-import,g-bad-import-order


class ShowExamplesTest(testing.TestCase):

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples(self, mock_fig):
    with testing.mock_data(num_examples=20):
      ds, ds_info = registered.load(
          'imagenet2012', split='train', with_info=True)
    visualization.show_examples(ds, ds_info)

  # TODO(tfds): Should add test when there isn't enough examples (ds.take(3))


class ShowStatisticsTest(testing.TestCase):

  def test_show_examples(self):
    with testing.mock_data():
      builder = registered.builder('imagenet2012')
      visualization.show_statistics(builder.info)


if __name__ == '__main__':
  testing.test_main()
