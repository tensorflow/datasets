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

r"""Beam pipeline which compute the number of examples in the given tfrecord."""

import collections
import dataclasses
import functools
import itertools
import os
import pprint
from typing import cast, Dict, List, Optional, Type

from etils import epath
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.proto import dataset_info_pb2

from google.protobuf import json_format

_SplitFilesDict = Dict[str, List[naming.FilenameInfo]]


@dataclasses.dataclass
class _ShardInfo:
  """Metadata computed for each shard."""
  file_info: naming.FilenameInfo
  num_examples: int
  bytes_size: int


def compute_split_info_from_directory(
    *,
    out_dir: Optional[epath.PathLike] = None,
    data_dir: epath.PathLike,
) -> List[split_lib.SplitInfo]:
  """Compute the split info for the split in the given data dir."""
  # Get the dataset name and filetype suffix from the files in the data dir.
  data_dir = epath.Path(data_dir)
  split_files = next(iter(_extract_split_files(data_dir).values()))
  split_file = split_files[0]
  filename_template = naming.ShardedFileTemplate(
      data_dir=data_dir,
      dataset_name=split_file.dataset_name,
      filetype_suffix=split_file.filetype_suffix)
  return compute_split_info(
      out_dir=out_dir, filename_template=filename_template)


def compute_split_info(
    *,
    out_dir: Optional[epath.PathLike] = None,
    filename_template: naming.ShardedFileTemplate,
) -> List[split_lib.SplitInfo]:
  """Compute the split info on the given files.

  Compute the split info (num shards, num examples,...) metadata required
  by `tfds.folder_dataset.write_metadata`.

  See documentation for usage:
  https://www.tensorflow.org/datasets/external_tfrecord

  Args:
    out_dir: Output directory on which save the metadata. It should be available
      from the apache beam workers. If not set, apache beam won't be used (only
      available with some file formats).
    filename_template: filename template of the splits that contains the dir
      which contains the data.

  Returns:
    split_infos: The list of `tfds.core.SplitInfo`.
  """
  # Auto-detect the splits from the files
  split_files = _extract_split_files(filename_template.data_dir)
  print('Auto-detected splits:')
  for split_name, file_infos in split_files.items():
    print(f' * {split_name}: {file_infos[0].num_shards} shards')

  # Launch the beam pipeline to compute the split info
  if out_dir is not None:
    split_infos = _compute_split_statistics_beam(
        split_files=split_files,
        out_dir=out_dir,
        filename_template=filename_template,
    )
  else:
    raise NotImplementedError('compute_split_info require out_dir kwargs.')

  print('Computed split infos: ')
  pprint.pprint(split_infos)

  return split_infos


def _extract_split_files(data_dir: epath.Path) -> _SplitFilesDict:
  """Extract the files."""
  files = sorted(data_dir.iterdir())
  file_infos = [
      naming.FilenameInfo.from_str(f.name)
      for f in files
      if naming.FilenameInfo.is_valid(f.name)
  ]
  if not file_infos:
    raise ValueError(
        f'No example files detected in {data_dir}. Make sure to follow the '
        'pattern: '
        '`<dataset_name>-<split_name>.<file-extension>-xxxxxx-of-yyyyyy`')

  split_files = collections.defaultdict(list)
  for file_info in file_infos:
    split_files[file_info.split].append(file_info)

  return split_files


def _compute_split_statistics_beam(
    *,
    split_files: _SplitFilesDict,
    out_dir: epath.PathLike,
    filename_template: naming.ShardedFileTemplate,
) -> List[split_lib.SplitInfo]:
  """Compute statistics."""
  out_dir = epath.Path(out_dir)

  assert out_dir.exists(), f'{out_dir} does not exists'

  beam = lazy_imports_lib.lazy_imports.apache_beam

  # Launch the beam pipeline computation
  runner = None
  # Create the global pipeline object common for all splits
  # Disable type_hint as it doesn't works with typing.Protocol
  beam_options = beam.options.pipeline_options.PipelineOptions()
  beam_options.view_as(
      beam.options.pipeline_options.TypeOptions).pipeline_type_check = False
  with beam.Pipeline(runner=runner, options=beam_options) as pipeline:
    for split_name, file_infos in split_files.items():
      _ = pipeline | split_name >> _process_split(  # pylint: disable=no-value-for-parameter
          filename_template=filename_template,
          out_dir=out_dir,
          file_infos=file_infos,  # pytype: disable=missing-parameter
      )

  # After the files have been computed
  return [
      _split_info_from_path(
          filename_template.replace(data_dir=out_dir, split=split))
      for split in split_files
  ]


