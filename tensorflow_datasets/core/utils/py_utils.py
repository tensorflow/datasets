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

"""Some python utils function and classes.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import itertools


class memoized_property(object):  # pylint: disable=invalid-name
  """Memoization property descriptor used as decorator.

  Allow to have members loaded only the first time there are needed and then
  there value is cached for later calls.
  """

  def __init__(self, fct):
    self.fct = fct  # Function which evaluate the attribute
    # Update __module__, __doc__ of the instance. Warning: This has no effect
    # on help() which look at the type().__doc__ and not the instance.__doc__
    functools.update_wrapper(self, fct)

  def __get__(self, instance, owner):
    if instance is None:  # Call from the class (cls.value)
      return None
    # The function is called only once per instance for loading the first time
    value = self.fct(instance)
    setattr(instance, self.fct.__name__, value)  # Overwrite the descriptor
    return value


def zip_dict(*dicts):
  """Iterate over items of dictionaries grouped by their keys."""
  for key in set(itertools.chain(*dicts)):  # set merge all keys
    # Will raise KeyError if the dict don't have the same keys
    yield key, tuple(d[key] for d in dicts)


class NonMutableDict(dict):
  """Dict where keys can only be added but not modified.

  Will raise an error if the user try to overwritte one key. The error message
  can be customized during construction. It will be formatted using {key} for
  the overwritted key.
  """

  def __init__(self, *args, **kwargs):
    self._error_msg = kwargs.pop(
        "error_msg",
        "Try to overwritte existing key: {key}",
    )
    if kwargs:
      raise ValueError("NonMutableDict cannot be initialized with kwargs.")
    super(NonMutableDict, self).__init__(*args, **kwargs)

  def __setitem__(self, key, value):
    if key in self:
      raise ValueError(self._error_msg.format(key=key))
    return super(NonMutableDict, self). __setitem__(key, value)

  def update(self, other):
    if any(k in self for k in other):
      raise ValueError(self._error_msg.format(key=set(self) & set(other)))
    return super(NonMutableDict, self).update(other)


def map_nested(function, data_struct):
  """Apply a function recursivelly to each element of a nested data struct."""
  if isinstance(data_struct, list):
    return [map_nested(function, v) for v in data_struct]
  elif isinstance(data_struct, dict):
    return {k: map_nested(function, v) for k, v in data_struct.items()}
  # Could add support for more exotic data_struct, like OrderedDict
  else:  # Singleton
    return function(data_struct)


def zip_nested(arg0, *args):
  """Zip data struct together and return a data struct with the same shape."""
  if isinstance(arg0, list):
    return [zip_nested(*a) for a in zip(arg0, *args)]
  elif isinstance(arg0, dict):
    return {k: zip_nested(*a) for k, a in zip_dict(arg0, *args)}
  # Could add support for more exotic data_struct, like OrderedDict
  else:  # Singleton
    return (arg0,) + args
