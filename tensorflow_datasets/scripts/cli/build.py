# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""`tfds build` command."""

import argparse
import functools
import os
import pathlib
from typing import Iterator

from absl import logging
import tensorflow_datasets as tfds
import termcolor

# pylint: disable=logging-format-interpolation


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `build` command."""
  build_parser = parsers.add_parser(
      'build', help='Commands for downloading and preparing datasets.'
  )
  build_parser.add_argument(
      'datasets',  # Positional arguments
      type=str,
      nargs='*',
      help='Name(s) of the dataset(s) to build. Default to current dir. '
      'See https://www.tensorflow.org/datasets/cli for accepted values.',
  )
  build_parser.add_argument(  # Also accept keyword arguments
      '--datasets',
      type=str,
      nargs='+',
      dest='datasets_keyword',
      help='Datasets can also be provided as keyword argument.',
  )

  # **** Debug options ****
  debug_group = build_parser.add_argument_group(
      'Debug & tests',
      description='--pdb Enter post-mortem debugging mode '
      'if an exception is raised.'
  )
  # TODO(tfds): Add flag to overwrite the existing dataset.
  debug_group.add_argument(
      '--max_examples_per_split',
      type=int,
      nargs='?',
      const=1,
      help=
      'When set, only generate the first X examples (default to 1), rather '
      'than the full dataset.',
  )

  # **** Path options ****
  path_group = build_parser.add_argument_group('Paths')
  path_group.add_argument(
      '--data_dir',
      type=pathlib.Path,
      # Should match tfds.core.constant.DATA_DIR !!
      default=pathlib.Path(os.environ.get(
          'TFDS_DATA_DIR', os.path.join('~', 'tensorflow_datasets')
      )),
      help=
      'Where to place datasets. Default to '
      '`~/tensorflow_datasets/` or `TFDS_DATA_DIR` environement variable.',
  )
  path_group.add_argument(
      '--download_dir',
      type=pathlib.Path,
      help='Where to place downloads. Default to `<data_dir>/downloads/`.',
  )
  path_group.add_argument(
      '--extract_dir',
      type=pathlib.Path,
      help='Where to extract files. Default to `<download_dir>/extracted/`.',
  )
  path_group.add_argument(
      '--manual_dir',
      type=pathlib.Path,
      help=
      'Where to manually download data (required for some datasets). '
      'Default to `<download_dir>/manual/`.',
  )
  path_group.add_argument(
      '--add_name_to_manual_dir',
      action='store_true',
      help=
      'If true, append the dataset name to the `manual_dir` (e.g. '
      '`<download_dir>/manual/<dataset_name>/`. Useful to avoid collisions '
      'if many datasets are generated.'
  )

  # **** Generation options ****
  generation_group = build_parser.add_argument_group('Generation')
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
  generation_group.add_argument(
      '--beam_pipeline_options',
      type=str,
      # nargs='+',
      help='A (comma-separated) list of flags to pass to `PipelineOptions` '
      'when preparing with Apache Beam. '
      '(see: https://www.tensorflow.org/datasets/beam_datasets). '
      'Example: `--beam_pipeline_options=job_name=my-job,project=my-project`'
  )

  # **** Automation options ****
  automation_group = build_parser.add_argument_group(
      'Automation', description='Used by automated scripts.'
  )
  automation_group.add_argument(
      '--exclude_datasets',
      type=str,
      help=
      'If set, generate all datasets except the one defined here. '
      'Comma separated list of datasets to exclude. '
  )
  automation_group.add_argument(
      '--builder_config_id',
      type=int,
      help='Id of the config to build: `builder_cls.BUILDER_CONFIGS[id]`'
  )
  automation_group.add_argument(
      '--experimental_latest_version',
      action='store_true',
      help='Build the latest Version(experiments=...) available rather than '
      'default version.'
  )

  build_parser.set_defaults(subparser_fn=_build_datasets)


def _build_datasets(args: argparse.Namespace) -> None:
  """Build the given datasets."""
  # Select datasets to generate
  datasets = (args.datasets or []) + (args.datasets_keyword or [])
  if args.exclude_datasets:  # Generate all datasets if `--exclude_datasets` set
    if datasets:
      raise ValueError('--exclude_datasets can\'t be used with `datasets`')
    datasets = set(tfds.list_builders()) - set(args.exclude_datasets.split(','))
  else:
    datasets = datasets or ['']  # Empty string for default

  if len(datasets) > 1 and args.builder_config_id is not None:
    raise ValueError(
        '--builder_config_id can only be used when building a single dataset.'
    )

  # Generate all datasets sequencially
  for ds_to_build in datasets:
    # Each `str` may correspond to multiple builder (e.g. multiple configs)
    for builder in _make_builder(args, ds_to_build):
      _download_and_prepare(args, builder)


def _make_builder(
    args: argparse.Namespace,
    ds_to_build: str,
) -> Iterator[tfds.core.DatasetBuilder]:
  """Yields builders to generate."""
  # TODO(tfds): Infer the dataset format.
  # And make sure --record_checksums works.
  # * From file (`.py`), dataset-as-folder (`my_dataset/`):
  # * Nothing (use current directory)
  # * From module `tensorflow_datasets.text.my_dataset`
  # * From partial / full name: `my_dataset/config`, `my_dataset:1.0.0`
  # * Community datasets: `namespace/my_dataset`

  # If no dataset selected, use current directory
  if not ds_to_build:
    raise NotImplementedError('No datasets provided not supported yet.')

  # Currently only single name supported
  builder_cls = tfds.builder_cls(ds_to_build)

  # Only pass the version kwargs when required. Otherwise, `version=None`
  # overwrite the version parsed from the name.
  # `tfds.builder('my_dataset:1.2.0', version=None)`
  if args.experimental_latest_version:
    version_kwarg = {'version': 'experimental_latest'}
  else:
    version_kwarg = {}

  make_builder = functools.partial(
      builder_cls,
      data_dir=args.data_dir,
      **version_kwarg,
  )
  if args.builder_config_id is not None:
    # Only generate a single builder if --builder_config_id is set.
    if not builder_cls.BUILDER_CONFIGS:
      raise ValueError(
          '--builder_config_id can only be used with datasets with configs'
      )
    if args.builder_config_id > len(builder_cls.BUILDER_CONFIGS):
      logging.warning(
          f'--builder_config_id {args.builder_config_id} greater than number '
          f'of configs {len(builder_cls.BUILDER_CONFIGS)} for '
          f'{builder_cls.name}. Skipping...'
      )
      return
    # Use `config.name` to avoid
    # https://github.com/tensorflow/datasets/issues/2348
    config = builder_cls.BUILDER_CONFIGS[args.builder_config_id]
    yield make_builder(config=config.name)
  else:
    # Generate all configs
    if builder_cls.BUILDER_CONFIGS:
      for config in builder_cls.BUILDER_CONFIGS:
        yield make_builder(config=config.name)
    # Generate only the dataset
    else:
      yield make_builder()


def _download_and_prepare(
    args: argparse.Namespace,
    builder: tfds.core.DatasetBuilder,
) -> None:
  """Generate a single builder."""
  logging.info(f'download_and_prepare for dataset {builder.info.full_name}...')

  dl_config = _make_download_config(args)
  if args.add_name_to_manual_dir:
    dl_config.manual_dir = os.path.join(dl_config.manual_dir, builder.name)

  builder.download_and_prepare(
      download_dir=args.download_dir,
      download_config=dl_config,
  )

  # Dataset generated successfully
  logging.info('Dataset generation complete...')
  termcolor.cprint(str(builder.info.as_proto), attrs=['bold'])


def _make_download_config(
    args: argparse.Namespace,
) -> tfds.download.DownloadConfig:
  """Generate the download and prepare configuration."""
  # Load the download config
  dl_config = tfds.download.DownloadConfig(
      extract_dir=args.extract_dir,
      manual_dir=args.manual_dir,
      # TODO(b/116270825): Add flag to force extraction / preparation.
      download_mode=tfds.download.GenerateMode.REUSE_DATASET_IF_EXISTS,
      max_examples_per_split=args.max_examples_per_split,
      register_checksums=args.register_checksums,
      force_checksums_validation=args.force_checksums_validation,
  )

  # Add Apache Beam options to download config
  try:
    import apache_beam as beam  # pylint: disable=g-import-not-at-top
  except ImportError:
    beam = None

  if beam is not None:
    if args.beam_pipeline_options:
      dl_config.beam_options = beam.options.pipeline_options.PipelineOptions(
          flags=[f'--{opt}' for opt in args.beam_pipeline_options.split(',')]
      )

  return dl_config
