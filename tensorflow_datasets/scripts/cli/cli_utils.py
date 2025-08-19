# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

import abc
import argparse
from collections.abc import Callable, Sequence
import dataclasses
import itertools
import pathlib
from typing import TypeVar

from absl import logging
from absl.flags import argparse_flags
from etils import epath
import simple_parsing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import download
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.scripts.utils import flag_utils

_DataclassT = TypeVar('_DataclassT')


class ArgumentParser(
    argparse_flags.ArgumentParser, simple_parsing.ArgumentParser
):
  """An `ArgumentParser` that handles both `simple_parsing` and `absl` flags.

  This class is a workaround for the fact that `simple_parsing.ArgumentParser`
  does not natively handle `absl.flags`. Without this, `absl` flags are not
  correctly parsed, especially when they are mixed with positional arguments,
  leading to errors.

  The `absl.flags.argparse_flags.ArgumentParser` is designed to integrate `absl`
  flags into an `argparse` setup. It does this by dynamically adding all
  defined `absl` flags to the parser instance upon initialization.

  By inheriting from both, we get the features of both:
  - `simple_parsing.ArgumentParser`: Allows defining arguments from typed
    dataclasses.
  - `argparse_flags.ArgumentParser`: Adds support for `absl` flags.

  The Method Resolution Order (MRO) is:
  `ArgumentParser` -> `argparse_flags.ArgumentParser` ->
  `simple_parsing.ArgumentParser` -> `argparse.ArgumentParser` -> `object`.

  This order is important. `argparse_flags.ArgumentParser` is first so that it
  can intercept arguments and handle `absl` flags before they are passed to
  `simple_parsing.ArgumentParser`.
  """

  def parse_known_args(
      self,
      args: Sequence[str] | None = None,
      namespace: argparse.Namespace | None = None,
      attempt_to_reorder: bool = False,
  ):
    # `argparse_flags.ArgumentParser` does not support `attempt_to_reorder` that
    # is used by `simple_parsing.ArgumentParser`. Since we don't need it, we can
    # just ignore it.
    del attempt_to_reorder
    if args:
      args = flag_utils.normalize_flags(args)
    return super().parse_known_args(args, namespace)


def make_flags_parser(
    args_dataclass: type[_DataclassT], description: str
) -> Callable[[list[str]], _DataclassT]:
  """Returns a function that parses flags and returns the dataclass instance."""

  def _parse_flags(argv: list[str]) -> _DataclassT:
    """Command lines flag parsing."""
    parser = ArgumentParser(
        description=description,
        allow_abbrev=False,
    )
    parser.add_arguments(args_dataclass, dest='args')
    return parser.parse_args(argv[1:]).args

  return _parse_flags


@dataclasses.dataclass(frozen=True, kw_only=True)
class Args(abc.ABC):
  """CLI arguments for TFDS CLI commands."""

  @abc.abstractmethod
  def execute(self) -> None:
    """Execute the CLI command."""
    ...


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


@dataclasses.dataclass(frozen=True, kw_only=True)
class DebugOptions:
  """Debug & tests options.

  Attributes:
    overwrite: If True, delete pre-existing dataset if it exists.
    fail_if_exists: If True, fails the program if there is a pre-existing
      dataset.
    max_examples_per_split: When set, only generate the first X examples
      (default to 1), rather than the full dataset. If set to 0, only execute
      the `_split_generators` (which download the original data), but skip
      `_generator_examples`.
  """

  overwrite: bool = simple_parsing.flag(default=False)
  fail_if_exists: bool = simple_parsing.flag(default=False)
  max_examples_per_split: int | None = simple_parsing.field(
      default=None, nargs='?', const=1
  )


@dataclasses.dataclass(frozen=True, kw_only=True)
class PathOptions:
  """Path options.

  Attributes:
    data_dir: Where to place datasets. Defaults to `~/tensorflow_datasets/` or
      `TFDS_DATA_DIR` environement variable.
    download_dir: Where to place downloads. Defaults to `<data_dir>/downloads/`.
    extract_dir: Where to extract files. Defaults to
      `<download_dir>/extracted/`.
    manual_dir: Where to manually download data (required for some datasets).
      Defaults to `<download_dir>/manual/`.
    add_name_to_manual_dir: If true, append the dataset name to the `manual_dir`
      (e.g. `<download_dir>/manual/<dataset_name>/`). Useful to avoid collisions
      if many datasets are generated.
  """

  data_dir: epath.Path = simple_parsing.field(
      default=epath.Path(constants.get_default_data_dir())
  )
  download_dir: epath.Path | None = None
  extract_dir: epath.Path | None = None
  manual_dir: epath.Path | None = None
  add_name_to_manual_dir: bool = simple_parsing.flag(default=False)


