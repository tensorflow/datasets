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
from tensorflow_datasets.core import tf_compat
tf.compat.v1.enable_eager_execution()

bools = functools.partial(np.array, dtype=np.bool)
ints = functools.partial(np.array, dtype=np.int64)

features = tfds.features


class ShapedTensorTest(test_utils.FeatureExpectationsTestCase):

  def test_shape_static(self):

    np_input = np.random.rand(2, 3).astype(np.float32)
    array_input = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    self.assertFeature(
        feature=features.ShapedTensor(shape=(2, 3), dtype=tf.float32),
        dtype=tf.float32,
        shape=(2, 3),
        tests=[
            # Np array
            test_utils.FeatureExpectationItem(
                value=np_input,
                expected=np_input,
            ),
            # Python array
            test_utils.FeatureExpectationItem(
                value=array_input,
                expected=array_input,
            ),
            # Invalid dtype
            test_utils.FeatureExpectationItem(
                value=np.random.randint(256, size=(2, 3)),
                raise_cls=ValueError,
                raise_msg='int64 do not match',
            ),
            # Invalid shape
            test_utils.FeatureExpectationItem(
                value=np.random.rand(2, 4).astype(np.float32),
                raise_cls=ValueError,
                raise_msg='is incompatible',
            ),
        ],
    )

  def test_shape_dynamic(self):

    np_input_dynamic_1 = np.random.randint(256, size=(2, 3, 2), dtype=np.int32)
    np_input_dynamic_2 = np.random.randint(256, size=(5, 3, 2), dtype=np.int32)

    self.assertFeature(
        feature=features.ShapedTensor(shape=(None, 3, 2), dtype=tf.int32),
        dtype=tf.int32,
        shape=(None, 3, 2),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np_input_dynamic_1,
                expected=np_input_dynamic_1,
                expected_serialized=np_input_dynamic_1.flatten()
            ),
            test_utils.FeatureExpectationItem(
                value=np_input_dynamic_2,
                expected=np_input_dynamic_2,
                expected_serialized=np_input_dynamic_2.flatten()
            ),
            # Invalid shape
            test_utils.FeatureExpectationItem(
                value=
                np.random.randint(256, size=(2, 3, 1), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='is incompatible',
            ),
        ]
    )

    self.assertFeature(
        feature=features.ShapedTensor(shape=(None, None, 2), dtype=tf.int32),
        dtype=tf.int32,
        shape=(None, None, 2),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np_input_dynamic_1,
                expected=np_input_dynamic_1,
                expected_serialized=dict(
                  shape=np_input_dynamic_1.shape,
                  flat_values=np_input_dynamic_1.flatten()
                )
            ),
            test_utils.FeatureExpectationItem(
                value=np_input_dynamic_2,
                expected=np_input_dynamic_2,
                expected_serialized=dict(
                  shape=np_input_dynamic_2.shape,
                  flat_values=np_input_dynamic_2.flatten()
                )
            ),
            # Invalid shape
            test_utils.FeatureExpectationItem(
                value=
                np.random.randint(256, size=(2, 3, 1), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='is incompatible',
            ),
        ]
    )



  def test_bool_flat(self):

    self.assertFeature(
        feature=features.ShapedTensor(shape=(), dtype=tf.bool),
        dtype=tf.bool,
        shape=(),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np.array(True),
                expected=True,
            ),
            test_utils.FeatureExpectationItem(
                value=np.array(False),
                expected=False,
            ),
            test_utils.FeatureExpectationItem(
                value=True,
                expected=True,
            ),
            test_utils.FeatureExpectationItem(
                value=False,
                expected=False,
            ),
        ]
    )

  def test_bool_array(self):

    self.assertFeature(
        feature=features.ShapedTensor(shape=(3,), dtype=tf.bool),
        dtype=tf.bool,
        shape=(3,),
        tests=[
            test_utils.FeatureExpectationItem(
                value=np.array([True, True, False]),
                expected=[True, True, False],
            ),
            test_utils.FeatureExpectationItem(
                value=[True, False, True],
                expected=[True, False, True],
            ),
        ]
    )


