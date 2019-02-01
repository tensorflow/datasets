"""(Binary) run length encoded ((B)RLE) feature connectors.

Provides `RleFeature` and `BrleFeature` for encoding each variant.

See `tensorflow_datasets/core/features/rle_feature/README.md` for for details.
"""
import abc
import numpy as np
import six
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.features.rle_feature.rle import np_impl
from tensorflow_datasets.core.features.rle_feature.rle import tf_impl


class RleFeatureBase(feature.FeatureConnector):
  """Abstract Base Class `FeatureConnector` class for (B)RLE 1D tensors.

  See `RleFeature` and `BrleFeature` for implementations.
  """
  _encoded_dtype = tf.int64

  def get_serialized_info(self):
    return feature.to_serialized_field(
        tfds.features.TensorInfo(shape=(None,), dtype=self._encoded_dtype))


class RleFeature(RleFeatureBase):
  """`FeatureConnector` for run length encoded 1D tensors."""
  def get_tensor_info(self):
    return tfds.features.TensorInfo(shape=(None,), dtype=self._encoded_dtype)

  def decode_example(self, tfexample_data):
    return tf_impl.rle_to_dense(tfexample_data)

  def encode_example(self, example_data):
    return np_impl.dense_to_rle(
      example_data, dtype=self._encoded_dtype.as_numpy_dtype)


class BrleFeature(RleFeatureBase):
  """`FeatureConnector` for brinary run length encoded 1D tensors."""
  def get_tensor_info(self):
    return tfds.features.TensorInfo(shape=(None,), dtype=tf.bool)

  def decode_example(self, tfexample_data):
    return tf_impl.brle_to_dense(tfexample_data)

  def encode_example(self, example_data):
    return np_impl.dense_to_brle(
      example_data, dtype=self._encoded_dtype.as_numpy_dtype)
