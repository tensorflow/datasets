# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Some python utils function and classes.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import hashlib
import io
import itertools
import logging
import os
import random
import string
import sys
import textwrap
import threading
from typing import Any, Callable, Iterator, List, TypeVar
import uuid

import six
from six.moves import urllib
import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import constants


# pylint: disable=g-import-not-at-top
try:  # Use shutil on Python 3.3+
  from shutil import disk_usage  # pytype: disable=import-error  # pylint: disable=g-importing-member
except ImportError:
  from psutil import disk_usage  # pytype: disable=import-error  # pylint: disable=g-importing-member
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


T = TypeVar('T')

Fn = TypeVar('Fn', bound=Callable[..., Any])


def is_notebook():
  """Returns True if running in a notebook (Colab, Jupyter) environement."""
  # Inspired from the tfdm autonotebook code
  try:
    import IPython  # pytype: disable=import-error  # pylint: disable=import-outside-toplevel,g-import-not-at-top
    if 'IPKernelApp' not in IPython.get_ipython().config:
      return False  # Run in a IPython terminal
  except:  # pylint: disable=bare-except
    return False
  else:
    return True


@contextlib.contextmanager
def temporary_assignment(obj, attr, value):
  """Temporarily assign obj.attr to value."""
  original = getattr(obj, attr)
  setattr(obj, attr, value)
  try:
    yield
  finally:
    setattr(obj, attr, original)


def zip_dict(*dicts):
  """Iterate over items of dictionaries grouped by their keys."""
  for key in set(itertools.chain(*dicts)):  # set merge all keys
    # Will raise KeyError if the dict don't have the same keys
    yield key, tuple(d[key] for d in dicts)


@contextlib.contextmanager
def disable_logging():
  """Temporarily disable the logging."""
  logger = logging.getLogger()
  logger_disabled = logger.disabled
  logger.disabled = True
  try:
    yield
  finally:
    logger.disabled = logger_disabled


class NonMutableDict(dict):
  """Dict where keys can only be added but not modified.

  Will raise an error if the user try to overwrite one key. The error message
  can be customized during construction. It will be formatted using {key} for
  the overwritten key.
  """

  def __init__(self, *args, **kwargs):
    self._error_msg = kwargs.pop(
        'error_msg',
        'Try to overwrite existing key: {key}',
    )
    if kwargs:
      raise ValueError('NonMutableDict cannot be initialized with kwargs.')
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
    return self.fget.__get__(None, objtype)()  # pytype: disable=attribute-error


class memoized_property(property):  # pylint: disable=invalid-name
  """Descriptor that mimics @property but caches output in member variable."""

  def __get__(self, obj, objtype=None):
    # See https://docs.python.org/3/howto/descriptor.html#properties
    if obj is None:
      return self
    if self.fget is None:  # pytype: disable=attribute-error
      raise AttributeError('unreadable attribute')
    attr = '__cached_' + self.fget.__name__  # pytype: disable=attribute-error
    cached = getattr(obj, attr, None)
    if cached is None:
      cached = self.fget(obj)  # pytype: disable=attribute-error
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
  dict_only = kwargs.pop('dict_only', False)
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


def flatten_nest_dict(d):
  """Return the dict with all nested keys flattened joined with '/'."""
  # Use NonMutableDict to ensure there is no collision between features keys
  flat_dict = NonMutableDict()
  for k, v in d.items():
    if isinstance(v, dict):
      flat_dict.update({
          '{}/{}'.format(k, k2): v2 for k2, v2 in flatten_nest_dict(v).items()
      })
    else:
      flat_dict[k] = v
  return flat_dict


def dedent(text):
  """Wrapper around `textwrap.dedent` which also `strip()` and handle `None`."""
  return textwrap.dedent(text).strip() if text else text


def pack_as_nest_dict(flat_d, nest_d):
  """Pack a 1-lvl dict into a nested dict with same structure as `nest_d`."""
  nest_out_d = {}
  for k, v in nest_d.items():
    if isinstance(v, dict):
      v_flat = flatten_nest_dict(v)
      sub_d = {
          k2: flat_d.pop('{}/{}'.format(k, k2)) for k2, _ in v_flat.items()
      }
      # Recursivelly pack the dictionary
      nest_out_d[k] = pack_as_nest_dict(sub_d, v)
    else:
      nest_out_d[k] = flat_d.pop(k)
  if flat_d:  # At the end, flat_d should be empty
    raise ValueError(
        'Flat dict strucure do not match the nested dict. Extra keys: '
        '{}'.format(list(flat_d.keys())))
  return nest_out_d


