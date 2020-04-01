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

from types import ModuleType

import importlib

from tensorflow_datasets.core.utils import py_utils as utils


def _try_import(module_name: str) -> ModuleType:
  """Try importing a module, with an informative error message on failure."""
  try:
    mod = importlib.import_module(module_name)
    return mod
  except ImportError:
    err_msg = ("Failed importing {name}. This likely means that the dataset "
               "requires additional dependencies that have to be "
               "manually installed (usually with `pip install {name}`). See "
               "setup.py extras_require.").format(name=module_name)
    utils.reraise(suffix=err_msg)


class LazyImporter(object):
  """Lazy importer for heavy dependencies.

  Some datasets require heavy dependencies for data generation. To allow for
  the default installation to remain lean, those heavy dependencies are
  lazily imported here.
  """

  @utils.classproperty
  @classmethod
  def apache_beam(cls) -> ModuleType("apache_beam"):
    return _try_import("apache_beam")

  @utils.classproperty
  @classmethod
  def crepe(cls) -> ModuleType("crepe"):
    return _try_import("crepe")

  @utils.classproperty
  @classmethod
  def cv2(cls) -> ModuleType("cv2"):
    return _try_import("cv2")  # pylint: disable=unreachable

  @utils.classproperty
  @classmethod
  def h5py(cls) -> ModuleType("h5py"):
    return _try_import("h5py")

  @utils.classproperty
  @classmethod
  def langdetect(cls) -> ModuleType("langdetect"):
    return _try_import("langdetect")

  @utils.classproperty
  @classmethod
  def librosa(cls) -> ModuleType("librosa"):
    return _try_import("librosa")

  @utils.classproperty
  @classmethod
  def matplotlib(cls) -> ModuleType("matplotlib"):
    return _try_import("matplotlib")

  @utils.classproperty
  @classmethod
  def mwparserfromhell(cls) -> ModuleType("mwparserfromhell"):
    return _try_import("mwparserfromhell")

  @utils.classproperty
  @classmethod
  def nltk(cls) -> ModuleType("nltk"):
    return _try_import("nltk")

  @utils.classproperty
  @classmethod
  def pandas(cls) -> ModuleType("pandas"):
    return _try_import("pandas")

  @utils.classproperty
  @classmethod
  def PIL_Image(cls) -> ModuleType("PIL.Image"):  # pylint: disable=invalid-name
    # TiffImagePlugin need to be activated explicitly on some systems
    # https://github.com/python-pillow/Pillow/blob/5.4.x/src/PIL/Image.py#L407
    _try_import("PIL.TiffImagePlugin")
    return _try_import("PIL.Image")

  @utils.classproperty
  @classmethod
  def pretty_midi(cls) -> ModuleType("pretty_midi"):
    return _try_import("pretty_midi")

  @utils.classproperty
  @classmethod
  def pydub(cls) -> ModuleType("pydub"):
    return _try_import("pydub")

  @utils.classproperty
  @classmethod
  def scipy(cls) -> ModuleType("scipy"):
    _try_import("scipy.io")
    _try_import("scipy.ndimage")
    return _try_import("scipy")

  @utils.classproperty
  @classmethod
  def skimage(cls) -> ModuleType("skimage"):
    _try_import("skimage.color")
    _try_import("skimage.filters")
    _try_import("skimage.external.tifffile")
    return _try_import("skimage")

  @utils.classproperty
  @classmethod
  def tensorflow_io(cls) -> ModuleType("tensorflow_io"):
    return _try_import("tensorflow_io")

  @utils.classproperty
  @classmethod
  def tldextract(cls) -> ModuleType("tldextract"):
    return _try_import("tldextract")

  @utils.classproperty
  @classmethod
  def os(cls) -> ModuleType("os"):
    """For testing purposes only."""
    return _try_import("os")

  @utils.classproperty
  @classmethod
  def test_foo(cls) -> ModuleType("test_foo"):
    """For testing purposes only."""
    return _try_import("test_foo")


lazy_imports = LazyImporter  # pylint: disable=invalid-name