@lazy_imports_lib.beam_ptransform_fn
def _process_split(
    pipeline,
    *,
    filename_template: naming.ShardedFileTemplate,
    out_dir: epath.Path,
    file_infos: List[naming.FilenameInfo],
):
  """Process a single split."""
  beam = lazy_imports_lib.lazy_imports.apache_beam

  # Use unpack syntax on set to implicitly check that all values are the same
  split_name, = {f.split for f in file_infos}

  # Check that all the file-info from the given split are consistent
  # (no missing file)
  shard_ids = sorted(f.shard_index for f in file_infos)
  num_shards, = {f.num_shards for f in file_infos}
  assert shard_ids == list(range(num_shards)), 'Missing shard files.'

  # Check that the file extension is correct.
  file_suffix, = {f.filetype_suffix for f in file_infos}
  file_format = file_adapters.file_format_from_suffix(file_suffix)
  adapter = file_adapters.ADAPTER_FOR_FORMAT[file_format]
  data_dir = epath.Path(filename_template.data_dir)

  # Build the pipeline to process one split
  return (pipeline
          | beam.Create(file_infos)
          | beam.Map(_process_shard, data_dir=data_dir, adapter=adapter)
          # Group everything in a single elem (_ShardInfo -> List[_ShardInfo])
          | _group_all()  # pytype: disable=missing-parameter  # pylint: disable=no-value-for-parameter
          | beam.Map(_merge_shard_info, filename_template=filename_template)
          | beam.Map(_split_info_to_json_str)
          | beam.io.WriteToText(  # pytype: disable=missing-parameter
              os.fspath(out_dir / _out_filename(split_name)),
              num_shards=1,
              shard_name_template='',
          ))


@lazy_imports_lib.beam_ptransform_fn
def _group_all(pipeline):
  beam = lazy_imports_lib.lazy_imports.apache_beam
  # We do not use CombineGlobally(_process_shard) as it might be called
  # recursively. We want `_process_shard` to be called only once on the full
  # collection.
  return (pipeline
          | beam.GroupBy(lambda x: None)
          | beam.MapTuple(lambda key, x: x))


def _process_shard(
    file_info: naming.FilenameInfo,
    *,
    data_dir: epath.Path,
    adapter: Type[file_adapters.FileAdapter],
) -> _ShardInfo:
  """Process a single `.tfrecord` file."""
  # Load the ds
  ds = adapter.make_tf_data(data_dir / str(file_info))
  num_examples = 0
  bytes_size = 0
  for ex in ds:
    num_examples += 1
    bytes_size += len(ex._numpy())  # pylint: disable=protected-access
  return _ShardInfo(
      file_info=file_info,
      num_examples=num_examples,
      bytes_size=bytes_size,
  )


def _merge_shard_info(
    shard_infos: List[_ShardInfo],
    filename_template: naming.ShardedFileTemplate,
) -> split_lib.SplitInfo:
  """Merge all shard info from one splits and returns the SplitInfo.

  Args:
    shard_infos: The shard infos from all shards.
    filename_template: filename template of the splits.

  Returns:
    The json SplitInfo proto
  """
  split_name, = {s.file_info.split for s in shard_infos}
  shard_infos = sorted(shard_infos, key=lambda s: s.file_info.shard_index)
  filename_template = filename_template.replace(split=split_name)
  return split_lib.SplitInfo(
      name=split_name,
      shard_lengths=[s.num_examples for s in shard_infos],
      num_bytes=sum(s.bytes_size for s in shard_infos),
      filename_template=filename_template,
  )


def _split_info_to_json_str(split_info: split_lib.SplitInfo) -> str:
  proto = split_info.to_proto()
  return json_format.MessageToJson(proto, sort_keys=True)


def _out_filename(split_name: str) -> str:
  return f'{split_name}-info.json'


def _split_info_from_path(
    filename_template: naming.ShardedFileTemplate,) -> split_lib.SplitInfo:
  """Load the split info from the path."""
  path = filename_template.data_dir / _out_filename(filename_template.split)
  json_str = path.read_text()
  proto = json_format.Parse(json_str, dataset_info_pb2.SplitInfo())
  return split_lib.SplitInfo.from_proto(
      proto, filename_template=filename_template.replace(split=proto.name))


def split_infos_from_path(
    split_names: List[str],
    filename_template: naming.ShardedFileTemplate,
) -> List[split_lib.SplitInfo]:
  """Restore the split info from a directory."""
  return [
      _split_info_from_path(
          filename_template=filename_template.replace(split=split_name))
      for split_name in split_names
  ]
