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

r"""Library to convert a dataset from one file format to another."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping, Sequence
import dataclasses
import functools
import os
import re
from typing import Callable, Type

from etils import epy

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  import concurrent.futures
  import tqdm

  from absl import logging
  import apache_beam as beam
  from etils import epath
  import tensorflow as tf
  from tensorflow_datasets.core import constants
  from tensorflow_datasets.core import dataset_info as dataset_info_lib
  from tensorflow_datasets.core import file_adapters
  from tensorflow_datasets.core import naming
  from tensorflow_datasets.core import splits as splits_lib
  from tensorflow_datasets.core.proto import dataset_info_pb2
  from tensorflow_datasets.core.utils import file_utils
  from tensorflow_datasets.core.utils import py_utils
  from tensorflow_datasets.core.utils import type_utils

  # pylint: enable=g-import-not-at-top


ConvertFn = Callable[[tf.train.Example], bytes]


@dataclasses.dataclass(frozen=True)
class ConvertConfig:
  """Configuration for the conversion of a shard.

  Attributes:
    out_file_format: the format to which the dataset should be converted to.
    in_file_format: the format of the dataset to convert. If `None`, then the
      config is not yet complete.
    convert_fn: optional function to convert a single example.
    overwrite: whether to overwrite existing shards.
    fail_on_error: whether to fail on error when converting a shard or just log
      the error.
    use_beam: whether to use Beam to convert datasets. Useful for big datasets.
    num_workers: number of workers to use when not using Beam. If `use_beam` is
      set, this flag is ignored. If `num_workers=1`, the conversion will be done
      sequentially.
    in_file_adapter: file adapter for the `in_file_format`.
    out_file_adapter: file adapter for the `out_file_format`.
  """

  out_file_format: file_adapters.FileFormat
  in_file_format: file_adapters.FileFormat | None = None
  convert_fn: ConvertFn | None = None
  overwrite: bool = False
  fail_on_error: bool = False
  use_beam: bool = False
  num_workers: int = 8

  @property
  def in_file_adapter(self) -> Type[file_adapters.FileAdapter]:
    if self.in_file_format is None:
      raise ValueError('in_file_format must be set!')
    return file_adapters.ADAPTER_FOR_FORMAT[self.in_file_format]

  @property
  def out_file_adapter(self) -> Type[file_adapters.FileAdapter]:
    return file_adapters.ADAPTER_FOR_FORMAT[self.out_file_format]

  def with_in_file_format(
      self, in_file_format: str | file_adapters.FileFormat
  ) -> ConvertConfig:
    """Returns a new config with the given `in_file_format`."""
    in_file_format = file_adapters.FileFormat(in_file_format)
    return dataclasses.replace(self, in_file_format=in_file_format)


@dataclasses.dataclass(frozen=True)
class ShardInstruction:
  """Instruction for how one single shard should be converted."""

  in_path: epath.Path
  out_path: epath.Path
  config: ConvertConfig

  def convert(self) -> epath.Path | None:
    """Converts the shard to the desired file format.

    Returns:
      The path of the converted shard or `None` if the shard was not converted.

    Raises:
      Exception: if the shard conversion failed and `config.fail_on_error` is
        `True`, else logs the error.
    """

    def read_in() -> Iterator[type_utils.KeySerializedExample]:
      in_dataset = self.config.in_file_adapter.make_tf_data(
          filename=self.in_path
      )
      for i, row in tqdm.tqdm(
          enumerate(in_dataset),
          unit=' examples',
          desc=f'Shard {self.in_path.name}',
      ):
        if self.config.convert_fn is not None:
          yield i, self.config.convert_fn(row)
        else:
          yield i, row.numpy()

    try:
      with py_utils.incomplete_file(self.out_path) as tmp_file:
        self.config.out_file_adapter.write_examples(
            path=tmp_file, iterator=read_in()
        )
      return self.out_path
    except Exception as e:  # pylint: disable=broad-except
      if self.config.fail_on_error:
        raise e
      else:
        logging.exception(
            'Failed to convert shard %s (format=%s) to %s (format=%s)!',
            self.in_path,
            self.config.in_file_adapter.FILE_SUFFIX,
            self.out_path,
            self.config.out_file_adapter.FILE_SUFFIX,
        )


def _shard_instructions_for_split(
    split_info: splits_lib.SplitInfo,
    out_path: epath.Path,
    convert_config: ConvertConfig,
) -> list[ShardInstruction]:
  """Returns shard instructions for the given split."""

  if split_info.filename_template is None:
    raise ValueError(f'Filename template for split {split_info.name} is empty.')

  in_filename_template = split_info.filename_template
  out_filename_template = in_filename_template.replace(
      data_dir=out_path,
      filetype_suffix=convert_config.out_file_format.file_suffix,
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
            out_path=out_path,
            config=convert_config,
        )
    )
  return instructions


def get_all_shard_instructions(
    info: dataset_info_pb2.DatasetInfo,
    in_path: epath.Path,
    out_path: epath.Path,
    convert_config: ConvertConfig,
) -> list[ShardInstruction]:
  """Returns all shard instructions for the given dataset info."""
  if info.file_format is None:
    raise ValueError('in_file_format must be set!')
  convert_config = convert_config.with_in_file_format(info.file_format)
  shard_instructions = []
  splits_dict = dataset_info_lib.get_split_dict_from_proto(
      dataset_info_proto=info,
      data_dir=in_path,
      file_format=convert_config.in_file_format,
  )
  for split_info in splits_dict.values():
    shard_instructions.extend(
        _shard_instructions_for_split(
            split_info=split_info,
            out_path=out_path,
            convert_config=convert_config,
        )
    )
  return shard_instructions


def _get_root_data_dir(
    in_dir: epath.Path, info: dataset_info_pb2.DatasetInfo
) -> epath.Path:
  in_dir = os.fspath(in_dir)
  if info.config_name:
    parts = [info.name, info.config_name, info.version]
  else:
    parts = [info.name, info.version]
  relative_data_dir = os.path.join(*parts)
  return epath.Path(re.sub(rf'{relative_data_dir}/?$', '', in_dir))


class ConvertMetadataFn(beam.DoFn):
  """Beam DoFn to convert metadata for a single dataset version."""

  def process(
      self,
      count,
      in_dir: epath.Path,
      info: dataset_info_pb2.DatasetInfo,
      out_path: epath.Path,
      convert_config: ConvertConfig,
  ):
    # This is necessary because sometimes `beam.combiners.Count.Globally()`
    # returned an integer and not a pCollection.
    if not isinstance(count, int):
      count = beam.pvalue.AsSingleton(count)
    convert_metadata(
        in_dir=in_dir,
        info=info,
        out_path=out_path,
        convert_config=convert_config,
        num_converted_shards=count,
    )


def convert_metadata(
    in_dir: epath.Path,
    info: dataset_info_pb2.DatasetInfo,
    out_path: epath.Path,
    convert_config: ConvertConfig,
    num_converted_shards: int | None = None,
) -> None:
  """Converts all metadata to the converted dataset.

  Args:
    in_dir: folder that contains the dataset to convert.
    info: dataset info of the dataset to convert.
    out_path: folder where the converted dataset should be stored.
    convert_config: configuration for the conversion.
    num_converted_shards: number of shards that were successfully converted,
      which is used to check that the conversion was successful. If part of a
      beam pipeline, this comes from `beam.combiners.Count.Globally()`.
  """
  splits_dict = dataset_info_lib.get_split_dict_from_proto(
      dataset_info_proto=info,
      data_dir=in_dir,
      file_format=convert_config.out_file_format,
  )

  missing_shards_per_split = {}
  for split_info in splits_dict.values():
    num_available_shards = len(
        split_info.get_available_shards(
            out_path, file_format=convert_config.out_file_format
        )
    )
    if num_converted_shards != num_available_shards:
      logging.warning(
          'Amount of converted shards calculated during conversion (%d) does'
          ' not match the amount of available shards in the data dir (%d) for'
          ' split %s.'
      )
    if num_available_shards < split_info.num_shards:
      missing_shards_per_split[split_info.name] = (
          num_available_shards,
          split_info.num_shards,
      )
      error_message = (
          (
              f'Found {num_available_shards} shards for split'
              f' {split_info.name}, but expected'
              f' {split_info.num_shards} shards.'
          ),
      )
      if convert_config.fail_on_error:
        raise ValueError(error_message)
      else:
        logging.warning(error_message)

    elif num_available_shards > split_info.num_shards:
      raise ValueError(
          f'Found more shards ({num_available_shards}) for split'
          f' {split_info.name}, but expected only'
          f' {split_info.num_shards} shards.'
      )

  if in_dir == out_path:
    if missing_shards_per_split:
      missing_shard_info = [
          f'split {name}: {available} / {total} shards'
          for name, (available, total) in missing_shards_per_split.items()
      ]
      logging.error(
          'Skipping updating metadata in %s because shards are missing: %s',
          os.fspath(in_dir),
          ', '.join(missing_shard_info),
      )
      return

    # File format was added to an existing dataset.
    # Add the file format to `alternative_file_formats` field.
    if convert_config.out_file_format not in info.alternative_file_formats:
      info.alternative_file_formats.append(convert_config.out_file_format.value)
      dataset_info_lib.write_dataset_info_proto(info, dataset_info_dir=out_path)
    else:
      logging.info(
          'File format %s is already an alternative file format of the dataset'
          ' in %s. Skipping updating metadata..',
          convert_config.out_file_format.value,
          os.fspath(in_dir),
      )
    return

  # Copy all json files except dataset_info.json because it needs to be updated.
  # Even if there are missing shards, it's better to copy the metadata than not
  # copying it at all.
  for json_file in in_dir.glob('*.json'):
    if json_file.name == constants.DATASET_INFO_FILENAME:
      continue
    out_file = out_path / json_file.name
    if out_file.exists():
      logging.info(
          'Not copying %s because it already exists.', os.fspath(json_file)
      )
    else:
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
  dataset_info_lib.add_tfds_data_source_access(
      dataset_info_proto=info,
      dataset_reference=in_dataset_reference,
  )
  info.file_format = convert_config.out_file_format.value
  dataset_info_lib.write_dataset_info_proto(info, dataset_info_dir=out_path)


def _convert_dataset(
    info: dataset_info_pb2.DatasetInfo,
    dataset_dir: epath.Path,
    out_dir: epath.Path,
    convert_config: ConvertConfig,
    pipeline: beam.Pipeline | None = None,
) -> None:
  """Converts a single dataset version to the given file format."""
  logging.info(
      'Converting shards in %s to %s, saving in %s.',
      dataset_dir,
      convert_config.out_file_format.value,
      out_dir,
  )
  if dataset_dir != out_dir:
    if convert_config.overwrite:
      out_dir.unlink(missing_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

  shard_instructions = get_all_shard_instructions(
      info=info,
      in_path=dataset_dir,
      out_path=out_dir,
      convert_config=convert_config,
  )

  if not shard_instructions:
    logging.warning(
        'No shard instructions found for %s. This could mean that all shards'
        ' were already converted',
        dataset_dir,
    )
    return
  else:
    logging.info('Found %d shards to convert.', len(shard_instructions))

  if pipeline is not None:
    converted_shards = (
        pipeline
        | f'CreateShardInstructions for {dataset_dir}'
        >> beam.Create(shard_instructions)
        | f'ConvertShards for {dataset_dir}'
        >> beam.Map(lambda shard_instruction: shard_instruction.convert())
        | f'Filter out shards that were not successfully converted for {dataset_dir}'
        >> beam.Filter(lambda shard_instruction: shard_instruction is not None)
    )
    count_shards = (
        converted_shards
        | f'CountConvertedShards for {dataset_dir}'
        >> beam.combiners.Count.Globally()
    )
    _ = count_shards | f'ConvertMetadata for {dataset_dir}' >> beam.ParDo(
        ConvertMetadataFn(),
        in_dir=dataset_dir,
        info=info,
        out_path=out_dir,
        convert_config=convert_config,
    )

  else:
    converted_shards = 0
    for shard_instruction in tqdm.tqdm(
        shard_instructions,
        unit=' shards',
        desc=f'Shards in {os.fspath(dataset_dir)}',
    ):
      result = shard_instruction.convert()
      if result is not None:
        converted_shards += 1
    logging.info('Converting metadata in %s.', dataset_dir)
    convert_metadata(
        in_dir=dataset_dir,
        info=info,
        out_path=out_dir,
        convert_config=convert_config,
        num_converted_shards=converted_shards,
    )


def _remove_incomplete_files(path: epath.Path) -> None:
  num_incomplete_files = 0
  for incomplete_file in path.glob(f'*{constants.INCOMPLETE_PREFIX}*'):
    if py_utils.is_incomplete_file(incomplete_file):
      incomplete_file.unlink()
      num_incomplete_files += 1
  logging.info('Removed %d incomplete files.', num_incomplete_files)


def _get_info_for_dirs_to_convert(
    from_dir: epath.Path,
    to_dir: epath.Path,
    out_file_format: file_adapters.FileFormat,
    overwrite: bool,
) -> dataset_info_pb2.DatasetInfo | None:
  """Returns the dataset info for the given dataset dirs."""
  try:
    dataset_info_proto = dataset_info_lib.read_proto_from_builder_dir(from_dir)
  except Exception:  # pylint: disable=broad-except
    logging.exception('Failed to read dataset info from %s', from_dir)
    return None
  in_file_format = file_adapters.FileFormat(dataset_info_proto.file_format)
  if out_file_format == in_file_format:
    if os.fspath(from_dir) == os.fspath(to_dir):
      logging.warning(
          'The file format to convert to (%s) is already the default file'
          ' format of the dataset in %s, and no different output folder is'
          ' specified. Skipping conversion.',
          out_file_format.value,
          os.fspath(from_dir),
      )
      return None
    else:
      logging.info(
          'The file format to convert to (%s) is the same as the default file'
          ' format, but the converted output is being written to a different'
          ' folder. The shards will be converted anyway from: %s, to: %s',
          out_file_format.value,
          os.fspath(from_dir),
          os.fspath(to_dir),
      )
      return dataset_info_proto
  if out_file_format.file_suffix in dataset_info_proto.alternative_file_formats:
    if overwrite:
      logging.warning(
          'The file format to convert to (%s) is already an alternative file'
          ' format for the dataset in %s. Overwriting the shards!',
          out_file_format.value,
          os.fspath(from_dir),
      )
    elif os.fspath(from_dir) == os.fspath(to_dir):
      logging.info(
          'The file format to convert to (%s) is already an alternative file'
          ' format of the dataset in %s. Converting missing shards if present.',
          os.fspath(from_dir),
          out_file_format.value,
      )
    else:
      logging.warning(
          'The file format to convert to (%s) is already an alternative file'
          ' format, but the converted output is being written to a different'
          ' folder, so the shards will be converted anyway. From: %s, to: %s',
          out_file_format.value,
          os.fspath(from_dir),
          os.fspath(to_dir),
      )
  else:
    logging.info(
        'The file format to convert to (%s) is not an alternative file format'
        ' of the dataset in %s. Converting the dataset.',
        out_file_format.value,
        os.fspath(from_dir),
    )
  return dataset_info_proto


def _convert_dataset_dirs(
    from_to_dirs: Mapping[epath.Path, epath.Path],
    convert_config: ConvertConfig,
) -> None:
  """Converts all datasets in the given `from_to_dirs` parameter.

  Args:
    from_to_dirs: mapping from specific input dataset folders to the folder
      where the converted dataset should be stored.
    convert_config: configuration for the conversion.
  """
  logging.info('Converting %d datasets.', len(from_to_dirs))
  found_dataset_versions: dict[epath.Path, dataset_info_pb2.DatasetInfo] = {}

  if convert_config.num_workers > 1:

    def _process_get_infos(from_to_dir):
      from_dir, to_dir = from_to_dir
      return from_dir, _get_info_for_dirs_to_convert(
          from_dir=from_dir,
          to_dir=to_dir,
          out_file_format=convert_config.out_file_format,
          overwrite=convert_config.overwrite,
      )

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=convert_config.num_workers
    ) as executor:
      for from_dir, info in executor.map(
          _process_get_infos,
          from_to_dirs.items(),
      ):
        if info is not None:
          found_dataset_versions[from_dir] = info
  else:
    for from_dir, to_dir in tqdm.tqdm(
        from_to_dirs.items(), unit=' directories'
    ):
      info = _get_info_for_dirs_to_convert(
          from_dir=from_dir,
          to_dir=to_dir,
          out_file_format=convert_config.out_file_format,
          overwrite=convert_config.overwrite,
      )
      if info is not None:
        found_dataset_versions[from_dir] = info
  convert_dataset_fn = functools.partial(
      _convert_dataset, convert_config=convert_config
  )

  # First convert all shards (with or without Beam), then convert the metadata.
  if convert_config.use_beam:
    runner = None
    with beam.Pipeline(runner=runner) as pipeline:
      for dataset_dir, info in found_dataset_versions.items():
        out_dir = from_to_dirs[dataset_dir]
        convert_dataset_fn(
            info=info,
            dataset_dir=dataset_dir,
            out_dir=out_dir,
            pipeline=pipeline,
        )
  elif convert_config.num_workers > 1:
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=convert_config.num_workers
    ) as executor:
      for dataset_dir, info in found_dataset_versions.items():
        out_dir = from_to_dirs[dataset_dir]
        executor.submit(
            convert_dataset_fn,
            info=info,
            dataset_dir=dataset_dir,
            out_dir=out_dir,
        )
  else:
    for dataset_dir, info in tqdm.tqdm(
        found_dataset_versions.items(), unit=' datasets'
    ):
      out_dir = from_to_dirs[dataset_dir]
      convert_dataset_fn(
          info=info,
          dataset_dir=dataset_dir,
          out_dir=out_dir,
      )

  logging.info(
      'All metadata and shards have been converted. Now removing incomplete'
      ' files.'
  )
  for out_dir in from_to_dirs.values():
    logging.info('Removing incomplete files in %s.', out_dir)
    _remove_incomplete_files(out_dir)


def _create_from_to_dirs(
    references: Iterable[naming.DatasetReference],
    root_in_dir: epath.Path,
    out_path: epath.Path | None,
) -> Mapping[epath.Path, epath.Path]:
  """Returns a mapping from dataset dirs to their corresponding out dirs."""
  from_to_dirs: dict[epath.Path, epath.Path] = {}
  for reference in references:
    dataset_dir = reference.dataset_dir()
    if not out_path:
      out_dir = dataset_dir
    else:
      out_dir = _create_out_dir(
          dataset_dir=dataset_dir,
          root_in_dir=root_in_dir,
          root_out_dir=out_path,
      )
    from_to_dirs[dataset_dir] = out_dir
  return from_to_dirs


def convert_root_data_dir(
    root_data_dir: epath.PathLike,
    out_dir: epath.PathLike | None,
    convert_config: ConvertConfig,
) -> None:
  """Converts all datasets found in the given dataset dir.

  Args:
    root_data_dir: folder that contains one or multiple TFDS datasets, each with
      their own configs and versions.
    out_dir: folder where the converted datasets should be stored. Datasets will
      be stored with the same folder structure as the input folder. If `None`,
      the converted datasets will be stored in the same folder as the input
      datasets.
    convert_config: configuration for the conversion.
  """
  root_data_dir = epath.Path(root_data_dir)
  out_path = epath.Path(out_dir) if out_dir is not None else None

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
      convert_config=convert_config,
  )


def _create_out_dir(
    dataset_dir: epath.Path,
    root_in_dir: epath.Path,
    root_out_dir: epath.Path,
) -> epath.Path:
  """Returns the folder where the data should be written."""
  relative_path = os.fspath(dataset_dir).removeprefix(os.fspath(root_in_dir))
  relative_path = relative_path.removeprefix('/')
  return epath.Path(root_out_dir) / relative_path


def convert_dataset_dir(
    dataset_dir: epath.PathLike,
    out_dir: epath.PathLike | None,
    convert_config: ConvertConfig,
) -> None:
  """Converts all datasets found in the given dataset dir.

  Args:
    dataset_dir: folder that contains a single dataset with all its configs and
      versions.
    out_dir: folder where the converted datasets should be stored. Datasets will
      be stored with the same folder structure as the input folder. If `None`,
      the converted shards will be stored in the same folder as the input
      datasets.
    convert_config: configuration for the conversion.
  """
  dataset_dir = epath.Path(dataset_dir)
  out_path = epath.Path(out_dir) if out_dir is not None else None

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
      convert_config=convert_config,
  )


def convert_dataset(
    out_dir: epath.PathLike | None,
    out_file_format: str | file_adapters.FileFormat,
    root_data_dir: epath.PathLike | None = None,
    dataset_dir: epath.PathLike | None = None,
    dataset_version_dir: (
        epath.PathLike | Sequence[epath.PathLike] | None
    ) = None,
    overwrite: bool = False,
    use_beam: bool = False,
    num_workers: int = 8,
    convert_fn: ConvertFn | None = None,
    fail_on_error: bool = True,
) -> None:
  """Convert a dataset from one file format to another format.

  Note that exactly one of `root_data_dir`, `dataset_dir`, or
  `dataset_version_dir` must be specified.

  Args:
    out_dir: folder where the converted datasets should be stored. Datasets will
      be stored with the same folder structure as the input folder. If `None`,
      the converted shards will be stored in the same folder as the input
      datasets.
    out_file_format: file format to which the dataset should be converted.
    root_data_dir: folder that contains one or multiple TFDS datasets, each with
      their own configs and versions.
    dataset_dir: folder that contains a single dataset with all its configs and
      versions.
    dataset_version_dir: a single or list of folders that each contains a single
      dataset version. If multiple folders are specified, `out_dir` should be
      `None`, since each dataset will be converted in the same folder as the
      input dataset.
    overwrite: whether to overwrite folders in `out_dir` if they already exist.
    use_beam: whether to use Beam to convert datasets. Useful for big datasets.
    num_workers: number of workers to use when not using Beam. If `use_beam` is
      set, this flag is ignored. If `num_workers=1`, the conversion will be done
      sequentially.
    convert_fn: optional function to convert TF examples into whatever is
      desired.
    fail_on_error: whether to fail the entire pipeline when one shard fails to
      convert. When converting an entire root data dir, setting this to `True`
      will fail the entire pipeline if a single shard fails to convert.
  """
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

  convert_config = ConvertConfig(
      overwrite=overwrite,
      out_file_format=out_file_format,
      in_file_format=None,  # Not yet known, will be set later.
      convert_fn=convert_fn,
      fail_on_error=fail_on_error,
      use_beam=use_beam,
      num_workers=num_workers,
  )

  if root_data_dir:
    convert_root_data_dir(
        root_data_dir=root_data_dir,
        out_dir=out_dir,
        convert_config=convert_config,
    )
  elif dataset_dir:
    convert_dataset_dir(
        dataset_dir=dataset_dir,
        out_dir=out_dir,
        convert_config=convert_config,
    )
  elif dataset_version_dir:
    if isinstance(dataset_version_dir, str):
      dataset_version_dir = [dataset_version_dir]

    if len(dataset_version_dir) > 1 and out_dir is not None:
      raise ValueError(
          'If multiple dataset version dirs are specified, `out_dir` must be'
          ' `None`, since each dataset will be converted in the same folder as'
          ' the input dataset.'
      )

    from_to_dirs = {}
    for path in dataset_version_dir:
      if out_dir is None:
        from_to_dirs[epath.Path(path)] = epath.Path(path)
      else:
        from_to_dirs[epath.Path(path)] = epath.Path(out_dir)

    _convert_dataset_dirs(
        from_to_dirs=from_to_dirs,
        convert_config=convert_config,
    )
  else:
    raise ValueError(
        'At least one of `root_data_dir`, `dataset_dir`, or'
        ' `dataset_version_dir` must be specified.'
    )
