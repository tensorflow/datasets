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

"""Dataset feature for nested datasets."""
import functools
from typing import Any, Dict, Iterator, Union

import tensorflow as tf

from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils


class Dataset(sequence_feature.Sequence):
  """A Dataset feature encodes a nested dataset.

  `Dataset` corresponds to a dataset of `tfds.features.FeatureConnector`. Using
  `tfds.features.Dataset` will return a nested `tf.data.Dataset` inside the
  top-level `tf.data.Dataset` returned by `tfds.load`. At generation time, an
  iterable over the dataset elements is given.

  This is an experimental feature. Currently, only one level of nesting is
  supported and TF1 graph is not supported either.

  Example:
  At construction time (inside `_info`):

  ```python
    features=tfds.features.FeatureDict({
     'agent_id': tf.string,
      'episode': tfds.features.Dataset({
        'observation': tfds.features.Image(),
        'reward': tfds.features.Image(),
      }),
    })
  ```


  Will return:

  ```
  {
    'agent_id': tf.Tensor(shape=(), dtype=tf.string),
    'episode': tf.data.Dataset(element_spec={
        'observation': tf.Tensor(shape=(None, None, 3), dtype=tf.uint8),
        'reward': tf.Tensor(shape=(), dtype=tf.int32),
    }),
    }
  ```

  The nested dataset can be used as:

  ```
  for e in tfds.load(...): # {'agent_id': tf.Tensor, 'episode': tf.data.Dataset}
    for step in e['episode']:  # Each episode is a nested  `tf.data.Dataset`
      step['observation']
  ```

  During generation,  it accept any `Iterable`/`Iterator`, like

  ```python
  yield _, {
    'agent_id': agent_name
    'episode': ({'observation': ..., 'reward': ...} for _ in range(10)),
  }
  ```

  Or a dictionary of `Iterable`, like

  ```python
  yield _, {
    'agent_id': agent_name
    'episode': {'observation': np.ones(10), 'reward': np.ones(10)} ,
  }
  ```
  """

  # TODO(tfds): Add support for TF1 graph mode.

  @py_utils.memoize()
  def get_tensor_info(self):
    """Shape of one element of the dataset."""
    # Add the dataset level
    tensor_info = self._feature.get_tensor_info()
    return tf.nest.map_structure(_add_dataset_lvl, tensor_info)

  def get_tensor_spec(self) -> tf.data.DatasetSpec:
    return tf.data.DatasetSpec(element_spec=self._feature.get_tensor_spec())

  @py_utils.memoize()
  def get_serialized_info(self):
    # Add the dataset level and the number of elements in the dataset
    tensor_info = super().get_serialized_info()
    return tf.nest.map_structure(_add_dataset_lvl, tensor_info)

  def encode_example(self, example_ds: Union[Iterator[type_utils.TreeDict[Any]],
                                             Dict[str, Any]]):
    if isinstance(example_ds, dict):
      dict_list = sequence_feature.transpose_dict_list(example_ds)
    else:
      dict_list = example_ds
    # Encode each individual element
    ds_elements = [
        self.feature.encode_example(example) for example in dict_list
    ]

    # Empty datasets return empty arrays
    if not ds_elements:
      return tf.nest.map_structure(sequence_feature.build_empty_np,
                                   self.get_serialized_info())

    # Then convert back list[nested dict] => nested dict[list]
    encoded = sequence_feature.stack_nested(ds_elements)
    return encoded

  def decode_example(self, serialized_example, decoders=None):
    # NOTE: By using from_tensor_slices we remove the possibility of nested
    # datasets.

    # Gets the decoding function of the inner feature to apply it to the
    # elements of the dataset.
    decode_fn = self.feature.decode_example
    if decoders:
      decode_fn = functools.partial(decode_fn, decoders=decoders)
    ds = tf.data.Dataset.from_tensor_slices(serialized_example).map(
        decode_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    return ds

  def _flatten(self, x):
    """See base class for details."""
    return [x]

  def _nest(self, list_x):
    """See base class for details."""
    assert len(list_x) == 1

    return list_x[0]


def _add_dataset_lvl(tensor_info):
  """Add the dataset nesting level to the tensor_info."""
  tensor_info = feature_lib.TensorInfo.copy_from(tensor_info)
  tensor_info.dataset_lvl += 1
  return tensor_info
