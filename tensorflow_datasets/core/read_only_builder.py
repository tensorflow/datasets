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

"""Load Datasets without reading dataset generation code."""

import os
from typing import Optional, Tuple

import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import utils


class ReadOnlyBuilder(
    dataset_builder.FileReaderBuilder, skip_registration=True
):
  """Generic DatasetBuilder loading from a directory."""

  def __init__(self, builder_dir: str):
    """Constructor.

    Args:
      builder_dir: Directory of the dataset to load (e.g.
        `~/tensorflow_datasets/mnist/3.0.0/`)

    Raises:
      FileNotFoundError: If the builder_dir does not exists.
    """
    builder_dir = os.path.expanduser(builder_dir)
    info_path = os.path.join(builder_dir, dataset_info.DATASET_INFO_FILENAME)
    if not tf.io.gfile.exists(info_path):
      raise FileNotFoundError(
          f'Could not load `ReadOnlyBuilder`: {info_path} does not exists.'
      )

    # Restore name, config, info
    info_proto = dataset_info.read_from_json(info_path)
    self.name = info_proto.name
    if info_proto.config_name:
      builder_config = dataset_builder.BuilderConfig(
          name=info_proto.config_name,
          version=info_proto.version,
          # TODO(tfds): Restore description.
      )
    else:
      builder_config = None
    # __init__ will call _build_data_dir, _create_builder_config,
    # _pick_version to set the data_dir, config, and version
    super().__init__(
        data_dir=builder_dir,
        config=builder_config,
        version=info_proto.version,
    )
    if self.info.features is None:
      raise ValueError(
          f'Cannot restore {self.info.full_name}. It likelly mean the dataset '
          'was generated with an old TFDS version (<=3.2.1).'
      )

  def _create_builder_config(
      self, builder_config: Optional[dataset_builder.BuilderConfig]
  ) -> Optional[dataset_builder.BuilderConfig]:
    return builder_config  # BuilderConfig is created in __init__

  def _pick_version(self, version: str) -> utils.Version:
    return utils.Version(version)

  def _build_data_dir(self, data_dir: str) -> Tuple[str, str]:
    return data_dir, data_dir  # _data_dir_root, _data_dir are builder_dir.

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(builder=self)

  def _download_and_prepare(self, **kwargs):  # pylint: disable=arguments-differ
    # DatasetBuilder.download_and_prepare is a no-op as self.data_dir already
    # exists.
    raise AssertionError('ReadOnlyBuilder can\'t be generated.')


def builder_from_directory(builder_dir: str) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from the given generated dataset path.

  This function reconstruct the `tfds.core.DatasetBuilder` without
  requirering the original generation code.

  It will read the `<builder_dir>/features.json` in order to infer the
  structure (feature names, nested dict,...) and content (image, sequence,...)
  of the dataset. The serialization format is defined in
  `tfds.features.FeatureConnector` in `to_json()`.

  Note: This function only works for datasets generated with TFDS `4.0.0` or
  above.

  Args:
    builder_dir: `str`, path of the directory containing the dataset to read (
      e.g. `~/tensorflow_datasets/mnist/3.0.0/`).

  Returns:
    builder: `tf.core.DatasetBuilder`, builder for dataset at the given path.
  """
  return ReadOnlyBuilder(builder_dir=builder_dir)
