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

import contextlib
import itertools
import sys

# pylint: disable=g-import-not-at-top
if sys.version_info[0] > 2:
  import functools
else:
  import functools32 as functools
# pylint: enable=g-import-not-at-top


# NOTE: When used on an instance method, the cache is shared across all
# instances and IS NOT per-instance.
# See
# https://stackoverflow.com/questions/14946264/python-lru-cache-decorator-per-instance
# For @property methods, use @memoized_property below.
# TODO(rsepassi): Write a @memoize decorator that does the right thing for
# instance methods.
memoize = functools.lru_cache


@contextlib.contextmanager
def temporary_assignment(obj, attr, value):
  """Temporarily assign obj.attr to value."""
  original = getattr(obj, attr, None)
  setattr(obj, attr, value)
  yield
  setattr(obj, attr, original)


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


class classproperty(property):  # pylint: disable=invalid-name
  """Descriptor to be used as decorator for @classmethods."""

  def __get__(self, obj, objtype=None):
    return self.fget.__get__(None, objtype)()


class memoized_property(property):  # pylint: disable=invalid-name
  """Descriptor that mimics @property but caches output in member variable."""

  def __get__(self, obj, objtype=None):
    # See https://docs.python.org/3/howto/descriptor.html#properties
    if obj is None:
      return self
    if self.fget is None:
      raise AttributeError("unreadable attribute")
    attr = "__cached_" + self.fget.__name__
    cached = getattr(obj, attr, None)
    if cached is None:
      cached = self.fget(obj)
      setattr(obj, attr, cached)
    return cached


def map_nested(function, data_struct, dict_only=False):
  """Apply a function recursivelly to each element of a nested data struct."""

  # Could add support for more exotic data_struct, like OrderedDict
  if isinstance(data_struct, dict):
    return {
        k: map_nested(function, v, dict_only) for k, v in data_struct.items()
    }
  elif not dict_only:
    if isinstance(data_struct, list):
      return [map_nested(function, v, dict_only) for v in data_struct]
  # Singleton
  return function(data_struct)


def zip_nested(arg0, *args, **kwargs):
  """Zip data struct together and return a data struct with the same shape."""
  # Python 2 do not support kwargs only arguments
  dict_only = kwargs.pop("dict_only", False)
  assert not kwargs

  # Could add support for more exotic data_struct, like OrderedDict
  if isinstance(arg0, dict):
    return {
        k: zip_nested(*a, dict_only=dict_only) for k, a in zip_dict(arg0, *args)
    }
  elif not dict_only:
    if isinstance(arg0, list):
      return [zip_nested(*a, dict_only=dict_only) for a in zip(arg0, *args)]
  # Singleton
  return (arg0,) + args


def as_proto_cls(proto_cls):
  """Simulate proto inheritance.

  By default, protobuf do not support direct inheritance, so this decorator
  simulate inheriance to the class to which it is applied.

  Example:

  ```
  @as_proto_class(proto.MyProto)
  class A(object):
    def custom_method(self):
      return self.proto_field * 10

  p = proto.MyProto(proto_field=123)

  a = A()
  a.CopyFrom(p)  # a is like a proto object
  assert a.proto_field == 123
  a.custom_method()  # But has additional methods

  ```

  Args:
    proto_cls: The protobuf class to inherit from

  Returns:
    decorated_cls: The decorated class
  """

  def decorator(cls):
    """Decorator applied to the class."""

    class ProtoCls(object):
      """Base class simulating the protobuf."""

      def __init__(self, *args, **kwargs):
        self.__proto = proto_cls(*args, **kwargs)

      def __getattr__(self, attr_name):
        return getattr(self.__proto, attr_name)

      def __eq__(self, other):
        return self.__proto, other.get_proto()

      def get_proto(self):
        return self.__proto

    decorator_cls = type(cls.__name__, (cls, ProtoCls), {})
    # Class cannot be wraped because __doc__ not overwritable with python2
    return decorator_cls
  return decorator


def str_to_version(version_str):
  """Return the tuple (major, minor, patch) version extracted from the str."""
  version_ids = version_str.split(".")
  if len(version_ids) != 3 or "-" in version_str:
    raise ValueError(
        "Could not convert the {} to version. Format should be x.y.z".format(
            version_str))
  try:
    version_ids = tuple(int(v) for v in version_ids)
  except ValueError:
    raise ValueError(
        "Could not convert the {} to version. Format should be x.y.z".format(
            version_str))
  return version_ids
