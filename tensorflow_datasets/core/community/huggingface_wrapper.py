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

"""Compatibility layer of Hugging Face datasets library."""

from __future__ import annotations

import builtins
import contextlib
import functools
import glob
import os
import sys
import types
from typing import Iterator, NamedTuple, Optional, Union
from unittest import mock

from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import logging as tfds_logging
from tensorflow_datasets.core import split_builder
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

__all__ = [
    'mock_builtin_to_use_gfile',
    'mock_huggingface_import',
]


@contextlib.contextmanager
def mock_huggingface_import() -> Iterator[None]:
  """Patch the HuggingFace datasets module to use TFDS.

  This allow using datasets defined in HG directly in TFDS.

  Usage:

  ```python
  import tensorflow_datasets as tfds

  with tfds.core.community.mock_huggingface_import():
    import datasets  # `datasets` is a _MockedHFDatasets

  # Using `datasets.Xyz` uses the corresponding `tfds.Xyz` API
  class MyDataset(datasets.GeneratorBasedBuilder):
    version = datasets.Version('1.0.0')
    ...

  # This works !!
  ds = tfds.load('my_dataset')
  ```

  Yields:
    None
  """
  # Replace `datasets` module by the TFDS mock
  old_hg_module = sys.modules.get('datasets')
  try:
    sys.modules['datasets'] = _MockedHFDatasets()
    yield
  finally:
    if old_hg_module:
      sys.modules['datasets'] = old_hg_module
    else:
      del sys.modules['datasets']


# Wrappers around `DatasetBuilder` & `DatasetInfo`


class GeneratorBasedBuilder(
    dataset_builder.GeneratorBasedBuilder,
    skip_registration=True,
):
  """Mocked Generator builder."""

  VERSION = utils.Version('1.0.0')

  # TODO(tfds): Support manual_data
  # MANUAL_DOWNLOAD_INSTRUCTIONS = 'Missing instructions.'

  BUILDER_CONFIG_CLASS = dataset_builder.BuilderConfig
  # In HF, default config is explicitly defined
  DEFAULT_CONFIG_NAME = None

  def __init_subclass__(cls, **kwargs):
    # In HF, default config is explicitly defined
    if cls.DEFAULT_CONFIG_NAME:
      if not cls.BUILDER_CONFIGS:
        # If no config is defined, HF implicitly create a
        # default config (e.g. `clickbait_news_bg`)
        cls.BUILDER_CONFIGS = [
            cls.BUILDER_CONFIG_CLASS(name=cls.DEFAULT_CONFIG_NAME)
        ]
      else:
        # Should re-order config so that the first config
        # is the default one
        name_to_configs = {c.name: c for c in cls.BUILDER_CONFIGS}
        new_ordered_configs = [name_to_configs[cls.DEFAULT_CONFIG_NAME]]
        new_ordered_configs.extend(
            config
            for name, config in name_to_configs.items()
            if name != cls.DEFAULT_CONFIG_NAME
        )
        cls.BUILDER_CONFIGS = new_ordered_configs
    super().__init_subclass__(**kwargs)

  @property
  @tfds_logging.builder_info()
  @functools.lru_cache(maxsize=128)
  def info(self) -> dataset_info.DatasetInfo:
    # HF supports Sequences defined as list: {'video': [{'image': Image()}]}
    with _mock_list_as_sequence():
      info = self._info()
    # HF DatasetInfo do not have `builder` args, so we insert
    # here
    return dataset_info.DatasetInfo(builder=self, **info.kwargs)

  @property
  def config(self) -> dataset_builder.BuilderConfig:
    # HF datasets uses `self.config` rather than `self.builder_config`
    return self.builder_config

  def _download_and_prepare(self, *args, **kwargs):
    # * Patch `open` to use the GFile API (to supports GCS)
    # * Patch `Tensor.encode_example` to support `None` strings
    with mock_builtin_to_use_gfile(), _mock_tensor_feature_empty_str():
      return super()._download_and_prepare(*args, **kwargs)


class BeamBasedBuilder(
    GeneratorBasedBuilder,
    dataset_builder.BeamBasedBuilder,
    skip_registration=True,
):
  pass


class DatasetInfo:
  """Wrapper around `DatasetInfo` kwargs."""

  def __init__(self, **kwargs):  # pylint: disable=redefined-builtin
    self.kwargs = kwargs


# Wrapper around the tfds.features


