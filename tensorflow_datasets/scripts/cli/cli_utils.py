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

"""Utility functions for TFDS CLI."""

import dataclasses
import itertools
import os
import pathlib

from absl import logging
from etils import epath
import simple_parsing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import download
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import file_utils


@dataclasses.dataclass
class DatasetInfo:
  """Structure for common string used for formatting.

  Attributes:
    name: Dataset name (`my_dataset`)
    cls_name: Class name (`MyDataset`)
    path: Root directory in which the dataset is added
    in_tfds: Whether the dataset is added in tensorflow_datasets/ or externally
    tfds_api: The Dataset API to import
    todo: Field to fill (`TODO(my_dataset)`)
    ds_import: Dataset import (`tensorflow_datasets.image.my_dataset`)
    data_format: Optional format of the input data used to generate
      format-specific dataset builders.
  """

  name: str
  in_tfds: bool
  path: pathlib.Path
  cls_name: str = dataclasses.field(init=False)
  tfds_api: str = dataclasses.field(init=False)
  todo: str = dataclasses.field(init=False)
  ds_import: str = dataclasses.field(init=False)
  data_format: str

  def __post_init__(self):
    self.cls_name = naming.snake_to_camelcase(self.name)
    self.tfds_api = (
        'tensorflow_datasets.public_api'
        if self.in_tfds
        else 'tensorflow_datasets'
    )
    self.todo = f'TODO({self.name.lower()})'

    if self.in_tfds:
      # `/path/to/tensorflow_datasets/image/my_dataset`
      # ->`tensorflow_datasets.image.my_dataset`
      import_parts = itertools.dropwhile(
          lambda p: p != 'tensorflow_datasets', self.path.parts
      )
      ds_import = '.'.join(import_parts)
    else:
      # For external datasets, it's difficult to correctly infer the full
      # `from my_module.path.datasets.my_dataset import MyDataset`.
      # Could try to auto-infer the absolute import path from the `setup.py`.
      # Instead uses relative import for now: `from . import my_dataset`
      ds_import = '.'
    self.ds_import = ds_import


def comma_separated_list_field(**kwargs):
  """Returns a field that parses a comma-separated list of values."""
  # Need to manually parse comma-separated list of values, see:
  # https://github.com/lebrice/SimpleParsing/issues/142.
  return simple_parsing.field(
      **kwargs,
      default_factory=list,
      type=lambda value: value.split(','),
      nargs='?',
  )


@dataclasses.dataclass(frozen=True, kw_only=True)
class DebugGroup:
  """--pdb Enter post-mortem debugging mode if an exception is raised.

  Attributes:
    overwrite: Delete pre-existing dataset if it exists.
    fail_if_exists: Fails the program if there is a pre-existing dataset.
    max_examples_per_split: When set, only generate the first X examples
      (default to 1), rather than the full dataset.If set to 0, only execute the
      `_split_generators` (which download the original data), but skip
      `_generator_examples`
  """

  overwrite: bool = False
  fail_if_exists: bool = False
  max_examples_per_split: int = simple_parsing.field(nargs='?', const=1)


@dataclasses.dataclass(frozen=True, kw_only=True)
class PathGroup:
  """Path related arguments.

  Attributes:
    data_dir: Where to place datasets. Default to `~/tensorflow_datasets/` or
      `TFDS_DATA_DIR` environement variable.
    download_dir: Where to place downloads. Default to `<data_dir>/downloads/`.
    extract_dir: Where to extract files. Default to `<download_dir>/extracted/`.
    manual_dir: Where to manually download data (required for some datasets).
      Default to `<download_dir>/manual/`.
    add_name_to_manual_dir: If true, append the dataset name to the `manual_dir`
      (e.g. `<download_dir>/manual/<dataset_name>/`. Useful to avoid collisions
      if many datasets are generated.
  """

  data_dir: epath.Path = simple_parsing.field(
      # Should match tfds.core.constant.DATA_DIR !!
      default_factory=lambda: epath.Path(
          os.environ.get(
              'TFDS_DATA_DIR',
              os.path.join(os.path.expanduser('~'), 'tensorflow_datasets'),
          )
      )
  )
  download_dir: epath.Path | None = None
  extract_dir: epath.Path | None = None
  manual_dir: epath.Path | None = None
  add_name_to_manual_dir: bool = False


