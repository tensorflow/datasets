"""Tests for tensorflow_datasets.core.features.shaped_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf
from tensorflow_datasets.testing import test_utils
import tensorflow_datasets.public_api as tfds

tf.compat.v1.enable_eager_execution()

f = tfds.features
b = functools.partial(np.array, dtype=np.bool)
af = functools.partial(np.array, dtype=np.float32)


class ShapedFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    static_test = test_utils.FeatureExpectation(
        name='static_shaped',
        feature=f.StaticShapedTensor(
            f.Tensor(shape=(None,), dtype=tf.float32), shape=(None, 2)),
        dtype=tf.float32,
        shape=(None, 2),
        tests=[
            test_utils.FeatureExpectationItem(
                value=af([[2, 3], [4, 5]]),
                expected=af([[2, 3], [4, 5]]),
                expected_serialized=af([2, 3, 4, 5])),
            test_utils.FeatureExpectationItem(
                value=af([[2, 3], [4, 5], [6, 7]]),
                expected=af([[2, 3], [4, 5], [6, 7]]),
                expected_serialized=af([2, 3, 4, 5, 6, 7])),
        ])

    dynamic_test = test_utils.FeatureExpectation(
        name='dynamic_shaped',
        feature=f.DynamicShapedTensor(
            f.Tensor(shape=(None,), dtype=tf.float32), shape=None),
        dtype=tf.float32,
        shape=None,
        tests=[
            test_utils.FeatureExpectationItem(
                value=af([[2, 3], [4, 5]]),
                expected=af([[2, 3], [4, 5]]),
                expected_serialized=dict(
                    flat_values=af([2, 3, 4, 5]), shape=(2, 2))),
            test_utils.FeatureExpectationItem(
                value=af([[2, 3, 4], [4, 5, 6], [7, 8, 9]]),
                expected=af([[2, 3, 4], [4, 5, 6], [7, 8, 9]]),
                expected_serialized=dict(
                    flat_values=af([2, 3, 4, 4, 5, 6, 7, 8, 9]), shape=(3, 3))),
        ]
    )

    static_brle_test = test_utils.FeatureExpectation(
        name='static_brle_test',
        feature=f.StaticShapedTensor(f.BrleFeature(), shape=(None, 4)),
        dtype=tf.bool,
        shape=(None, 4),
        tests=[
            test_utils.FeatureExpectationItem(
                value=b([0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]),
                expected=b([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=np.array([5, 3, 4, 0], dtype=np.int64))
        ]
    )

    static_brle_rle_test = test_utils.FeatureExpectation(
        name='static_brle_rle_test',
        feature=f.SkipEncodingFeature(
            f.StaticShapedTensor(f.BrleFeature(), shape=(None, 4))),
        dtype=tf.bool,
        shape=(None, 4),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np.array([5, 3, 4, 0], dtype=np.int64),
                expected=b([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=np.array([5, 3, 4, 0], dtype=np.int64))
        ]
    )

    dynamic_brle_test = test_utils.FeatureExpectation(
        name='dynamic_brle_test',
        feature=f.DynamicShapedTensor(f.BrleFeature()),
        dtype=tf.bool,
        shape=None,
        tests=[
            test_utils.FeatureExpectationItem(
                value=b([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected=b([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]),
                expected_serialized=dict(
                    shape=(3, 4),
                    flat_values=np.array([5, 3, 4, 0], dtype=np.int64)
                )
            )
        ]
    )

    return [
        static_test,
        dynamic_test,
        static_brle_test,
        static_brle_rle_test,
        dynamic_brle_test,
    ]

  def test_base_shape(self):
    flat = f.Tensor(shape=(None,), dtype=tf.float32)
    for shape in (None, (None, None), (None, None, 3)):
      self.assertTrue(
          isinstance(f.ShapedTensor(flat, shape=shape), f.DynamicShapedTensor))
    for shape in ((None,), (None, 3), (3,), (2, None, 3,), (3, 4, 5)):
      self.assertTrue(
          isinstance(f.ShapedTensor(flat, shape=shape), f.StaticShapedTensor))

if __name__ == '__main__':
  tf.test.main()
