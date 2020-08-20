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

"""Image feature."""

import json
import os

import numpy as np
import six
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json

ENCODE_FN = {
    'png': tf.image.encode_png,
    'jpeg': tf.image.encode_jpeg,
}

ACCEPTABLE_CHANNELS = {
    'png': (0, 1, 2, 3),
    'jpeg': (0, 1, 3),
}

ACCEPTABLE_DTYPES = {
    'png': [tf.uint8, tf.uint16],
    'jpeg': [tf.uint8],
}


class Image(feature.FeatureConnector):
  """`FeatureConnector` for images.

  During `_generate_examples`, the feature connector accept as input any of:

    * `str`: path to a {bmp,gif,jpeg,png} image (ex: `/path/to/img.png`).
    * `np.array`: 3d `np.uint8` array representing an image.
    * A file object containing the png or jpeg encoded image string (ex:
      `io.BytesIO(encoded_img_bytes)`)

  Output:

    `tf.Tensor` of type `tf.uint8` and shape `[height, width, num_channels]`
    for BMP, JPEG, and PNG images and shape `[num_frames, height, width, 3]` for
    GIF images.

  Example:

    * In the `tfds.core.DatasetInfo` object:

    ```python
    features=features.FeaturesDict({
        'input': features.Image(),
        'target': features.Image(shape=(None, None, 1),
                                   encoding_format='png'),
    })
    ```

    * During generation:

    ```python
    yield {
        'input': 'path/to/img.jpg',
        'target': np.ones(shape=(64, 64, 1), dtype=np.uint8),
    }
    ```
  """

  def __init__(self, *, shape=None, dtype=None, encoding_format=None):
    """Construct the connector.

    Args:
      shape: tuple of ints or None, the shape of decoded image.
        For GIF images: (num_frames, height, width, channels=3). num_frames,
          height and width can be None.
        For other images: (height, width, channels). height and width can be
          None. See `tf.image.encode_*` for doc on channels parameter.
        Defaults to (None, None, 3).
      dtype: tf.uint16 or tf.uint8 (default).
        tf.uint16 can be used only with png encoding_format
      encoding_format: 'jpeg' or 'png' (default). Format to serialize np.ndarray
        images on disk.
        If image is loaded from {bmg,gif,jpeg,png} file, this parameter is
        ignored, and file original encoding is used.

    Raises:
      ValueError: If the shape is invalid
    """
    self._encoding_format = None
    self._shape = None
    self._runner = None
    self._dtype = None

    # Set and validate values
    self.set_encoding_format(encoding_format or 'png')
    self.set_shape(shape or (None, None, 3))
    self.set_dtype(dtype or tf.uint8)

  def set_dtype(self, dtype):
    """Update the dtype."""
    dtype = tf.as_dtype(dtype)
    acceptable_dtypes = ACCEPTABLE_DTYPES[self._encoding_format]
    if dtype not in acceptable_dtypes:
      raise ValueError('Acceptable `dtype` for %s: %s (was %s)' % (
          self._encoding_format, acceptable_dtypes, dtype))
    self._dtype = dtype

  def set_encoding_format(self, encoding_format):
    """Update the encoding format."""
    supported = ENCODE_FN.keys()
    if encoding_format not in supported:
      raise ValueError('`encoding_format` must be one of %s.' % supported)
    self._encoding_format = encoding_format

  def set_shape(self, shape):
    """Update the shape."""
    channels = shape[-1]
    acceptable_channels = ACCEPTABLE_CHANNELS[self._encoding_format]
    if channels not in acceptable_channels:
      raise ValueError('Acceptable `channels` for %s: %s (was %s)' % (
          self._encoding_format, acceptable_channels, channels))
    self._shape = tuple(shape)

  def get_tensor_info(self):
    # Image is returned as a 3-d uint8 tf.Tensor.
    return feature.TensorInfo(shape=self._shape, dtype=self._dtype)

  def get_serialized_info(self):
    # Only store raw image (includes size).
    return feature.TensorInfo(shape=(), dtype=tf.string)

  def _encode_image(self, np_image):
    """Returns np_image encoded as jpeg or png."""
    if not self._runner:
      self._runner = utils.TFGraphRunner()
    if np_image.dtype != self._dtype.as_numpy_dtype:
      raise ValueError('Image dtype should be %s. Detected: %s.' % (
          self._dtype.as_numpy_dtype, np_image.dtype))
    utils.assert_shape_match(np_image.shape, self._shape)
    return self._runner.run(ENCODE_FN[self._encoding_format], np_image)

  def __getstate__(self):
    state = self.__dict__.copy()
    state['_runner'] = None
    return state

  def encode_example(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    if isinstance(image_or_path_or_fobj, np.ndarray):
      encoded_image = self._encode_image(image_or_path_or_fobj)
    elif isinstance(image_or_path_or_fobj, six.string_types):
      with tf.io.gfile.GFile(image_or_path_or_fobj, 'rb') as image_f:
        encoded_image = image_f.read()
    else:
      encoded_image = image_or_path_or_fobj.read()
    return encoded_image

  def decode_example(self, example):
    """Reconstruct the image from the tf example."""
    img = tf.image.decode_image(
        example, channels=self._shape[-1], dtype=self._dtype)
    img.set_shape(self._shape)
    return img

  def save_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    filepath = _get_metadata_filepath(data_dir, feature_name)
    with tf.io.gfile.GFile(filepath, 'w') as f:
      json.dump({
          'shape': [-1 if d is None else d for d in self._shape],
          'encoding_format': self._encoding_format,
      }, f, sort_keys=True)

  def load_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Restore names if defined
    filepath = _get_metadata_filepath(data_dir, feature_name)
    if tf.io.gfile.exists(filepath):
      with tf.io.gfile.GFile(filepath, 'r') as f:
        info_data = json.load(f)
      self.set_encoding_format(info_data['encoding_format'])
      self.set_shape([None if d == -1 else d for d in info_data['shape']])

  def repr_html(self, ex: np.ndarray) -> str:
    """Images are displayed as thumbnail."""
    # Normalize image and resize
    img = create_thumbnail(ex)

    # Convert to base64
    img_str = utils.get_base64(lambda buff: img.save(buff, format='PNG'))

    # Display HTML
    return f'<img src="data:image/png;base64,{img_str}" alt="Img" />'

  @classmethod
  def from_json_content(cls, value: Json) -> 'Image':
    shape = tuple(value['shape'])
    dtype = tf.dtypes.as_dtype(value['dtype'])
    encoding_format = value['encoding_format']
    return cls(shape=shape, dtype=dtype, encoding_format=encoding_format)

  def to_json_content(self) -> Json:
    return {
        'shape': list(self._shape),
        'dtype': self._dtype.name,
        'encoding_format': self._encoding_format
    }


def create_thumbnail(ex):
  """Creates the image from the np.array input."""
  PIL_Image = lazy_imports_lib.lazy_imports.PIL_Image  # pylint: disable=invalid-name

  _, _, c = ex.shape
  postprocess = _postprocess_noop
  if c == 1:
    ex = ex.squeeze(axis=-1)
    mode = 'L'
  elif ex.dtype == np.uint16:
    mode = 'I;16'
    postprocess = _postprocess_convert_rgb
  else:
    mode = None
  img = PIL_Image.fromarray(ex, mode=mode)
  img = postprocess(img)
  img.thumbnail((128, 128))  # Resize the image in-place
  return img


def _postprocess_noop(img):
  return img


def _postprocess_convert_rgb(img):
  return img.convert('RGB')


def _get_metadata_filepath(data_dir, feature_name):
  return os.path.join(data_dir, '{}.image.json'.format(feature_name))
