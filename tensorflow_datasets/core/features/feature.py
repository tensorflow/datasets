# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Feature connector."""

import abc
import collections
import functools
import html
import importlib
import json
import os
from typing import Dict, List, Type, TypeVar, Union

import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils

from google.protobuf import descriptor
from google.protobuf import json_format
from google.protobuf import message

Json = type_utils.Json
Shape = type_utils.Shape

T = TypeVar('T', bound='FeatureConnector')

# FeatureConnector-like input accepted by `Sequence()`, `Optional()`,...
FeatureConnectorArg = Union['FeatureConnector',
                            Dict[str, 'FeatureConnectorArg'], tf.dtypes.DType]  # pytype: disable=not-supported-yet


class TensorInfo(object):
  """Structure containing info on the `tf.Tensor` shape/dtype."""

  __slots__ = [
      'shape', 'dtype', 'default_value', 'sequence_rank', 'dataset_lvl'
  ]

  def __init__(self,
               shape,
               dtype,
               default_value=None,
               sequence_rank=None,
               dataset_lvl=0):
    """Constructor.

    Args:
      shape: `tuple[int]`, shape of the tensor
      dtype: Tensor dtype
      default_value: Used for retrocompatibility with previous files if a new
        field is added to provide a default value when reading the file.
      sequence_rank: `int`, Number of `tfds.features.Sequence` dimension.
      dataset_lvl: `int`, if >0, nesting level of a `tfds.features.Dataset`.
    """
    self.shape = shape
    self.dtype = dtype
    self.default_value = default_value
    self.sequence_rank = sequence_rank or 0
    self.dataset_lvl = dataset_lvl

  @classmethod
  def copy_from(cls, tensor_info):
    """Copy constructor."""
    return cls(
        shape=tensor_info.shape,
        dtype=tensor_info.dtype,
        default_value=tensor_info.default_value,
        sequence_rank=tensor_info.sequence_rank,
        dataset_lvl=tensor_info.dataset_lvl,
    )

  def __eq__(self, other):
    """Equality."""
    return (self.shape == other.shape and self.dtype == other.dtype and
            self.default_value == other.default_value)

  def __repr__(self):
    return '{}(shape={}, dtype={})'.format(
        type(self).__name__,
        self.shape,
        repr(self.dtype),
    )


