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

"""Tests for tensorflow_datasets.core.features.image_feature."""

import contextlib
import enum
import os
import pathlib
from typing import Optional, Type

from absl.testing import parameterized
import numpy as np
import PIL
import pytest
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib

randint = np.random.randint


class LibWithImportError(enum.Enum):
  CV2 = 'cv2'
  PIL = 'pil'


@contextlib.contextmanager
def make_cv2_fail():
  """Recreates OpenCV not being installed during the test."""
  real_cv2 = tfds.features.image_feature.cv2
  tfds.features.image_feature.cv2 = None
  try:
    yield LibWithImportError.CV2
  finally:
    tfds.features.image_feature.cv2 = real_cv2


@contextlib.contextmanager
def make_pil_fail():
  """Recreates Pillow not being installed during the test."""
  real_pil = tfds.features.image_feature.PIL_Image
  tfds.features.image_feature.PIL_Image = None
  try:
    yield LibWithImportError.PIL
  finally:
    tfds.features.image_feature.PIL_Image = real_pil


@contextlib.contextmanager
def make_none_fail():
  """Used for a regular scenario, where both OpenCV and PIL are installed."""
  yield


def _unsupported_images_for_pil(
    np_dtype: Type[np.generic], failing_lib: Optional[LibWithImportError]
) -> bool:
  # PIL is used when OpenCV is not installed, but PIL doesn't support 16-bit
  # images.
  return np_dtype == np.uint16 and failing_lib == LibWithImportError.CV2


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
      if _unsupported_images_for_pil(np_dtype, failing_lib):
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
          [
              [[0, 255, 0, 255], [255, 0, 0, 255], [255, 0, 255, 255]],
              [[0, 0, 255, 255], [255, 255, 0, 255], [126, 127, 128, 255]],
          ],
          dtype=np_dtype,
      )[
          :, :, :channels
      ]  # Truncate (h, w, 4) -> (h, w, c)
      if dtype == np.uint16 or dtype == tf.uint16:
        img_file_expected_content *= 257  # Scale int16 images

      numpy_array = testing.FeatureExpectationItem(
          value=img,
          expected=img,
          expected_np=img,
      )
      file_path_as_string = testing.FeatureExpectationItem(
          value=img_file_path,
          expected=img_file_expected_content,
          expected_np=img_file_expected_content,
      )
      file_path_as_path = testing.FeatureExpectationItem(
          value=pathlib.Path(img_file_path),
          expected=img_file_expected_content,
          expected_np=img_file_expected_content,
      )
      images_bytes = testing.FeatureExpectationItem(
          value=img_byte_content,
          expected=img_file_expected_content,
          expected_np=img_file_expected_content,
      )
      img_shape_can_be_dynamic = testing.FeatureExpectationItem(
          value=img_other_shape,
          expected=img_other_shape,
          expected_np=img_other_shape,
      )
      invalid_type = testing.FeatureExpectationItem(
          value=randint(256, size=(128, 128, channels), dtype=np.uint32),
          raise_cls=ValueError,
          raise_cls_np=ValueError,
          raise_msg='dtype should be',
      )
      tests = [
          numpy_array,
          file_path_as_string,
          file_path_as_path,
          images_bytes,
          img_shape_can_be_dynamic,
          invalid_type,
      ]
      # PIL doesn't support 16-bit images.
      if (failing_lib != LibWithImportError.PIL) and np_dtype != np.uint16:
        tests.append(
            testing.FeatureExpectationItem(
                value=PIL.Image.open(img_file_path),
                expected=img_file_expected_content,
                expected_np=img_file_expected_content,
            )
        )
      self.assertFeature(
          feature=features_lib.Image(shape=(None, None, channels), dtype=dtype),
          shape=(None, None, channels),
          dtype=dtype,
          tests=tests,
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
      if _unsupported_images_for_pil(np_dtype, failing_lib):
        return
      invalid_number_of_dimensions = testing.FeatureExpectationItem(
          value=randint(256, size=(128, 128), dtype=np_dtype),
          raise_cls=ValueError,
          raise_cls_np=ValueError,
          raise_msg='must have the same rank',
      )
      invalid_number_of_channels = testing.FeatureExpectationItem(
          value=randint(256, size=(128, 128, 1), dtype=np_dtype),
          raise_cls=ValueError,
          raise_cls_np=ValueError,
          raise_msg='are incompatible',
      )
      self.assertFeature(
          feature=features_lib.Image(shape=(None, None, channels), dtype=dtype),
          shape=(None, None, channels),
          dtype=dtype,
          tests=[invalid_number_of_dimensions, invalid_number_of_channels],
          test_attributes=dict(
              _encoding_format=None,
              _use_colormap=False,
          ),
      )

  @parameterized.product(
      make_lib_fail=[make_none_fail, make_cv2_fail, make_pil_fail]
  )
  def test_image_with_statically_defined_shape(self, make_lib_fail):
    with make_lib_fail():
      img_shaped = randint(256, size=(32, 64, 1), dtype=np.uint8)

      img_shape_should_be_conserved = testing.FeatureExpectationItem(
          value=img_shaped,
          expected=img_shaped,
          expected_np=img_shaped,
      )
      img_shape_should_be_static = testing.FeatureExpectationItem(
          value=randint(256, size=(31, 64, 1), dtype=np.uint8),
          raise_cls=ValueError,
          raise_cls_np=ValueError,
          raise_msg='are incompatible',
      )
      self.assertFeature(
          feature=features_lib.Image(
              shape=(32, 64, 1),
              encoding_format='png',
              use_colormap=True,
          ),
          shape=(32, 64, 1),
          dtype=np.uint8,
          tests=[img_shape_should_be_conserved, img_shape_should_be_static],
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

      numpy_array = testing.FeatureExpectationItem(
          value=img,
          expected=img,
          expected_np=img,
      )
      img_shape_can_be_dynamic = testing.FeatureExpectationItem(
          value=img_other_shape,
          expected=img_other_shape,
          expected_np=img_other_shape,
      )
      invalid_type = testing.FeatureExpectationItem(
          value=img.astype(np.float64),
          raise_cls=ValueError,
          raise_cls_np=ValueError,
          raise_msg='dtype should be',
      )
      self.assertFeature(
          feature=features_lib.Image(shape=(None, None, 1), dtype=dtype),
          shape=(None, None, 1),
          dtype=dtype,
          tests=[
              numpy_array,
              img_shape_can_be_dynamic,
              invalid_type,
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


def test_pil_encoding():
  image_feat = features_lib.Image(encoding_format='png')
  x = np.uint8(np.array([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]]))
  pil_image = PIL.Image.fromarray(x)
  pil_image.format = 'png'
  encoded_example = image_feat.encode_example(pil_image)

  assert isinstance(encoded_example, bytes)
