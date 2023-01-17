# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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
import importlib
import json
import os
import typing
from typing import Dict, Iterator, Optional, Tuple, Type, Union

from absl import logging
from etils import epath
import tensorflow_datasets as tfds

# pylint: disable=logging-fstring-interpolation


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `build` command."""
  build_parser = parsers.add_parser(
      'build', help='Commands for downloading and preparing datasets.'
  )
  build_parser.add_argument(
      'datasets',  # Positional arguments
      type=str,
      nargs='*',
      help=(
          'Name(s) of the dataset(s) to build. Default to current dir. '
          'See https://www.tensorflow.org/datasets/cli for accepted values.'
      ),
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

  # **** Path options ****
  path_group = build_parser.add_argument_group('Paths')
  path_group.add_argument(
      '--data_dir',
      type=tfds.core.Path,
      # Should match tfds.core.constant.DATA_DIR !!
      default=tfds.core.Path(
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
      type=tfds.core.Path,
      help='Where to place downloads. Default to `<data_dir>/downloads/`.',
  )
  path_group.add_argument(
      '--extract_dir',
      type=tfds.core.Path,
      help='Where to extract files. Default to `<download_dir>/extracted/`.',
  )
  path_group.add_argument(
      '--manual_dir',
      type=tfds.core.Path,
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

  # **** Generation options ****
  generation_group = build_parser.add_argument_group('Generation')
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
  format_values = [f.value for f in tfds.core.FileFormat]
  generation_group.add_argument(
      '--file_format',
      type=str,
      help=(
          'File format to which generate the tf-examples. '
          f'Available values: {format_values} (see `tfds.core.FileFormat`).'
      ),
  )

  publish_group = build_parser.add_argument_group(
      'Publishing',
      description='Options for publishing successfully created datasets.',
  )
  publish_group.add_argument(
      '--publish_dir',
      type=tfds.core.Path,
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

  # **** Automation options ****
  automation_group = build_parser.add_argument_group(
      'Automation', description='Used by automated scripts.'
  )
  automation_group.add_argument(
      '--exclude_datasets',
      type=str,
      help=(
          'If set, generate all datasets except the one defined here. '
          'Comma separated list of datasets to exclude. '
      ),
  )
  automation_group.add_argument(
      '--experimental_latest_version',
      action='store_true',
      help=(
          'Build the latest Version(experiments=...) available rather than '
          'default version.'
      ),
  )

  build_parser.set_defaults(subparser_fn=_build_datasets)


def _build_datasets(args: argparse.Namespace) -> None:
  """Build the given datasets."""
  # Eventually register additional datasets imports
  if args.imports:
    list(importlib.import_module(m) for m in args.imports.split(','))

  # Select datasets to generate
  datasets = (args.datasets or []) + (args.datasets_keyword or [])
  if args.exclude_datasets:  # Generate all datasets if `--exclude_datasets` set
    if datasets:
      raise ValueError("--exclude_datasets can't be used with `datasets`")
    datasets = set(tfds.list_builders(with_community_datasets=False)) - set(
        args.exclude_datasets.split(',')
    )
    datasets = sorted(datasets)  # `set` is not deterministic
  else:
    datasets = datasets or ['']  # Empty string for default

  # Generate all datasets sequentially.
  for ds_to_build in datasets:
    # Each `str` may correspond to multiple builder (e.g. multiple configs)
    for builder in _make_builders(args, ds_to_build):
      if args.download_only:
        _download(args, builder)
      else:
        _download_and_prepare(args, builder)


def _make_builders(
    args: argparse.Namespace,
    ds_to_build: str,
) -> Iterator[tfds.core.DatasetBuilder]:
  """Yields builders to generate."""
  builder_cls, builder_kwargs = _get_builder_cls(
      ds_to_build,
      has_imports=bool(args.imports),
  )

  # Eventually overwrite version
  if args.experimental_latest_version:
    if 'version' in builder_kwargs:
      raise ValueError(
          "Can't have both `--experimental_latest` and version set (`:1.0.0`)"
      )
    builder_kwargs['version'] = 'experimental_latest'

  # Eventually overwrite config
  builder_kwargs['config'] = _get_config_name(
      builder_cls=builder_cls,
      config_kwarg=builder_kwargs.get('config'),
      config_name=args.config,
      config_idx=args.config_idx,
  )

  if args.file_format:
    builder_kwargs['file_format'] = args.file_format

  make_builder = functools.partial(
      _make_builder,
      builder_cls,
      overwrite=args.overwrite,
      fail_if_exists=args.fail_if_exists,
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


def _get_builder_cls(
    ds_to_build: str,
    *,
    has_imports: bool,
) -> Tuple[Type[tfds.core.DatasetBuilder], Dict[str, str]]:
  """Infer the builder class to build.

  Args:
    ds_to_build: Dataset argument.
    has_imports: Whether `--imports` was passed

  Returns:
    builder_cls: The dataset class to download and prepare
    kwargs:
  """
  # 1st case: Requested dataset is a path to `.py` script
  # When `--imports=` is set, it means the user expects the dataset to be
  # registered through the `imports` and not locally.
  if not has_imports:
    path = _search_script_path(ds_to_build)
    if path is not None:
      logging.info(f'Loading dataset {ds_to_build} from path: {path}')
      # Dynamically load user dataset script
      # When possible, load from the parent's parent, so module is named
      # "foo.foo_dataset_builder".
      try:
        with tfds.core.utils.add_sys_path(path.parent.parent):
          builder_cls = tfds.core.community.builder_cls_from_module(
              f'{path.parent.stem}.{path.stem}'
          )
        return builder_cls, {}
      except ImportError:
        pass
      # There might be cases where user imports from a legacy builder module,
      # in which case the above wouldn't necessarily work, so we fall back to
      # importing the module directly.
      with tfds.core.utils.add_sys_path(path.parent):
        builder_cls = tfds.core.community.builder_cls_from_module(path.stem)
      return builder_cls, {}

  # 2nd case: Dataset is registered through imports.

  # Extract `name/config:version`
  name, builder_kwargs = tfds.core.naming.parse_builder_name_kwargs(ds_to_build)
  builder_cls = tfds.builder_cls(str(name))
  logging.info(
      f'Loading dataset {ds_to_build} from imports: {builder_cls.__module__}'
  )
  builder_kwargs = typing.cast(Dict[str, str], builder_kwargs)
  return builder_cls, builder_kwargs


def _search_script_path(ds_to_build: str) -> Optional[tfds.core.Path]:
  """Check whether the requested dataset match a file on disk."""
  # If the dataset file exists, use it. Valid values are:
  # * Empty string (use default directory)
  # * Dataset folder (e.g. `my_dataset/my_dataset_dataset_builder.py`)
  # * Legacy dataset folder (e.g. `my_dataset/my_dataset.py`)
  # * Dataset file (e.g. `my_dataset.py`)
  # * Dataset module (e.g. `my_dataset`)

  path = tfds.core.Path(ds_to_build).expanduser().resolve()
  if path.exists():
    if path.is_dir():
      # dataset-as-folder, use `my_dataset/my_dataset_dataset_builder.py` ...
      module_path = path / f'{path.name}_dataset_builder.py'
      if module_path.exists():
        return _validate_script_path(module_path)
      # ... or `my_dataset/my_dataset.py` (legacy)
      return _validate_script_path(path / f'{path.name}.py')
    else:  # `my_dataset.py` script
      return _validate_script_path(path)

  # Try with `.py`
  path = path.with_suffix('.py')
  if path.exists():
    return path
  # Path not found. Use heuristic to detect if user intended to pass a path:
  elif (
      not ds_to_build
      or ds_to_build.endswith((os.sep, '.py'))  # ds.py
      or tfds.core.Path(ds_to_build).is_absolute()  # /path/to
      or ds_to_build.count(os.sep) > 1  # path/dataset/config
  ):
    raise FileNotFoundError(
        f'Could not find generation script for `{ds_to_build}`: '
        f'{path} not found.'
    )
  else:
    return None


def _validate_script_path(
    path: tfds.core.Path,
) -> Optional[tfds.core.Path]:
  """Validates and returns the `dataset_builder.py` generation script path."""
  if path.suffix != '.py':
    raise ValueError(f'Expected `.py` file. Invalid dataset path: {path}.')
  if not path.exists():
    raise FileNotFoundError(
        f'Could not find dataset generation script: {path}. '
    )
  return path


def _make_builder(
    builder_cls: Type[tfds.core.DatasetBuilder],
    overwrite: bool,
    fail_if_exists: bool,
    **builder_kwargs,
) -> tfds.core.DatasetBuilder:
  """Builder factory, eventually deleting pre-existing dataset."""
  builder = builder_cls(**builder_kwargs)  # pytype: disable=not-instantiable
  data_exists = builder.data_path.exists()
  if fail_if_exists and data_exists:
    raise RuntimeError(
        'The `fail_if_exists` flag was True and '
        f'the data already exists in {builder.data_path}'
    )
  if overwrite and data_exists:
    builder.data_path.rmtree()  # Delete pre-existing data
    # Re-create the builder with clean state
    builder = builder_cls(**builder_kwargs)  # pytype: disable=not-instantiable
  return builder


def _download(
    args: argparse.Namespace,
    builder: tfds.core.DatasetBuilder,
) -> None:
  """Downloads all files of the given builder."""
  dl_config = _make_download_config(args, dataset_name=builder.name)

  if dl_config.register_checksums:
    raise ValueError(
        'It is not allowed to enable --register_checksums '
        'when using --download_only!'
    )

  if builder.url_infos is None:
    raise ValueError(
        f'URL infos of builder {builder.name} are not defined, '
        'so cannot download these URLs.'
    )

  max_simultaneous_downloads = None
  if builder.MAX_SIMULTANEOUS_DOWNLOADS is not None:
    max_simultaneous_downloads = builder.MAX_SIMULTANEOUS_DOWNLOADS

  download_dir = args.download_dir or os.path.join(
      builder._data_dir_root, 'downloads'  # pylint: disable=protected-access
  )
  dl_manager = tfds.download.DownloadManager(
      download_dir=download_dir,
      url_infos=builder.url_infos,
      force_download=False,
      force_extraction=False,
      force_checksums_validation=dl_config.force_checksums_validation,
      register_checksums=False,
      verify_ssl=dl_config.verify_ssl,
      dataset_name=builder.name,
      max_simultaneous_downloads=max_simultaneous_downloads,
  )

  urls_to_download = {
      f'file{i}': url for i, url in enumerate(builder.url_infos.keys())
  }
  dl_manager.download(urls_to_download)


def _download_and_prepare(
    args: argparse.Namespace,
    builder: tfds.core.DatasetBuilder,
) -> None:
  """Generate a single builder."""
  logging.info(f'download_and_prepare for dataset {builder.info.full_name}...')

  publish_data_dir = _publish_data_dir(args.publish_dir, builder)
  if args.skip_if_published and publish_data_dir is not None:
    if publish_data_dir.exists():
      logging.info(
          f'Dataset already exists in {publish_data_dir}. Skipping generation.'
      )
      return

  dl_config = _make_download_config(args, dataset_name=builder.name)
  builder.download_and_prepare(
      download_dir=args.download_dir,
      download_config=dl_config,
  )

  # Dataset generated successfully
  logging.info('Dataset generation complete...')

  print()
  print(repr(builder.info))
  print()

  # Publish data if requested.
  if publish_data_dir is not None:
    logging.info(f'Publishing dataset to {publish_data_dir}')
    _publish_data(
        publish_data_dir=publish_data_dir,
        builder=builder,
        overwrite=args.overwrite,
    )
    logging.info(f'Dataset successfully published to {publish_data_dir}')


def _publish_data_dir(
    publish_dir: Optional[tfds.core.Path], builder: tfds.core.DatasetBuilder
) -> Optional[epath.Path]:
  if publish_dir is None:
    return None
  return epath.Path(publish_dir) / builder.info.full_name


def _publish_data(
    publish_data_dir: epath.Path,
    builder: tfds.core.DatasetBuilder,
    overwrite: bool = False,
) -> None:
  """Publishes the data from the given builder to `publish_data_dir`.

  Arguments:
    publish_data_dir: folder where the data should be published. Should include
      config and version.
    builder: the builder whose data needs to be published.
    overwrite: whether to overwrite existing data in the `publish_root_dir` if
      it exists.
  """
  from_data_dir = epath.Path(builder.data_dir)
  publish_data_dir.mkdir(parents=True, exist_ok=True)
  for filepath in from_data_dir.iterdir():
    filepath.copy(dst=publish_data_dir / filepath.name, overwrite=overwrite)


def _make_download_config(
    args: argparse.Namespace,
    dataset_name: str,
) -> tfds.download.DownloadConfig:
  """Generate the download and prepare configuration."""
  # Load the download config
  manual_dir = args.manual_dir
  if args.add_name_to_manual_dir:
    manual_dir = os.path.join(manual_dir, dataset_name)

  dl_config = tfds.download.DownloadConfig(
      extract_dir=args.extract_dir,
      manual_dir=manual_dir,
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
) -> Optional[Union[str, tfds.core.BuilderConfig]]:
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
    if config_name.startswith('{'):
      # Json: Dynamically recreate the builder_config
      return builder_cls.builder_config_cls(**json.loads(config_name))
    else:
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
