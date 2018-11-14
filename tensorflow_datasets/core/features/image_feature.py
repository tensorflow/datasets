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

"""Image feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature

ENCODE_FN = {
    'png': tf.image.encode_png,
    'jpeg': tf.image.encode_jpeg,
}

ACCEPTABLE_CHANNELS = {
    'png': (0, 1, 2, 3),
    'jpeg': (0, 1, 3),
}


class Image(feature.FeatureConnector):
  """Feature which encode/decode an image.

  Input: The image connector accepts as input:
    * path to a {bmp,gif,jpeg,png} image.
    * uint8 array representing an image.

  Output:
    image: tf.Tensor of type tf.uint8 and shape [height, width, num_channels]
    for BMP, JPEG, and PNG images and shape [num_frames, height, width, 3] for
    GIF images.

  Example:
    * In the DatasetInfo object:
      features=features.FeatureDict({
          'input': features.Image(),
          'target': features.Image(shape=(None, None, 1),
                                   encoding_format='png'),
      })

    * During generation:
      yield self.info.features.encode_sample({
          'input': 'path/to/img.jpg',
          'target': np.ones(shape=(64, 64, 1), dtype=np.uint8),
      })
  """

  def __init__(self, shape=(None, None, 3), encoding_format='png'):
    """Construct the connector.

    Args:
      shape: tuple of ints or None, the shape of decoded image.
        For GIF images: (num_frames, height, width, channels=3). num_frames,
          height and width can be None.
        For other images: (height, width, channels). height and width can be
          None. See `tf.image.encode_*` for doc on channels parameter.
        Defaults to (None, None, 3).
      encoding_format: 'jpeg' or 'png' (default). Format to serialize np.ndarray
        images on disk.
        If image is loaded from {bmg,gif,jpeg,png} file, this parameter is
        ignored, and file original encoding is used.

    Raises:
      ValueError: If the shape is invalid
    """
    self._shape = tuple(shape)
    supported = ENCODE_FN.keys()
    if encoding_format not in supported:
      raise ValueError('`encoding_format` must be one of %s.' % supported)
    channels = shape[-1]
    acceptable_channels = ACCEPTABLE_CHANNELS[encoding_format]
    if channels not in acceptable_channels:
      raise ValueError('Acceptable `channels` for %s: %s (was %s)' % (
          encoding_format, acceptable_channels, channels))
    self._encode_fn = ENCODE_FN[encoding_format]

  def get_tensor_info(self):
    # Image is returned as a 3-d uint8 tf.Tensor.
    return feature.TensorInfo(shape=self._shape, dtype=tf.uint8)

  def get_serialized_features(self):
    # Only store raw image (includes size).
    return tf.FixedLenFeature(tuple(), tf.string)

  @utils.memoized_property
  def _runner(self):
    # TODO(epot): Should clear the runner once every image has been encoded.
    # TODO(epot): Better support for multi-shape image (instead of re-building
    # a new graph every time)
    return utils.TFGraphRunner()

  def _encode_image(self, np_image):
    """Returns np_image encoded as jpeg or png."""
    if np_image.dtype != np.uint8:
      raise ValueError('Image should be uint8. Detected: %s.' % np_image.dtype)
    utils.assert_shape_match(np_image.shape, self._shape)
    return self._runner.run(self._encode_fn, np_image)

  def encode_sample(self, image_or_path):
    """Convert the given image into a dict convertible to tf example."""
    if isinstance(image_or_path, np.ndarray):
      encoded_image = self._encode_image(image_or_path)
    else:
      with tf.gfile.Open(image_or_path, 'rb') as image_f:
        encoded_image = image_f.read()
    return encoded_image

  def decode_sample(self, sample):
    """Reconstruct the image from the tf example."""
    img = tf.image.decode_image(sample, channels=self._shape[-1],
                                dtype=tf.uint8)
    img.set_shape(self._shape)
    return img
