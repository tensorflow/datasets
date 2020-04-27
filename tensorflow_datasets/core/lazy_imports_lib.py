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
"""Lazy imports for heavy dependencies."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import importlib
import sys
import types

from tensorflow_datasets.core.utils import py_utils as utils

_ERR_MSG = ("Failed importing {name}. This likely means that the dataset "
            "requires additional dependencies that have to be "
            "manually installed (usually with `pip install {name}`). See "
            "setup.py extras_require.")

# `lazy_imports` currently only allow the following external dependencies to
# be used during dataset generation.
_ALLOWED_LAZY_DEPS = [
    "apache_beam",
    "crepe",
    "cv2",
    "h5py",
    "langdetect",
    "librosa",
    "matplotlib",
    "matplotlib.pyplot",
    "mwparserfromhell",
    "nltk",
    "pandas",
    "PIL_Image",
    "pretty_midi",
    "pydub",
    "scipy",
    "skimage",
    "tensorflow_io",
    "tldextract",
    "os",
    # "test_foo",
]


def _try_import(module_name):
  """Try importing a module, with an informative error message on failure."""
  try:
    mod = importlib.import_module(module_name)
    return mod
  except ImportError:
    err_msg = _ERR_MSG.format(name=module_name)
    utils.reraise(suffix=err_msg)


class FakeModule(types.ModuleType):
  """A fake module which raise ImportError whenever an unknown attribute is accessed"""
  def __init__(self, name):
    self.__path__ = None
    super(FakeModule, self).__init__(name)

  def __getattr__(self, attr):
    err_msg = _ERR_MSG.format(name=self.__name__)
    raise ImportError(err_msg)


class LazyImporterHook(object):
  """Finder and Loader for modules in `_ALLOWED_LAZY_DEPS`"""
  # https://www.python.org/dev/peps/pep-0302/#specification-part-2-registering-hooks
  # Each path_hook is called with one argument, the path item.
  # It must raise ImportError if it is unable to handle the path item,
  # and return an importer object if it can handle the path item
  PATH = "FAKE_PATH_TRIGGER"

  def __init__(self, path):
    if path is not self.PATH:
      raise ImportError()

  def find_module(self, fullname):
    # Accept if fullname is present in `_ALLOWED_LAZY_DEPS`, else return None
    if fullname in _ALLOWED_LAZY_DEPS:
      return self
    return None

  def load_module(self, fullname):
    """Load a `FakeModule` if the requested module is not present in sys.modules"""
    if fullname not in sys.modules:
      mod = FakeModule(fullname)
      mod.__loader__ = self
      mod.__path__ = []
      sys.modules[fullname] = mod
    return sys.modules[fullname]

class LazyImporter(object):
  """Lazy importer for heavy dependencies.

  Some datasets require heavy dependencies for data generation. To allow for
  the default installation to remain lean, those heavy dependencies are
  lazily imported here.
  """

  @staticmethod
  @contextlib.contextmanager
  def lazy_importer():
    """Context Manager for lazy_imports.

    Fake Module is created if the lazy import is not present in `sys.modules`.
    A fake module is created only if module_name is present in `_ALLOWED_LAZY_DEPS`.
    """
    try:
      sys.path_hooks.append(LazyImporterHook)
      sys.path.append(LazyImporterHook.PATH)
      yield
    except ImportError as err:
      err_msg = ("Unknown import {name}. Currently lazy_imports does not "
                 "support {name} module. If you believe this is correct, "
                 "please add it to the list of `_ALLOWED_LAZY_DEPS` in "
                 "`tfds/core/lazy_imports_lib.py`".format(name=err.name))
      utils.reraise(suffix=err_msg)
    finally:
      sys.path_hooks.remove(LazyImporterHook)
      sys.path.remove(LazyImporterHook.PATH)

  @utils.classproperty
  @classmethod
  def apache_beam(cls):
    return _try_import("apache_beam")

  @utils.classproperty
  @classmethod
  def crepe(cls):
    return _try_import("crepe")

  @utils.classproperty
  @classmethod
  def cv2(cls):
    return _try_import("cv2")  # pylint: disable=unreachable

  @utils.classproperty
  @classmethod
  def h5py(cls):
    return _try_import("h5py")

  @utils.classproperty
  @classmethod
  def langdetect(cls):
    return _try_import("langdetect")

  @utils.classproperty
  @classmethod
  def librosa(cls):
    return _try_import("librosa")

  @utils.classproperty
  @classmethod
  def matplotlib(cls):
    _try_import("matplotlib.pyplot")
    return _try_import("matplotlib")

  @utils.classproperty
  @classmethod
  def mwparserfromhell(cls):
    return _try_import("mwparserfromhell")

  @utils.classproperty
  @classmethod
  def nltk(cls):
    return _try_import("nltk")

  @utils.classproperty
  @classmethod
  def pandas(cls):
    return _try_import("pandas")

  @utils.classproperty
  @classmethod
  def PIL_Image(cls):  # pylint: disable=invalid-name
    # TiffImagePlugin need to be activated explicitly on some systems
    # https://github.com/python-pillow/Pillow/blob/5.4.x/src/PIL/Image.py#L407
    _try_import("PIL.TiffImagePlugin")
    return _try_import("PIL.Image")

  @utils.classproperty
  @classmethod
  def pretty_midi(cls):
    return _try_import("pretty_midi")

  @utils.classproperty
  @classmethod
  def pydub(cls):
    return _try_import("pydub")

  @utils.classproperty
  @classmethod
  def scipy(cls):
    _try_import("scipy.io")
    _try_import("scipy.ndimage")
    return _try_import("scipy")

  @utils.classproperty
  @classmethod
  def skimage(cls):
    _try_import("skimage.color")
    _try_import("skimage.filters")
    _try_import("skimage.external.tifffile")
    return _try_import("skimage")

  @utils.classproperty
  @classmethod
  def tensorflow_io(cls):
    return _try_import("tensorflow_io")

  @utils.classproperty
  @classmethod
  def tldextract(cls):
    return _try_import("tldextract")

  @utils.classproperty
  @classmethod
  def os(cls):
    """For testing purposes only."""
    return _try_import("os")

  @utils.classproperty
  @classmethod
  def test_foo(cls):
    """For testing purposes only."""
    return _try_import("test_foo")


lazy_imports = LazyImporter  # pylint: disable=invalid-name
