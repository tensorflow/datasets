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

r"""`tfds convert_format` command.

Example usage:
```
tfds convert_format \
  --dataset_version_dir=/data/dataset/config/1.2.3 \
  --out_file_format=array_record \
  --out_dir=/data_array_record/dataset/config/1.2.3 \
  --use_beam=True
```
"""

import argparse
from collections.abc import Sequence

from etils import epath
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.scripts.cli import convert_format_utils


def add_parser_arguments(parser: argparse.ArgumentParser) -> None:
  """Add arguments for `convert_format` subparser."""
  parser.add_argument(
      '--root_data_dir',
      type=str,
      help=(
          'Root data dir that contains all datasets. All datasets and all their'
          ' configs and versions that are in this folder will be converted.'
      ),
      required=False,
  )
  parser.add_argument(
      '--dataset_dir',
      type=str,
      help=(
          'Path where the dataset to be converted is located. Converts all'
          ' configs and versions in this folder.'
      ),
      required=False,
  )
  parser.add_argument(
      '--dataset_version_dir',
      type=str,
      help=(
          'Path where the dataset to be converted is located. Should include'
          ' config and version. Can also be a comma-separated list of paths. If'
          ' multiple paths are specified, `--out_dir` should not be specified,'
          ' since each dataset will be converted in the same directory as the'
          ' input dataset.'
      ),
      required=False,
  )
  parser.add_argument(
      '--out_file_format',
      type=str,
      choices=[file_format.value for file_format in file_adapters.FileFormat],
      help='File format to convert the dataset to.',
      required=True,
  )
  parser.add_argument(
      '--out_dir',
      type=str,
      help=(
          'Path where the converted dataset will be stored. Should include the'
          ' config and version, e.g. `/data/dataset_name/config/1.2.3`. If not'
          ' specified, the converted shards will be stored in the same'
          ' directory as the input dataset.'
      ),
      default='',
      required=False,
  )
  parser.add_argument(
      '--overwrite',
      action='store_true',
      help='Whether to overwrite the output directory if it already exists.',
  )
  parser.add_argument(
      '--use_beam',
      action='store_true',
      help='Use beam to convert the dataset.',
  )
  parser.add_argument(
      '--num_workers',
      type=int,
      default=8,
      help=(
          'Number of workers to use when not using Beam. If `--use_beam` is'
          ' set, this flag is ignored. If `--num_workers=1`, the conversion'
          ' will be done sequentially.'
      ),
  )
  parser.add_argument(
      '--only_log_errors',
      action='store_true',
      default=False,
      help=(
          'If set, errors during the conversion will be logged as errors and'
          ' will not crash the conversion. If you are converting a large number'
          ' of datasets, you might want to set this flag to true.'
      ),
  )


def register_subparser(parsers: argparse._SubParsersAction) -> None:
  """Add subparser for `convert_format` command."""
  parser = parsers.add_parser(
      'convert_format',
      help='Converts a dataset from one file format to another format.',
  )
  add_parser_arguments(parser)

  def _parse_dataset_version_dir(
      dataset_version_dir: str | None,
  ) -> Sequence[epath.Path] | None:
    if not dataset_version_dir:
      return None
    return [epath.Path(path) for path in dataset_version_dir.split(',')]

  parser.set_defaults(
      subparser_fn=lambda args: convert_format_utils.convert_dataset(
          out_dir=epath.Path(args.out_dir) if args.out_dir else None,
          out_file_format=args.out_file_format,
          dataset_dir=args.dataset_dir or None,
          root_data_dir=args.root_data_dir or None,
          dataset_version_dir=_parse_dataset_version_dir(
              args.dataset_version_dir
          ),
          overwrite=args.overwrite,
          use_beam=args.use_beam,
          num_workers=args.num_workers,
          fail_on_error=not args.only_log_errors,
      )
  )