@dataclasses.dataclass(frozen=True, kw_only=True)
class GenerationGroup:
  """Generation related arguments.

  Attributes:
    download_only: If True, download all files but do not prepare the dataset.
      Uses the checksum.tsv to find out what to download. Therefore, this does
      not work in combination with --register_checksums.
    config: Config name to build. Build all configs if not set. Can also be a
      json of the kwargs forwarded to the config `__init__` (for custom
      configs).
    config_idx: Config id to build (`builder_cls.BUILDER_CONFIGS[config_idx]`).
      Mutually exclusive with `--config`.
    update_metadata_only: If True, existing dataset_info.json is updated with
      metadata defined in Builder class(es). Datasets must already have been
      prepared.
    download_config: A json of the kwargs forwarded to the config `__init__`
      (for custom DownloadConfigs).
    imports: Comma separated list of module to import to register datasets.
    register_checksums: If True, store size and checksum of downloaded files.
    force_checksums_validation: If True, raise an error if the checksums are not
      found.
    beam_pipeline_options: A (comma-separated) list of flags to pass to
      `PipelineOptions` when preparing with Apache Beam. (see:
      https://www.tensorflow.org/datasets/beam_datasets). Example:
        `--beam_pipeline_options=job_name=my-job,project=my-project`
    file_format: File format to which generate the tf-examples.
    max_shard_size_mb: The max shard size in megabytes.
    num_processes: Number of parallel build processes.
  """

  download_only: bool = False
  config: str | None = simple_parsing.field(default=None, alias='c')
  # We are forced to have 2 flags to avoid ambiguity when config name is a
  # number (e.g. `voc/2017`)
  config_idx: int | None = None
  update_metadata_only: bool = False
  download_config: str | None = None
  imports: list[str] = comma_separated_list_field(alias='i')
  register_checksums: bool = False
  force_checksums_validation: bool = False
  beam_pipeline_options: list[str] = comma_separated_list_field()
  file_format: str | None = simple_parsing.choice(
      *(file_format.value for file_format in file_adapters.FileFormat),
      default=None,
  )
  max_shard_size_mb: int | None = None
  num_processes: int = simple_parsing.field(default=1, alias='num-processes')


@dataclasses.dataclass(frozen=True, kw_only=True)
class PublishGroup:
  # pyformat: disable
  """Options for publishing successfully created datasets.

  Attributes:
    publish_dir: Where to optionally publish the dataset after it has been
      generated successfully. Should be the root data dir under which datasets
      are stored. If unspecified, dataset will not be published
    skip_if_published: If the dataset with the same version and config is
      already published, then it will not be regenerated.
  """
  # pyformat: enable

  publish_dir: epath.Path | None = None
  skip_if_published: bool = False


def download_and_prepare(
    builder: dataset_builder.DatasetBuilder,
    download_config: download.DownloadConfig | None,
    download_dir: epath.Path | None,
    publish_dir: epath.Path | None,
    skip_if_published: bool,
    overwrite: bool,
) -> None:
  """Generate a single builder."""
  dataset = builder.info.full_name
  logging.info('download_and_prepare for dataset %s...', dataset)

  publish_data_dir = publish_dir / dataset if publish_dir else None
  if skip_if_published and publish_data_dir is not None:
    if publish_data_dir.exists():
      logging.info(
          'Dataset already exists in %s. Skipping generation.', publish_data_dir
      )
      return

  builder.download_and_prepare(
      download_dir=download_dir,
      download_config=download_config,
  )

  # Dataset generated successfully
  logging.info('Dataset generation complete...')

  print()
  print(repr(builder.info))
  print()

  # Publish data if requested.
  if publish_data_dir is not None:
    logging.info('Publishing dataset to %s', publish_data_dir)
    file_utils.publish_data(
        from_data_dir=epath.Path(builder.data_dir),
        to_data_dir=publish_data_dir,
        overwrite=overwrite,
    )
    logging.info('Dataset successfully published to %s', publish_data_dir)