def _make_scalar_feature(dtype: str) -> tf.dtypes.DType:
  """Returns the `tf.dtype` scalar feature."""
  str2val = {
      'bool_': tf.bool,
      'float': tf.float32,
      'double': tf.float64,
      'large_string': tf.string,
      'utf8': tf.string,
  }
  if dtype in str2val:
    return str2val[dtype]
  elif hasattr(tf.dtypes, dtype):
    return getattr(tf.dtypes, dtype)
  else:
    raise ValueError(
        f'Unrecognized type {dtype}. Please open an issue if you think '
        'this is a bug.'
    )


class Value:

  def __new__(cls, dtype):
    return _make_scalar_feature(dtype)


@contextlib.contextmanager
def _mock_tensor_feature_empty_str() -> Iterator[None]:
  """Support `yield {'text': None}`."""

  # Note: We cannot create some custom
  # `class Text(tfds.features.Tensor)` as it would be
  # badly exported when reading from files.

  encode_example_fn = features.Tensor.encode_example

  def new_encode_example(self, example_data):
    if example_data is None and self.dtype == tf.string:
      example_data = ''
    return encode_example_fn(self, example_data)

  with mock.patch.object(features.Tensor, 'encode_example', new_encode_example):
    yield


@contextlib.contextmanager
def _mock_list_as_sequence() -> Iterator[None]:
  """Supports `Sequence` defined as list (e.g. `{'video': [{'frame': ...}]`."""

  to_feature_fn = features.features_dict.to_feature

  def new_to_feature(value):
    if isinstance(value, list):
      (value,) = (
          value  # List should contain a single element  # pylint: disable=self-assigning-variable
      )
      return features.Sequence(value)
    else:
      return to_feature_fn(value)

  # Should this be supported nativelly ?
  with mock.patch.object(features.features_dict, 'to_feature', new_to_feature):
    yield


# Other wrappers


class Version(utils.Version):

  def __init__(
      self,
      version: Union[utils.Version, str],
      description: Optional[str] = None,
  ):
    del description  # Description not used.
    super().__init__(version)
    self.version_str = str(self)  # e.g. used by `compguesswhat`


class _MockedHFDatasets(types.ModuleType):
  """Hugging face API mocked to redirect to TFDS methods."""

  def __init__(self):
    super().__init__('datasets')

  # pylint: disable=invalid-name

  Version = Version
  Split = splits.Split
  SplitGenerator = split_builder.SplitGeneratorLegacy
  DownloadManager = download.DownloadManager

  # dataset_builder.py
  GeneratorBasedBuilder = GeneratorBasedBuilder
  BeamBasedBuilder = BeamBasedBuilder
  BuilderConfig = dataset_builder.BuilderConfig
  DatasetInfo = DatasetInfo

  class features(types.ModuleType):
    """`datasets.features` module."""

    Features = features.FeaturesDict
    Sequence = features.Sequence
    ClassLabel = features.ClassLabel
    Value = Value
    Translation = features.Translation

  class info(types.ModuleType):
    """`datasets.info` module."""

    class SupervisedKeysData(NamedTuple):  # pylint: disable=invalid-namedtuple-arg
      input: str
      output: str

  # pylint: enable=invalid-name


# `datasets.features.Xyz` API can also be accessed as `datasets.Xyz`
for attr in dir(_MockedHFDatasets.features):
  if attr.startswith('_'):
    continue
  setattr(_MockedHFDatasets, attr, getattr(_MockedHFDatasets.features, attr))

# Mock the standard file API to use GFile


def _new_open(*args, encoding=None, **kwargs):
  """Mocked `open`."""
  if encoding and encoding.lower() not in ('utf8', 'utf-8'):
    raise ValueError('Do not support non UTF-8 encoding')
  return tf.io.gfile.GFile(*args, **kwargs)


def _new_pathlib_path_new(cls, *args):
  """Mocked `pathlib.Path.__new__`."""
  del cls
  return epath.Path(*args)


@contextlib.contextmanager
def mock_builtin_to_use_gfile() -> Iterator[None]:
  """Mock the standard library to support GCS access.

  Usage:

  ```python
  with tfds.core.community.mock_builtin_to_use_gfile():
    files = os.listdir('gs://some-bucket')
  ```

  Yields:
    None
  """
  with mock.patch.object(builtins, 'open', _new_open), mock.patch(
      # Patch `__new__` as `Path` might have already be imported as
      # `from pathlib import Path`
      'pathlib.Path.__new__',
      _new_pathlib_path_new,
  ), mock.patch.object(
      os.path, 'exists', tf.io.gfile.exists
  ), mock.patch.object(
      os.path, 'isdir', tf.io.gfile.isdir
  ), mock.patch.object(
      os, 'listdir', tf.io.gfile.listdir
  ), mock.patch.object(
      os, 'walk', tf.io.gfile.walk
  ), mock.patch.object(
      glob, 'glob', tf.io.gfile.glob
  ):
    yield
