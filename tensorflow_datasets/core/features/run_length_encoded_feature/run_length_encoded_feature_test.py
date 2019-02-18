"""Tests for tensorflow_datasets.core.features.run_length_encoded_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import tensorflow as tf
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.testing import test_main
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import tf_impl
from tensorflow_datasets.core import tf_compat
tf.compat.v1.enable_eager_execution()

bools = functools.partial(np.array, dtype=np.bool)
ints = functools.partial(np.array, dtype=np.int64)

features = tfds.features

if tf_compat.get_tf_version() >= tf_impl.REQUIRED_TF_VERSION:
  class RunLengthEncodedFeatureTest(test_utils.FeatureExpectationsTestCase):

    def test_brle(self):
      brle_dense_and_encodings = (
          (bools([0, 0, 0, 1, 1, 0, 0, 0, 1, 1]), ints([3, 2, 3, 2])),
          (bools([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]), ints([3, 2, 3, 1, 1, 0])),
      )
      brle_items = []
      for dense, encoding in brle_dense_and_encodings:
        dense_item = test_utils.FeatureExpectationItem(
            value=dense,
            expected=dense,
            expected_serialized=encoding,
        )
        encoding_item = test_utils.FeatureExpectationItem(
            value=encoding,
            expected=dense,
            expected_serialized=encoding,
        )
        brle_items.extend((dense_item, encoding_item))

      self.assertFeature(
          feature=features.BinaryRunLengthEncodedFeature(),
          dtype=tf.bool,
          shape=(None,),
          tests=brle_items
        )
      self.assertFeature(
          feature=features.BinaryRunLengthEncodedFeature(size=10),
          dtype=tf.bool,
          shape=(10,),
          tests=brle_items
      )

    def test_rle(self):
      rle_items = [
          test_utils.FeatureExpectationItem(
            value=ints([0, 0, 0, 2, 2, 5, 5, 5, 5, 3]),
            expected=ints([0, 0, 0, 2, 2, 5, 5, 5, 5, 3]),
            expected_serialized=ints([0, 3, 2, 2, 5, 4, 3, 1])
        ),
      ]

      self.assertFeature(
          feature=features.RunLengthEncodedFeature(),
          dtype=tf.int64,
          shape=(None,),
          tests=rle_items)

      self.assertFeature(
          feature=features.RunLengthEncodedFeature(10),
          dtype=tf.int64,
          shape=(10,),
          tests=rle_items)


if __name__ == '__main__':
  test_main()
