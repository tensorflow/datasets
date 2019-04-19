# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Feature connector.

FeatureConnector is a way of abstracting what data is returned by the
tensorflow/datasets builders from how they are encoded/decoded from file.

# Use FeatureConnector in `GeneratorBasedBuilder`

1) In the _build_info() function, define the features as you would like them
to be returned by the tf.data.Dataset() object.

Ex:
  features=features.FeaturesDict({
      'input': features.Image(),
      'target': features.Text(encoder=SubWordEncoder()),
      'extra_data': {
          'label_id': tf.int64,
          'language': tf.string,
      }
  })

The tf.data.Dataset will return each examples as a dict:
  {
      'input': tf.Tensor(shape=(batch, height, width, channel), tf.uint8),
      'target': tf.Tensor(shape=(batch, sequence_length), tf.int64),
      'extra_data': {
          'label_id': tf.Tensor(shape=(batch,), tf.int64),
          'language': tf.Tensor(shape=(batch,), tf.string),
      }
  }

2) In the generator function, yield the examples to match what you have defined
in the spec. The values will automatically be encoded.

  yield {
      'input': np_image,
      'target': 'This is some text',
      'extra_data': {
          'label_id': 43,
          'language': 'en',
      }
  }

# Create your own FeatureConnector

To create your own feature connector, you need to inherit from FeatureConnector
and implement the abstract methods.

1. If your connector only contains one value, then the get_serialized_info,
   get_tensor_info, encode_example, and decode_example can directly process
   single value, without wrapping it in a dict.

2. If your connector is a container of multiple sub-connectors, the easiest
   way is to inherit from features.FeaturesDict and use the super() methods to
   automatically encode/decode the sub-connectors.

This file contains the following FeatureConnector:
 * FeatureConnector: The abstract base class defining the interface
 * FeaturesDict: Container of FeatureConnector
 * Tensor: Simple tensor value with static or dynamic shape

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import collections
import posixpath

import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import utils


