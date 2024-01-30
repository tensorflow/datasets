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

"""Optional feature connector."""

from __future__ import annotations

from typing import Any

from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json


class Optional(feature_lib.FeatureConnector):
  r"""Optional feature connector.

  Warning: This feature is under active development. For now,
  `tfds.features.Optional` can only wrap `tfds.features.Scalar`:

  ```python
  features = tfds.features.FeaturesDict({
      'myfeature': tfds.features.Optional(np.int32),
  })
  ```

  In `_generate_examples`, you can yield `None` instead of the actual feature
  value:

  ```python
  def _generate_examples(self):
    yield {
        'myfeature': None,  # Accept `None` or feature
    }
  ```

  For Grain/NumPy users, `tfds.data_source` will output None values.

  ```python
  ds = tfds.data_source('dataset_with_optional', split='train')
  for element in ds:
    if element is None:
      # ...
    else:
      # ...
  ```

  For tf.data users, None values don't make sense in tensors, so we haven't
  implemented the feature yet. If you're a tf.data user with a use case for
  optional values, we'd like to hear from you.
  """

  def __init__(
      self,
      feature: feature_lib.FeatureConnectorArg,
      *,
      doc: feature_lib.DocArg = None,
  ):
    """Constructor.

    Args:
      feature: The feature to wrap (any TFDS feature is supported).
      doc: Documentation of this feature (e.g. description).
    """
    self._feature = features_dict.to_feature(feature)
    if not isinstance(self._feature, tensor_feature.Tensor):
      raise NotImplementedError(
          'tfds.features.Optional only supports Tensors. Refer to its'
          ' documentation for more information.'
      )
    super().__init__(doc=doc)

  @py_utils.memoize()
  def get_tensor_info(self):
    """See base class for details."""
    return self._feature.get_tensor_info()

  @py_utils.memoize()
  def get_serialized_info(self):
    """See base class for details."""
    return self._feature.get_serialized_info()

  def __getitem__(self, key: str) -> feature_lib.FeatureConnector:
    """Allows to access the underlying features directly."""
    return self._feature[key]

  def __contains__(self, key: str) -> bool:
    return key in self._feature

  def save_metadata(self, *args, **kwargs):
    """See base class for details."""
    self._feature.save_metadata(*args, **kwargs)

  def load_metadata(self, *args, **kwargs):
    """See base class for details."""
    self._feature.load_metadata(*args, **kwargs)

  @classmethod
  def from_json_content(cls, value: feature_pb2.Optional) -> Optional:
    """See base class for details."""
    feature = feature_lib.FeatureConnector.from_proto(value.feature)
    return cls(feature)

  def to_json_content(self) -> feature_pb2.Optional:
    """See base class for details."""
    return feature_pb2.Optional(feature=self._feature.to_proto())

  @property
  def feature(self):
    """The inner feature."""
    return self._feature

  def encode_example(self, example: Any) -> Any:
    """See base class for details."""
    if example is None:
      return None
    else:
      return self._feature.encode_example(example)

  def decode_example(self, example: Any) -> Any:
    """See base class for details."""
    raise NotImplementedError(
        'tfds.features.Optional only supports tfds.data_source.'
    )

  def decode_example_np(
      self, example: Any
  ) -> type_utils.NpArrayOrScalar | None:
    if example is None:
      return None
    else:
      return self._feature.decode_example_np(example)
