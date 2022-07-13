# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""FeatureDict: Main feature connector container."""

import concurrent.futures
from typing import Dict, List, Union

import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.features import top_level_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json
WORKER_COUNT = 16


class _DictGetCounter(object):
  """Wraps dict.get and counts successful key accesses."""

  def __init__(self, d):
    self.count = 0
    self.wrapped_mapping = d

  def get(self, key: str):
    if self.wrapped_mapping and key in self.wrapped_mapping:
      self.count += 1
      return self.wrapped_mapping[key]
    return None


class FeaturesDict(top_level_feature.TopLevelFeature):
  """Composite `FeatureConnector`; each feature in `dict` has its own connector.

  The encode/decode method of the spec feature will recursively encode/decode
  every sub-connector given on the constructor.
  Other features can inherit from this class and call super() in order to get
  nested container.

  Example:

  For DatasetInfo:

  ```
  features = tfds.features.FeaturesDict({
      'input': tfds.features.Image(),
      'output': tf.int32,
  })
  ```

  At generation time:

  ```
  for image, label in generate_examples:
    yield {
        'input': image,
        'output': label
    }
  ```

  At tf.data.Dataset() time:

  ```
  for example in tfds.load(...):
    tf_input = example['input']
    tf_output = example['output']
  ```

  For nested features, the FeaturesDict will internally flatten the keys for the
  features and the conversion to tf.train.Example. Indeed, the tf.train.Example
  proto do not support nested features while tf.data.Dataset does.
  But internal transformation should be invisible to the user.

  Example:

  ```
  tfds.features.FeaturesDict({
      'input': tf.int32,
      'target': {
          'height': tf.int32,
          'width': tf.int32,
      },
  })
  ```

  Will internally store the data as:

  ```
  {
      'input': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
      'target/height': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
      'target/width': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
  }
  ```

  """

  def __init__(
      self,
      feature_dict: Dict[str, feature_lib.FeatureConnectorArg],
      *,
      doc: feature_lib.DocArg = None,
  ):
    """Initialize the features.

    Args:
      feature_dict (dict): Dictionary containing the feature connectors of a
        example. The keys should correspond to the data dict as returned by
        tf.data.Dataset(). Types (tf.int32,...) and dicts will automatically be
        converted into FeatureConnector.
      doc: Documentation of this feature (e.g. description).

    Raises:
      ValueError: If one of the given features is not recognized
    """
    super(FeaturesDict, self).__init__(doc=doc)
    self._feature_dict = {k: to_feature(v) for k, v in feature_dict.items()}

  # Dict functions.
  # In Python 3, should inherit from collections.abc.Mapping().

  def keys(self):
    return self._feature_dict.keys()

  def items(self):
    return self._feature_dict.items()

  def values(self):
    return self._feature_dict.values()

  def __contains__(self, k):
    return k in self._feature_dict

  def __getitem__(self, key):
    """Return the feature associated with the key."""
    return self._feature_dict[key]

  def __len__(self):
    return len(self._feature_dict)

  def __iter__(self):
    return iter(self._feature_dict)

  # Feature functions

  def __repr__(self):
    """Display the feature dictionary."""
    lines = ['{}({{'.format(type(self).__name__)]
    # Add indentation
    for key, feature in sorted(list(self._feature_dict.items())):
      feature_repr = tensor_feature.get_inner_feature_repr(feature)
      all_sub_lines = '\'{}\': {},'.format(key, feature_repr)
      lines.extend('    ' + l for l in all_sub_lines.split('\n'))
    lines.append('})')
    return '\n'.join(lines)

  def catalog_documentation(
      self) -> List[feature_lib.CatalogFeatureDocumentation]:
    feature_docs = [
        feature_lib.CatalogFeatureDocumentation(
            name='',
            cls_name=type(self).__name__,
            tensor_info=None,
            description=self._doc.desc,
            value_range=self._doc.value_range,
        )
    ]
    for feature_name, feature in sorted(list(self._feature_dict.items())):
      for documentation in feature.catalog_documentation():
        if documentation.name:
          nested_name = f'{feature_name}/{documentation.name}'
        else:
          nested_name = feature_name
        feature_docs.append(documentation.replace(name=nested_name))
    return feature_docs

  @py_utils.memoize()
  def get_tensor_info(self):
    """See base class for details."""
    return {
        feature_key: feature.get_tensor_info()
        for feature_key, feature in self._feature_dict.items()
    }

  @py_utils.memoize()
  def get_serialized_info(self):
    """See base class for details."""
    return {
        feature_key: feature.get_serialized_info()
        for feature_key, feature in self._feature_dict.items()
    }

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.FeaturesDict]) -> 'FeaturesDict':
    if isinstance(value, dict):
      features = {
          k: feature_lib.FeatureConnector.from_json(v)
          for k, v in value.items()
      }
    else:
      features = {
          name: feature_lib.FeatureConnector.from_proto(proto)
          for name, proto in value.features.items()
      }
    return cls(features)

  def to_json_content(self) -> feature_pb2.FeaturesDict:
    return feature_pb2.FeaturesDict(
        features={
            feature_key: feature.to_proto()
            for feature_key, feature in self._feature_dict.items()
        },)

  def encode_example(self, example_dict):
    """See base class for details."""
    example = {}
    for k, (feature, example_value) in utils.zip_dict(self._feature_dict,
                                                      example_dict):
      try:
        example[k] = feature.encode_example(example_value)
      except Exception as e:  # pylint: disable=broad-except
        utils.reraise(
            e, prefix=f'In <{feature.__class__.__name__}> with name "{k}":\n')
    return example

  def _flatten(self, x):
    """See base class for details."""
    if x and not isinstance(x, (dict, FeaturesDict)):
      raise ValueError(
          'Error while flattening dict: FeaturesDict received a non dict item: '
          '{}'.format(x))

    dict_counter = _DictGetCounter(x)
    out = []
    for k, f in sorted(self.items()):
      out.extend(f._flatten(dict_counter.get(k)))  # pylint: disable=protected-access

    if x and dict_counter.count != len(x):
      raise ValueError(
          'Error while flattening dict: Not all dict items have been consumed, '
          'this means that the provided dict structure does not match the '
          '`FeatureDict`. Please check for typos in the key names. '
          'Available keys: {}. Unrecognized keys: {}'.format(
              list(self.keys()), list(set(x.keys()) - set(self.keys()))))
    return out

  def _nest(self, list_x):
    """See base class for details."""
    curr_pos = 0
    out = {}
    for k, f in sorted(self.items()):
      offset = len(f._flatten(None))  # pylint: disable=protected-access
      out[k] = f._nest(list_x[curr_pos:curr_pos + offset])  # pylint: disable=protected-access
      curr_pos += offset
    if curr_pos != len(list_x):
      raise ValueError(
          'Error while nesting: Expected length {} does not match input '
          'length {} of {}'.format(curr_pos, len(list_x), list_x))
    return out

  def save_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Recursively save all child features
    for feature_key, feature in self._feature_dict.items():
      feature_key = feature_key.replace('/', '.')
      if feature_name:
        feature_key = '-'.join((feature_name, feature_key))
      feature.save_metadata(data_dir, feature_name=feature_key)

  def load_metadata(self, data_dir, feature_name=None):
    """See base class for details."""

    # Load all child features asynchronously
    def load_metadata(feature_item):
      feature_key, feature = feature_item
      feature_key = feature_key.replace('/', '.')
      if feature_name:
        feature_key = '-'.join((feature_name, feature_key))
      feature.load_metadata(data_dir, feature_name=feature_key)

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=WORKER_COUNT) as executor:
      executor.map(load_metadata, self._feature_dict.items())


def to_feature(value: feature_lib.FeatureConnectorArg):
  """Convert the given value to Feature if necessary."""
  if isinstance(value, feature_lib.FeatureConnector):
    return value
  elif utils.is_dtype(value):  # tf.int32, tf.string,...
    return tensor_feature.Tensor(shape=(), dtype=tf.as_dtype(value))
  elif isinstance(value, dict):
    return FeaturesDict(value)
  else:
    raise ValueError('Feature not supported: {}'.format(value))
