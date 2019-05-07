# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Test for ImageLabelFolder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
from tensorflow_datasets import testing
from tensorflow_datasets.core import registered
from tensorflow_datasets.image import image_folder


class ImageLabelFolderTest(testing.DatasetBuilderTestCase):
  """Test for ImageLabelFolder."""
  DATASET_CLASS = functools.partial(
      image_folder.ImageLabelFolder, dataset_name="image_folder_data")
  # The above construct forces us to disable those checks:
  MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = False
  SPLITS = {
      "train": 2,  # Number of examples.
      "test": 6,
  }

  def test_info(self):
    pass

  def test_registered(self):
    self.assertIn("image_label_folder", registered.list_builders(),
                  "Dataset was not registered.")


if __name__ == "__main__":
  testing.test_main()
