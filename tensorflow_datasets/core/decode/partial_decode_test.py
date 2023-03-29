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

"""Tests for partial_decode."""

import pytest

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import features as features_lib


def _extract_features(feature, expected_feature):
  decoder = decode.PartialDecoding(expected_feature)
  return decoder.extract_features(feature)


def test_extract_features():
  features = features_lib.FeaturesDict({
      'img': features_lib.Image(shape=(256, 256, 3)),
      'img2': features_lib.Image(shape=(256, 256, 3)),
      'metadata': {
          'label': features_lib.ClassLabel(num_classes=4),
          'other': tf.string,
      },
      'sequence': features_lib.Sequence({
          'x': tf.int64,
          'y': tf.int64,
      }),
      'sequence_flat': features_lib.Sequence(tf.int64),
  })

  result = _extract_features(
      feature=features,
      expected_feature={},
  )
  testing.assert_features_equal(result, features_lib.FeaturesDict({}))

  # Feature spec accepted
  result = _extract_features(
      feature=features,
      expected_feature={
          'img': features_lib.Image(shape=(None, None, 3)),
          'metadata': {
              'other': tf.string,
          },
          'sequence': features_lib.Sequence(
              {
                  'x': tf.int64,
              }
          ),
      },
  )
  testing.assert_features_equal(
      result,
      features_lib.FeaturesDict({
          'img': features_lib.Image(shape=(256, 256, 3)),
          'metadata': {
              'other': tf.string,
          },
          'sequence': features_lib.Sequence(
              {
                  'x': tf.int64,
              }
          ),
      }),
  )

  # Failure mode:
  # * Structure not matching
  # * Type not matching
  # * Shape/dtype not matching
  # * Sequence values not matching (e.g. try bad dtype)

  with pytest.raises(ValueError, match="Missing expected feature 'unknown'"):
    _extract_features(
        feature=features,
        expected_feature={
            'sequence': features_lib.Sequence(
                {
                    'unknown': tf.bool,
                }
            )
        },
    )

  with pytest.raises(ValueError, match="Missing expected feature 'non_exista"):
    _extract_features(
        feature=features,
        expected_feature={
            'non_existant': features_lib.Image(shape=(None, None, 3)),
        },
    )

  with pytest.raises(TypeError, match='Expected: Tensor.*. Got: Image'):
    _extract_features(
        feature=features,
        expected_feature={
            'img': features_lib.Tensor(shape=(256, 256, 3), dtype=tf.uint8),
        },
    )

  with pytest.raises(ValueError, match='Expected: Image.*. Got: Image'):
    _extract_features(
        feature=features,
        expected_feature={
            'img': features_lib.Image(shape=(None, None, 1)),
        },
    )

  with pytest.raises(ValueError, match='Expected: Tensor.*. Got: Tensor'):
    _extract_features(
        feature=features,
        expected_feature={
            'sequence_flat': features_lib.Sequence(tf.float32),  # Wrong dtype
        },
    )


def test_extract_features_values():
  features = features_lib.FeaturesDict({
      'img': features_lib.Image(shape=(256, 256, 3)),
      'img2': features_lib.Image(shape=(256, 256, 3)),
      'metadata': {
          'label': features_lib.ClassLabel(num_classes=4),
          'other': tf.string,
      },
      'sequence': features_lib.Sequence({
          'x': tf.int64,
          'y': tf.int64,
      }),
      'sequence_flat': features_lib.Sequence(tf.int64),
  })

  result = _extract_features(
      feature=features,
      expected_feature={
          'img': True,
          'img2': False,
          'unknown_key': False,  # Extra keys are filtered
          'metadata': ['label'],
          'sequence': {'y'},
          'sequence_flat': True,
      },
  )
  testing.assert_features_equal(
      result,
      features_lib.FeaturesDict({
          'img': features_lib.Image(shape=(256, 256, 3)),
          'metadata': {
              'label': features_lib.ClassLabel(num_classes=4),
          },
          'sequence': features_lib.Sequence(
              {
                  'y': tf.int64,
              }
          ),
          'sequence_flat': features_lib.Sequence(tf.int64),
      }),
  )

  result = _extract_features(
      feature=features,
      expected_feature={'metadata', 'sequence'},
  )
  testing.assert_features_equal(
      result,
      features_lib.FeaturesDict({
          'metadata': {
              'label': features_lib.ClassLabel(num_classes=4),
              'other': tf.string,
          },
          'sequence': features_lib.Sequence({
              'x': tf.int64,
              'y': tf.int64,
          }),
      }),
  )

  # Test, mixing Features with non-features.
  result = _extract_features(
      feature=features,
      expected_feature={
          'img': features_lib.Image(),
          'sequence': {
              'x': tf.int64,
              'y': False,
          },
      },
  )
  testing.assert_features_equal(
      result,
      features_lib.FeaturesDict({
          'img': features_lib.Image(shape=(256, 256, 3)),
          'sequence': features_lib.Sequence(
              {
                  'x': tf.int64,
              }
          ),
      }),
  )


def test_partial_decode(dummy_mnist: testing.DummyMnist):
  ds = dummy_mnist.as_dataset(
      split='train',
      decoders=decode.PartialDecoding(
          {
              'image': features_lib.Image(shape=(None, None, 1)),
          }
      ),
  )
  assert ds.element_spec == {
      'image': tf.TensorSpec(shape=(28, 28, 1), dtype=tf.uint8)
  }
  for ex in ds.take(2):
    assert ex['image'].shape == (28, 28, 1)


def test_partial_decode_with_skip_decode(dummy_mnist: testing.DummyMnist):
  ds = dummy_mnist.as_dataset(
      split='train',
      decoders=decode.PartialDecoding(
          {
              'image': features_lib.Image(shape=(None, None, 1)),
          },
          decoders={
              'image': decode.SkipDecoding(),
          },
      ),
  )
  assert ds.element_spec == {'image': tf.TensorSpec(shape=(), dtype=tf.string)}
  for ex in ds.take(2):
    assert ex['image'].dtype == tf.string
