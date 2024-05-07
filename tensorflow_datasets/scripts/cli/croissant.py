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
  --data_dir=/tmp/foo \
  --file_format=array_record \
  --record_sets=record1 --record_sets=record2 \
  --mapping='{"document.csv": "~/Downloads/document.csv"}"'
```
"""

import argparse
from collections.abc import Sequence
import json

from etils import epath
from tensorflow_datasets.core.dataset_builders import croissant_builder
from tensorflow_datasets.scripts.cli import cli_utils


def add_parser_arguments(parser: argparse.ArgumentParser):
  """Add arguments for `build_croissant` subparser."""
  parser.add_argument(
      '--jsonld',
      type=str,
      help='The Croissant config file for the given dataset.',
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
      '--mapping',
      type=str,
      help=(
          'Mapping filename->filepath as a Python dict[str, str] to handle'
          ' manual downloads. If `document.csv` is the FileObject and you'
          ' downloaded it to `~/Downloads/document.csv`, you can'
          ' specify`--mapping=\'{"document.csv": "~/Downloads/document.csv"}\''
      ),
  )

  cli_utils.add_debug_argument_group(parser)
  cli_utils.add_path_argument_group(parser)
  cli_utils.add_generation_argument_group(parser)
  cli_utils.add_publish_argument_group(parser)


def register_subparser(parsers: argparse._SubParsersAction):
  """Add subparser for `convert_format` command."""
  parser = parsers.add_parser(
      'build_croissant',
      help='Prepares a croissant dataset',
  )
  add_parser_arguments(parser)
  parser.set_defaults(
      subparser_fn=lambda args: prepare_croissant_builder(
          jsonld=args.jsonld,
          data_dir=args.data_dir,
          file_format=args.file_format,
          record_sets=args.record_sets,
          mapping=args.mapping,
          download_dir=args.download_dir,
          publish_dir=args.publish_dir,
          skip_if_published=args.skip_if_published,
          overwrite=args.overwrite,
      )
  )


def prepare_croissant_builder(
    jsonld: epath.PathLike,
    data_dir: epath.PathLike,
    file_format: str,
    record_sets: Sequence[str],
    mapping: str | None,
    download_dir: epath.PathLike | None,
    publish_dir: epath.PathLike | None,
    skip_if_published: bool,
    overwrite: bool,
) -> None:
  # pyformat: disable
  """Creates a Croissant Builder and runs the preparation.

  Args:
    jsonld: The Croissant config file for the given dataset
    data_dir: Path where the converted dataset will be stored.
    file_format: File format to convert the dataset to.
    record_sets: The `@id`s of the record sets to generate. Each record set will
      correspond to a separate config. If not specified, it will use all the
      record sets
    mapping: Mapping filename->filepath as a Python dict[str, str] to handle
      manual downloads. If `document.csv` is the FileObject and you downloaded
      it to `~/Downloads/document.csv`, you can specify
      `mapping={"document.csv": "~/Downloads/document.csv"}`.,
    download_dir: Where to place downloads. Default to `<data_dir>/downloads/`.
    publish_dir: Where to optionally publish the dataset after it has been
      generated successfully. Should be the root data dir under which datasets
      are stored. If unspecified, dataset will not be published.
    skip_if_published: If the dataset with the same version and config is
      already published, then it will not be regenerated.
    overwrite: Delete pre-existing dataset if it exists.
  """
  # pyformat: enable
  if not record_sets:
    record_sets = None

  if mapping:
    try:
      mapping = json.loads(mapping)
    except json.JSONDecodeError as e:
      raise ValueError(f'Error parsing mapping parameter: {mapping}') from e

  builder = croissant_builder.CroissantBuilder(
      jsonld=jsonld,
      record_set_ids=record_sets,
      file_format=file_format,
      data_dir=data_dir,
      mapping=mapping,
  )
  cli_utils.download_and_prepare(
      builder=builder,
      download_config=None,
      download_dir=epath.Path(download_dir) if download_dir else None,
      publish_dir=epath.Path(publish_dir) if publish_dir else None,
      skip_if_published=skip_if_published,
      freeze_files=freeze_files,
      overwrite=overwrite,
  )