@contextlib.contextmanager
def nullcontext(enter_result: T = None) -> Iterator[T]:
  """Backport of `contextlib.nullcontext`."""
  yield enter_result


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
        super(ProtoCls, self).__setattr__(
            '_ProtoCls__proto',
            proto_cls(*args, **kwargs),
        )

      def __getattr__(self, attr_name):
        return getattr(self.__proto, attr_name)

      def __setattr__(self, attr_name, new_value):
        try:
          if isinstance(new_value, list):
            self.ClearField(attr_name)
            getattr(self.__proto, attr_name).extend(new_value)
          else:
            return setattr(self.__proto, attr_name, new_value)
        except AttributeError:
          return super(ProtoCls, self).__setattr__(attr_name, new_value)

      def __eq__(self, other):
        return self.__proto, other.get_proto()

      def get_proto(self):
        return self.__proto

      def __repr__(self):
        return '<{cls_name}\n{proto_repr}\n>'.format(
            cls_name=cls.__name__, proto_repr=repr(self.__proto))

    decorator_cls = type(cls.__name__, (cls, ProtoCls), {
        '__doc__': cls.__doc__,
    })
    return decorator_cls
  return decorator


def _get_incomplete_path(filename):
  """Returns a temporary filename based on filename."""
  random_suffix = ''.join(
      random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
  return filename + '.incomplete' + random_suffix


@contextlib.contextmanager
def incomplete_dir(dirname):
  """Create temporary dir for dirname and rename on exit."""
  tmp_dir = _get_incomplete_path(dirname)
  tf.io.gfile.makedirs(tmp_dir)
  try:
    yield tmp_dir
    tf.io.gfile.rename(tmp_dir, dirname)
  finally:
    if tf.io.gfile.exists(tmp_dir):
      tf.io.gfile.rmtree(tmp_dir)


def tfds_dir() -> str:
  """Path to tensorflow_datasets directory.

  The difference with `tfds.core.get_tfds_path` is that this function can be
  used for write access while `tfds.core.get_tfds_path` should be used for
  read-only.

  Returns:
    tfds_dir: The root TFDS path.
  """
  return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@contextlib.contextmanager
def atomic_write(path, mode):
  """Writes to path atomically, by writing to temp file and renaming it."""
  tmp_path = '%s%s_%s' % (path, constants.INCOMPLETE_SUFFIX, uuid.uuid4().hex)
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
  with tf.io.gfile.GFile(path, 'rb') as f:
    while True:
      block = f.read(io.DEFAULT_BUFFER_SIZE)
      size += len(block)
      if not block:
        break
      checksum.update(block)
  return checksum.hexdigest(), size


def reraise(prefix=None, suffix=None):
  """Reraise an exception with an additional message."""
  exc_type, exc_value, exc_traceback = sys.exc_info()
  prefix = prefix or ''
  suffix = '\n' + suffix if suffix else ''
  msg = prefix + str(exc_value) + suffix
  six.reraise(exc_type, exc_type(msg), exc_traceback)


@contextlib.contextmanager
def try_reraise(*args, **kwargs):
  """Reraise an exception with an additional message."""
  try:
    yield
  except Exception:   # pylint: disable=broad-except
    reraise(*args, **kwargs)


def rgetattr(obj, attr, *args):
  """Get attr that handles dots in attr name."""
  def _getattr(obj, attr):
    return getattr(obj, attr, *args)
  return functools.reduce(_getattr, [obj] + attr.split('.'))


def has_sufficient_disk_space(needed_bytes, directory='.'):
  try:
    free_bytes = disk_usage(os.path.abspath(directory)).free
  except OSError:
    return True
  return needed_bytes < free_bytes


def get_class_path(cls, use_tfds_prefix=True):
  """Returns path of given class or object. Eg: `tfds.image.cifar.Cifar10`."""
  if not isinstance(cls, type):
    cls = cls.__class__
  module_path = cls.__module__
  if use_tfds_prefix and module_path.startswith('tensorflow_datasets'):
    module_path = 'tfds' + module_path[len('tensorflow_datasets'):]
  return '.'.join([module_path, cls.__name__])


def get_class_url(cls):
  """Returns URL of given class or object."""
  cls_path = get_class_path(cls, use_tfds_prefix=False)
  module_path, unused_class_name = cls_path.rsplit('.', 1)
  module_path = module_path.replace('.', '/')
  return constants.SRC_BASE_URL + module_path + '.py'


def build_synchronize_decorator() -> Callable[[Fn], Fn]:
  """Returns a decorator which prevents concurrent calls to functions.

  Usage:
    synchronized = build_synchronize_decorator()

    @synchronized
    def read_value():
      ...

    @synchronized
    def write_value(x):
      ...

  Returns:
    make_threadsafe (fct): The decorator which lock all functions to which it
      is applied under a same lock
  """
  lock = threading.Lock()

  def lock_decorator(fn: Fn) -> Fn:

    @functools.wraps(fn)
    def lock_decorated(*args, **kwargs):
      with lock:
        return fn(*args, **kwargs)

    return lock_decorated

  return lock_decorator


def basename_from_url(url: str) -> str:
  """Returns file name of file at given url."""
  return os.path.basename(urllib.parse.urlparse(url).path) or 'unknown_name'


def list_info_files(dir_path: str) -> List[str]:
  """Returns name of info files within dir_path."""
  # TODO(tfds): Is there a better filtering scheme which would be more
  # resistant to future modifications (ex: tfrecord => other format)
  return [
      fname for fname in tf.io.gfile.listdir(dir_path)
      if '.tfrecord' not in fname and
      not tf.io.gfile.isdir(os.path.join(dir_path, fname))
  ]
