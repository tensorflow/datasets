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

"""Feature connector.

FeatureConnector is a way of abstracting what data is returned by the
tensorflow/datasets builders from how they are encoded/decoded from file.

#Use FeatureConnector in DatasetBuilder

1) In the _build_info() function, define the features as you would like them
to be returned by the tf.data.Dataset() object.

Ex:
  features=features.FeaturesDict({
      'input': features.Image(),
      'target': features.Text(encoder=SubWordEncoder()),
      'extra_data': {
          'label_id': tf.int64,
          'language': tf.string,
      }
  })

The tf.data.Dataset will return each samples as a dict:
  {
      'input': tf.Tensor(shape=(batch, height, width, channel), tf.uint8),
      'target': tf.Tensor(shape=(batch, sequence_length), tf.int64),
      'extra_data': {
          'label_id': tf.Tensor(shape=(batch,), tf.int64),
          'language': tf.Tensor(shape=(batch,), tf.string),
      }
  }

2) In the generator function, yield the samples to match what you have defined
in the spec. The values will automatically be encoded.

  yield self.info.features.encode_sample({
      'input': np_image,
      'target': 'This is some text',
      'extra_data': {
          'label_id': 43,
          'language': 'en',
      }
  })

# Create your own FeatureConnector

To create your own feature connector, you need to inherit from FeatureConnector
and implement the abstract methods.

1. If your connector only contains one value, then the get_serialized_features,
   encode_sample, and decode_sample can directly process single value, without
   wrapping it in a dict.

2. If your connector is a container of multiple sub-connectors, the easiest
   way is to inherit from features.FeaturesDict and use the super() methods to
   automatically encode/decode the sub-connectors. See features.OneOf as
   example.

This file contains the following FeatureConnector:
 * FeatureConnector: The abstract base class defining the interface
 * FeaturesDict: Container of FeatureConnector
 * Tensor: Simple tensor value with static or dynamic shape
 * OneOf: Choose one between multiple sub-connector at runtime

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import posixpath

import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import utils


@six.add_metaclass(abc.ABCMeta)
class FeatureConnector(object):
  """Feature connector class.

  This class provides an interface between the way the information is stored
  on disk, and the way it is presented to the user.

  Here is a diagram on how FeatureConnector methods fit into the data
  generation/reading:

    generator => encode_sample() => tf_example => decode_sample() => data dict

  The connector can either get raw or dictionary values as input, depending on
  the connector type.

  """

  @abc.abstractmethod
  def get_serialized_features(self):
    """Return the tf-example features for the adapter, as stored on disk.

    This function indicates how this feature is encoded on file internally.
    The DatasetBuilder are written on disk as tf.train.Example proto.

    Ex:

      return {
          'image': tf.VarLenFeature(tf.uint8):
          'height': tf.FixedLenFeature((), tf.int32),
          'width': tf.FixedLenFeature((), tf.int32),
      }

    FeatureConnector which are not containers should return the feature proto
    directly:

      return tf.FixedLenFeature((64, 64), tf.uint8)

    Returns:
      features: Either a dict of feature proto object, or a feature proto object

    """
    raise NotImplementedError

  @abc.abstractmethod
  def encode_sample(self, sample_data):
    """Encode the feature dict into tf-example compatible input.

    Args:
      sample_data: Value or dictionary of values to convert into tf-example
        compatible data.

    Returns:
      tfexample_data: Data or dictionary of data to write as tf-example
    """
    raise NotImplementedError

  @abc.abstractmethod
  def decode_sample(self, tfexample_data):
    """Decode the feature dict to TF compatible input.

    Args:
      tfexample_data: Data or dictionary of data, as read by the tf-example
        reader.

    Returns:
      tensor_data: Tensor or dictionary of tensor, output of the tf.data.Dataset
        object
    """
    raise NotImplementedError

  @utils.memoized_property
  def features_keys(self):
    """List of the feature features keys."""
    features = self.get_serialized_features()
    if isinstance(features, dict):
      return list(features)
    return None


class FeaturesDict(FeatureConnector):
  """Main feature connector orchestrator.

  The encode/decode method of the spec feature will recursivelly encode/decode
  every sub-connector given on the constructor.
  Other features can inherit from this class and call super() in order to get
  nested container.

  Example:

  For DatasetInfo:

    features = tfds.features.FeaturesDict({
        'input': tfds.features.Image(),
        'target': tf.int32,
    })

  At generation time:

    for image, label in generate_samples:
      yield self.info.features.encode_sample({
          'input': image,
          'output': label
      })

  At tf.data.Dataset() time:

    for sample in tfds.load(...):
      tf_input = sample['input']
      tf_output = sample['output']

  For nested features, the FeaturesDict will internally flatten the keys for the
  features and the conversion to tf.train.Example. Indeed, the tf.train.Example
  proto do not support nested feature, while tf.data.Dataset does.
  But internal transformation should be invisible to the user.

  Example:

    tfds.features.FeaturesDict({
        'input': tf.int32,
        'target': {
            'height': tf.int32,
            'width': tf.int32,
        },
    })

  Will internally store the data as:

  {
      'input': ...,
      'target/height': ...,
      'target/width': ...,
  }

  """

  def __init__(self, feature_dict):
    """Initialize the features.

    Args:
      feature_dict (dict): Dictionary containing the feature connectors of a
        sample. The keys should correspond to the data dict as returned by
        tf.data.Dataset(). Types (tf.int32,...) and dicts will automatically
        be converted into FeatureConnector.

    Raises:
      ValueError: If one of the given features is not recognised
    """
    super(FeaturesDict, self).__init__()
    self._feature_dict = {k: to_feature(v) for k, v in feature_dict.items()}

  def get_serialized_features(self):
    """See base class for details."""
    # Flatten tf-example features dict
    # Use NonMutableDict to ensure there is no collision between features keys
    features_dict = utils.NonMutableDict()
    for feature_key, feature in self._feature_dict.items():
      serialized_features = feature.get_serialized_features()

      # Features can be either containers (dict of other features) or plain
      # features (ex: single tensor). Plain features have a None
      # feature.features_keys
      if not feature.features_keys:
        features_dict[feature_key] = serialized_features
      else:
        # Sanity check which should always be True, as feature.features_keys is
        # computed using feature.get_serialized_features()
        _assert_keys_match(serialized_features.keys(), feature.features_keys)
        features_dict.update({
            posixpath.join(feature_key, k): v for k, v
            in serialized_features.items()
        })

    return features_dict

  def encode_sample(self, sample_dict):
    """See base class for details."""
    # Flatten dict matching the tf-example features
    # Use NonMutableDict to ensure there is no collision between features keys
    tfexample_dict = utils.NonMutableDict()

    # Iterate over sample fields
    for feature_key, (feature, sample_value) in utils.zip_dict(
        self._feature_dict,
        sample_dict
    ):
      # Encode the field with the associated encoder
      encoded_feature = feature.encode_sample(sample_value)

      # Singleton case
      if not feature.features_keys:
        tfexample_dict[feature_key] = encoded_feature
      # Feature contains sub features
      else:
        _assert_keys_match(encoded_feature.keys(), feature.features_keys)
        tfexample_dict.update({
            posixpath.join(feature_key, k): encoded_feature[k]
            for k in feature.features_keys
        })
    return tfexample_dict

  def decode_sample(self, tfexample_dict):
    """See base class for details."""
    tensor_dict = {}
    # Iterate over the Tensor dict keys
    for feature_key, feature in six.iteritems(self._feature_dict):
      decoded_feature = decode_single_feature_from_dict(
          feature_k=feature_key,
          feature=feature,
          tfexample_dict=tfexample_dict,
      )
      tensor_dict[feature_key] = decoded_feature
    return tensor_dict

  # TODO(epot): Should investigate if fixed size feature read can be more
  # optimized. And eventually expose a property has_fixed_shape_feature.


class Tensor(FeatureConnector):
  """Feature encoding a tf.Tensor value (both fixed and variable)."""
  # TODO(epot): For variable length feature, will probably have to include the
  # shape in the spec, as it seems tf-example lose the shape by flattening the
  # value
  # TODO(epot): Call tf.compat.as_text for string data. Add unittests for str.

  @api_utils.disallow_positional_args
  def __init__(self, shape, dtype):
    """Construct a Tensor feature."""
    self._shape = shape
    self._dtype = dtype

  def get_serialized_features(self):
    """See base class for details."""
    if (self._shape and  # Shape is a sequence (None, ...)
        len(self._shape) >= 2 and
        self._shape[0] is None and
        None not in self._shape[1:]):
      return tf.FixedLenSequenceFeature(shape=self._shape, dtype=self._dtype)
    elif None in self._shape:  # At least one dimension is undefined
      return tf.VarLenFeature(dtype=self._dtype)
    else:
      return tf.FixedLenFeature(shape=self._shape, dtype=self._dtype)

  def encode_sample(self, sample_data):
    """See base class for details."""
    np_dtype = np.dtype(self._dtype.as_numpy_dtype)
    # Convert to numpy if possible
    if not isinstance(sample_data, np.ndarray):
      sample_data = np.array(sample_data, dtype=np_dtype)
    # Ensure the shape and dtype match
    if sample_data.dtype != np_dtype:
      raise ValueError('Dtype {} do not match {}'.format(
          sample_data.dtype, np_dtype))
    utils.assert_shape_match(sample_data.shape, self._shape)
    return sample_data

  def decode_sample(self, tfexample_data):
    """See base class for details."""
    # TODO(epot): Should assert the shape here
    return tfexample_data


class OneOf(FeaturesDict):
  """Feature which encodes multiple features, but decodes only one at runtime.

  This avoids having duplicate files for every version of your dataset. You
  can just encode everything on disk in a single dataset, and choose which
  output you want for the tf.data.Dataset at decode time.

  Example:

    features = tfds.features.FeaturesDict({
        'labels': features.OneOf('coco', {
            'coco': tf.string,
            'cifar10': tf.string,
        }),
    })

  At generation time, encode both coco and cifar labels:

    for sample in generate_samples:
      yield self.info.features.encode_sample({
          'labels': {
              'coco': 'person',
              'cifar10': 'airplane',
          },
      })

  At tf.data.Dataset() time, only the label from coco is decoded:

    for sample in tfds.load(...):
      tf_label = sample['labels']  # == 'person'

  """

  def __init__(self, choice, feature_dict):
    """Create the features for the container.

    Args:
      choice (str): The key of the spec to decode.
      feature_dict (dict): Dictionary containing the sub fields. The choice
        should match one of the key.

    Raises:
      ValueError: If the choice is invalid.
    """
    if choice not in feature_dict:
      raise ValueError(
          'Field {} selected not found in the features.'.format(choice))

    super(OneOf, self).__init__(feature_dict)
    self._choice = choice

  def decode_sample(self, tfexample_dict):
    """See base class for details."""
    return decode_single_feature_from_dict(
        feature_k=self._choice,
        feature=self._feature_dict[self._choice],
        tfexample_dict=tfexample_dict,
    )


def to_feature(value):
  """Convert the given value to Feature if necessary."""
  if isinstance(value, FeatureConnector):
    return value
  elif utils.is_dtype(value):  # tf.int32, tf.string,...
    return Tensor(shape=(), dtype=tf.as_dtype(value))
  elif isinstance(value, dict):
    return FeaturesDict(value)
  else:
    raise ValueError('Feature not supported: {}'.format(value))


def decode_single_feature_from_dict(
    feature_k,
    feature,
    tfexample_dict):
  """Decode the given feature from the tfexample_dict.

  Args:
    feature_k (str): Feature key in the tfexample_dict
    feature (FeatureConnector): Connector object to use to decode the field
    tfexample_dict (dict): Dict containing the data to decode.

  Returns:
    decoded_feature: The output of the feature.decode_sample
  """
  # Singleton case
  if not feature.features_keys:
    data_to_decode = tfexample_dict[feature_k]
  # Feature contains sub features
  else:
    # Extract the sub-features from the global feature dict
    data_to_decode = {
        k: tfexample_dict[posixpath.join(feature_k, k)]
        for k in feature.features_keys
    }
  return feature.decode_sample(data_to_decode)


def _assert_keys_match(keys1, keys2):
  """Ensure the two list of keys matches."""
  if set(keys1) != set(keys2):
    raise ValueError('{} {}'.format(list(keys1), list(keys2)))
