# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for ble_wind_field."""

from unittest import mock

from tensorflow_datasets.datasets.ble_wind_field import ble_wind_field_dataset_builder
import tensorflow_datasets.public_api as tfds


class BLEWindFieldTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = ble_wind_field_dataset_builder.Builder
  SPLITS = {'train': 4}

  def setUp(self):
    super().setUp()
    # Patch BLEWindField's GCS_URL and GCS_FILENAME class attributes to
    # point to the placeholder Zarr array instead. Also patch
    # tfds.core.lazy_imports.gcsfs_store to turn it into an identity function,
    # because the original function doesn't work with local paths (i.e. not of
    # the form 'gs://*').
    module_name = self.DATASET_CLASS.__module__
    class_name = self.DATASET_CLASS.__name__
    patchers = [
        mock.patch(f'{module_name}.{class_name}.GCS_URL', self.dummy_data),
        mock.patch(f'{module_name}.{class_name}.GCS_FILENAME', 'array.zarr'),
        mock.patch(
            'tensorflow_datasets.public_api.core.lazy_imports.gcsfs_store',
            lambda s: s,
        ),
    ]
    for patcher in patchers:
      patcher.start()
    self.patchers.extend(patchers)


if __name__ == '__main__':
  tfds.testing.test_main()
