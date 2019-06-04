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

"""Image transformations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc

import six
import tensorflow as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import image_feature


@six.add_metaclass(abc.ABCMeta)
class Decoder(object):
  """Base image decoder object.

  `tfds.transform.image.Decoder` allow to overwrite the default image decoding,
  for instance to decode and crop at the same time, or to skip the image
  decoding entirely.

  All image decoding should derive from this base class. The decoders have
  to the `self.feature` property corresponding to the feature to which the
  transformation is applied.

  To implement a decoder, the main method to overwrite is `_decode_example`
  which take the serialized image as input and return the decoded image.

  If your decode method change the output dtype, you should also overwrite
  the `get_tensor_info` method. This is required for compatibility with
  `tfds.features.Sequence`.

  """

  def __init__(self):
    self.feature = None

  @api_utils.disallow_positional_args
  def _setup(self, feature):
    """Transformation contructor.

    The initialization of transform object is deferred because the objects only
    know the builder/features on which it is used after it has been
    constructed, the initialization is done in this function.

    Args:
      feature: `tfds.features.FeatureConnector`, the feature to which is applied
        this transformation.
    """
    if not isinstance(feature, image_feature.Image):
      raise ValueError(
          'Try to apply image decoder to non image feature: {}'.format(feature))
    self.feature = feature

  def get_tensor_info(self):
    """Returns the `TensorInfo` containing output shape/dtype."""
    return self.feature.get_tensor_info()

  def decode_example(self, serialized_example):
    """Decode the image."""
    return self._decode_example(serialized_example)

  @abc.abstractmethod
  def _decode_example(self, serialize_image):
    """Decode the image.

    Args:
      serialize_image: `tf.Tensor`, the `tf.string` serialized image

    Returns:
      image: Decoded image.
    """
    raise NotImplementedError('Abstract class')


class SkipDecoding(Decoder):
  """Transformation which skip the image decoding entirelly.

  Example of usage:

  ```python
  ds = ds.load(
      'imagenet2012',
      split='train',
      decoders={
          'image': tfds.transform.image.SkipDecoding(),
      }
  )

  for ex in ds.take(1):
    assert ex['image'].dtype == tf.string
  ```
  """

  def get_tensor_info(self):
    """`SkipDecoding` overwrite the default dtype."""
    return feature_lib.TensorInfo(shape=(), dtype=tf.string)

  def _decode_example(self, serialized_image):
    """Forward the serialized image string."""
    return serialized_image
