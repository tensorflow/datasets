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

r"""`tfds convert_format` command.

Example usage:
```
tfds convert_format \
  --dataset_dir=/data/dataset/config/1.2.3 \
  --out_file_format=array_record \
  --out_dir=/data_array_record/dataset/config/1.2.3 \
  --use_beam=True
```
"""

import argparse
import pathlib

from absl import logging
from etils import epath
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import read_only_builder as read_only_builder_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.scripts.cli import convert_format_utils


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `new` command."""
  new_parser = parsers.add_parser(
      'convert_format',
      help='Converts a dataset from one file format to another format.',
  )
  new_parser.add_argument(
      '--dataset_dir',
      type=str,
      help=(
          'Path where the dataset to be converted is located. Should include'
          ' config and version.'
      ),
      required=True,
  )
  new_parser.add_argument(
      '--out_file_format',
      type=str,
      choices=[file_format.value for file_format in file_adapters.FileFormat],
      help='File format to convert the dataset to.',
      required=True,
  )
  new_parser.add_argument(
      '--out_dir',
      type=pathlib.Path,
      help=(
          'Path where the converted dataset will be stored. Should include the'
          ' config and version, e.g. `/data/dataset_name/config/1.2.3`.'
      ),
      required=True,
  )
  new_parser.add_argument(
      '--use_beam',
      type=bool,
      help='Whether to use beam to convert the dataset.',
  )
  new_parser.set_defaults(subparser_fn=_convert_dataset)


def _convert_dataset(args: argparse.Namespace) -> None:
  """Convert a dataset from one file format to another format."""
  out_path = epath.Path(args.out_dir)
  out_path.mkdir(parents=True, exist_ok=False)

  out_file_format = file_adapters.file_format_from_suffix(args.out_file_format)
  out_file_adapter = file_adapters.ADAPTER_FOR_FORMAT[out_file_format]

  builder = read_only_builder_lib.builder_from_directory(args.dataset_dir)
  if out_file_format == builder.info.file_format:
    raise ValueError(
        f'The file format of the dataset ({builder.info.file_format}) is the'
        f' same as the specified out file format! ({out_file_format})'
    )
  in_file_adapter = file_adapters.ADAPTER_FOR_FORMAT[builder.info.file_format]

  logging.info(
      'Converting dataset in %s from %s to %s.',
      args.dataset_dir,
      builder.info.file_format,
      out_file_format,
  )
  shard_instructions = convert_format_utils.get_all_shard_instructions(
      info=builder.info,
      out_file_format=out_file_format,
      out_path=out_path,
      in_file_adapter=in_file_adapter,
      out_file_adapter=out_file_adapter,
  )
  if args.use_beam:
    runner = None
    with beam.Pipeline(runner=runner) as pipeline:
      _ = (
          pipeline
          | beam.Create(shard_instructions)
          | beam.Reshuffle()
          | beam.Map(lambda shard_instruction: shard_instruction.convert())
      )

  else:
    for shard_instruction in shard_instructions:
      shard_instruction.convert()

  logging.info('Converting metadata in %s.', args.dataset_dir)
  convert_format_utils.convert_metadata(
      info=builder.info, out_file_format=out_file_format, out_path=out_path
  )
  logging.info('Dataset in %s successfully converted.', args.dataset_dir)
