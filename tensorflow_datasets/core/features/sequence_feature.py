# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.core.features import feature


class SequenceDict(feature.FeaturesDict):
  """Sequence feature.

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
  yield self.info.encode_example({
      'frame': np.ones(shape=(NB_FRAME, 64, 64, 3)),
      'action': ['left', 'left', 'up', ...],
  })
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
      return feature.TensorInfo(
          shape=(self._length,) + tensor_info.shape,
          dtype=tensor_info.dtype,
      )

    tensor_info = super(SequenceDict, self).get_tensor_info()
    return utils.map_nested(add_length_dim, tensor_info)

  def get_serialized_features(self):
    """See base class for details."""
    # Add the additional length dimension to every serialized features

    def add_length_dim(serialized_feature):
      """Add the length dimension to the serialized_feature."""
      if isinstance(serialized_feature, tf.io.FixedLenFeature):
        if self._length is not None:
          return tf.io.FixedLenFeature(
              shape=(self._length,) + serialized_feature.shape,
              dtype=serialized_feature.dtype,
          )
        else:
          return tf.io.FixedLenSequenceFeature(
              shape=serialized_feature.shape,
              dtype=serialized_feature.dtype,
              allow_missing=True,
          )
      elif isinstance(serialized_feature, tf.io.VarLenFeature):
        return serialized_feature
      else:
        raise ValueError(
            'FixedLenSequenceFeature not supported inside SequenceDict'
        )
      return serialized_feature

    tensor_info = super(SequenceDict, self).get_serialized_features()
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
    # Empty sequences not supported
    if not sequence_elements:
      raise ValueError('SequenceFeatures do not support empty sequences.')

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


def stack_arrays(*elems):
  if isinstance(elems[0], np.ndarray):
    return np.stack(elems)
  else:
    return [e for e in elems]


def np_to_list(elem):
  if isinstance(elem, list):
    return elem
  elif isinstance(elem, np.ndarray):
    elem = np.split(elem, elem.shape[0])
    elem = np.squeeze(elem, axis=0)
    return elem
  else:
    raise ValueError(
        'Input elements of a sequence should be either a numpy array or a '
        'python list. Got {}'.format(type(elem)))


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
