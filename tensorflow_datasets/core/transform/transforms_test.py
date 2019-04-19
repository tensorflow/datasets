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

"""Tests for tensorflow_datasets.core.transform.transform."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import transform as transform_lib


class TransformsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls._builder = testing.DummyMnist(data_dir=cls._tfds_tmp_dir)
    cls._builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def _get_data(self, transform):
    ds = self._builder.as_dataset(
        split='train',
        transform=transform,
    )
    ds = dataset_utils.as_numpy(ds)
    return list(ds)

  def test_transformation(self):

    class OneHot(transform_lib.MapAbc):

      def _apply(self, example):
        return tf.one_hot(example, self.feature.num_classes)

    data = self._get_data(transform={
        'label': OneHot(),
        'image': transform_lib.Map(lambda x: tf.cast(x, tf.float32))
    })
    self.assertEqual(set(data[0].keys()), {'label', 'image'})
    self.assertEqual(data[0]['image'].shape, (28, 28, 1))
    self.assertEqual(data[0]['image'].dtype, np.float32)
    self.assertEqual(data[0]['label'].shape, (10,))
    self.assertEqual(data[0]['label'].dtype, np.float32)


if __name__ == '__main__':
  testing.test_main()
