"""Tests for tensorflow_datasets.core.features.shaped_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.testing import test_main
import tensorflow_datasets.public_api as tfds

tf.compat.v1.enable_eager_execution()

features = tfds.features
bools = functools.partial(np.array, dtype=np.bool)
floats = functools.partial(np.array, dtype=np.float32)


class ShapedFeatureTest(test_utils.FeatureExpectationsTestCase):

  def test_static_shape(self):
    self.assertFeature(
        feature=features.StaticShapedTensor(
            features.Tensor(shape=(None,), dtype=tf.float32), shape=(None, 2)),
        dtype=tf.float32,
        shape=(None, 2),
        tests=[
            test_utils.FeatureExpectationItem(
                value=floats([[2, 3], [4, 5]]),
                expected=floats([[2, 3], [4, 5]]),
                expected_serialized=floats([2, 3, 4, 5])),
            test_utils.FeatureExpectationItem(
                value=floats([[2, 3], [4, 5], [6, 7]]),
                expected=floats([[2, 3], [4, 5], [6, 7]]),
                expected_serialized=floats([2, 3, 4, 5, 6, 7])),
        ])

  def test_dynamic_shape(self):
    base = features.Tensor(shape=(None,), dtype=tf.float32)
    reshaped = features.DynamicShapedTensor(base, shape=None)
    # return
    self.assertFeature(
        feature=reshaped,
        dtype=tf.float32,
        shape=None,
        tests=[
            test_utils.FeatureExpectationItem(
                value=floats([[2, 3], [4, 5]]),
                expected=floats([[2, 3], [4, 5]]),
                expected_serialized=dict(
                    base_feature=floats([2, 3, 4, 5]), shape=(2, 2))),
            test_utils.FeatureExpectationItem(
                value=floats([[2, 3, 4], [4, 5, 6], [7, 8, 9]]),
                expected=floats([[2, 3, 4], [4, 5, 6], [7, 8, 9]]),
                expected_serialized=dict(
                    base_feature=floats(
                        [2, 3, 4, 4, 5, 6, 7, 8, 9]),
                    shape=(3, 3))),
        ]
    )

  def test_static_brle_test(self):
    self.assertFeature(
        feature=features.StaticShapedTensor(
            features.BinaryRunLengthEncodedFeature(), shape=(None, 4)),
        dtype=tf.bool,
        shape=(None, 4),
        tests=[
            test_utils.FeatureExpectationItem(
                value=bools([0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]),
                expected=bools([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=np.array([5, 3, 4, 0], dtype=np.int64))
        ]
    )

  def test_static_brle_rle_test(self):
    self.assertFeature(
        feature=features.StaticShapedTensor(
            features.BinaryRunLengthEncodedFeature(), shape=(None, 4)),
        dtype=tf.bool,
        shape=(None, 4),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np.array([5, 3, 4, 0], dtype=np.int64),
                expected=bools([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=np.array([5, 3, 4, 0], dtype=np.int64))
        ]
    )

  def test_dynamic_brle_test(self):
    self.assertFeature(
        feature=features.DynamicShapedTensor(features.BinaryRunLengthEncodedFeature()),
        dtype=tf.bool,
        shape=None,
        tests=[
            test_utils.FeatureExpectationItem(
                value=bools([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected=bools([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=dict(
                    shape=(3, 4),
                    base_feature=np.array([5, 3, 4, 0], dtype=np.int64)
                )
            )
        ]
    )

  def test_base_shape(self):
    base = features.Tensor(shape=(None,), dtype=tf.float32)
    for shape in (None, (None, None), (None, None, 3)):
      self.assertTrue(isinstance(
          features.ShapedTensor(base, shape=shape),
          features.DynamicShapedTensor))
    for shape in ((None,), (None, 3), (2, None, 3,)):
      self.assertTrue(isinstance(
          features.ShapedTensor(base, shape=shape),
          features.StaticShapedTensor))

if __name__ == '__main__':
  test_main()
