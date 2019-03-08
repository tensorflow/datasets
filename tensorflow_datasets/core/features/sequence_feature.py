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

"""Sequence feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib


class SequenceDict(feature_lib.FeaturesDict):
  """Composite `FeatureConnector` for a `dict` where each value is a list.

  `SequenceDict` correspond to sequence of `tfds.features.FeatureDict`. At
  generation time, a list for each of the sequence element is given. The output
  of `tf.data.Dataset` will batch all the elements of the sequence together.

  If the length of the sequence is static and known in advance, it should be
  specified in the constructor using the `length` param.

  Note that `SequenceDict` do not support features which are of type
  `tf.io.FixedLenSequenceFeature` and do not support empty sequences.

  Example:
  At construction time:

  ```
  tfds.SequenceDict({
      'frame': tfds.features.Image(shape=(64, 64, 3))
      'action': tfds.features.ClassLabel(['up', 'down', 'left', 'right'])
  }, length=NB_FRAME)
  ```

  During data generation:

  ```
  yield {
      'frame': np.ones(shape=(NB_FRAME, 64, 64, 3)),
      'action': ['left', 'left', 'up', ...],
  }
  ```

  Tensor returned by `.as_dataset()`:

  ```
  {
      'frame': tf.Tensor(shape=(NB_FRAME, 64, 64, 3), dtype=tf.uint8),
      'action': tf.Tensor(shape=(NB_FRAME,), dtype=tf.int64),
  }
  ```

  At generation time, you can specify a list of features dict, a dict of list
  values or a stacked numpy array. The lists will automatically be distributed
  into their corresponding `FeatureConnector`.

  """

  def __init__(self, feature_dict, length=None, **kwargs):
    """Construct a sequence dict.

    Args:
      feature_dict: `dict`, the features to wrap
      length: `int`, length of the sequence if static and known in advance
      **kwargs: `dict`, constructor kwargs of `tfds.features.FeaturesDict`
    """
    # TODO(epot): Should add a context_keys=('...', ...) to indicate
    # the features which are not sequences. Similarly to
    # tf.train.SequenceExample which has both sequence and context features
    self._length = length
    super(SequenceDict, self).__init__(feature_dict, **kwargs)

  def get_tensor_info(self):
    """See base class for details."""
    # Add the additional length dimension to every shape

    def add_length_dim(tensor_info):
      return feature_lib.TensorInfo(
          shape=(self._length,) + tensor_info.shape,
          dtype=tensor_info.dtype,
      )

    tensor_info = super(SequenceDict, self).get_tensor_info()
    return utils.map_nested(add_length_dim, tensor_info)

  def get_serialized_info(self):
    """See base class for details."""
    # Add the additional length dimension to every serialized features

    def add_length_dim(serialized_info):
      """Add the length dimension to the serialized_info.

      Args:
        serialized_info: One of tf.io.FixedLenFeature, tf.io.VarLenFeature,...

      Returns:
        new_serialized_info: serialized_info with extended first dimension
      """
      if isinstance(serialized_info, tf.io.FixedLenFeature):
        if self._length is not None:
          return tf.io.FixedLenFeature(
              shape=(self._length,) + serialized_info.shape,
              dtype=serialized_info.dtype,
          )
        else:
          return tf.io.FixedLenSequenceFeature(
              shape=serialized_info.shape,
              dtype=serialized_info.dtype,
              allow_missing=True,
          )
      elif isinstance(serialized_info, tf.io.VarLenFeature):
        return serialized_info
      else:
        raise ValueError(
            'FixedLenSequenceFeature not supported inside SequenceDict'
        )
      return serialized_info

    tensor_info = super(SequenceDict, self).get_serialized_info()
    return utils.map_nested(add_length_dim, tensor_info)

  def encode_example(self, example_dict):
    # Convert nested dict[list] into list[nested dict]
    sequence_elements = _transpose_dict_list(example_dict)

    # If length is static, ensure that the given length match
    if self._length is not None and len(sequence_elements) != self._length:
      raise ValueError(
          'Input sequence length do not match the defined one. Got {} != '
          '{}'.format(len(sequence_elements), self._length)
      )

    # Empty sequences return empty arrays
    if not sequence_elements:
      return {
          key: np.empty(shape=(0,), dtype=serialized_info.dtype.as_numpy_dtype)
          for key, serialized_info in self.get_serialized_info().items()
      }

    # Encode each individual elements
    sequence_elements = [
        super(SequenceDict, self).encode_example(sequence_elem)
        for sequence_elem in sequence_elements
    ]

    # Then merge the elements back together
    sequence_elements = {
        # Stack along the first dimension
        k: stack_arrays(*elems)
        for k, elems in utils.zip_dict(*sequence_elements)
    }
    return sequence_elements

  def decode_example(self, tfexample_dict):
    # TODO(epot): In eager mode, should investigate the use of
    # tf.contrib.eager.defun to parallelize the calls and improve the pipeline
    # performances, as recommended in tf.map_fn documentation

    # Apply the decoding to each of the individual feature.
    return tf.map_fn(
        super(SequenceDict, self).decode_example,
        tfexample_dict,
        dtype=self.dtype,
        parallel_iterations=10,
        back_prop=False,
        name='sequence_decode',
    )


class Sequence(feature_lib.FeatureConnector):
  """Similar to `tfds.featuresSequenceDict`, but only contains a single feature.

  Ex:
  In `DatasetInfo`:

  ```
  features=tfds.features.FeatureDict({
      'image': tfds.features.Image(),
      'labels': tfds.features.Sequence(tfds.features.ClassLabel(num_classes=5)),
  })
  ```

  At generation time:

  ```
  yield {
      'image': 'path/to/img.png',
      'labels': [0, 3, 3, 2, 4],
  }
  ```

  Note that the underlying feature attributes can be accessed directly through
  the sequence.

  ```
  builder.info.features['labels'].names
  ```

  """

  def __init__(self, feature, **kwargs):
    """Construct a sequence from a specific feature.

    Args:
      feature: `tfds.features.FeatureConnector`, The feature to wrap as sequence
      **kwargs: Same additional arguments as for `tfds.features.SequenceDict`,
        like `length`.
    """
    self._seq_feature = SequenceDict({'inner': feature}, **kwargs)

  def __getattr__(self, key):
    """Allow to access the underlying attributes directly."""
    return getattr(self._seq_feature['inner'], key)

  def get_tensor_info(self):
    return self._seq_feature.get_tensor_info()['inner']

  def get_serialized_info(self):
    return self._seq_feature.get_serialized_info()['inner']

  def encode_example(self, example_data):
    """Wrapper arround SequenceDict."""
    return self._seq_feature.encode_example({'inner': example_data})['inner']

  def decode_example(self, tfexample_data):
    """Wrapper arround SequenceDict."""
    return self._seq_feature.decode_example({'inner': tfexample_data})['inner']

  def _additional_repr_info(self):
    """Override to return addtional info to go into __repr__."""
    return {'feature': repr(self._seq_feature['inner'])}


def stack_arrays(*elems):
  if isinstance(elems[0], np.ndarray):
    return np.stack(elems)
  else:
    return [e for e in elems]


def np_to_list(elem):
  """Returns list from list, tuple or ndarray."""
  if isinstance(elem, list):
    return elem
  elif isinstance(elem, tuple):
    return list(elem)
  elif isinstance(elem, np.ndarray):
    return list(elem)
  else:
    raise ValueError(
        'Input elements of a sequence should be either a numpy array, a '
        'python list or tuple. Got {}'.format(type(elem)))


def _transpose_dict_list(dict_list):
  """Transpose a nested dict[list] into a list[nested dict]."""
  # 1. Unstack numpy arrays into list
  dict_list = utils.map_nested(np_to_list, dict_list, dict_only=True)

  # 2. Extract the sequence length (and ensure the length is constant for all
  # elements)
  length = {'value': None}  # dict because `nonlocal` is Python3 only
  def update_length(elem):
    if length['value'] is None:
      length['value'] = len(elem)
    elif length['value'] != len(elem):
      raise ValueError(
          'The length of all elements of one sequence should be the same. '
          'Got {} != {}'.format(length['value'], len(elem)))
    return elem
  utils.map_nested(update_length, dict_list, dict_only=True)

  # 3. Extract each individual elements
  return [
      utils.map_nested(lambda elem: elem[i], dict_list, dict_only=True)   # pylint: disable=cell-var-from-loop
      for i in range(length['value'])
  ]
