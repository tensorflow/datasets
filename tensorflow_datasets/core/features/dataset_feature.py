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

"""Dataset feature for nested datasets."""
from __future__ import annotations

import dataclasses
import functools
from typing import Any, Callable, Dict, Iterator, Union

from tensorflow_datasets.core.data_sources import python
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.features import top_level_feature
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import tree_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


@dataclasses.dataclass(frozen=True)
class _getitem:  # pylint: disable=invalid-name
  """A pickable version of getitem that can be fed to Beam pipelines."""

  decode_fn: Callable[[Any], Any]
  nest: Callable[[Any], Any]
  flat_example: list[Any]

  def __call__(self, i):
    return self.decode_fn(self.nest([v[i] for v in self.flat_example]))


class Dataset(sequence_feature.Sequence):
  """A Dataset feature encodes a nested dataset.

  `Dataset` corresponds to a dataset of `tfds.features.FeatureConnector`. Using
  `tfds.features.Dataset` will return a nested `tf.data.Dataset` inside the
  top-level `tf.data.Dataset` returned by `tfds.load`. At generation time, an
  iterable over the dataset elements is given.

  If you use tfds.data_source and the NumPy path, `Dataset` will return
  a [data
  source](https://www.tensorflow.org/datasets/api_docs/python/tfds/data_source).
  The advantage of having a data source is that decoding will be lazily executed
  when you access each example in the dataset.

  This is an experimental feature. Currently, only one level of nesting is
  supported and TF1 graph is not supported either.

  Example:
  At construction time (inside `_info`):

  ```python
    features=tfds.features.FeatureDict({
     'agent_id': np.object_,
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
    return tree_utils.map_structure(_add_dataset_lvl, tensor_info)

  def get_tensor_spec(self) -> tf.data.DatasetSpec:
    return tf.data.DatasetSpec(element_spec=self._feature.get_tensor_spec())

  @py_utils.memoize()
  def get_serialized_info(self):
    # Add the dataset level and the number of elements in the dataset
    tensor_info = super().get_serialized_info()
    return tree_utils.map_structure(_add_dataset_lvl, tensor_info)

  def encode_example(
      self,
      example_ds: Union[Iterator[type_utils.TreeDict[Any]], Dict[str, Any]],
  ):
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
      return tree_utils.map_structure(
          sequence_feature.build_empty_np, self.get_serialized_info()
      )

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
        decode_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE
    )
    return ds

  def decode_example_np(
      self, serialized_example, decoders=None
  ) -> python.PythonDataSource:
    """See base class for details."""
    flatten = self.feature._flatten  # pylint: disable=protected-access
    nest = self.feature._nest  # pylint: disable=protected-access
    flat_example = flatten(serialized_example)
    flat_features = flatten(self.feature)
    num_slices: int | None = None

    # First discover the number of slices in the Dataset. Notably, it's possible
    # that tensors have to be reshaped. We call slice a record in the Dataset.
    # We don't use `example` to avoid confusion with the `serialized_example`.
    for i, feature in enumerate(flat_features):
      if isinstance(feature, tensor_feature.Tensor) and feature.shape:
        try:
          flat_example[i] = flat_example[i].reshape((-1,) + feature.shape)
        except ValueError as e:
          raise ValueError(
              "The length of all elements of one slice should be the same."
          ) from e
        feature_num_slices = flat_example[i].shape[0]
      else:
        feature_num_slices = len(flat_example[i])
      if num_slices is None:
        num_slices = feature_num_slices
      else:
        if feature_num_slices != num_slices:
          raise ValueError(
              "The length of elements of all slices should be the same. Got"
              f" {num_slices} and {feature_num_slices}"
          )
    if num_slices is None:
      raise ValueError("no feature was found.")

    # Then, we apply the decode function on each slice.
    if isinstance(self.feature, top_level_feature.TopLevelFeature):
      # Only top-level features accept decoders.
      decode_fn = functools.partial(
          self.feature.decode_example_np, decoders=decoders
      )
    else:
      decode_fn = self.feature.decode_example_np

    return python.PythonDataSource(
        length=num_slices, getitem=_getitem(decode_fn, nest, flat_example)
    )

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
