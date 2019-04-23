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

"""Transform API.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc

import six
from tensorflow_datasets.core import api_utils


@six.add_metaclass(abc.ABCMeta)
class TransformAbc(object):
  """Base transformation object.

  Transformations object allow to apply modifications to the default
  `tfds.features.FeatureConnector` decoding. For instance, skiping the image
  decoding or applying some data augmentation.

  All transformations derive from this base class. Transformations have access
  to the `self.feature` property corresponding to the feature to which the
  transformation is applied.

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
    self.feature = feature

  @property
  def dtype(self):
    """New dtype returned after the transformation.

    If the transformation modify the returned dtype, then it should be updated
    here.

    Returns:
      dtype: The tf dtype returned by the feature if modified, or None.
    """
    return None


class MapAbc(TransformAbc):
  """Base class to apply a transformation to the decoded example.

  `MabAbc` transformations are applied after the example has been decoded and
  can be used to apply additional post-processing to the example.
  """

  def setup_and_apply(self, example, **setup_kwargs):
    """Initialize the transformation and apply it."""
    self._setup(**setup_kwargs)
    return self._apply(example)

  @abc.abstractmethod
  def _apply(self, example):
    """Apply the transformation to the example.

    Args:
      example: The example after decoded by the feature.

    Returns:
      example: The new example after transformation
    """
    raise NotImplementedError('Abstract method')


class Map(MapAbc):
  """Transformation which apply some function to the decoded image.

  Usage:
  """

  def __init__(self, fct, *args, **kwargs):
    """Map constructor.

    Args:
      fct: Function of form `fct(example, *args, **kwargs) => example`, will be
        applied to the feature connector after decoding.
      *args: Args to forward to `fct`
      **kwargs: Kwargs to forward to `fct`
    """
    super(Map, self).__init__()
    self._fct = fct
    self._args = tuple(args)
    self._kwargs = dict(**kwargs)

  def _apply(self, decoded_image):
    """Apply the transformation to the example."""
    return self._fct(decoded_image, *self._args, **self._kwargs)
