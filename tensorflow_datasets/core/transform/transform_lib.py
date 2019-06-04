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

"""Transform utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def partial_map_nested(map_fns, data):
  """Maps fns on data, respecting the structure.

  Note that this function is applied recursively on substructures in data
  and fns.

  Args:
    map_fns: structured set of callables whose structure (partially) matches
      `data`. Lists correspond to callables that should be applied in sequence.
    data: structured data element.

  Returns:
    data mapped. Any entries that are None or missing from fns are
    passed-through (i.e. mapped with identity).
  """
  if not isinstance(map_fns, list):
    map_fns = [map_fns]

  for fn in map_fns:
    if isinstance(fn, dict):
      assert isinstance(data, dict)
      for k in fn:
        assert k in data
        data[k] = partial_map_nested(fn[k], data[k])
    elif isinstance(fn, tuple):
      assert isinstance(data, tuple)
      assert len(data) == len(fn)
      mapped = []
      for i in range(len(fn)):
        if fn[i] is None:
          mapped.append(data[i])
        else:
          mapped.append(partial_map_nested(fn[i], data[i]))
      data = tuple(mapped)
    else:
      data = fn(data)
  return data
