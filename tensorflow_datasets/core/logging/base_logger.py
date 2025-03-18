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

"""This module defines the methods a logger implementation should define."""

from __future__ import annotations

from typing import Any

from etils import epy

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from etils import epath
  from tensorflow_datasets.core import decode
  from tensorflow_datasets.core import download as download_lib
  from tensorflow_datasets.core import file_adapters
  from tensorflow_datasets.core import splits as splits_lib
  from tensorflow_datasets.core.logging import call_metadata
  from tensorflow_datasets.core.utils import read_config as read_config_lib
  from tensorflow_datasets.core.utils import type_utils
  # pylint: enable=g-import-not-at-top


TreeDict = type_utils.TreeDict


class Logger:
  """Defines interface any TFDS logger must implement.

  Registered loggers methods are called on TFDS events, synchronously, from the
  same thread the call was made, in sequence, and in registration order.
  Exceptions are *NOT* caught.
  """

  def tfds_import(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      import_time_ms_tensorflow: int,
      import_time_ms_dataset_builders: int,
  ) -> None:
    """Callback called when user calls `import tensorflow_datasets`."""
    pass

  def builder_init(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      data_dir: str | None,
      config: str | None,
      version: str | None,
      is_read_only_builder: bool,
  ) -> None:
    """Callback called when user calls `DatasetBuilder(...)`."""
    pass

  def builder_info(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      config_name: str | None,
      version: str,
      data_path: str,
  ) -> None:
    """Callback called when user calls `builder.info()`."""
    pass

  def as_dataset(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      config_name: str | None,
      version: str,
      data_path: str,
      split: type_utils.Tree[splits_lib.SplitArg] | None,
      batch_size: int | None,
      shuffle_files: bool,
      read_config: read_config_lib.ReadConfig,
      as_supervised: bool,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
  ) -> None:
    """Callback called when user calls `dataset_builder.as_dataset`.

    Callback is also triggered by `tfds.load`, which calls `as_dataset`.
    The logger MUST NOT mutate passed objects (decoders, read_config, ...).

    Args:
      metadata: CallMetadata associated to call.
      name: the name of the dataset. E.g.: "mnist".
      config_name: the name of the config or None.
      version: the dataset version. E.g.: "1.2.3".
      data_path: The path to directory of the dataset loaded. E.g.:
        "/home/alice/.tensorflow_datasets/mnist/1.2.3".
      split: name of the split requested by user. 'all' for all splits.
      batch_size: See DatasetBuilder.as_dataset docstring.
      shuffle_files: -
      read_config: -
      as_supervised: -
      decoders: flatten dict of decoders dict given to `as_dataset`, with the
        values being `{module_name}.{class_name}` instad of a
    """
    pass

  def download_and_prepare(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      config_name: str | None,
      version: str,
      data_path: str,
      download_dir: str | None,
      download_config: download_lib.DownloadConfig | None,
      file_format: str | file_adapters.FileFormat | None,
  ) -> None:
    """Callback called when user calls `dataset_builder.download_and_prepare`."""
    pass

  def as_numpy(self, *, metadata: call_metadata.CallMetadata, dataset: Any):
    """Callback called when user calls `tfds.as_numpy(...)`."""
    pass

  def builder(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      try_gcs: bool | None,
  ) -> None:
    """Callback called when user calls `tfds.builder(...)`."""
    pass

  def dataset_collection(
      self,
      metadata: call_metadata.CallMetadata,
      name: str,
      loader_kwargs: dict[str, Any] | None,
  ) -> None:
    """Callback called when user calls `tfds.dataset_collection(...)`."""
    pass

  def load(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      split: type_utils.Tree[splits_lib.SplitArg] | None,
      data_dir: str | None,
      batch_size: int | None,
      shuffle_files: bool | None,
      download: bool | None,
      as_supervised: bool | None,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
      read_config: read_config_lib.ReadConfig | None,
      with_info: bool | None,
      try_gcs: bool | None,
  ) -> None:
    """Callback called when user calls `tfds.load(...)`."""
    pass

  def list_builders(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      with_community_datasets: bool | None,
  ) -> None:
    """Callback called when user calls `tfds.list_builders(...)`."""
    pass

  def process_ends(self):
    """Called when the process is about to end (atexit)."""
    pass

  def data_source(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      split: type_utils.Tree[splits_lib.SplitArg] | None,
      data_dir: str | None,
      download: bool | None,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
      try_gcs: bool | None,
  ) -> None:
    """Callback called when user calls `tfds.data_source(...)`."""
    pass

  def as_data_source(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      config_name: str | None,
      version: str,
      data_path: str,
      split: type_utils.Tree[splits_lib.SplitArg] | None,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
  ) -> None:
    """Callback called when user calls `dataset_builder.as_data_source(...)`."""
    pass
