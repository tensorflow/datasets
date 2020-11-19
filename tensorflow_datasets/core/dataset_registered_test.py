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

"""Tests for tensorflow_datasets.core.registered."""

import tensorflow_datasets as tfds


class ListBuilderTest(tfds.testing.TestCase):
  """Ensure that the tests datasets are not registered."""

  def test_list_builder(self):
    test_datasets = {
        tfds.testing.DummyMnist.name,
        tfds.testing.DummyDatasetSharedGenerator.name,
    }
    registered_datasets = set(tfds.list_builders())
    # The tests datasets should not be present in the registered datasets
    self.assertEmpty(test_datasets & registered_datasets)

if __name__ == "__main__":
  tfds.testing.test_main()
