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

"""Image feature.

The `features.Image` allows to easily encode an image into a 3D tensor of
uint8.
The features.Image can take as input an image path (png or jpg), or a numpy
array. Images can have either static (ex: (64, 64, 3)), or dynamic (ex:
(None, None, 1)) shape.

Example:

In the DatasetInfo object:

  specs=features.Specs({
      'input': features.Image(),  # Dynamic shape
      'target': features.Image(shape=(64, 64, 3)),  # Static shape
  })

During generation:

  yield self.info.spec.encode_sample({
      'input': 'path/to/img.jpg',
      'target': np.ones(shape=(64, 64, 3), dtype=np.uint8),
  })

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature


ENCODE_FN = {
    'png': tf.image.encode_png,
    'jpg': tf.image.encode_jpeg,
}


class Image(feature.FeatureConnector):
  """Feature which encode/decode an image.

  Input: The image connector accepts as input:
    * A path to a jpg or png image.
    * A 3-D numpy uint8 array

  Output:
    image: The 3-D image tf.Tensor of type tf.uint8
  """
  # Should we support 2D array too ?
  # Should we support float images ?
  # Add an option to resize the shape automatically ?

  def __init__(self, shape=None):
    """Construct the connector.

    Args:
      shape (tuple): The shape of the image (h, w, c). The image dimensions can
        be None if the images do not have constant length.

    Raises:
      ValueError: If the shape is invalid
    """
    self._shape = shape or (None, None, 1)
    self._image_encoder = None
    # Runner to execute the image encoding/decoding
    self._runner = utils.TFGraphRunner()

    if len(self._shape) != 3:
      raise ValueError('Shape {} should be of length 3.'.format(
          self._shape))
    if self._shape[-1] is None:
      raise ValueError('Shape {} should have a non-None channel.'.format(
          self._shape))

  def get_specs(self):
    return {
        'encoded': tf.FixedLenFeature(tuple(), tf.string),
        'format': tf.FixedLenFeature(tuple(), tf.string),
        'shape': tf.FixedLenFeature((3,), tf.int32),
    }

  def encode_sample(self, image_or_path):
    """Convert the given image into a dict convertible to tf example."""
    if isinstance(image_or_path, six.string_types):
      # TODO(epot): np_image = load_image_from_disk(image_or_path)
      raise NotImplementedError
    elif isinstance(image_or_path, np.ndarray):
      np_image = image_or_path
    else:
      # Could also add PIL support
      raise ValueError('Could not convert {} to image'.format(image_or_path))

    # Check that the image is valid
    if np_image.dtype != np.uint8:
      raise ValueError('Image should be uint8. Detected: {}'.format(
          np_image.dtype))
    utils.assert_shape_match(np_image.shape, self._shape)

    # TODO(epot): Should support additional format
    image_format = 'png'
    # TODO(epot): Should clear the runner once every image has been encoded.
    # TODO(epot): Better support for multi-shape image (instead of re-building
    # a new graph every time)
    image_encoded = self._runner.run(ENCODE_FN[image_format], np_image)

    return {
        'encoded': image_encoded,
        'format': image_format,
        'shape': np_image.shape,
    }

  def decode_sample(self, encoded_image):
    """Reconstruct the image from the tf example."""
    tf_image = tf.image.decode_image(
        encoded_image['encoded'],
        channels=encoded_image['shape'][-1],
        dtype=tf.uint8,
    )
    # TODO(epot): Add image shape. tf_image.set_shape(self._shape) ?
    return tf_image


def load_image_from_disk(image_path):
  # TODO(epot): PIL.load(...)
  _ = image_path
  raise NotImplementedError
