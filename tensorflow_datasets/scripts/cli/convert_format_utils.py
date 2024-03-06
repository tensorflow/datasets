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

r"""`tfds convert_format` command."""

from collections.abc import Iterable, Iterator, Mapping
import dataclasses
import os
import re
from typing import Type

from absl import logging
from etils import epath
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder as read_only_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam


@dataclasses.dataclass(frozen=True)
class ShardInstruction:
  """Instruction for how one single shard should be converted."""

  in_path: epath.Path
  in_file_adapter: Type[file_adapters.FileAdapter]
  out_path: epath.Path
  out_file_adapter: Type[file_adapters.FileAdapter]

  def convert(self) -> None:
    def read_in() -> Iterator[type_utils.KeySerializedExample]:
      in_dataset = self.in_file_adapter.make_tf_data(filename=self.in_path)
      for i, row in enumerate(in_dataset):
        yield i, row.numpy()

    with py_utils.incomplete_file(self.out_path) as tmp_file:
      self.out_file_adapter.write_examples(path=tmp_file, iterator=read_in())


def _shard_instructions_for_split(
    split_info: splits_lib.SplitInfo,
    out_file_format: file_adapters.FileFormat,
    out_path: epath.Path,
    in_file_adapter: Type[file_adapters.FileAdapter],
    out_file_adapter: Type[file_adapters.FileAdapter],
) -> list[ShardInstruction]:
  """Returns shard instructions for the given split."""

  if split_info.filename_template is None:
    raise ValueError(f'Filename template for split {split_info.name} is empty.')

  in_filename_template = split_info.filename_template
  out_filename_template = in_filename_template.replace(
      data_dir=out_path, filetype_suffix=out_file_format.value
  )
  num_shards = len(split_info.shard_lengths)
  if num_shards <= 0:
    raise ValueError('num_shards must be positive.')

  instructions = []
  existing_files = set(out_filename_template.data_dir.glob('*'))
  for shard_index in range(num_shards):
    out_path = out_filename_template.sharded_filepath(
        shard_index=shard_index, num_shards=num_shards
    )
    if out_path in existing_files:
      logging.info('Skipping %s because it exists.', out_path)
      continue
    in_file_path = in_filename_template.sharded_filepath(
        shard_index=shard_index, num_shards=num_shards
    )
    instructions.append(
        ShardInstruction(
            in_path=in_file_path,
            in_file_adapter=in_file_adapter,
            out_path=out_path,
            out_file_adapter=out_file_adapter,
        )
    )
  return instructions


def get_all_shard_instructions(
    info: dataset_info.DatasetInfo,
    out_file_format: file_adapters.FileFormat,
    out_path: epath.Path,
    in_file_adapter: Type[file_adapters.FileAdapter],
    out_file_adapter: Type[file_adapters.FileAdapter],
) -> list[ShardInstruction]:
  """Returns all shard instructions for the given dataset info."""
  shard_instructions = []
  for split_info in info.splits.values():
    shard_instructions.extend(
        _shard_instructions_for_split(
            split_info=split_info,
            out_file_format=out_file_format,
            out_path=out_path,
            in_file_adapter=in_file_adapter,
            out_file_adapter=out_file_adapter,
        )
    )
  return shard_instructions


def _get_root_data_dir(
    in_dir: epath.Path, info: dataset_info.DatasetInfo
) -> epath.Path:
  in_dir = os.fspath(in_dir)
  if info.config_name:
    parts = [info.name, info.config_name, str(info.version)]
  else:
    parts = [info.name, str(info.version)]
  relative_data_dir = os.path.join(*parts)
  return epath.Path(re.sub(rf'{relative_data_dir}/?$', '', in_dir))


def convert_metadata(
    in_dir: epath.Path,
    info: dataset_info.DatasetInfo,
    out_file_format: file_adapters.FileFormat,
    out_path: epath.Path,
) -> None:
  """Converts all metadata to the converted dataset."""
  # Copy all json files except dataset_info.json because it needs to be updated.
  for json_file in in_dir.glob('*.json'):
    if json_file.name == constants.DATASET_INFO_FILENAME:
      continue
    out_file = out_path / json_file.name
    json_file.copy(out_file)
    logging.info('Copied %s to %s', json_file, out_file)

  # Update dataset info and store it.
  in_dataset_reference = naming.DatasetReference(
      dataset_name=info.name,
      config=info.config_name,
      version=info.version,
      data_dir=os.fspath(_get_root_data_dir(in_dir, info)),
  )
  # Record the source TFDS dataset. Note that existing data source accesses will
  # not be removed.
  info.add_tfds_data_source_access(in_dataset_reference)
  info.as_proto.file_format = out_file_format.value
  info.write_to_directory(out_path)


