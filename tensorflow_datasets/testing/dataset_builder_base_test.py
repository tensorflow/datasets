# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Base TestCase to test a DatasetBuilder base class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.download import download_manager


class TestCase(tf.test.TestCase):
  """Inherit this class to test your DatasetBuilder class.

  You must set the following class attributes:
    DATASET_CLASS: class object of DatasetBuilder you want to test.
  """

  DATASET_CLASS = None

  @classmethod
  def setUpClass(cls):
    name = cls.__name__
    # Check class has the right attributes
    if cls.DATASET_CLASS is None or not callable(cls.DATASET_CLASS):
      raise AssertionError(
          "Assign your DatasetBuilder class to %s.DATASET_CLASS." % name)

  def setUp(self):
    data_dir = tf.test.get_temp_dir()
    self.builder = self.DATASET_CLASS(data_dir=data_dir)  # pylint: disable=not-callable
    self.sample_dir = os.path.join(
        os.path.dirname(__file__),
        "test_data/fake_samples/%s" % self.builder.name)

  def test_baseclass(self):
    self.assertIsInstance(
        self.builder, dataset_builder.DatasetBuilder,
        "Dataset class must inherit from `dataset_builder.DatasetBuilder`.")
    # Since class was instantiated and base class is ABCMeta, then we know
    # all needed methods were implemented.

  def test_registered(self):
    self.assertIn(self.builder.name, registered.list_builders(),
                  "Dataset was not registered.")

  def test_info(self):
    self.assertIsInstance(self.builder.info, dataset_info.DatasetInfo)

  def test_download_and_prepare(self):
    dl_manager = tf.test.mock.Mock(spec_set=download_manager.DownloadManager)
    dl_manager.download_and_extract.return_value = self.sample_dir
    self.builder.download_and_prepare(dl_manager=dl_manager)

  # TODO(pierrot): retrieve data from dataset


main = tf.test.main
