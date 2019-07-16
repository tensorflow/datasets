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

"""Tests for tensorflow_datasets.core.features.image_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib

tf.compat.v1.enable_eager_execution()


randint = np.random.randint


class ImageFeatureTest(testing.FeatureExpectationsTestCase):

  def test_images(self):

    img = randint(256, size=(128, 100, 3), dtype=np.uint8)
    img_other_shape = randint(256, size=(64, 200, 3), dtype=np.uint8)
    img_file_path = os.path.join(os.path.dirname(__file__),
                                 '../../testing/test_data/6pixels.png')
    img_file_expected_content = [  # see tests_data/README.md
        [[0, 255, 0], [255, 0, 0], [255, 0, 255]],
        [[0, 0, 255], [255, 255, 0], [126, 127, 128]],
    ]

    self.assertFeature(
        feature=features_lib.Image(),
        shape=(None, None, 3),
        dtype=tf.uint8,
        tests=[
            # Numpy array
            testing.FeatureExpectationItem(
                value=img,
                expected=img,
),  
            # File path
            testing.FeatureExpectationItem(
                value=img_file_path,
                expected=img_file_expected_content,
            ),
            # 'img' shape can be dynamic
            testing.FeatureExpectationItem(
                value=img_other_shape,
                expected=img_other_shape,
            ),
            # Invalid type
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128, 3), dtype=np.uint32),
                raise_cls=ValueError,
                raise_msg='dtype should be',
            ),
            # Invalid number of dimensions
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128), dtype=np.uint8),
                raise_cls=ValueError,
                raise_msg='must have the same rank',
            ),
            # Invalid number of channels
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128, 1), dtype=np.uint8),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ],
    )

  def test_image_shaped(self):

    img_shaped = randint(256, size=(32, 64, 3), dtype=np.uint8)

    self.assertFeature(
        # Image with statically defined shape
        feature=features_lib.Image(shape=(32, 64, 3)),
        shape=(32, 64, 3),
        dtype=tf.uint8,
        tests=[
            testing.FeatureExpectationItem(
                value=img_shaped,
                expected=img_shaped,
            ),
            # 'img_shaped' shape should be static
            testing.FeatureExpectationItem(
                value=randint(256, size=(31, 64, 3), dtype=np.uint8),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ],
    )

  def  test_image_dtype(self):
      img = randint(256 , size=(128,128,3) ,dtype=np.uint8)
      
      # Image with statically defined dtype   
      self.assertFeature(
        feature=features_lib.Image( dtype=tf.uint16),
        shape=(None, None, 3),
        dtype=tf.uint8,
        tests=[
            testing.FeatureExpectationItem(
                value = img , 
                raise_cls = ValueError , 
                raise_msg = 'dtype should be'
            ),
        ],
    )

if __name__ == '__main__':
  testing.test_main()