def _convert_dataset(
    info: dataset_info.DatasetInfo,
    dataset_dir: epath.Path,
    out_dir: epath.Path,
    out_file_format: file_adapters.FileFormat,
    overwrite: bool = False,
    pipeline: beam.Pipeline | None = None,
) -> None:
  """Converts a single dataset version to the given file format."""
  logging.info('Converting shards in %s, saving in %s.', dataset_dir, out_dir)
  if dataset_dir == out_dir:
    raise ValueError(
        f'The dataset dir is the same as the out dir: {dataset_dir=} =='
        f' {out_dir=}'
    )
  if overwrite:
    out_dir.unlink(missing_ok=True)
  out_dir.mkdir(parents=True, exist_ok=True)

  in_file_adapter = file_adapters.ADAPTER_FOR_FORMAT[info.file_format]
  out_file_adapter = file_adapters.ADAPTER_FOR_FORMAT[out_file_format]
  shard_instructions = get_all_shard_instructions(
      info=info,
      out_file_format=out_file_format,
      out_path=out_dir,
      in_file_adapter=in_file_adapter,
      out_file_adapter=out_file_adapter,
  )

  if not shard_instructions:
    logging.warning(
        'No shard instructions found for %s. This could mean that all shards'
        ' were already converted',
        dataset_dir,
    )
    return

  if pipeline is not None:
    _ = (
        pipeline
        | f'CreateShardInstructions for {dataset_dir}'
        >> beam.Create(shard_instructions)
        | f'ConvertShards for {dataset_dir}'
        >> beam.Map(lambda shard_instruction: shard_instruction.convert())
    )

  else:
    for shard_instruction in shard_instructions:
      shard_instruction.convert()


def _remove_incomplete_files(path: epath.Path) -> None:
  num_incomplete_files = 0
  for incomplete_file in path.glob(f'*{constants.INCOMPLETE_PREFIX}*'):
    if py_utils.is_incomplete_file(incomplete_file):
      incomplete_file.unlink()
      num_incomplete_files += 1
  logging.info('Removed %d incomplete files.', num_incomplete_files)


def _convert_dataset_dirs(
    from_to_dirs: Mapping[epath.Path, epath.Path],
    out_file_format: file_adapters.FileFormat,
    overwrite: bool = False,
    use_beam: bool = False,
) -> None:
  """Converts all datasets in the given `from_to_dirs` parameter.

  Args:
    from_to_dirs: mapping from specific input dataset folders to the folder
      where the converted dataset should be stored.
    out_file_format: the format to which the datasets should be converted to.
    overwrite: whether to overwrite the to_dirs if they exist.
    use_beam: whether to use Beam to convert the datasets.
  """
  logging.info('Converting %d datasets.', len(from_to_dirs))

  found_dataset_versions: dict[epath.Path, dataset_info.DatasetInfo] = {}
  for from_dir in from_to_dirs.keys():
    builder = read_only_builder_lib.builder_from_directory(from_dir)
    if out_file_format == builder.info.file_format:
      raise ValueError(
          f'The file format of the dataset ({builder.info.file_format}) is the'
          f' same as the specified out file format! ({out_file_format})'
      )
    found_dataset_versions[from_dir] = builder.info

  # First convert all shards (with or without Beam), then convert the metadata.
  if use_beam:
    runner = None
    with beam.Pipeline(runner=runner) as pipeline:
      for dataset_dir, info in found_dataset_versions.items():
        out_dir = from_to_dirs[dataset_dir]
        _convert_dataset(
            info=info,
            dataset_dir=dataset_dir,
            out_dir=out_dir,
            out_file_format=out_file_format,
            overwrite=overwrite,
            pipeline=pipeline,
        )
  else:
    for dataset_dir, info in found_dataset_versions.items():
      out_dir = from_to_dirs[dataset_dir]
      _convert_dataset(
          info=info,
          dataset_dir=dataset_dir,
          out_dir=out_dir,
          out_file_format=out_file_format,
          overwrite=overwrite,
          pipeline=None,
      )

  logging.info('All shards have been converted. Now converting metadata.')
  for dataset_dir, info in found_dataset_versions.items():
    out_dir = from_to_dirs[dataset_dir]
    logging.info('Converting metadata in %s.', dataset_dir)
    convert_metadata(
        in_dir=dataset_dir,
        info=info,
        out_file_format=out_file_format,
        out_path=out_dir,
    )

  logging.info(
      'All metadata has been converted. Now removing incomplete files.'
  )
  for out_dir in from_to_dirs.values():
    logging.info('Removing incomplete files in %s.', out_dir)
    _remove_incomplete_files(out_dir)


def _create_from_to_dirs(
    references: Iterable[naming.DatasetReference],
    root_in_dir: epath.Path,
    out_path: epath.Path,
) -> Mapping[epath.Path, epath.Path]:
  """Returns a mapping from dataset dirs to their corresponding out dirs."""
  from_to_dirs: dict[epath.Path, epath.Path] = {}
  for reference in references:
    dataset_dir = reference.dataset_dir()
    out_dir = _create_out_dir(
        dataset_dir=dataset_dir,
        root_in_dir=root_in_dir,
        root_out_dir=out_path,
    )
    from_to_dirs[dataset_dir] = out_dir
  return from_to_dirs


