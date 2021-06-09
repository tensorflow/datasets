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

r"""Beam pipeline which compute the number of examples in the given tfrecord.

Compute the split info (num shards, num examples,...) metadata required
by `tfds.core.DatasetInfo`. See documentation and usage at:
https://www.tensorflow.org/datasets/external_tfrecord

"""

import argparse
import collections
import os
import pprint
from typing import Dict, List, Type

from absl import app
from absl.flags import argparse_flags
import apache_beam as beam
import dataclasses
import tensorflow_datasets as tfds
from tensorflow_datasets.core.proto import dataset_info_pb2

from google.protobuf import json_format

_SplitFilesDict = Dict[str, List[tfds.core.naming.FilenameInfo]]


@dataclasses.dataclass
class _ShardInfo:
  """Metadata computed for each shard."""
  file_info: tfds.core.naming.FilenameInfo
  num_examples: int
  bytes_size: int


# Open source pytests globally import all files, so create duplicate FLAGS
# error when using absl.flags. So we use argparse instead.
def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Parse command line flags."""
  parser = argparse_flags.ArgumentParser(
      description='Tensorflow Datasets CLI tool',)
  parser.add_argument(
      '--data_dir',
      type=tfds.core.as_path,
      help='Path to the dataset files.',
  )
  parser.add_argument(
      '--out_dir',
      type=tfds.core.as_path,
      help='Computed metadata will be written here.',
  )
  return parser.parse_args(argv[1:])


def main(args: argparse.Namespace) -> None:

  compute_split_info(data_dir=args.data_dir, out_dir=args.out_dir)


def compute_split_info(
    *,
    data_dir: tfds.core.PathLike,
    out_dir: tfds.core.PathLike,
) -> List[tfds.core.SplitInfo]:
  """Compute the split info on the given files."""
  data_dir = tfds.core.as_path(data_dir)
  out_dir = tfds.core.as_path(out_dir)

  assert out_dir.exists(), f'{out_dir} does not exists'

  # Auto-detect the splits from the files
  split_files = _extract_split_files(data_dir)
  print('Auto-detected splits:')
  for split_name, file_infos in split_files.items():
    print(f' * {split_name}: {file_infos[0].num_shards} shards')

  # Launch the beam pipeline to extract compute the split info
  split_infos = _compute_split_statistics(
      split_files=split_files,
      data_dir=data_dir,
      out_dir=out_dir,
  )

  print('Computed split infos: ')
  pprint.pprint(split_infos)

  return split_infos


def _extract_split_files(data_dir: tfds.core.ReadWritePath,) -> _SplitFilesDict:
  """Extract the files."""
  files = sorted(data_dir.iterdir())
  file_infos = [
      tfds.core.naming.FilenameInfo.from_str(f.name)
      for f in files
      if tfds.core.naming.FilenameInfo.is_valid(f.name)
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


def _compute_split_statistics(
    *,
    split_files: _SplitFilesDict,
    data_dir: tfds.core.ReadWritePath,
    out_dir: tfds.core.ReadWritePath,
) -> List[tfds.core.SplitInfo]:
  """Compute statistics."""

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
          data_dir=data_dir,
          out_dir=out_dir,
          file_infos=file_infos,
      )

  # After the files have been computed
  return [
      _split_info_from_path(out_dir / _out_filename(split_name))
      for split_name in split_files
  ]


@beam.ptransform_fn
def _process_split(
    pipeline: beam.Pipeline,
    *,
    data_dir: tfds.core.ReadWritePath,
    out_dir: tfds.core.ReadWritePath,
    file_infos: List[tfds.core.naming.FilenameInfo],
) -> beam.Pipeline:
  """Process a single split."""
  # Use unpack syntax on set to implicitly check that all values are the same
  split_name, = {f.split for f in file_infos}

  # Check that all the file-info from the given split are consistent
  # (no missing file)
  shard_ids = sorted(f.shard_index for f in file_infos)
  num_shards, = {f.num_shards for f in file_infos}
  assert shard_ids == list(range(num_shards)), 'Missing shard files.'

  # Check that the file extension is correct.
  file_suffix, = {f.filetype_suffix for f in file_infos}
  file_suffix_to_adapter = {
      adapter.FILE_SUFFIX: adapter
      for adapter in tfds.core.file_adapters.ADAPTER_FOR_FORMAT.values()
  }
  if file_suffix not in file_suffix_to_adapter:
    raise ValueError('Unrecognized file extension: Should be one of '
                     f'{file_suffix_to_adapter.values()}')
  adapter = file_suffix_to_adapter[file_suffix]

  # Build the pipeline to process one split
  return (pipeline
          | beam.Create(file_infos)
          | beam.Map(_process_shard, data_dir=data_dir, adapter=adapter)
          # Group everything in a single elem (_ShardInfo -> List[_ShardInfo])
          | _group_all()  # pylint: disable=no-value-for-parameter
          | beam.Map(_merge_shard_info)
          | beam.io.WriteToText(
              os.fspath(out_dir / _out_filename(split_name)),
              num_shards=1,
              shard_name_template='',
          ))


@beam.ptransform_fn
def _group_all(pipeline: beam.Pipeline):
  # We do not use CombineGlobally(_process_shard) as it might be called
  # recursivelly. We want `_process_shard` to be called only once on the full
  # collection.
  return (pipeline
          | beam.GroupBy(lambda x: None)
          | beam.MapTuple(lambda key, x: x))


def _process_shard(
    file_info: tfds.core.naming.FilenameInfo,
    *,
    data_dir: tfds.core.ReadWritePath,
    adapter: Type[tfds.core.file_adapters.FileAdapter],
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


def _merge_shard_info(shard_infos: List[_ShardInfo],) -> str:
  """Merge all shard info from one splits and returns the json.

  Args:
    shard_infos: The shard infos from all shards.

  Returns:
    The json SplitInfo proto
  """
  split_name, = {s.file_info.split for s in shard_infos}
  shard_infos = sorted(shard_infos, key=lambda s: s.file_info.shard_index)
  split_info = tfds.core.SplitInfo(
      name=split_name,
      shard_lengths=[s.num_examples for s in shard_infos],
      num_bytes=sum(s.bytes_size for s in shard_infos),
  )
  proto = split_info.to_proto()
  return json_format.MessageToJson(proto, sort_keys=True)


def _out_filename(split_name: str) -> str:
  return f'{split_name}-info.json'


def _split_info_from_path(path: tfds.core.ReadWritePath) -> tfds.core.SplitInfo:
  """Load the split info from the path."""
  json_str = path.read_text()
  proto = json_format.Parse(json_str, dataset_info_pb2.SplitInfo())
  return tfds.core.SplitInfo.from_proto(proto)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
