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
from typing import Iterator, Optional, Type

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
  debug_group.add_argument(
      '--overwrite',
      action='store_true',
      help='Delete pre-existing dataset if it exists.',
  )
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
      '--config', '-c',
      type=str,
      help='Config name to build. Build all configs if not set.'
  )
  # We are forced to have 2 flags to avoid ambiguity when config name is
  # a number (e.g. `voc/2017`)
  generation_group.add_argument(
      '--config_idx',
      type=int,
      help=
      'Config id to build (`builder_cls.BUILDER_CONFIGS[config_idx]`). '
      'Mutually exclusive with `--config`.'
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

  # Generate all datasets sequencially
  for ds_to_build in datasets:
    # Each `str` may correspond to multiple builder (e.g. multiple configs)
    for builder in _make_builders(args, ds_to_build):
      _download_and_prepare(args, builder)


def _make_builders(
    args: argparse.Namespace,
    ds_to_build: str,
) -> Iterator[tfds.core.DatasetBuilder]:
  """Yields builders to generate."""
  # TODO(tfds): Infer the dataset format.
  # And make sure --record_checksums works.
  # * From file (`.py`), dataset-as-folder (`my_dataset/`):
  # * Nothing (use current directory)
  # * From module `tensorflow_datasets.text.my_dataset`
  # * Community datasets: `namespace/my_dataset`

  # If no dataset selected, use current directory
  if not ds_to_build:
    raise NotImplementedError('No datasets provided not supported yet.')

  # Extract `name/config:version`
  extract_name_and_kwargs = tfds.core.load.dataset_name_and_kwargs_from_name_str
  builder_name, builder_kwargs = extract_name_and_kwargs(ds_to_build)
  builder_cls = tfds.builder_cls(builder_name)

  # Eventually overwrite version
  if args.experimental_latest_version:
    if 'version' in builder_kwargs:
      raise ValueError(
          'Can\'t have both `--experimental_latest` and version set (`:1.0.0`)'
      )
    builder_kwargs['version'] = 'experimental_latest'

  # Eventually overwrite config
  builder_kwargs['config'] = _get_config_name(
      builder_cls=builder_cls,
      config_kwarg=builder_kwargs.get('config'),
      config_name=args.config,
      config_idx=args.config_idx,
  )

  make_builder = functools.partial(
      _make_builder,
      builder_cls,
      overwrite=args.overwrite,
      data_dir=args.data_dir,
      **builder_kwargs,
  )

  # Generate all configs if no config requested.
  if builder_cls.BUILDER_CONFIGS and builder_kwargs['config'] is None:
    for config in builder_cls.BUILDER_CONFIGS:
      yield make_builder(config=config.name)
  # Generate only the dataset
  else:
    yield make_builder()


def _make_builder(
    builder_cls: Type[tfds.core.DatasetBuilder],
    overwrite: bool,
    **builder_kwargs,
) -> tfds.core.DatasetBuilder:
  """Builder factory, eventually deleting pre-existing dataset."""
  builder = builder_cls(**builder_kwargs)  # pytype: disable=not-instantiable
  if overwrite and builder.data_path.exists():
    builder.data_path.rmtree()  # Delete pre-existing data
    # Re-create the builder with clean state
    builder = builder_cls(**builder_kwargs)  # pytype: disable=not-instantiable
  return builder


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


def _get_config_name(
    builder_cls: Type[tfds.core.DatasetBuilder],
    config_kwarg: Optional[str],
    config_name: Optional[str],
    config_idx: Optional[int],
) -> Optional[str]:
  """Extract the config name.

  Args:
    builder_cls: Builder class
    config_kwarg: Config passed as `ds_name/config`
    config_name: Config passed as `--config name`
    config_idx: Config passed as `--config_idx 0`

  Returns:
    The config name to generate, or None.
  """
  num_config = sum(
      c is not None for c in (config_kwarg, config_name, config_idx)
  )
  if num_config > 1:
    raise ValueError(
        'Config should only be defined once by either `ds_name/config`, '
        '`--config` or `--config_idx`'
    )
  elif num_config == 1 and not builder_cls.BUILDER_CONFIGS:
    raise ValueError(
        f'Cannot generate requested config: Dataset {builder_cls.name} does '
        'not have config.'
    )

  if config_kwarg:  # `ds_name/config`
    return config_kwarg
  elif config_name:  # `--config name`
    return config_name
  elif config_idx is not None:  # `--config_idx 123`
    if config_idx > len(builder_cls.BUILDER_CONFIGS):
      raise ValueError(
          f'--config_idx {config_idx} greater than number '
          f'of configs {len(builder_cls.BUILDER_CONFIGS)} for '
          f'{builder_cls.name}.'
      )
    else:
      # Use `config.name` to avoid
      # https://github.com/tensorflow/datasets/issues/2348
      return builder_cls.BUILDER_CONFIGS[config_idx].name
  else:  # No config defined
    return None