def convert_root_data_dir(
    root_data_dir: epath.PathLike,
    out_dir: epath.PathLike,
    out_file_format: str | file_adapters.FileFormat,
    use_beam: bool,
    overwrite: bool = False,
) -> None:
  """Converts all datasets found in the given dataset dir.

  Args:
    root_data_dir: folder that contains one or multiple TFDS datasets, each with
      their own configs and versions.
    out_dir: folder where the converted datasets should be stored. Datasets will
      be stored with the same folder structure as the input folder.
    out_file_format: file format to which the dataset should be converted.
    use_beam: whether to use Beam to convert datasets. Useful for big datasets.
    overwrite: whether to overwrite folders in `out_dir` if they already exist.
  """
  root_data_dir = epath.Path(root_data_dir)
  out_path = epath.Path(out_dir)

  if isinstance(out_file_format, str):
    out_file_format = file_adapters.file_format_from_suffix(out_file_format)

  references = file_utils.list_datasets_in_data_dir(
      data_dir=root_data_dir,
      include_configs=True,
      include_versions=True,
      include_old_tfds_version=True,
  )
  from_to_dirs = _create_from_to_dirs(
      references=references, root_in_dir=root_data_dir, out_path=out_path
  )

  if not from_to_dirs:
    raise ValueError(f'No datasets found in the root data dir {root_data_dir}.')

  _convert_dataset_dirs(
      from_to_dirs=from_to_dirs,
      out_file_format=out_file_format,
      overwrite=overwrite,
      use_beam=use_beam,
  )


def _create_out_dir(
    dataset_dir: epath.PathLike,
    root_in_dir: epath.PathLike,
    root_out_dir: epath.PathLike,
) -> epath.Path:
  """Returns the folder where the data should be written."""
  relative_path = os.fspath(dataset_dir).removeprefix(os.fspath(root_in_dir))
  relative_path = relative_path.removeprefix('/')
  return epath.Path(root_out_dir) / relative_path


def convert_dataset_dir(
    dataset_dir: epath.PathLike,
    out_dir: epath.PathLike,
    out_file_format: file_adapters.FileFormat,
    use_beam: bool,
    overwrite: bool = False,
) -> None:
  """Converts all datasets found in the given dataset dir.

  Args:
    dataset_dir: folder that contains a single dataset with all its configs and
      versions.
    out_dir: folder where the converted datasets should be stored. Datasets will
      be stored with the same folder structure as the input folder.
    out_file_format: file format to which the dataset should be converted.
    use_beam: whether to use Beam to convert datasets. Useful for big datasets.
    overwrite: whether to overwrite folders in `out_dir` if they already exist.
  """
  dataset_dir = epath.Path(dataset_dir)
  out_path = epath.Path(out_dir)

  logging.info(
      'Converting all configs and versions in dataset dir %s, saving to %s.',
      dataset_dir,
      out_dir,
  )

  references = file_utils.list_dataset_variants(
      dataset_dir=dataset_dir,
      include_versions=True,
      include_old_tfds_version=True,
  )
  from_to_dirs = _create_from_to_dirs(
      references=references, root_in_dir=dataset_dir, out_path=out_path
  )

  if not from_to_dirs:
    raise ValueError(f'No datasets found in the dataset dir {dataset_dir}.')

  _convert_dataset_dirs(
      from_to_dirs=from_to_dirs,
      out_file_format=out_file_format,
      overwrite=overwrite,
      use_beam=use_beam,
  )


def convert_dataset(
    out_dir: epath.PathLike,
    out_file_format: str | file_adapters.FileFormat,
    root_data_dir: epath.PathLike | None = None,
    dataset_dir: epath.PathLike | None = None,
    dataset_version_dir: epath.PathLike | None = None,
    overwrite: bool = False,
    use_beam: bool = False,
) -> None:
  """Convert a dataset from one file format to another format."""
  if (
      root_data_dir is None
      and dataset_dir is None
      and dataset_version_dir is None
  ):
    raise ValueError(
        'One of `root_data_dir`, `dataset_dir`, or `dataset_version_dir`'
        ' must be specified.'
    )

  if isinstance(out_file_format, str):
    out_file_format = file_adapters.file_format_from_suffix(out_file_format)

  if root_data_dir:
    convert_root_data_dir(
        root_data_dir=root_data_dir,
        out_dir=out_dir,
        out_file_format=out_file_format,
        use_beam=use_beam,
        overwrite=overwrite,
    )
  elif dataset_dir:
    convert_dataset_dir(
        dataset_dir=dataset_dir,
        out_dir=out_dir,
        out_file_format=out_file_format,
        use_beam=use_beam,
        overwrite=overwrite,
    )
  elif dataset_version_dir:
    from_to_dirs = {epath.Path(dataset_version_dir): epath.Path(out_dir)}
    _convert_dataset_dirs(
        from_to_dirs=from_to_dirs,
        out_file_format=out_file_format,
        overwrite=overwrite,
        use_beam=use_beam,
    )
  else:
    raise ValueError(
        'At least one of `root_data_dir`, `dataset_dir`, or'
        ' `dataset_version_dir` must be specified.'
    )
