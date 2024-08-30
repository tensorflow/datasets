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
  --record_sets=record1,record2 \
  --mapping='{"document.csv": "~/Downloads/document.csv"}"'
```
"""

import dataclasses
import functools
import json

from etils import epath
import mlcroissant as mlc
import simple_parsing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core.dataset_builders import croissant_builder
from tensorflow_datasets.core.utils import croissant_utils
from tensorflow_datasets.scripts.cli import cli_utils


@dataclasses.dataclass(frozen=True, kw_only=True)
class CmdArgs(simple_parsing.helpers.FrozenSerializable):
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
    overwrite_version: Semantic version of the dataset to be set.
  """

  jsonld: epath.Path
  data_dir: epath.Path
  # Need to override the default use of `Enum.name` for choice options.
  file_format: str = simple_parsing.choice(
      *(file_format.value for file_format in file_adapters.FileFormat),
      default=file_adapters.FileFormat.ARRAY_RECORD.value,
  )
  record_sets: list[str] = cli_utils.comma_separated_list_field()
  mapping: str | None = None
  download_dir: epath.Path | None = None
  publish_dir: epath.Path | None = None
  skip_if_published: bool = False
  overwrite: bool = False
  overwrite_version: str | None = None

  @functools.cached_property
  def mapping_json(self) -> dict[str, epath.PathLike]:
    if self.mapping:
      try:
        return json.loads(self.mapping)
      except json.JSONDecodeError as e:
        raise ValueError(
            f'Error parsing mapping parameter: {self.mapping}'
        ) from e
    return {}

  @functools.cached_property
  def dataset(self) -> mlc.Dataset:
    return mlc.Dataset(jsonld=self.jsonld, mapping=self.mapping_json)

  @functools.cached_property
  def dataset_name(self) -> str:
    return croissant_utils.get_dataset_name(self.dataset)

  @functools.cached_property
  def record_set_ids(self) -> list[str]:
    return self.record_sets or croissant_utils.get_record_set_ids(
        self.dataset.metadata
    )

  def execute(self):
    prepare_croissant_builder(self)


def prepare_croissant_builder(args: CmdArgs) -> None:
  """Creates a Croissant Builder and runs the preparation.

  Args:
    args: CLI arguments.
  """
  builder = croissant_builder.CroissantBuilder(
      jsonld=args.jsonld,
      record_set_ids=args.record_set_ids,
      file_format=args.file_format,
      data_dir=args.data_dir,
      mapping=args.mapping_json,
      overwrite_version=args.overwrite_version,
  )

  # Generate each config sequentially.
  for config in builder.BUILDER_CONFIGS:
    builder_for_config = croissant_builder.CroissantBuilder(
        jsonld=args.jsonld,
        record_set_ids=[config.name],
        file_format=args.file_format,
        data_dir=args.data_dir,
        mapping=args.mapping_json,
        overwrite_version=args.overwrite_version,
    )
    cli_utils.download_and_prepare(
        builder=builder_for_config,
        download_config=None,
        download_dir=args.download_dir,
        publish_dir=args.publish_dir,
        skip_if_published=args.skip_if_published,
        overwrite=args.overwrite,
    )
