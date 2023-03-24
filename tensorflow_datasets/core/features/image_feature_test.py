# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

import contextlib
import enum
import os
import pathlib

from absl.testing import parameterized
import numpy as np
import pytest
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib

randint = np.random.randint


class FailingLib(enum.Enum):
  CV2 = 'cv2'
  PIL = 'pil'


@contextlib.contextmanager
def make_cv2_fail():
  real_cv2 = tfds.features.image_feature.cv2
  tfds.features.image_feature.cv2 = None
  try:
    yield FailingLib.CV2
  finally:
    tfds.features.image_feature.cv2 = real_cv2


@contextlib.contextmanager
def make_pil_fail():
  real_pil = tfds.features.image_feature.PIL_Image
  tfds.features.image_feature.PIL_Image = None
  try:
    yield FailingLib.PIL
  finally:
    tfds.features.image_feature.PIL_Image = real_pil


# This is used for a regular scenario, where neither OpenCV, nor PIL fail.
make_none_fail = contextlib.nullcontext  # pylint: disable=invalid-name


class ImageFeatureTest(
    testing.FeatureExpectationsTestCase, parameterized.TestCase
):

  @parameterized.product(
      make_lib_fail=[make_none_fail, make_cv2_fail, make_pil_fail],
      dtypes=[
          (np.uint8, np.uint8),
          (np.uint16, np.uint16),
          (tf.uint8, np.uint8),
          (tf.uint16, np.uint16),
      ],
      channels=[1, 3, 4],
  )
  def test_images(self, make_lib_fail, dtypes, channels):
    dtype, np_dtype = dtypes
    with make_lib_fail() as failing_lib:
      # PIL is used when OpenCV fails, but PIL doesn't support 16-bit images.
      if np_dtype == np.uint16 and failing_lib == FailingLib.CV2:
        return
      img = randint(256, size=(128, 100, channels), dtype=np_dtype)
      img_other_shape = randint(256, size=(64, 200, channels), dtype=np_dtype)

      filename = {
          np.uint8: {
              1: '6pixels_grayscale.png',
              3: '6pixels.png',
              4: '6pixels_4chan.png',
          },
          np.uint16: {
              1: '6pixels_grayscale_16bit.png',
              3: '6pixels_16bit.png',
              4: '6pixels_16bit_4chan.png',
          },
      }[np_dtype][channels]

      img_file_path = os.path.join(
          os.path.dirname(__file__), '../../testing/test_data', filename
      )
      with tf.io.gfile.GFile(img_file_path, 'rb') as f:
        img_byte_content = f.read()
      img_file_expected_content = np.array(
          [  # see tensorflow_datasets/testing/test_data/README.md
              [[0, 255, 0, 255], [255, 0, 0, 255], [255, 0, 255, 255]],
              [[0, 0, 255, 255], [255, 255, 0, 255], [126, 127, 128, 255]],
          ],
          dtype=np_dtype,
      )[
          :, :, :channels
      ]  # Truncate (h, w, 4) -> (h, w, c)
      if dtype == np.uint16 or dtype == tf.uint16:
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
                  expected_np=img,
              ),
              # File path
              testing.FeatureExpectationItem(
                  value=img_file_path,
                  expected=img_file_expected_content,
                  expected_np=img_file_expected_content,
              ),
              # File Path
              testing.FeatureExpectationItem(
                  value=pathlib.Path(img_file_path),
                  expected=img_file_expected_content,
                  expected_np=img_file_expected_content,
              ),
              # Images bytes
              testing.FeatureExpectationItem(
                  value=img_byte_content,
                  expected=img_file_expected_content,
                  expected_np=img_file_expected_content,
              ),
              # 'img' shape can be dynamic
              testing.FeatureExpectationItem(
                  value=img_other_shape,
                  expected=img_other_shape,
                  expected_np=img_other_shape,
              ),
              # Invalid type
              testing.FeatureExpectationItem(
                  value=randint(
                      256, size=(128, 128, channels), dtype=np.uint32
                  ),
                  raise_cls=ValueError,
                  raise_cls_np=ValueError,
                  raise_msg='dtype should be',
              ),
          ],
          test_attributes=dict(
              _encoding_format=None,
              _use_colormap=False,
          ),
      )

  @parameterized.product(
      make_lib_fail=[make_none_fail, make_cv2_fail, make_pil_fail],
      dtypes=[
          (np.uint8, np.uint8),
          (tf.uint8, np.uint8),
          (np.uint16, np.uint16),
          (tf.uint16, np.uint16),
      ],
      channels=[3, 4],
  )
  def test_images_with_invalid_shape(self, make_lib_fail, dtypes, channels):
    dtype, np_dtype = dtypes
    with make_lib_fail() as failing_lib:
      # PIL is used when OpenCV fails, but PIL doesn't support 16-bit images.
      if np_dtype == np.uint16 and failing_lib == FailingLib.CV2:
        return
      self.assertFeature(
          feature=features_lib.Image(shape=(None, None, channels), dtype=dtype),
          shape=(None, None, channels),
          dtype=dtype,
          tests=[
              # Invalid number of dimensions
              testing.FeatureExpectationItem(
                  value=randint(256, size=(128, 128), dtype=np_dtype),
                  raise_cls=ValueError,
                  raise_cls_np=ValueError,
                  raise_msg='must have the same rank',
              ),
              # Invalid number of channels
              testing.FeatureExpectationItem(
                  value=randint(256, size=(128, 128, 1), dtype=np_dtype),
                  raise_cls=ValueError,
                  raise_cls_np=ValueError,
                  raise_msg='are incompatible',
              ),
          ],
          test_attributes=dict(
              _encoding_format=None,
              _use_colormap=False,
          ),
      )

  @parameterized.product(
      make_lib_fail=[make_none_fail, make_cv2_fail, make_pil_fail]
  )
  def test_image_shaped(self, make_lib_fail):
    with make_lib_fail():
      img_shaped = randint(256, size=(32, 64, 1), dtype=np.uint8)

      self.assertFeature(
          # Image with statically defined shape
          feature=features_lib.Image(
              shape=(32, 64, 1),
              encoding_format='png',
              use_colormap=True,
          ),
          shape=(32, 64, 1),
          dtype=np.uint8,
          tests=[
              testing.FeatureExpectationItem(
                  value=img_shaped,
                  expected=img_shaped,
                  expected_np=img_shaped,
              ),
              # 'img_shaped' shape should be static
              testing.FeatureExpectationItem(
                  value=randint(256, size=(31, 64, 1), dtype=np.uint8),
                  raise_cls=ValueError,
                  raise_cls_np=ValueError,
                  raise_msg='are incompatible',
              ),
          ],
          test_attributes=dict(
              _encoding_format='png',
              _use_colormap=True,
          ),
      )

  @parameterized.product(
      make_lib_fail=[make_none_fail, make_cv2_fail, make_pil_fail],
      dtype=[np.float32, tf.float32],
  )
  def test_images_float(self, make_lib_fail, dtype):
    with make_lib_fail():
      img = np.random.rand(28, 28, 1).astype(np.float32)
      img_other_shape = np.random.rand(12, 34, 1).astype(np.float32)

      self.assertFeature(
          feature=features_lib.Image(shape=(None, None, 1), dtype=dtype),
          shape=(None, None, 1),
          dtype=dtype,
          tests=[
              # Numpy array
              testing.FeatureExpectationItem(
                  value=img,
                  expected=img,
                  expected_np=img,
              ),
              # 'img' shape can be dynamic
              testing.FeatureExpectationItem(
                  value=img_other_shape,
                  expected=img_other_shape,
                  expected_np=img_other_shape,
              ),
              # Invalid type
              testing.FeatureExpectationItem(
                  value=img.astype(np.float64),
                  raise_cls=ValueError,
                  raise_cls_np=ValueError,
                  raise_msg='dtype should be',
              ),
          ],
          test_attributes=dict(
              _encoding_format=None,
              _use_colormap=False,
          ),
      )

  @parameterized.product(
      dtypes=[
          (np.uint16, np.uint16),
          (tf.uint16, np.uint16),
      ],
      channels=[1, 3, 4],
  )
  def test_cannot_decode_16_bit_images_with_pil(self, dtypes, channels):
    dtype, np_dtype = dtypes
    # PIL is used when OpenCV fails.
    with make_cv2_fail():
      self.assertFeature(
          feature=features_lib.Image(shape=(128, 128, channels), dtype=dtype),
          shape=(128, 128, channels),
          dtype=dtype,
          tests=[
              testing.FeatureExpectationItem(
                  value=randint(256, size=(128, 128, channels), dtype=np_dtype),
                  raise_cls_np=ValueError,
                  raise_msg='PIL does not handle',
              )
          ],
      )

  def test_fail_if_neither_opencv_nor_pil_is_installed(self):
    with make_pil_fail():
      with make_cv2_fail():
        self.assertFeature(
            feature=features_lib.Image(shape=(128, 128, 3), dtype=np.uint8),
            shape=(128, 128, 3),
            dtype=np.uint8,
            tests=[
                testing.FeatureExpectationItem(
                    value=randint(256, size=(128, 128, 3), dtype=np.uint8),
                    raise_cls_np=ImportError,
                    raise_msg='requires either OpenCV or PIL',
                )
            ],
        )


@pytest.mark.parametrize(
    'shape, dtype, encoding_format, err_msg',
    [
        (None, np.uint16, r'jpeg', 'Acceptable `dtype` for jpeg:'),
        (None, tf.uint16, r'jpeg', 'Acceptable `dtype` for jpeg:'),
        (None, np.float32, None, 'only support single-channel'),
        (None, tf.float32, None, 'only support single-channel'),
        ((None, None, 1), np.float64, None, 'Acceptable `dtype`'),
        ((None, None, 1), tf.float64, None, 'Acceptable `dtype`'),
    ],
)
def test_invalid_img(shape, dtype, encoding_format, err_msg):
  with pytest.raises(ValueError, match=err_msg):
    features_lib.Image(
        shape=shape, dtype=dtype, encoding_format=encoding_format
    )
