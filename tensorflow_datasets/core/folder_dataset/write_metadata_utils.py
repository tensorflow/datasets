# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Util to add metadata into an existing dataset folder."""

import types
from typing import List, Union

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.folder_dataset import compute_split_utils
from tensorflow_datasets.core.utils import type_utils


class _WriteBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True):
  """Dummy builder used as base to save metadata."""

  def _info(self):
    return dataset_info.DatasetInfo(builder=self)

  def _split_generators(self, dl_manager):
    return {}

  def _generate_examples(self):
    yield


def write_metadata(
    *,
    data_dir: type_utils.PathLike,
    features: features_lib.FeatureConnector,
    split_infos: Union[None, type_utils.PathLike,
                       List[split_lib.SplitInfo]] = None,
    version: Union[None, str, utils.Version] = None,
    check_data: bool = True,
    **ds_info_kwargs,
) -> None:
  """Add metadata required to load with TFDS.

  See documentation for usage:
  https://www.tensorflow.org/datasets/external_tfrecord

  Args:
    data_dir: Dataset path on which save the metadata
    features: `tfds.features.FeaturesDict` matching the proto specs.
    split_infos: Can be either:  * A path to the pre-computed split info values
      ( the `out_dir` kwarg of `tfds.folder_dataset.compute_split_info`) * A
      list of `tfds.core.SplitInfo` (returned value of
      `tfds.folder_dataset.compute_split_info`) * `None` to auto-compute the
      split info.
    version: Optional dataset version (auto-infer by default, or fallback to
      1.0.0)
    check_data: If True, perform additional check to validate the data in
      data_dir is valid
    **ds_info_kwargs: Additional metadata forwarded to `tfds.core.DatasetInfo` (
      description, homepage,...). Will appear in the doc.
  """
  data_dir = utils.as_path(data_dir)
  # Extract the tf-record filenames
  tfrecord_files = [
      f for f in data_dir.iterdir() if naming.FilenameInfo.is_valid(f.name)
  ]
  if not tfrecord_files:
    raise ValueError(
        f'Could not find tf-record (or compatible format) in {data_dir}. '
        'Make sure to follow the pattern: '
        '`<dataset_name>-<split_name>.<file-extension>-xxxxxx-of-yyyyyy`')

  file_infos = [naming.FilenameInfo.from_str(f.name) for f in tfrecord_files]

  # Use set with tuple expansion syntax to ensure all names are consistents
  snake_name, = {f.dataset_name for f in file_infos}
  camel_name = naming.snake_to_camelcase(snake_name)
  file_format, = {f.filetype_suffix for f in file_infos}
  file_format = file_adapters.file_format_from_suffix(file_format)

  cls = types.new_class(
      camel_name,
      bases=(_WriteBuilder,),
      kwds=dict(skip_registration=True),
      exec_body=None,
  )

  if version is None:  # Automatically detect the version
    if utils.Version.is_valid(data_dir.name):
      version = data_dir.name
    else:
      version = '1.0.0'
  cls.VERSION = utils.Version(version)

  # Create a dummy builder (use non existant folder to make sure
  # dataset_info.json is not restored)
  builder = cls(file_format=file_format, data_dir='/tmp/non-existent-dir/')

  # Create the metadata
  ds_info = dataset_info.DatasetInfo(
      builder=builder,
      features=features,
      **ds_info_kwargs,
  )
  ds_info.set_file_format(file_format)

  # Add the split infos
  split_dict = _load_splits(
      data_dir=data_dir,
      split_infos=split_infos,
      file_infos=file_infos,
      builder=builder,
  )
  ds_info.set_splits(split_dict)

  # Save all metadata (dataset_info.json, features.json,...)
  ds_info.write_to_directory(data_dir)

  # Make sure that the data can be loaded (feature connector match the actual
  # specs)
  if check_data:
    builder = read_only_builder.builder_from_directory(data_dir)
    ds = builder.as_dataset(split=next(iter(builder.info.splits)))
    for _ in ds.take(1):  # Try to load the first example
      pass


def _load_splits(
    *,
    data_dir: utils.ReadWritePath,
    split_infos: Union[None, type_utils.PathLike, List[split_lib.SplitInfo]],
    file_infos: List[naming.FilenameInfo],
    builder: dataset_builder.DatasetBuilder,
) -> split_lib.SplitDict:
  """Load the SplitDict which can be passed to DatasetInfo."""
  split_names = sorted(set(f.split for f in file_infos))

  if split_infos is None:  # Auto-compute the split-infos
    split_infos = compute_split_utils.compute_split_info(data_dir=data_dir)
  # Load the List[SplitInfo]
  elif isinstance(split_infos, type_utils.PathLikeCls):
    split_infos = compute_split_utils.split_infos_from_path(
        path=split_infos,
        split_names=split_names,
    )
  elif all(isinstance(s, split_lib.SplitInfo) for s in split_infos):
    given_splits = sorted([s.name for s in split_infos])
    if given_splits != split_names:
      raise ValueError(f'Splits {given_splits} do not match {split_names}')
  else:
    raise TypeError(f'Invalid split info: {split_infos}')

  split_protos = [s.to_proto() for s in split_infos]
  return split_lib.SplitDict.from_proto(
      repeated_split_infos=split_protos, dataset_name=builder.name)
