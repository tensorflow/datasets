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

import argparse
import dataclasses
import itertools
import os
import pathlib

from absl import logging
from etils import epath
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


def add_debug_argument_group(parser: argparse.ArgumentParser):
  """Adds debug argument group to the parser."""
  debug_group = parser.add_argument_group(
      'Debug & tests',
      description=(
          '--pdb Enter post-mortem debugging mode if an exception is raised.'
      ),
  )
  debug_group.add_argument(
      '--overwrite',
      action='store_true',
      help='Delete pre-existing dataset if it exists.',
  )
  debug_group.add_argument(
      '--fail_if_exists',
      action='store_true',
      default=False,
      help='Fails the program if there is a pre-existing dataset.',
  )
  debug_group.add_argument(
      '--max_examples_per_split',
      type=int,
      nargs='?',
      const=1,
      help=(
          'When set, only generate the first X examples (default to 1), rather'
          ' than the full dataset.If set to 0, only execute the'
          ' `_split_generators` (which download the original data), but skip'
          ' `_generator_examples`'
      ),
  )


def add_path_argument_group(parser: argparse.ArgumentParser):
  """Adds path argument group to the parser."""
  path_group = parser.add_argument_group('Paths')
  path_group.add_argument(
      '--data_dir',
      type=epath.Path,
      # Should match tfds.core.constant.DATA_DIR !!
      default=epath.Path(
          os.environ.get(
              'TFDS_DATA_DIR',
              os.path.join(os.path.expanduser('~'), 'tensorflow_datasets'),
          )
      ),
      help=(
          'Where to place datasets. Default to '
          '`~/tensorflow_datasets/` or `TFDS_DATA_DIR` environement variable.'
      ),
  )
  path_group.add_argument(
      '--download_dir',
      type=epath.Path,
      help='Where to place downloads. Default to `<data_dir>/downloads/`.',
  )
  path_group.add_argument(
      '--extract_dir',
      type=epath.Path,
      help='Where to extract files. Default to `<download_dir>/extracted/`.',
  )
  path_group.add_argument(
      '--manual_dir',
      type=epath.Path,
      help=(
          'Where to manually download data (required for some datasets). '
          'Default to `<download_dir>/manual/`.'
      ),
  )
  path_group.add_argument(
      '--add_name_to_manual_dir',
      action='store_true',
      help=(
          'If true, append the dataset name to the `manual_dir` (e.g. '
          '`<download_dir>/manual/<dataset_name>/`. Useful to avoid collisions '
          'if many datasets are generated.'
      ),
  )


def add_generation_argument_group(parser: argparse.ArgumentParser):
  """Adds generation argument group to the parser."""
  generation_group = parser.add_argument_group('Generation')
  generation_group.add_argument(
      '--download_only',
      action='store_true',
      help=(
          'If True, download all files but do not prepare the dataset. Uses the'
          ' checksum.tsv to find out what to download. Therefore, this does not'
          ' work in combination with --register_checksums.'
      ),
  )
  generation_group.add_argument(
      '--config',
      '-c',
      type=str,
      help=(
          'Config name to build. Build all configs if not set. Can also be a'
          ' json of the kwargs forwarded to the config `__init__` (for custom'
          ' configs).'
      ),
  )
  # We are forced to have 2 flags to avoid ambiguity when config name is
  # a number (e.g. `voc/2017`)
  generation_group.add_argument(
      '--config_idx',
      type=int,
      help=(
          'Config id to build (`builder_cls.BUILDER_CONFIGS[config_idx]`). '
          'Mutually exclusive with `--config`.'
      ),
  )
  generation_group.add_argument(
      '--update_metadata_only',
      action='store_true',
      default=False,
      help=(
          'If True, existing dataset_info.json is updated with metadata defined'
          ' in Builder class(es). Datasets must already have been prepared.'
      ),
  )
  generation_group.add_argument(
      '--download_config',
      type=str,
      help=(
          'A json of the kwargs forwarded to the config `__init__` (for custom'
          ' DownloadConfigs).'
      ),
  )
  generation_group.add_argument(
      '--imports',
      '-i',
      type=str,
      help='Comma separated list of module to import to register datasets.',
  )
  generation_group.add_argument(
      '--register_checksums',
      action='store_true',
      help='If True, store size and checksum of downloaded files.',
  )
  generation_group.add_argument(
      '--force_checksums_validation',
      action='store_true',
      help='If True, raise an error if the checksums are not found.',
  )
  # For compatibility with absl.flags (which generates --foo and --nofoo).
  generation_group.add_argument(
      '--noforce_checksums_validation',
      dest='force_checksums_validation',
      action='store_false',
      help='If specified, bypass the checks on the checksums.',
  )
  generation_group.add_argument(
      '--beam_pipeline_options',
      type=str,
      # nargs='+',
      help=(
          'A (comma-separated) list of flags to pass to `PipelineOptions` when'
          ' preparing with Apache Beam. (see:'
          ' https://www.tensorflow.org/datasets/beam_datasets). Example:'
          ' `--beam_pipeline_options=job_name=my-job,project=my-project`'
      ),
  )
  format_values = [f.value for f in file_adapters.FileFormat]
  generation_group.add_argument(
      '--file_format',
      type=str,
      help=(
          'File format to which generate the tf-examples. '
          f'Available values: {format_values} (see `tfds.core.FileFormat`).'
      ),
  )
  generation_group.add_argument(
      '--max_shard_size_mb', type=int, help='The max shard size in megabytes.'
  )
  generation_group.add_argument(
      '--num-processes',
      type=int,
      default=1,
      help='Number of parallel build processes.',
  )


def add_publish_argument_group(parser: argparse.ArgumentParser):
  """Adds publish argument group to the parser."""
  publish_group = parser.add_argument_group(
      'Publishing',
      description='Options for publishing successfully created datasets.',
  )
  publish_group.add_argument(
      '--publish_dir',
      type=epath.Path,
      default=None,
      required=False,
      help=(
          'Where to optionally publish the dataset after it has been '
          'generated successfully. Should be the root data dir under which'
          'datasets are stored. '
          'If unspecified, dataset will not be published'
      ),
  )
  publish_group.add_argument(
      '--skip_if_published',
      action='store_true',
      default=False,
      help=(
          'If the dataset with the same version and config is already '
          'published, then it will not be regenerated.'
      ),
  )


def download_and_prepare(
    builder: dataset_builder.DatasetBuilder,
    download_config: download.DownloadConfig | None,
    download_dir: epath.Path | None,
    publish_dir: epath.Path | None,
    skip_if_published: bool,
    overwrite: bool,
    beam_pipeline_options: str | None,
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

  # Add Apache Beam options to download config
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
