from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature


class SkipEncodingFeature(feature.FeatureConnector):
  """FeatureConnector for adapting an existing connector by skipping encoding.

  Useful when you want to use an existing FeatureConnector but the data is
  more easily calculated in it's encoded form.

  The following methods are forwarded to the base connector:
    * get_serialized_info
    * get_tensor_info
    * decode_example
  """

  def __init__(self, base_connector):
    """Wrap the provided `base_connector`. Must be a `FeatureConnector`."""
    if not isinstance(base_connector, feature.FeatureConnector):
      raise TypeError(
          "`base_connector` must be a `FeatureConnector`, got %s"
          % base_connector)
    self._base_connector = base_connector

  def get_serialized_info(self):
    return self._base_connector.get_serialized_info()

  def get_tensor_info(self):
    return self._base_connector.get_tensor_info()

  def decode_example(self, tfexample_data):
    return self._base_connector.decode_example(tfexample_data)

  def encode_example(self, example_data):
    return example_data
