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

r"""`tfds build_croissant` command.

Example usage:
```
tfds build_croissant \
  --jsonld=/tmp/croissant.json \
  --record_sets=record1 --record_sets=record2
  --file_format=array_record
  --out_dir=/tmp/foo
  --mapping='{"document.csv": "~/Downloads/document.csv"}"'
```
"""

import argparse
import json
import pathlib

from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core.dataset_builders import croissant_builder


def add_parser_arguments(parser: argparse.ArgumentParser) -> None:
  """Add arguments for `build_croissant` subparser."""
  parser.add_argument(
      '--jsonld',
      type=str,
      help='The Croissant config file for the given dataset.',
      required=True,
  )
  parser.add_argument(
      '--file_format',
      type=str,
      choices=[file_format.value for file_format in file_adapters.FileFormat],
      help='File format to convert the dataset to.',
      required=True,
  )
  parser.add_argument(
      '--record_sets',
      nargs='*',
      help=(
          'The names of the record sets to generate. Each record set will'
          ' correspond to a separate config. If not specified, it will use all'
          ' the record sets'
      ),
  )
  parser.add_argument(
      '--out_dir',
      type=pathlib.Path,
      help='Path where the converted dataset will be stored.',
      required=True,
  )
  parser.add_argument(
      '--mapping',
      type=str,
      help=(
          'Mapping filename->filepath as a Python dict[str, str] to handle'
          ' manual downloads. If `document.csv` is the FileObject and you'
          ' downloaded it to `~/Downloads/document.csv`, you can'
          ' specify`--mapping=\'{"document.csv": "~/Downloads/document.csv"}\''
      ),
  )


def register_subparser(parsers: argparse._SubParsersAction) -> None:
  """Add subparser for `convert_format` command."""
  parser = parsers.add_parser(
      'build_croissant',
      help='Prepares a croissant dataset',
  )
  add_parser_arguments(parser)
  parser.set_defaults(
      subparser_fn=lambda args: prepare_croissant_builder(
          jsonld=args.jsonld,
          record_sets=args.record_sets,
          file_format=args.file_format,
          out_dir=args.out_dir,
          mapping=args.mapping,
      )
  )


def prepare_croissant_builder(
    jsonld: pathlib.Path,
    record_sets: list[str],
    file_format: str,
    out_dir: pathlib.Path,
    mapping: str | None,
) -> None:
  """Creates a Croissant Builder and runs the preparation.

  Args:
    jsonld: The Croissant config file for the given dataset
    record_sets: The names of the record sets to generate. Each record set will
      correspond to a separate config. If not specified, it will use all the
      record sets
    file_format: File format to convert the dataset to.
    out_dir: Path where the converted dataset will be stored.
    mapping: Mapping filename->filepath as a Python dict[str, str] to handle
      manual downloads. If `document.csv` is the FileObject and you downloaded
      it to `~/Downloads/document.csv`, you can specify
      `mapping={"document.csv": "~/Downloads/document.csv"}`.,
  """
  if not record_sets:
    record_sets = None

  if mapping:
    try:
      mapping = json.loads(mapping)
    except json.JSONDecodeError as e:
      raise ValueError(f'Error parsing mapping parameter: {mapping}') from e
  builder = croissant_builder.CroissantBuilder(
      jsonld=jsonld,
      record_set_names=record_sets,
      file_format=file_format,
      data_dir=out_dir,
      mapping=mapping,
  )
  builder.download_and_prepare()
  return
