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

r"""Prepare a Croissant dataset.

Example usage:
```
python tensorflow_datasets/scripts/prepare_croissant.py \
  --jsonld=/tmp/croissant.json \
  --data_dir=/tmp/foo \
  --file_format=array_record \
  --record_sets=record1,record2 \
  --mapping='{"document.csv": "~/Downloads/document.csv"}"'
```
"""

import dataclasses

from absl import app
from etils import eapp
from etils import epath
import simple_parsing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.scripts.cli import croissant


@dataclasses.dataclass
class CmdArgs:
  """CLI arguments for preparing a Croissant dataset.

  Attributes:
    jsonld: Path to the JSONLD file.
    data_dir: Path where the converted dataset will be stored.
    file_format: File format to convert the dataset to.
    record_sets: The names of the record sets to generate. Each record set will
      correspond to a separate config. If not specified, it will use all the
      record sets.
    mapping: Mapping filename->filepath as a Python dict[str, str] to handle
      manual downloads. If `document.csv` is the FileObject and you downloaded
      it to `~/Downloads/document.csv`, you can specify
      `--mapping='{"document.csv": "~/Downloads/document.csv"}'`
    download_dir: Where to place downloads. Default to `<data_dir>/downloads/`.
    publish_dir: Where to optionally publish the dataset after it has been
      generated successfully. Should be the root data dir under which datasets
      are stored. If unspecified, dataset will not be published.
    skip_if_published: If the dataset with the same version and config is
      already published, then it will not be regenerated.
    overwrite: Delete pre-existing dataset if it exists.
  """

  jsonld: epath.PathLike
  data_dir: epath.PathLike
  # Need to override the default use of `Enum.name` for choice options.
  file_format: str = simple_parsing.choice(
      *(file_format.value for file_format in file_adapters.FileFormat),
      default=file_adapters.FileFormat.ARRAY_RECORD.value,
  )
  # Need to manually parse comma-separated list of values, see:
  # https://github.com/lebrice/SimpleParsing/issues/142.
  record_sets: list[str] = simple_parsing.field(
      default_factory=list,
      type=lambda record_sets_str: record_sets_str.split(','),
      nargs='?',
  )
  mapping: str | None = None
  download_dir: epath.PathLike | None = None
  publish_dir: epath.PathLike | None = None
  skip_if_published: bool = False
  overwrite: bool = False

parse_flags = eapp.make_flags_parser(CmdArgs)


def main(args: CmdArgs):
  croissant.prepare_croissant_builder(
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


if __name__ == '__main__':
  app.run(main, flags_parser=parse_flags)