@dataclasses.dataclass(frozen=True, kw_only=True)
class GenerationOptions:
  """Generation options.

  Attributes:
    download_only: If True, download all files but do not prepare the dataset.
      Uses the checksum.tsv to find out what to download. Therefore, this does
      not work in combination with --register_checksums.
    config: Config name to build. Build all configs if not set. Can also be a
      json of the kwargs forwarded to the config `__init__` (for custom
      configs).
    config_idx: Config id to build (`builder_cls.BUILDER_CONFIGS[config_idx]`).
      Mutually exclusive with `--config`. We are forced to have 2 flags to avoid
      ambiguity when `config` is a number (e.g. `voc/2017`).
    update_metadata_only: If True, existing dataset_info.json is updated with
      metadata defined in Builder class(es). Datasets must already have been
      prepared.
    download_config: A json of the kwargs forwarded to the config `__init__`
      (for custom DownloadConfigs).
    imports: Comma separated list of module to import to register datasets.
    register_checksums: If True, store size and checksum of downloaded files.
    force_checksums_validation: If True, raise an error if the checksums are not
      found. Otherwise, bypass the checks on the checksums
    beam_pipeline_options: A (comma-separated) list of flags to pass to
      `PipelineOptions` when preparing with Apache Beam. (see:
      https://www.tensorflow.org/datasets/beam_datasets). Example:
        `--beam_pipeline_options=job_name=my-job,project=my-project`
    file_format: File format to which generate the tf-examples.
    max_shard_size_mb: The max shard size in megabytes.
    num_shards: The number of shards to write to.
    num_processes: Number of parallel build processes.
    nondeterministic_order: If True, it will not assure deterministic ordering
      when writing examples to disk. This might result in quicker dataset
      preparation. Otherwise, it will assure deterministic ordering when writing
      examples to disk
  """

  download_only: bool = simple_parsing.flag(default=False)
  config: str | None = simple_parsing.field(default=None, alias='-c')
  config_idx: int | None = simple_parsing.field(
      default=None, alias='--builder_config_id'
  )
  update_metadata_only: bool = simple_parsing.flag(default=False)
  download_config: str | None = None
  imports: str | None = simple_parsing.field(
      default=None, alias=['-i', '--module_import']
  )
  register_checksums: bool = simple_parsing.flag(default=False)
  force_checksums_validation: bool = simple_parsing.flag(default=False)
  beam_pipeline_options: str | None = None
  file_format: str | None = simple_parsing.choice(
      *(file_format.value for file_format in file_adapters.FileFormat),
      default=None,
  )
  max_shard_size_mb: int | None = None
  num_shards: int | None = None
  num_processes: int = simple_parsing.field(default=1, alias='num-processes')
  nondeterministic_order: bool = simple_parsing.flag(default=False)


@dataclasses.dataclass(frozen=True, kw_only=True)
class PublishingOptions:
  """Publishing options.

  Attributes:
    publish_dir: Where to optionally publish the dataset after it has been
      generated successfully. Should be the root data dir under which datasets
      are stored. If unspecified, dataset will not be published.
    skip_if_published: If the dataset with the same version and config is
      already published, then it will not be regenerated.
  """

  publish_dir: epath.Path | None = None
  skip_if_published: bool = simple_parsing.flag(default=False)


@dataclasses.dataclass(frozen=True, kw_only=True)
class AutomationOptions:
  """Automation options.

  Attributes:
    exclude_datasets: If set, generate all datasets except the one defined here.
      Comma separated list of datasets to exclude.
    experimental_latest_version: Build the latest Version(experiments=...)
      available rather than default version.
  """

  exclude_datasets: str | None = None
  experimental_latest_version: bool = simple_parsing.flag(default=False)


def download_and_prepare(
    builder: dataset_builder.DatasetBuilder,
    download_config: download.DownloadConfig | None,
    download_dir: epath.Path | None,
    publish_dir: epath.Path | None,
    skip_if_published: bool,
    overwrite: bool,
    beam_pipeline_options: str | None,
    nondeterministic_order: bool = False,
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

  if not download_config:
    download_config = download.DownloadConfig()
  if overwrite and not download_config.download_mode.overwrite_dataset:
    download_config.download_mode = download.GenerateMode.REUSE_CACHE_IF_EXISTS
  if nondeterministic_order:
    download_config.nondeterministic_order = True

  # Add Apache Beam options to download config.
  try:
    import apache_beam as beam  # pylint: disable=g-import-not-at-top

    if beam_pipeline_options:
      download_config.beam_options = (
          beam.options.pipeline_options.PipelineOptions(
              flags=[f'--{opt}' for opt in beam_pipeline_options.split(',')]
          )
      )
  except ImportError:
    pass

  builder.download_and_prepare(
      download_dir=download_dir,
      download_config=download_config,
  )

  # Dataset generated successfully.
  logging.info('Dataset generation completed...')

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