@six.add_metaclass(abc.ABCMeta)
class FeatureConnector(object):
  """Abstract base class for feature types.

  This class provides an interface between the way the information is stored
  on disk, and the way it is presented to the user.

  Here is a diagram on how FeatureConnector methods fit into the data
  generation/reading:

  ```
  generator => encode_example() => tf_example => decode_example() => data dict
  ```

  The connector can either get raw or dictionary values as input, depending on
  the connector type.

  """

  # Keep track of all sub-classes.
  _registered_features: Dict[str, Type['FeatureConnector']] = {}

  # FeatureConnector use the module name to reconstruct/reload the features in
  # `features = FeatureConnector.from_config('features.json')`
  # For backward compatibility, after renaming/moving/ `my_feature.py` to a new
  # location, it is possible to specify the previous `module.MyFeature` names.
  ALIASES: List[str] = []

  def __init_subclass__(cls):
    """Registers subclasses features."""
    cls._registered_features[f'{cls.__module__}.{cls.__name__}'] = cls
    # Also register the aliases. Note: We use __dict__ to make sure the alias
    # is only registered for the class. Not it's child.
    for module_alias in cls.__dict__.get('ALIASES', []):
      cls._registered_features[module_alias] = cls

  @abc.abstractmethod
  def get_tensor_info(self):
    """Return the tf.Tensor dtype/shape of the feature.

    This returns the tensor dtype/shape, as returned by .as_dataset by the
    `tf.data.Dataset` object.

    Ex:

    ```
    return {
        'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8),
        'height': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
        'width': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
    }
    ```

    FeatureConnector which are not containers should return the feature proto
    directly:

    ```
    return tfds.features.TensorInfo(shape=(256, 256), dtype=tf.uint8)
    ```

    Returns:
      tensor_info: Either a dict of `tfds.features.TensorInfo` object, or a
        `tfds.features.TensorInfo`

    """
    raise NotImplementedError

  @property
  def shape(self):
    """Return the shape (or dict of shape) of this FeatureConnector."""
    return tf.nest.map_structure(lambda t: t.shape, self.get_tensor_info())

  @property
  def dtype(self):
    """Return the dtype (or dict of dtype) of this FeatureConnector."""
    return tf.nest.map_structure(lambda t: t.dtype, self.get_tensor_info())

  @classmethod
  def cls_from_name(cls, python_class_name: str) -> Type['FeatureConnector']:
    """Returns the feature class for the given Python class."""
    err_msg = f'Unrecognized FeatureConnector type: {python_class_name}.'

    # Dynamically import custom feature-connectors
    if python_class_name not in cls._registered_features:
      # Split `my_project.xyz.MyFeature` -> (`my_project.xyz`, `MyFeature`)
      if '.' not in python_class_name:
        raise ValueError(
            f'Python class name must contain a dot, got: "{python_class_name}"')
      module_name, _ = python_class_name.rsplit('.', maxsplit=1)  # pytype: disable=attribute-error
      try:
        # Import to register the FeatureConnector
        importlib.import_module(module_name)
      except ImportError:
        raise ValueError(
            f'{err_msg}\nCould not import {module_name}. You might have to '
            'install additional dependencies.')

    feature_class = cls._registered_features.get(python_class_name)
    if feature_class is None:
      raise ValueError(f'{err_msg}\n'
                       f'Supported: {list(cls._registered_features)}')
    return feature_class

  @property
  def _fully_qualified_class_name(self):
    return f'{type(self).__module__}.{type(self).__name__}'

  @classmethod
  def from_json(cls, value: Json) -> 'FeatureConnector':
    """FeatureConnector factory.

    This function should be called from the `tfds.features.FeatureConnector`
    base class. Subclass should implement the `from_json_content`.

    Example:

    ```py
    feature = tfds.features.FeatureConnector.from_json(
        {'type': 'Image', 'content': {'shape': [32, 32, 3], 'dtype': 'uint8'}}
    )
    assert isinstance(feature, tfds.features.Image)
    ```

    Args:
      value: `dict(type=, content=)` containing the feature to restore. Match
        dict returned by `to_json`.

    Returns:
      The reconstructed FeatureConnector.
    """
    class_name = value['type']  # my_project.xyz.MyFeature
    content = value['content']
    feature_cls = cls.cls_from_name(class_name)
    proto_cls_name = value.get('proto_cls')
    if proto_cls_name:  # The content is a proto, need to reconstruct it
      proto_cls = _name2proto_cls(proto_cls_name)
      content = json_format.Parse(content, proto_cls())
    return feature_cls.from_json_content(content)

  def to_json(self) -> Json:
    # pylint: disable=line-too-long
    """Exports the FeatureConnector to Json.

    Each feature is serialized as a `dict(type=..., content=...)`.

    * `type`: The cannonical name of the feature (`module.FeatureName`).
    * `content`: is specific to each feature connector and defined in
      `to_json_content`. Can contain nested sub-features (like for
      `tfds.features.FeaturesDict` and `tfds.features.Sequence`).

    For example:

    ```python
    tfds.features.FeaturesDict({
        'input': tfds.features.Image(),
        'target': tfds.features.ClassLabel(num_classes=10),
    })
    ```

    Is serialized as:

    ```json
    {
        "type": "tensorflow_datasets.core.features.features_dict.FeaturesDict",
        "content": {
            "input": {
                "type": "tensorflow_datasets.core.features.image_feature.Image",
                "content": {
                    "shape": [null, null, 3],
                    "dtype": "uint8",
                    "encoding_format": "png"
                }
            },
            "target": {
                "type":
                "tensorflow_datasets.core.features.class_label_feature.ClassLabel",
                "content": {
                  "num_classes": 10
                }
            }
        }
    }
    ```

    Returns:
      A `dict(type=, content=)`. Will be forwarded to `from_json` when
      reconstructing the feature.
    """
    # pylint: enable=line-too-long
    content = self.to_json_content()
    if isinstance(content, message.Message):  # Content is proto
      # e.g. `tensorflow_datasets.JsonFeature`
      proto_cls_name = type(content).DESCRIPTOR.full_name
      content = json_format.MessageToJson(content)
    elif isinstance(content, dict):  # Content is json
      proto_cls_name = ''
    else:
      raise TypeError(f'Unexpected feature connector value: {content}')
    return {
        'type': self._fully_qualified_class_name,
        'content': content,
        'proto_cls': proto_cls_name,
    }

  @classmethod
  def from_json_content(
      cls: Type[T],
      value: Union[Json, message.Message],
  ) -> T:
    """FeatureConnector factory (to overwrite).

    Subclasses should overwrite this method. This method is used when
    importing the feature connector from the config.

    This function should not be called directly. `FeatureConnector.from_json`
    should be called instead.

    See existing FeatureConnectors for implementation examples.

    Args:
      value: FeatureConnector information represented as either Json or a
        Feature proto. The content must match what is returned by
        `to_json_content`.

    Returns:
      The reconstructed FeatureConnector.
    """
    if not isinstance(value, dict):
      raise TypeError(f'Unexpected feature connector value: {value!r}')
    return cls(**value)  # pytype: disable=not-instantiable

  def to_json_content(self) -> Union[Json, message.Message]:
    """FeatureConnector factory (to overwrite).

    This function should be overwritten by the subclass to allow re-importing
    the feature connector from the config. See existing FeatureConnector for
    example of implementation.

    Returns:
      The FeatureConnector metadata in either a dict, or a Feature proto. This
      output is used in `from_json_content` when reconstructing the feature.
    """
    return {}

  def to_proto(self) -> feature_pb2.Feature:
    """Exports the FeatureConnector to the Feature proto.

    For features that have a specific schema defined in a proto, this
    function needs to be overriden. If there's no specific proto schema,
    then the feature will be represented using JSON.

    Returns:
      The feature proto describing this feature.
    """
    content = self.to_json_content()
    # If the feature metadata is represented in JSON, then wrap the JSON in the
    # Feature proto.
    if isinstance(content, dict):
      content = feature_pb2.JsonFeature(json=json.dumps(content))
    if not isinstance(content, message.Message):
      raise TypeError(
          f'to_json_content should return json or proto. Not: {content!r}')
    # Automatically compute the oneof field name:
    # e.g. {'json_feature': feature_pb2.JsonFeature()}
    oneof_kwarg = {_proto2oneof_field_name(content): content}
    return feature_pb2.Feature(
        python_class_name=self._fully_qualified_class_name,
        **oneof_kwarg,
    )

  @classmethod
  def from_proto(cls, feature: feature_pb2.Feature) -> T:
    feature_cls = cls.cls_from_name(feature.python_class_name)
    # Extract which feature is set (e.g. `json_feature`)
    feature_field_name = feature.WhichOneof('content')
    feature_content = getattr(feature, feature_field_name)
    # Legacy mode, json content is restored as dict
    if isinstance(feature_content, feature_pb2.JsonFeature):
      feature_content = json.loads(feature_content.json)
    return feature_cls.from_json_content(feature_content)

  def save_config(self, root_dir: str) -> None:
    """Exports the `FeatureConnector` to a file.

    Args:
      root_dir: `path/to/dir` containing the `features.json`
    """
    with tf.io.gfile.GFile(make_config_path(root_dir), 'w') as f:
      f.write(json.dumps(self.to_json(), indent=4))
    self.save_metadata(root_dir, feature_name=None)

  @classmethod
  def from_config(cls, root_dir: str) -> 'FeatureConnector':
    """Reconstructs the FeatureConnector from the config file.

    Usage:

    ```
    features = FeatureConnector.from_config('path/to/features.json')
    ```

    Args:
      root_dir: Directory containing to the features.json file.

    Returns:
      The reconstructed feature instance.
    """
    with tf.io.gfile.GFile(make_config_path(root_dir)) as f:
      feature = FeatureConnector.from_json(json.loads(f.read()))
    feature.load_metadata(root_dir, feature_name=None)
    return feature

  def get_serialized_info(self):
    """Return the shape/dtype of features after encoding (for the adapter).

    The `FileAdapter` then use those information to write data on disk.

    This function indicates how this feature is encoded on file internally.
    The DatasetBuilder are written on disk as tf.train.Example proto.

    Ex:

    ```
    return {
        'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8),
        'height': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
        'width': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
    }
    ```

    FeatureConnector which are not containers should return the feature proto
    directly:

    ```
    return tfds.features.TensorInfo(shape=(64, 64), tf.uint8)
    ```

    If not defined, the retuned values are automatically deduced from the
    `get_tensor_info` function.

    Returns:
      features: Either a dict of feature proto object, or a feature proto object

    """
    return self.get_tensor_info()

  @abc.abstractmethod
  def encode_example(self, example_data):
    """Encode the feature dict into tf-example compatible input.

    The input example_data can be anything that the user passed at data
    generation. For example:

    For features:

    ```
    features={
        'image': tfds.features.Image(),
        'custom_feature': tfds.features.CustomFeature(),
    }
    ```

    At data generation (in `_generate_examples`), if the user yields:

    ```
    yield {
        'image': 'path/to/img.png',
        'custom_feature': [123, 'str', lambda x: x+1]
    }
    ```

    Then:

     * `tfds.features.Image.encode_example` will get `'path/to/img.png'` as
       input
     * `tfds.features.CustomFeature.encode_example` will get `[123, 'str',
       lambda x: x+1] as input

    Args:
      example_data: Value or dictionary of values to convert into tf-example
        compatible data.

    Returns:
      tfexample_data: Data or dictionary of data to write as tf-example. Data
        can be a list or numpy array.
        Note that numpy arrays are flattened so it's the feature connector
        responsibility to reshape them in `decode_example()`.
        Note that tf.train.Example only supports int64, float32 and string so
        the data returned here should be integer, float or string. User type
        can be restored in `decode_example()`.
    """
    raise NotImplementedError

  def decode_example(self, tfexample_data):
    """Decode the feature dict to TF compatible input.

    Note: If eager is not enabled, this function will be executed as a
    tensorflow graph (in `tf.data.Dataset.map(features.decode_example)`).

    Args:
      tfexample_data: Data or dictionary of data, as read by the tf-example
        reader. It correspond to the `tf.Tensor()` (or dict of `tf.Tensor()`)
        extracted from the `tf.train.Example`, matching the info defined in
        `get_serialized_info()`.

    Returns:
      tensor_data: Tensor or dictionary of tensor, output of the tf.data.Dataset
        object
    """
    return tfexample_data

  def decode_batch_example(self, tfexample_data):
    """Decode multiple features batched in a single tf.Tensor.

    This function is used to decode features wrapped in
    `tfds.features.Sequence()`.
    By default, this function apply `decode_example` on each individual
    elements using `tf.map_fn`. However, for optimization, features can
    overwrite this method to apply a custom batch decoding.

    Args:
      tfexample_data: Same `tf.Tensor` inputs as `decode_example`, but with and
        additional first dimension for the sequence length.

    Returns:
      tensor_data: Tensor or dictionary of tensor, output of the tf.data.Dataset
        object
    """
    ex = tfexample_data

    # Note: This all works fine in Eager mode (without tf.function) because
    # tf.data pipelines are always executed in Graph mode.

    # Apply the decoding to each of the individual distributed features.
    decode_map_fn = functools.partial(
        tf.map_fn,
        self.decode_example,
        fn_output_signature=self.dtype,
        parallel_iterations=10,
        name='sequence_decode',
    )

    if (
        # input/output could potentially be a `dict` for custom feature
        # connectors. Empty length not supported for those for now.
        isinstance(ex, dict) or isinstance(self.shape, dict) or
        not _has_shape_ambiguity(in_shape=ex.shape, out_shape=self.shape)):
      return decode_map_fn(ex)
    else:
      # `tf.map_fn` cannot resolve ambiguity when decoding an empty sequence
      # with unknown output shape (e.g. decode images `tf.string`):
      # `(0,)` -> `(0, None, None, 3)`.
      # Instead, we arbitrarily set unknown shape to `0`:
      # `(0,)` -> `(0, 0, 0, 3)`
      return tf.cond(
          tf.equal(tf.shape(ex)[0], 0),  # Empty sequence
          lambda: _make_empty_seq_output(shape=self.shape, dtype=self.dtype),
          lambda: decode_map_fn(ex),
      )

  def decode_ragged_example(self, tfexample_data):
    """Decode nested features from a tf.RaggedTensor.

    This function is used to decode features wrapped in nested
    `tfds.features.Sequence()`.
    By default, this function apply `decode_batch_example` on the flat values
    of the ragged tensor. For optimization, features can
    overwrite this method to apply a custom batch decoding.

    Args:
      tfexample_data: `tf.RaggedTensor` inputs containing the nested encoded
        examples.

    Returns:
      tensor_data: The decoded `tf.RaggedTensor` or dictionary of tensor,
        output of the tf.data.Dataset object
    """
    return tf.ragged.map_flat_values(self.decode_batch_example, tfexample_data)

  def repr_html(self, ex: np.ndarray) -> str:
    """Returns the HTML str representation of the object."""
    return _repr_html(ex)

  def repr_html_batch(self, ex: np.ndarray) -> str:
    """Returns the HTML str representation of the object (Sequence)."""
    _MAX_SUB_ROWS = 7  # pylint: disable=invalid-name
    if isinstance(ex, tf.RaggedTensor):  # e.g. `Sequence(Video())`
      return _repr_html(ex)
    # Truncate sequences which contains too many sub-examples
    if len(ex) > _MAX_SUB_ROWS:
      ex = ex[:_MAX_SUB_ROWS]
      overflow = ['...']
    else:
      overflow = []
    batch_ex = '<br/>'.join([self.repr_html(x) for x in ex] + overflow)
    # TODO(tfds): How to limit the max-height to the neighboors cells ?
    return (
        f'<div style="overflow-y: scroll; max-height: 300px;" >{batch_ex}</div>'
    )

  def repr_html_ragged(self, ex: np.ndarray) -> str:
    """Returns the HTML str representation of the object (Nested sequence)."""
    return _repr_html(ex)

  def _flatten(self, x):
    """Flatten the input dict into a list of values.

    For instance, the following feature:
    ```
    feature = FeatureDict({
        'a': w,
        'b': x,
        'c': {
            'd': y,
            'e': z,
        },
    })
    ```

    Applied to the following `dict`:
    ```
    feature._flatten({
        'b': X,
        'c': {
            'd': Y,
        },
    })
    ```

    Will produce the following flattened output:
    ```
    [
        None,
        X,
        Y,
        None,
    ]
    ```

    Args:
      x: A nested `dict` like structure matching the structure of the
        `FeatureConnector`. Note that some elements may be missing.

    Returns:
      `list`: The flattened list of element of `x`. Order is guaranteed to be
      deterministic. Missing elements will be filled with `None`.
    """
    return [x]

  def _nest(self, list_x):
    """Pack the list into a nested dict.

    This is the reverse function of flatten.

    For instance, the following feature:
    ```
    feature = FeatureDict({
        'a': w,
        'b': x,
        'c': {
            'd': y,
            'e': z,
        },
    })
    ```

    Applied to the following `dict`:
    ```
    feature._nest([
        None,
        X,
        Y,
        None,
    ])
    ```

    Will produce the following nested output:
    ```
    {
        'a': None,
        'b': X,
        'c': {
            'd': Y,
            'e': None,
        },
    }
    ```

    Args:
      list_x: List of values matching the flattened `FeatureConnector`
        structure. Missing values should be filled with None.

    Returns:
      nested_x: nested `dict` matching the flattened `FeatureConnector`
        structure.
    """
    assert len(list_x) == 1
    return list_x[0]

  def _additional_repr_info(self):
    """Override to return additional info to go into __repr__."""
    return {}

  def __repr__(self):
    """Display the feature dictionary."""
    tensor_info = self.get_tensor_info()
    if not isinstance(tensor_info, TensorInfo):
      return '{}({})'.format(type(self).__name__, tensor_info)

    # Ensure ordering of keys by adding them one-by-one
    repr_info = collections.OrderedDict()
    repr_info['shape'] = tensor_info.shape
    repr_info['dtype'] = repr(tensor_info.dtype)
    additional_info = self._additional_repr_info()
    for k, v in additional_info.items():
      repr_info[k] = v

    info_str = ', '.join(['%s=%s' % (k, v) for k, v in repr_info.items()])
    return '{}({})'.format(
        type(self).__name__,
        info_str,
    )

  def save_metadata(self, data_dir, feature_name):
    """Save the feature metadata on disk.

    This function is called after the data has been generated (by
    `_download_and_prepare`) to save the feature connector info with the
    generated dataset.

    Some dataset/features dynamically compute info during
    `_download_and_prepare`. For instance:

     * Labels are loaded from the downloaded data
     * Vocabulary is created from the downloaded data
     * ImageLabelFolder compute the image dtypes/shape from the manual_dir

    After the info have been added to the feature, this function allow to
    save those additional info to be restored the next time the data is loaded.

    By default, this function do not save anything, but sub-classes can
    overwrite the function.

    Args:
      data_dir: `str`, path to the dataset folder to which save the info (ex:
        `~/datasets/cifar10/1.2.0/`)
      feature_name: `str`, the name of the feature (from the FeaturesDict key)
    """
    pass

  def load_metadata(self, data_dir, feature_name):
    """Restore the feature metadata from disk.

    If a dataset is re-loaded and generated files exists on disk, this function
    will restore the feature metadata from the saved file.

    Args:
      data_dir: `str`, path to the dataset folder to which save the info (ex:
        `~/datasets/cifar10/1.2.0/`)
      feature_name: `str`, the name of the feature (from the FeaturesDict key)
    """
    pass