class RunLengthEncodedFeatureTest(test_utils.FeatureExpectationsTestCase):

  def test_flat_brle(self):
    shape = (10,)
    brle_dense_and_encodings = (
        (bools([0, 0, 0, 1, 1, 0, 0, 0, 1, 1]), ints([3, 2, 3, 2])),
        (bools([0, 0, 0, 1, 1, 0, 0, 0, 1, 0]), ints([3, 2, 3, 1, 1])),
    )
    brle_items = []
    for dense, encoding in brle_dense_and_encodings:
      dense_item = test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=encoding,
      )
      encoding_item = test_utils.FeatureExpectationItem(
          value=(shape, encoding),
          expected=dense,
          expected_serialized=encoding,
      )
      brle_items.extend((
        dense_item,
        encoding_item,
      ))

    self.assertFeature(
        feature=features.BinaryRunLengthEncodedFeature((None,)),
        dtype=tf.bool,
        shape=(None,),
        tests=brle_items
      )
    self.assertFeature(
        feature=features.BinaryRunLengthEncodedFeature(shape=shape),
        dtype=tf.bool,
        shape=shape,
        tests=brle_items
    )

  def test_shaped_brle(self):
    dense, enc = bools([0, 0, 0, 1, 1, 0, 0, 0, 1, 1]), ints([3, 2, 3, 2])
    shape = np.array((5, 2), dtype=np.int64)
    dense = np.reshape(dense, shape)
    tests = [
      test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=dict(
            flat_values=enc, shape=shape
          ))
        ]

    self.assertFeature(
        feature=features.BinaryRunLengthEncodedFeature((None, None)),
        dtype=tf.bool,
        shape=(None, None),
        tests=tests)

    self.assertFeature(
        feature=features.BinaryRunLengthEncodedFeature(None),
        dtype=tf.bool,
        shape=None,
        tests=tests)

    tests = [
      test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=enc)
        ]
    for shape in ((None, 2), (5, None)):
      self.assertFeature(
          feature=features.BinaryRunLengthEncodedFeature(shape),
          dtype=tf.bool,
          shape=shape,
          tests=tests)

  def test_flat_rle(self):
    dense = ints([0, 0, 0, 2, 2, 5, 5, 5, 5, 3])
    enc = ints([0, 3, 2, 2, 5, 4, 3, 1])
    rle_items = [
        test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=enc
      ),
    ]

    self.assertFeature(
        feature=features.RunLengthEncodedFeature((None,)),
        dtype=tf.int64,
        shape=(None,),
        tests=rle_items)

    self.assertFeature(
        feature=features.RunLengthEncodedFeature((10,)),
        dtype=tf.int64,
        shape=(10,),
        tests=rle_items)

  def test_shaped_rle(self):
    shape = (5, 2)
    dense = ints([0, 0, 0, 2, 2, 5, 5, 5, 5, 3])
    dense = np.reshape(dense, shape)
    enc = ints([0, 3, 2, 2, 5, 4, 3, 1])
    shaped_enc = dict(flat_values=enc, shape=shape)

    rle_items = [
        test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=shaped_enc
      ),
    ]

    self.assertFeature(
        feature=features.RunLengthEncodedFeature(None),
        dtype=tf.int64,
        shape=None,
        tests=rle_items)

    self.assertFeature(
        feature=features.RunLengthEncodedFeature((None, None)),
        dtype=tf.int64,
        shape=(None, None),
        tests=rle_items)

    rle_items = [
        test_utils.FeatureExpectationItem(
          value=dense,
          expected=dense,
          expected_serialized=enc
      ),
    ]

    for shape in ((None, 2), (5, None)):
      self.assertFeature(
        feature=features.RunLengthEncodedFeature(shape),
        dtype=tf.int64,
        shape=shape,
        tests=rle_items)

if __name__ == '__main__':
  test_main()