TensorInfo = collections.namedtuple('TensorInfo', ['shape', 'dtype'])


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

  @abc.abstractmethod
  def get_tensor_info(self):
    """Return the tf.Tensor dtype/shape of the feature.

    This returns the tensor dtype/shape, as returned by .as_dataset by the
    `tf.data.Dataset` object.

    Ex:

    ```
    return {
        'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8):
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
    return utils.map_nested(lambda t: t.shape, self.get_tensor_info())

  @property
  def dtype(self):
    """Return the dtype (or dict of dtype) of this FeatureConnector."""
    return utils.map_nested(lambda t: t.dtype, self.get_tensor_info())

  def get_serialized_info(self):
    """Return the tf-example features for the adapter, as stored on disk.

    This function indicates how this feature is encoded on file internally.
    The DatasetBuilder are written on disk as tf.train.Example proto.

    Ex:

    ```
    return {
        'image': tf.VarLenFeature(tf.uint8):
        'height': tf.FixedLenFeature((), tf.int32),
        'width': tf.FixedLenFeature((), tf.int32),
    }
    ```

    FeatureConnector which are not containers should return the feature proto
    directly:

    ```
    return tf.FixedLenFeature((64, 64), tf.uint8)
    ```

    If not defined, the retuned values are automatically deduced from the
    `get_tensor_info` function.

    Returns:
      features: Either a dict of feature proto object, or a feature proto object

    """
    return utils.map_nested(to_serialized_field, self.get_tensor_info())

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

  @abc.abstractmethod
  def decode_example(self, tfexample_data):
    """Decode the feature dict to TF compatible input.

    Note: If eager is not enabled, this function will be executed as a
    tensorflow graph (in `tf.data.Dataset.map(features.decode_examples)`).

    Args:
      tfexample_data: Data or dictionary of data, as read by the tf-example
        reader. It correspond to the `tf.Tensor()` (or dict of `tf.Tensor()`)
        extracted from the `tf.train.Example`, matching the info defined in
        `get_serialize_info()`.

    Returns:
      tensor_data: Tensor or dictionary of tensor, output of the tf.data.Dataset
        object
    """
    raise NotImplementedError

  @property
  def serialized_keys(self):
    """List of the flattened feature keys after serialization."""
    features = self.get_serialized_info()
    if isinstance(features, dict):
      return list(features)
    return None

  def _additional_repr_info(self):
    """Override to return addtional info to go into __repr__."""
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


class FeaturesDict(FeatureConnector):
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
  proto do not support nested feature, while tf.data.Dataset does.
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

  def __init__(self, feature_dict):
    """Initialize the features.

    Args:
      feature_dict (dict): Dictionary containing the feature connectors of a
        example. The keys should correspond to the data dict as returned by
        tf.data.Dataset(). Types (tf.int32,...) and dicts will automatically
        be converted into FeatureConnector.

    Raises:
      ValueError: If one of the given features is not recognized
    """
    super(FeaturesDict, self).__init__()
    self._feature_dict = {k: to_feature(v) for k, v in feature_dict.items()}

  # Dict functions.
  # In Python 3, should inherit from collections.abc.Mapping().

  def keys(self):
    return self._feature_dict.keys()

  def items(self):
    return self._feature_dict.items()

  def values(self):
    return self._feature_dict.values()

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
    return '{}({})'.format(type(self).__name__, self._feature_dict)

  def get_tensor_info(self):
    """See base class for details."""
    return {
        feature_key: feature.get_tensor_info()
        for feature_key, feature in self._feature_dict.items()
    }

  def get_serialized_info(self):
    """See base class for details."""
    # Flatten tf-example features dict
    # Use NonMutableDict to ensure there is no collision between features keys
    features_dict = utils.NonMutableDict()
    for feature_key, feature in self._feature_dict.items():
      serialized_info = feature.get_serialized_info()

      # Features can be either containers (dict of other features) or plain
      # features (ex: single tensor). Plain features have a None
      # feature.features_keys
      if not feature.serialized_keys:
        features_dict[feature_key] = serialized_info
      else:
        # Sanity check which should always be True, as feature.serialized_keys
        # is computed using feature.get_serialized_info()
        _assert_keys_match(serialized_info.keys(), feature.serialized_keys)
        features_dict.update({
            posixpath.join(feature_key, k): v
            for k, v in serialized_info.items()
        })

    return features_dict

  def encode_example(self, example_dict):
    """See base class for details."""
    # Flatten dict matching the tf-example features
    # Use NonMutableDict to ensure there is no collision between features keys
    tfexample_dict = utils.NonMutableDict()

    # Iterate over example fields
    for feature_key, (feature, example_value) in utils.zip_dict(
        self._feature_dict, example_dict):
      # Encode the field with the associated encoder
      encoded_feature = feature.encode_example(example_value)

      # Singleton case
      if not feature.serialized_keys:
        tfexample_dict[feature_key] = encoded_feature
      # Feature contains sub features
      else:
        _assert_keys_match(encoded_feature.keys(), feature.serialized_keys)
        tfexample_dict.update({
            posixpath.join(feature_key, k): encoded_feature[k]
            for k in feature.serialized_keys
        })
    return tfexample_dict

  def decode_example(self, tfexample_dict):
    """See base class for details."""
    tensor_dict = {}
    # Iterate over the Tensor dict keys
    for feature_key, feature in six.iteritems(self._feature_dict):
      decoded_feature = decode_single_feature_from_dict(
          feature_k=feature_key,
          feature=feature,
          tfexample_dict=tfexample_dict,
      )
      tensor_dict[feature_key] = decoded_feature
    return tensor_dict

  # TODO(epot): Should investigate if fixed size feature read can be more
  # optimized. And eventually expose a property has_fixed_shape_feature.

  def save_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Recursively save all child features
    for feature_key, feature in six.iteritems(self._feature_dict):
      if feature_name:
        feature_key = '-'.join((feature_name, feature_key))
      feature.save_metadata(data_dir, feature_name=feature_key)

  def load_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Recursively load all child features
    for feature_key, feature in six.iteritems(self._feature_dict):
      if feature_name:
        feature_key = '-'.join((feature_name, feature_key))
      feature.load_metadata(data_dir, feature_name=feature_key)


class Tensor(FeatureConnector):
  """`FeatureConnector` for generic data of arbitrary shape and type."""
  # TODO(epot): For variable length feature, will probably have to include the
  # shape in the spec, as it seems tf-example lose the shape by flattening the
  # value
  # TODO(epot): Call tf.compat.as_bytes for string data. Add unittests for str.

  @api_utils.disallow_positional_args
  def __init__(self, shape, dtype):
    """Construct a Tensor feature."""
    self._shape = shape
    self._dtype = dtype

    if self._shape is None or self._shape.count(None) > 1:
      raise NotImplementedError(
          'Tensor feature connector do not support tensors with more than '
          'one unknown dimension. Got {}'.format(self._shape)
      )

  def get_tensor_info(self):
    """See base class for details."""
    return TensorInfo(shape=self._shape, dtype=self._dtype)

  def encode_example(self, example_data):
    """See base class for details."""
    np_dtype = np.dtype(self._dtype.as_numpy_dtype)
    # Convert to numpy if possible
    if not isinstance(example_data, np.ndarray):
      example_data = np.array(example_data, dtype=np_dtype)
    # Ensure the shape and dtype match
    if example_data.dtype != np_dtype:
      raise ValueError('Dtype {} do not match {}'.format(
          example_data.dtype, np_dtype))
    utils.assert_shape_match(example_data.shape, self._shape)
    # For booleans, convert to integer (tf.train.Example does not support bool)
    if example_data.dtype == np.bool_:
      example_data = example_data.astype(int)
    return example_data

  def decode_example(self, tfexample_data):
    """See base class for details."""
    # TODO(epot): Support dynamic shape
    if self.shape.count(None) < 2:
      # Restore the shape if possible. TF Example flattened it.
      shape = [-1 if i is None else i for i in self.shape]
      tfexample_data = tf.reshape(tfexample_data, shape)
    if tfexample_data.dtype != self.dtype:
      tfexample_data = tf.dtypes.cast(tfexample_data, self.dtype)
    return tfexample_data


def to_serialized_field(tensor_info):
  """Convert a `TensorInfo` object into a feature proto object."""
  # Select the type
  dtype = tensor_info.dtype

  # TODO(b/119937875): TF Examples proto only support int64, float32 and string
  # This create limitation like float64 downsampled to float32, bool converted
  # to int64 which is space ineficient, no support for complexes or quantized
  if tensor_info.dtype.is_integer or tensor_info.dtype.is_bool:
    dtype = tf.int64
  elif tensor_info.dtype.is_floating:
    dtype = tf.float32
  # It seems quite space inefficient to convert bool to int64
  # We may want to add support for complex, quantize dtype in the future

  # TFRecord only support 3 types
  if dtype not in (tf.int64, tf.float32, tf.string):
    raise NotImplementedError(
        'Serialization not implemented for {}'.format(dtype))

  # Select the feature proto type in function of the unknown shape
  if (tensor_info.shape is not None and  # Shape is a sequence (None, ...)
      tensor_info.shape.count(None) == 1 and
      tensor_info.shape[0] is None):
    return tf.io.FixedLenSequenceFeature(
        shape=tensor_info.shape[1:],
        dtype=dtype,
        allow_missing=True,
    )
  # At least one dimension is undefined
  elif tensor_info.shape is None or None in tensor_info.shape:
    return tf.io.VarLenFeature(dtype=dtype)
  else:
    return tf.io.FixedLenFeature(
        shape=tensor_info.shape,
        dtype=dtype,
    )


def to_feature(value):
  """Convert the given value to Feature if necessary."""
  if isinstance(value, FeatureConnector):
    return value
  elif utils.is_dtype(value):  # tf.int32, tf.string,...
    return Tensor(shape=(), dtype=tf.as_dtype(value))
  elif isinstance(value, dict):
    return FeaturesDict(value)
  else:
    raise ValueError('Feature not supported: {}'.format(value))


def decode_single_feature_from_dict(
    feature_k,
    feature,
    tfexample_dict):
  """Decode the given feature from the tfexample_dict.

  Args:
    feature_k (str): Feature key in the tfexample_dict
    feature (FeatureConnector): Connector object to use to decode the field
    tfexample_dict (dict): Dict containing the data to decode.

  Returns:
    decoded_feature: The output of the feature.decode_example
  """
  # Singleton case
  if not feature.serialized_keys:
    data_to_decode = tfexample_dict[feature_k]
  # Feature contains sub features
  else:
    # Extract the sub-features from the global feature dict
    data_to_decode = {
        k: tfexample_dict[posixpath.join(feature_k, k)]
        for k in feature.serialized_keys
    }
  return feature.decode_example(data_to_decode)


def _assert_keys_match(keys1, keys2):
  """Ensure the two list of keys matches."""
  if set(keys1) != set(keys2):
    raise ValueError('{} {}'.format(list(keys1), list(keys2)))
