# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
import os
from typing import List, Union

from etils import epath
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.folder_dataset import compute_split_utils


def _get_file_infos(
    filename_template: naming.ShardedFileTemplate,
) -> List[naming.FilenameInfo]:
  """Returns the file infos from the files matching the given template."""
  file_infos = []
  for f in filename_template.data_dir.iterdir():
    file_info = filename_template.parse_filename_info(f.name)
    if file_info is not None:
      file_infos.append(file_info)
  if not file_infos:
    raise ValueError(
        f'Could not find data files in {filename_template.data_dir}. '
        f'Make sure to follow the pattern: `{filename_template.template}`'
    )
  return file_infos


def _construct_filename_template(
    data_dir: epath.PathLike,
    filename_template: Union[None, str, naming.ShardedFileTemplate] = None,
) -> naming.ShardedFileTemplate:
  """Returns a basic filename template based on the given data dir and template."""
  data_dir = epath.Path(data_dir)
  if filename_template is None:
    filename_template = naming.ShardedFileTemplate(
        data_dir=data_dir, template=naming.DEFAULT_FILENAME_TEMPLATE
    )
  elif isinstance(filename_template, str):
    filename_template = naming.ShardedFileTemplate(
        data_dir=data_dir, template=filename_template
    )
  return filename_template.replace(data_dir=data_dir)


def _enrich_filename_template(
    filename_template: naming.ShardedFileTemplate,
    file_infos: List[naming.FilenameInfo],
) -> naming.ShardedFileTemplate:
  """Enriches the given template with data from the given file infos."""
  # Use set with tuple expansion syntax to ensure all names are consistent.
  (dataset_name,) = {f.dataset_name for f in file_infos}
  if (
      filename_template.dataset_name
      and dataset_name
      and filename_template.dataset_name != dataset_name
  ):
    raise ValueError(
        f'Detected dataset name {dataset_name}, but '
        f'{filename_template.dataset_name} was specified '
        'in the filename template!'
    )
  elif dataset_name:
    # dataset_name can be None if the files don't specify the name
    filename_template = filename_template.replace(dataset_name=dataset_name)

  (filetype_suffix,) = {f.filetype_suffix for f in file_infos}
  if (
      filename_template.filetype_suffix
      and filename_template.filetype_suffix != filetype_suffix
  ):
    raise ValueError(
        f'Detected filetype suffix {filetype_suffix}, but '
        f'{filename_template.filetype_suffix} was specified '
        'in the filename template!'
    )
  elif filetype_suffix:
    # filetype_suffix can be None if the files don't specify the name
    filename_template = filename_template.replace(
        filetype_suffix=filetype_suffix
    )

  return filename_template


def write_metadata(
    *,
    data_dir: epath.PathLike,
    features: features_lib.feature.FeatureConnectorArg,
    split_infos: Union[None, epath.PathLike, List[split_lib.SplitInfo]] = None,
    version: Union[None, str, utils.Version] = None,
    filename_template: Union[None, str, naming.ShardedFileTemplate] = None,
    check_data: bool = True,
    **ds_info_kwargs,
) -> None:
  """Add metadata required to load with TFDS.

  See documentation for usage:
  https://www.tensorflow.org/datasets/external_tfrecord

  Args:
    data_dir: Dataset path on which to save the metadata
    features: dict of `tfds.features.FeatureConnector` matching the proto specs.
    split_infos: Can be either:  * A path to the pre-computed split info values
      ( the `out_dir` kwarg of `tfds.folder_dataset.compute_split_info`) * A
      list of `tfds.core.SplitInfo` (returned value of
      `tfds.folder_dataset.compute_split_info`) * `None` to auto-compute the
      split info.
    version: Optional dataset version (auto-infer by default, or fallback to
      1.0.0)
    filename_template: the template for the filenames of the data. If None, then
      the default template `'{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}'` is
      used. A string or a ShardedFileTemplate can be given for custom templates.
    check_data: If True, perform additional check to validate the data in
      data_dir is valid
    **ds_info_kwargs: Additional metadata forwarded to `tfds.core.DatasetInfo` (
      description, homepage,...). Will appear in the doc.
  """
  filename_template = _construct_filename_template(
      data_dir=data_dir, filename_template=filename_template
  )
  file_infos = _get_file_infos(filename_template=filename_template)
  filename_template = _enrich_filename_template(filename_template, file_infos)

  if version is None:  # Automatically detect the version
    if utils.Version.is_valid(filename_template.data_dir.name):
      version = filename_template.data_dir.name
    else:
      version = '1.0.0'

  dataset_identity = dataset_info.DatasetIdentity(
      name=filename_template.dataset_name,
      version=utils.Version(version),
      data_dir=os.fspath(filename_template.data_dir),
      module_name='',
  )

  # Create the metadata
  features = features_lib.features_dict.to_feature(features)
  ds_info = dataset_info.DatasetInfo(
      builder=dataset_identity,
      features=features,
      **ds_info_kwargs,
  )
  file_format = file_adapters.file_format_from_suffix(
      filename_template.filetype_suffix
  )
  ds_info.set_file_format(file_format)

  # Add the split infos
  split_dict = _load_splits(
      split_infos=split_infos,
      file_infos=file_infos,
      filename_template=filename_template,
  )
  ds_info.set_splits(split_dict)

  # Save all metadata (dataset_info.json, features.json,...)
  ds_info.write_to_directory(data_dir)

  # Make sure that the data can be loaded (feature connector matches the actual
  # specs)
  if check_data:
    utils.print_notebook(
        'Metadata written. Testing by reading first example. '
        'Set check_data=False to skip.'
    )
    builder = read_only_builder.builder_from_directory(data_dir)
    split_name = next(iter(builder.info.splits))
    (_,) = builder.as_dataset(
        split=f'{split_name}[:1]'
    )  # Load the first example


def _load_splits(
    *,
    split_infos: Union[None, epath.PathLike, List[split_lib.SplitInfo]],
    file_infos: List[naming.FilenameInfo],
    filename_template: naming.ShardedFileTemplate,
) -> split_lib.SplitDict:
  """Load the SplitDict which can be passed to DatasetInfo."""
  split_names = sorted(set(f.split for f in file_infos))

  if split_infos is None:  # Auto-compute the split-infos
    split_infos = compute_split_utils.compute_split_info(
        filename_template=filename_template
    )
  # Load the List[SplitInfo]
  elif isinstance(split_infos, epath.PathLikeCls):
    split_infos = compute_split_utils.split_infos_from_path(
        split_names=split_names,
        filename_template=filename_template,
    )
  elif all(isinstance(s, split_lib.SplitInfo) for s in split_infos):
    given_splits = sorted([s.name for s in split_infos])
    if given_splits != split_names:
      raise ValueError(f'Splits {given_splits} do not match {split_names}')
  else:
    raise TypeError(f'Invalid split info: {split_infos}')

  split_protos = [s.to_proto() for s in split_infos]
  return split_lib.SplitDict.from_proto(
      repeated_split_infos=split_protos,
      filename_template=filename_template,
  )
