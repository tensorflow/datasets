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

"""Utilities for image datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def encode_image_as_png_dict(image, key_prefix="image", encoder=None):
  """Encode image as png and include format and shape in returned dict."""
  if encoder is None:
    encoder = ImagePNGEncoder()
  return {
      key_prefix + "/encoded": encoder.encode(image),
      key_prefix + "/format": "png",
      key_prefix + "/shape": list(image.shape),
  }


def image_classification_generator(images_and_labels):
  """Yields feature dicts with encoded image and label as 'target'."""
  encoder = ImagePNGEncoder()
  for image, label in images_and_labels:
    feature_dict = {"target": label}
    image_dict = encode_image_as_png_dict(image, "input", encoder=encoder)
    feature_dict.update(image_dict)
    yield feature_dict


class ImagePNGEncoder(object):
  """Encodes Tensor images to PNG in graph mode and Eager mode."""

  def __init__(self):
    self._graph_initialized = False
    self._session = None

  def encode(self, image):
    """Encode image to PNG.

    Args:
      image: `uint8` `Tensor` of shape `[height, width, channels]`.

    Returns:
      `str` `Tensor` png-encoded image
    """
    if tf.executing_eagerly():
      return tf.image.encode_png(image).numpy()
    else:
      return self._graph_encode(image)

  def _graph_encode(self, image):
    if not self._graph_initialized:
      self._init_graph_mode_encoder(image)
    return self._session.run(
        self._encoded_t, feed_dict={self._image_placeholder: image})

  def _init_graph_mode_encoder(self, image):
    assert not self._graph_initialized
    self._graph_initialized = True

    self._graph = tf.Graph()
    with self._graph.as_default():
      self._image_placeholder = tf.placeholder(
          dtype=tf.uint8, shape=image.shape)
      self._encoded_t = tf.image.encode_png(self._image_placeholder)
      self._session = tf.Session()

  def __del__(self):
    if self._session is not None:
      self._session.close()


def decode_png(png, image_shape):
  """TensorFlow function to decodes a PNG and set its shape."""
  image = tf.image.decode_png(png, channels=image_shape[-1])
  image.set_shape(image_shape)
  return image
