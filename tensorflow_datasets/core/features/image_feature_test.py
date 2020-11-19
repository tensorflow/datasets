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

"""Tests for tensorflow_datasets.core.features.image_feature."""

import os
import pathlib

from absl.testing import parameterized
import numpy as np
import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib

tf.enable_v2_behavior()


randint = np.random.randint


class ImageFeatureTest(
    testing.FeatureExpectationsTestCase, parameterized.TestCase):

  @parameterized.parameters(
      (tf.uint8, 3),
      (tf.uint16, 3),
      (tf.uint8, 4),
  )
  def test_images(self, dtype, channels):
    np_dtype = dtype.as_numpy_dtype
    img = randint(256, size=(128, 100, channels), dtype=np_dtype)
    img_other_shape = randint(256, size=(64, 200, channels), dtype=np_dtype)

    filename = {
        3: '6pixels.png',
        4: '6pixels_4chan.png',
    }[channels]

    img_file_path = os.path.join(
        os.path.dirname(__file__), '../../testing/test_data', filename
    )
    with tf.io.gfile.GFile(img_file_path, 'rb') as f:
      img_byte_content = f.read()
    img_file_expected_content = np.array([  # see tests_data/README.md
        [[0, 255, 0, 255], [255, 0, 0, 255], [255, 0, 255, 255]],
        [[0, 0, 255, 255], [255, 255, 0, 255], [126, 127, 128, 255]],
    ], dtype=np_dtype)[:, :, :channels]  # Truncate (h, w, 4) -> (h, w, c)
    if dtype == tf.uint16:
      img_file_expected_content *= 257  # Scale int16 images

    self.assertFeature(
        feature=features_lib.Image(shape=(None, None, channels), dtype=dtype),
        shape=(None, None, channels),
        dtype=dtype,
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
            # File Path
            testing.FeatureExpectationItem(
                value=pathlib.Path(img_file_path),
                expected=img_file_expected_content,
            ),
            # Images bytes
            testing.FeatureExpectationItem(
                value=img_byte_content,
                expected=img_file_expected_content,
            ),
            # 'img' shape can be dynamic
            testing.FeatureExpectationItem(
                value=img_other_shape,
                expected=img_other_shape,
            ),
            # Invalid type
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128, channels), dtype=np.uint32),
                raise_cls=ValueError,
                raise_msg='dtype should be',
            ),
            # Invalid number of dimensions
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128), dtype=np_dtype),
                raise_cls=ValueError,
                raise_msg='must have the same rank',
            ),
            # Invalid number of channels
            testing.FeatureExpectationItem(
                value=randint(256, size=(128, 128, 1), dtype=np_dtype),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ],
        test_attributes=dict(_encoding_format=None)
    )

  def test_image_shaped(self):

    img_shaped = randint(256, size=(32, 64, 3), dtype=np.uint8)

    self.assertFeature(
        # Image with statically defined shape
        feature=features_lib.Image(shape=(32, 64, 3), encoding_format='png'),
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
        test_attributes=dict(_encoding_format='png')
    )


if __name__ == '__main__':
  testing.test_main()
