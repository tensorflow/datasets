"""Tests for tensorflow_datasets.core.features.skip_encoding_reature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.public_api as tfds


b = functools.partial(np.array, dtype=np.bool)
a = functools.partial(np.array, dtype=np.int64)

f = tfds.features


class SkipEncodingFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    brle_brle_test = test_utils.FeatureExpectation(
        name='brle_brle',
        feature=f.SkipEncodingFeature(f.BrleFeature()),
        dtype=tf.bool,
        shape=(None,),
        tests=[
            test_utils.FeatureExpectationItem(
                value=a([0, 5, 2, 0]),
                expected=b([1, 1, 1, 1, 1, 0, 0]),
                expected_serialized=a([0, 5, 2, 0])
            ),
        ]
    )

    rle_rle_test = test_utils.FeatureExpectation(
        name='rle_rle',
        feature=f.SkipEncodingFeature(f.RleFeature()),
        dtype=tf.int64,
        shape=(None,),
        tests=[
            test_utils.FeatureExpectationItem(
                value=a([1, 5, 0, 2]),
                expected=b([1, 1, 1, 1, 1, 0, 0]),
                expected_serialized=a([1, 5, 0, 2])
            ),
        ])

    return [
        brle_brle_test,
        rle_rle_test,
    ]


if __name__ == '__main__':
  tf.test.main()