def make_config_path(root_dir: str) -> str:
  """Returns the path to the features config."""
  return os.path.join(root_dir, 'features.json')


def _repr_html(ex) -> str:
  """Default HTML repr."""
  if isinstance(ex, np.ndarray) and ex.size > 1:
    # Do not print individual values for array as it is slow
    # TODO(tfds): We could display a snippet, like the first/last tree items
    return f'{type(ex).__qualname__}(shape={ex.shape}, dtype={ex.dtype})'

  # Escape symbols which might have special meaning in HTML like '<', '>'
  return html.escape(repr(ex))


def _has_shape_ambiguity(in_shape: Shape, out_shape: Shape) -> bool:
  """Returns True if the shape can be an empty sequence with unknown shape."""
  # Normalize shape if running with `tf.compat.v1.disable_v2_tensorshape`
  if isinstance(in_shape, tf.TensorShape):
    in_shape = in_shape.as_list()  # pytype: disable=attribute-error

  return bool(
      in_shape[0] is None  # Empty sequence
      # Unknown output shape (note that sequence length isn't present,
      # as `self.shape` is called from the inner feature).
      and None in out_shape)


@functools.lru_cache(None)
def _feature_content_fields() -> List[descriptor.FieldDescriptor]:
  """Returns the `oneof content` descriptor fields of the `Feature` proto."""
  return list(feature_pb2.Feature.DESCRIPTOR.oneofs_by_name['content'].fields)


