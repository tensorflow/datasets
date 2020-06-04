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
"""Test for ImageLabelFolder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow_datasets.public_api as tfds

original_init = tfds.ImageLabelFolder.__init__

def new_init(self, root_dir=None, **kwargs):
  assert root_dir is None
  del kwargs
  root_dir = os.path.join(
      tfds.core.utils.tfds_dir(), 'testing',
      'test_data', 'fake_examples', 'image_label_folder')
  original_init(self, root_dir=root_dir)

tfds.ImageLabelFolder.__init__ = new_init

class ImageLabelFolderTest(tfds.testing.DatasetBuilderTestCase):
  """Test for ImageLabelFolder."""

  DATASET_CLASS = tfds.ImageLabelFolder

  SPLITS = {
      "train": 2,  # Number of examples.
      "test": 6,
  }

  def test_registered(self):
    self.assertNotIn("image_label_folder", tfds.list_builders(),
                     "This dataset should not be registered.")


if __name__ == "__main__":
  tfds.testing.test_main()
