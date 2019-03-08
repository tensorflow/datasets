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

"""Some python utils function and classes.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import hashlib
import io
import itertools
import os
import sys
import uuid

import six
import tensorflow as tf
from tensorflow_datasets.core import constants


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

  Will raise an error if the user try to overwrite one key. The error message
  can be customized during construction. It will be formatted using {key} for
  the overwritten key.
  """

  def __init__(self, *args, **kwargs):
    self._error_msg = kwargs.pop(
        "error_msg",
        "Try to overwrite existing key: {key}",
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


def map_nested(function, data_struct, dict_only=False, map_tuple=False):
  """Apply a function recursively to each element of a nested data struct."""

  # Could add support for more exotic data_struct, like OrderedDict
  if isinstance(data_struct, dict):
    return {
        k: map_nested(function, v, dict_only, map_tuple)
        for k, v in data_struct.items()
    }
  elif not dict_only:
    types = [list]
    if map_tuple:
      types.append(tuple)
    if isinstance(data_struct, tuple(types)):
      mapped = [map_nested(function, v, dict_only, map_tuple)
                for v in data_struct]
      if isinstance(data_struct, list):
        return mapped
      else:
        return tuple(mapped)
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
  simulates inheritance to the class to which it is applied.

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

      def __repr__(self):
        return "<{cls_name}\n{proto_repr}\n>".format(
            cls_name=cls.__name__, proto_repr=repr(self.__proto))

    decorator_cls = type(cls.__name__, (cls, ProtoCls), {
        "__doc__": cls.__doc__,
    })
    return decorator_cls
  return decorator


def tfds_dir():
  """Path to tensorflow_datasets directory."""
  return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@contextlib.contextmanager
def atomic_write(path, mode):
  """Writes to path atomically, by writing to temp file and renaming it."""
  tmp_path = "%s%s_%s" % (path, constants.INCOMPLETE_SUFFIX, uuid.uuid4().hex)
  with tf.io.gfile.GFile(tmp_path, mode) as file_:
    yield file_
  tf.io.gfile.rename(tmp_path, path, overwrite=True)


class abstractclassmethod(classmethod):  # pylint: disable=invalid-name
  """Decorate a method to mark it as an abstract @classmethod."""

  __isabstractmethod__ = True

  def __init__(self, fn):
    fn.__isabstractmethod__ = True
    super(abstractclassmethod, self).__init__(fn)


def get_tfds_path(relative_path):
  """Returns absolute path to file given path relative to tfds root."""
  path = os.path.join(tfds_dir(), relative_path)
  return path


def read_checksum_digest(path, checksum_cls=hashlib.sha256):
  """Given a hash constructor, returns checksum digest and size of file."""
  checksum = checksum_cls()
  size = 0
  with tf.io.gfile.GFile(path, "rb") as f:
    while True:
      block = f.read(io.DEFAULT_BUFFER_SIZE)
      size += len(block)
      if not block:
        break
      checksum.update(block)
  return checksum.hexdigest(), size


def reraise(additional_msg):
  """Reraise an exception with an additional message."""
  exc_type, exc_value, exc_traceback = sys.exc_info()
  msg = str(exc_value) + "\n" + additional_msg
  six.reraise(exc_type, exc_type(msg), exc_traceback)


def rgetattr(obj, attr, *args):
  """Get attr that handles dots in attr name."""
  def _getattr(obj, attr):
    return getattr(obj, attr, *args)
  return functools.reduce(_getattr, [obj] + attr.split("."))
