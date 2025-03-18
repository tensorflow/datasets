# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""NumPy utils."""

from typing import Any, Callable, Tuple, Union

import numpy as np
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tree


@py_utils.memoize()
def to_np_shape(shape: type_utils.Shape, replace_int=-1) -> Tuple[int]:
  return tuple(dim if dim is not None else replace_int for dim in shape)


def _dict_to_list(dict_of_lists: dict[str, Any]) -> list[Any]:
  """Converts a dict of lists to a list of dicts with the same structure."""
  feature_name = next(iter(dict_of_lists.keys()))
  length = len(dict_of_lists[feature_name])
  return [
      {k: dict_of_lists[k][i] for k in dict_of_lists} for i in range(length)
  ]


def _list_to_dict(
    list_of_elements: list[Any],
) -> Union[dict[str, Any], np.ndarray]:
  """Converts a list of elements to a dict of elements with the same struct."""
  if not list_of_elements:
    return {}
  first = list_of_elements[0]
  if isinstance(first, dict):
    return {k: np.asarray([v[k] for v in list_of_elements]) for k in first}
  else:
    return np.asarray(list_of_elements)


def np_map_fn(
    fn: Callable[[Any], Any],
    slices: Union[list[Any], dict[str, Any], np.ndarray],
):
  """Executes fn on all slices. NumPy equivalent of tf.map_fn.

  Args:
    fn: The function to execute.
    slices: An iterable or a dict of iterables.

  Returns:
    An object with the same structure as `slices` where every slice has `fn`
      applied.
  """
  if isinstance(slices, (list, np.ndarray)):
    return [fn(example) for example in slices]
  elif isinstance(slices, dict):
    if not slices:
      return slices
    if any(tree.is_nested(value) for value in slices.values()):
      raise NotImplementedError("Nested dict not supported by np_map_fn.")
    # For each slice of the dictionary...
    # {             <----- slice1 ----->     <----- slice2 ----->
    #     "image": [b"\x89PNG\r\n\x1a\n...", b"\x89PNG\r\n\x1a\n...", ...]
    #     "shape": [(100, 100, 3),           (100, 100, 3),           ...]
    # }
    # ...we apply the `fn` and reconstruct the dictionary:
    # {
    #     "image": np.array([[[255, 255, 0], ...]], ...])
    #     "shape": [(100, 100, 3),                  ...]
    # }
    fn_slices = [fn(s) for s in _dict_to_list(slices)]
    return _list_to_dict(fn_slices)
  else:
    raise ValueError(f"type {type(slices)} is not supported by np_map_fn.")
