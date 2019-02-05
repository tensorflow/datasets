"""Tests for tensorflow_datasets.core.features.rle_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.public_api as tfds
tf.compat.v1.enable_eager_execution()

b = functools.partial(np.array, dtype=np.bool)
a = functools.partial(np.array, dtype=np.int64)
z = functools.partial(np.zeros, dtype=np.bool)
o = functools.partial(np.ones, dtype=np.bool)

f = tfds.features


class BrleFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    brle_dense_test = test_utils.FeatureExpectation(
        name='brle_dense',
        feature=f.BrleFeature(),
        dtype=tf.bool,
        shape=(None,),
        tests=[
            test_utils.FeatureExpectationItem(
                value=b([0, 0, 0, 1, 1, 0, 0, 0, 1]),
                expected=b([0, 0, 0, 1, 1, 0, 0, 0, 1]),
                expected_serialized=a([3, 2, 3, 1])
            ),
            test_utils.FeatureExpectationItem(
                value=b([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
                expected=b([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
                expected_serialized=a([3, 2, 3, 1, 1, 0])
            ),
            test_utils.FeatureExpectationItem(
                value=b([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
                expected=b([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
                expected_serialized=a([3, 2, 3, 1, 1, 0])
            )
        ])

    rle_dense_test = test_utils.FeatureExpectation(
        name='rle_dense',
        feature=f.RleFeature(),
        dtype=tf.int64,
        shape=(None,),
        tests=[
            test_utils.FeatureExpectationItem(
                value=a([0, 0, 0, 2, 2, 5, 5, 5, 5, 3]),
                expected=a([0, 0, 0, 2, 2, 5, 5, 5, 5, 3]),
                expected_serialized=a([0, 3, 2, 2, 5, 4, 3, 1])
            ),
        ])

    return [
        brle_dense_test,
        rle_dense_test,
    ]


if __name__ == '__main__':
  tf.test.main()
