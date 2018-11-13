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

"""Tests for tensorflow_datasets.core.features.feature.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import features as features_lib


class AnInputConnector(features_lib.FeaturesDict):
  """Simple FeatureConnector implementing the based methods used for test."""

  def __init__(self):
    super(AnInputConnector, self).__init__({
        'a': tf.int32,
        'b': tf.int32,
    })

  def encode_sample(self, sample_data):
    # Encode take the input data and wrap in in a dict
    return super(AnInputConnector, self).encode_sample({
        'a': sample_data + 1,
        'b': sample_data * 10
    })

  def decode_sample(self, tfexample_dict):
    # Decode take the saved dict and merge the two values
    tfexample_dict = super(AnInputConnector, self).decode_sample(
        tfexample_dict)
    return tfexample_dict['a'] + tfexample_dict['b']


class AnOutputConnector(features_lib.FeatureConnector):
  """Simple FeatureConnector implementing the based methods used for test."""

  def get_serialized_features(self):
    return tf.FixedLenFeature(shape=(), dtype=tf.float32)

  def encode_sample(self, sample_data):
    return sample_data * 10.0

  def decode_sample(self, tfexample_data):
    return tfexample_data / 10.0


class FeatureTest(tf.test.TestCase):

  def setUp(self):
    # Create the spec dict used for all tests
    self._features = features_lib.FeaturesDict({
        'input': AnInputConnector(),
        'output': AnOutputConnector(),
        'img': {
            'size': {
                'height': tf.int32,
                'width': tf.int32,
            },
            'metadata/path': tf.string,
        }
    })

  def test_features(self):
    # Specs of the tf example file
    self.assertEqual(self._features.get_serialized_features(), {
        'input/a': tf.FixedLenFeature(shape=(), dtype=tf.int32),
        'input/b': tf.FixedLenFeature(shape=(), dtype=tf.int32),
        'output': tf.FixedLenFeature(shape=(), dtype=tf.float32),
        'img/size/height': tf.FixedLenFeature(shape=(), dtype=tf.int32),
        'img/size/width': tf.FixedLenFeature(shape=(), dtype=tf.int32),
        'img/metadata/path': tf.FixedLenFeature(shape=(), dtype=tf.string),
    })

  def test_encode(self):

    # During encoding, all FeatureConnector.encode_sample() are applied
    encoded_sample = self._features.encode_sample({
        'input': 1,
        'output': -1,
        'img': {
            'size': {
                'height': 256,
                'width': 128,
            },
            'metadata/path': 'path/to/xyz.jpg',
        }
    })
    self.assertEqual(encoded_sample, {
        'input/a': 2,  # 1 + 1
        'input/b': 10,  # 1 * 10
        'output': -10.0,  # -1 * 10.0
        'img/size/height': 256,
        'img/size/width': 128,
        'img/metadata/path': 'path/to/xyz.jpg',
    })

  def test_decode(self):

    # Decoding call all FeatureConnector.decode_sample()
    decoded_sample = self._features.decode_sample({
        'input/a': 2,  # 1 + 1
        'input/b': 10,  # 1 * 10
        'output': -10.0,  # -1 * 10.0
        'img/size/height': 256,
        'img/size/width': 128,
        'img/metadata/path': 'path/to/xyz.jpg',
    })
    self.assertEqual(decoded_sample, {
        'input': 12,  # 2 + 10
        'output': -1,
        'img': {
            'size': {
                'height': 256,
                'width': 128,
            },
            'metadata/path': 'path/to/xyz.jpg',
        },
    })


class OneOfTest(tf.test.TestCase):

  def setUp(self):
    # Create the spec dict used for all tests
    self._features = features_lib.FeaturesDict({
        'input': features_lib.OneOf(
            choice='choice2',
            feature_dict={
                'choice1': tf.float32,
                'choice2': AnInputConnector(),
            },
        ),
    })

  def test_features(self):
    # All choices are present in the spec
    self.assertEqual(self._features.get_serialized_features(), {
        'input/choice1': tf.FixedLenFeature(shape=(), dtype=tf.float32),
        'input/choice2/a': tf.FixedLenFeature(shape=(), dtype=tf.int32),
        'input/choice2/b': tf.FixedLenFeature(shape=(), dtype=tf.int32),
    })

  def test_encode(self):
    # All choices are encoded
    encoded_sample = self._features.encode_sample({
        'input': {
            'choice1': 0.0,
            'choice2': 1,
        },
    })
    self.assertEqual(encoded_sample, {
        'input/choice1': 0.0,
        'input/choice2/a': 2,  # 1 + 1
        'input/choice2/b': 10,  # 1 * 10
    })

  def test_decode(self):
    # Only choice 2 is decoded.
    decoded_sample = self._features.decode_sample({
        'input/choice1': 0.0,
        'input/choice2/a': 2,  # 1 + 1
        'input/choice2/b': 10,  # 1 * 10
    })
    self.assertEqual(decoded_sample, {
        'input': 12,  # 2 + 10
    })


class FeatureTensorTest(tf.test.TestCase):

  def test_shapes_static(self):
    features = features_lib.FeaturesDict({
        'input': features_lib.Tensor(shape=(2, 3), dtype=tf.float32),
    })

    # Numpy array
    np_input = np.random.rand(2, 3).astype(np.float32)
    tf_output = _encode_decode(features, {
        'input': np_input,
    })
    self.assertAllEqual(tf_output['input'], np_input)

    # Python array
    array_input = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    tf_output = _encode_decode(features, {
        'input': array_input,
    })
    self.assertAllEqual(tf_output['input'], array_input)

    # Invalid type
    with self.assertRaisesWithPredicateMatch(ValueError, 'int64 do not match'):
      _encode_decode(features, {
          'input': np.random.randint(256, size=(2, 3)),
      })

    # Invalid shape
    with self.assertRaisesWithPredicateMatch(ValueError, 'are incompatible'):
      _encode_decode(features, {
          'input': np.random.rand(2, 4).astype(np.float32),
      })

  def test_shapes_dynamic(self):
    features = features_lib.FeaturesDict({
        'input': features_lib.Tensor(shape=(None, None, 1), dtype=tf.int32),
    })

    # Numpy array
    np_input = np.random.randint(256, size=(2, 3, 1), dtype=np.int32)
    tf_output = _encode_decode(features, {
        'input': np_input,
    })
    self.assertAllEqual(tf_output['input'], np_input)

    # Invalid shape
    with self.assertRaisesWithPredicateMatch(ValueError, 'are incompatible'):
      _encode_decode(features, {
          'input': np.random.randint(256, size=(2, 3, 2), dtype=np.int32),
      })


def _encode_decode(features, sample):
  encoded_sample = features.encode_sample(sample)
  return features.decode_sample(encoded_sample)


if __name__ == '__main__':
  tf.test.main()