def _name2proto_cls(cls_name: str) -> Type[message.Message]:
  """Returns the name to the proto class."""
  all_cls_descriptors = [f.message_type for f in _feature_content_fields()]
  name2cls = {
      desc.full_name: desc._concrete_class for desc in all_cls_descriptors  # pylint: disable=protected-access
  }
  return name2cls[cls_name]


def _proto2oneof_field_name(proto: message.Message) -> str:
  """Returns the field name associated with the class."""
  for field in _feature_content_fields():
    if field.message_type._concrete_class == type(proto):  # pylint: disable=protected-access
      return field.name
  supported_cls = [
      f.message_type._concrete_class.name for f in _feature_content_fields()  # pylint: disable=protected-access
  ]
  raise ValueError(f'Unknown proto {type(proto)}. Supported: {supported_cls}.')


def _make_empty_seq_output(
    shape: Shape,
    dtype: tf.dtypes.DType,
) -> tf.Tensor:
  """Return an empty (0, *shape) `tf.Tensor` with `0` instead of `None`."""
  if not isinstance(shape, (tuple, list)) or None not in shape:
    raise ValueError(f'Could not construct empty output for shape: {shape}')
  return tf.constant([],
                     shape=[0] + [0 if d is None else d for d in shape],
                     dtype=dtype)
