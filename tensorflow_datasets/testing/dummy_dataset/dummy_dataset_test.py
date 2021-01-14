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

"""Dummy dataset tests."""

import tensorflow_datasets.public_api as tfds


class DummyDatasetTest(tfds.testing.DatasetBuilderTestCase):

  @classmethod
  def setUpClass(cls):
    # DummyDataset is used by other tests to test dynamic class registration
    # (e.g. in `cli/build_test.py`)
    # However, pytest test collection import all `_test.py` files, thus
    # registering the dataset for all tests.
    # To avoid this, we move the import registration inside the test.
    from tensorflow_datasets.testing.dummy_dataset import dummy_dataset  # pylint: disable=g-import-not-at-top
    cls.DATASET_CLASS = dummy_dataset.DummyDataset
    super().setUpClass()

  SPLITS = {
      'train': 20,
  }

  def test_registered(self):
    # We disable the registration test:
    # * `load_test.py` import `dummy_dataset` with `skip_registration` to test
    #   dynamic loading of community datasets.
    # * It seems imports are global between tests.
    # So dataset may or may not be registered depending on test execution order.
    pass


if __name__ == '__main__':
  tfds.testing.test_main()
