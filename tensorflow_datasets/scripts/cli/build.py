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

"""`tfds build` command."""

from collections.abc import Iterator
import dataclasses
import functools
import importlib
import itertools
import json
import multiprocessing
import os
from typing import Any, Type

from absl import logging
import simple_parsing
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.cli import cli_utils


@dataclasses.dataclass(frozen=True, kw_only=True)
class Args(cli_utils.Args):
  """Commands for downloading and preparing datasets."""

  # Name(s) of the dataset(s) to build. Default to current dir. See
  # https://www.tensorflow.org/datasets/cli for accepted values.
  positional_datasets: list[str] = simple_parsing.list_field(
      positional=True,
      # Need to explicitly set metavar for command-line help.
      metavar='datasets',
  )

  datasets: list[str] = simple_parsing.list_field(alias='--dataset')
  """Datasets can also be provided as keyword argument."""

  debug: cli_utils.DebugOptions = cli_utils.DebugOptions()
  """Debug & tests options. Use --pdb to enter post-mortem debugging mode if an
  exception is raised."""

  paths: cli_utils.PathOptions = simple_parsing.field(
      default_factory=cli_utils.PathOptions
  )
  """Path options."""

  generation: cli_utils.GenerationOptions = simple_parsing.field(
      default_factory=cli_utils.GenerationOptions
  )
  """Generation options."""

  publishing: cli_utils.PublishingOptions = simple_parsing.field(
      default_factory=cli_utils.PublishingOptions
  )
  """Publishing options."""

  automation: cli_utils.AutomationOptions = simple_parsing.field(
      default_factory=cli_utils.AutomationOptions
  )
  """Automation options."""

  def execute(self) -> None:
    """Build the given datasets."""
    # Eventually register additional datasets imports
    if self.generation.imports:
      list(
          importlib.import_module(m) for m in self.generation.imports.split(',')
      )

    # Select datasets to generate
    datasets = self.positional_datasets + self.datasets
    if (
        self.automation.exclude_datasets
    ):  # Generate all datasets if `--exclude_datasets` set
      if datasets:
        raise ValueError("--exclude_datasets can't be used with `datasets`")
      datasets = set(tfds.list_builders(with_community_datasets=False)) - set(
          self.automation.exclude_datasets.split(',')
      )
      datasets = sorted(datasets)  # `set` is not deterministic
    else:
      datasets = datasets or ['']  # Empty string for default

    # Import builder classes
    builders_cls_and_kwargs = [
        _get_builder_cls_and_kwargs(
            dataset, has_imports=bool(self.generation.imports)
        )
        for dataset in datasets
    ]

    # Parallelize datasets generation.
    builders = itertools.chain(*(
        _make_builders(self, builder_cls, builder_kwargs)
        for (builder_cls, builder_kwargs) in builders_cls_and_kwargs
    ))
    process_builder_fn = functools.partial(
        _download if self.generation.download_only else _download_and_prepare,
        self,
    )

    if self.generation.num_processes == 1:
      for builder in builders:
        process_builder_fn(builder)
    else:
      with multiprocessing.Pool(self.generation.num_processes) as pool:
        pool.map(process_builder_fn, builders)


def _make_builders(
    args: Args,
    builder_cls: Type[tfds.core.DatasetBuilder],
    builder_kwargs: dict[str, Any],
) -> Iterator[tfds.core.DatasetBuilder]:
  """Yields builders to generate.

  Args:
    args: Command line arguments.
    builder_cls: Dataset builder class.
    builder_kwargs: Dataset builder kwargs.

  Yields:
    Initialized dataset builders.
  """
  # Eventually overwrite version
  if args.automation.experimental_latest_version:
    if 'version' in builder_kwargs:
      raise ValueError(
          "Can't have both `--experimental_latest` and version set (`:1.0.0`)"
      )
    builder_kwargs['version'] = 'experimental_latest'

  # Eventually overwrite config
  builder_kwargs['config'] = _get_config_name(
      builder_cls=builder_cls,
      config_kwarg=builder_kwargs.get('config'),
      config_name=args.generation.config,
      config_idx=args.generation.config_idx,
  )

  if args.generation.file_format:
    builder_kwargs['file_format'] = args.generation.file_format

  make_builder = functools.partial(
      _make_builder,
      builder_cls,
      overwrite=args.debug.overwrite,
      fail_if_exists=args.debug.fail_if_exists,
      data_dir=args.paths.data_dir,
      **builder_kwargs,
  )

  # Generate all configs if no config requested.
  if builder_cls.BUILDER_CONFIGS and builder_kwargs['config'] is None:
    for config in builder_cls.BUILDER_CONFIGS:
      yield make_builder(config=config.name)
  # Generate only the dataset
  else:
    yield make_builder()


def _get_builder_cls_and_kwargs(
    ds_to_build: str,
    *,
    has_imports: bool,
) -> tuple[Type[tfds.core.DatasetBuilder], dict[str, Any]]:
  """Infer the builder class to build and its kwargs.

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
      logging.info('Loading dataset %s from path: %s', ds_to_build, path)
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
      'Loading dataset %s from imports: %s',
      ds_to_build,
      builder_cls.__module__,
  )
  return builder_cls, builder_kwargs


def _search_script_path(ds_to_build: str) -> tfds.core.Path | None:
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
) -> tfds.core.Path | None:
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
  builder = builder_cls(**builder_kwargs)
  is_prepared = builder.is_prepared()
  if fail_if_exists and is_prepared:
    raise RuntimeError(
        'The `fail_if_exists` flag was True and '
        f'the data already exists in {builder.data_path}'
    )
  if overwrite and is_prepared:
    builder.data_path.rmtree()  # Delete pre-existing data
    # Re-create the builder with clean state
    builder = builder_cls(**builder_kwargs)
  return builder


def _download(
    args: Args,
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

  download_dir = args.paths.download_dir or os.path.join(
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
    args: Args,
    builder: tfds.core.DatasetBuilder,
) -> None:
  """Generate a single builder."""
  cli_utils.download_and_prepare(
      builder=builder,
      download_config=_make_download_config(args, dataset_name=builder.name),
      download_dir=args.paths.download_dir,
      publish_dir=args.publishing.publish_dir,
      skip_if_published=args.publishing.skip_if_published,
      overwrite=args.debug.overwrite,
      beam_pipeline_options=args.generation.beam_pipeline_options,
      nondeterministic_order=args.generation.nondeterministic_order,
  )


def _make_download_config(
    args: Args,
    dataset_name: str,
) -> tfds.download.DownloadConfig:
  """Generate the download and prepare configuration."""
  # Load the download config
  manual_dir = args.paths.manual_dir
  if args.paths.add_name_to_manual_dir:
    manual_dir = manual_dir / dataset_name

  kwargs = {}
  if args.generation.max_shard_size_mb:
    kwargs['max_shard_size'] = args.generation.max_shard_size_mb << 20
  if args.generation.num_shards:
    kwargs['num_shards'] = args.generation.num_shards
  if args.generation.download_config:
    kwargs.update(json.loads(args.generation.download_config))

  if 'download_mode' in kwargs:
    kwargs['download_mode'] = tfds.download.GenerateMode(
        kwargs['download_mode']
    )
  else:
    kwargs['download_mode'] = tfds.download.GenerateMode.REUSE_DATASET_IF_EXISTS
  if args.generation.update_metadata_only:
    kwargs['download_mode'] = tfds.download.GenerateMode.UPDATE_DATASET_INFO

  return tfds.download.DownloadConfig(
      extract_dir=args.paths.extract_dir,
      manual_dir=manual_dir,
      max_examples_per_split=args.debug.max_examples_per_split,
      register_checksums=args.generation.register_checksums,
      force_checksums_validation=args.generation.force_checksums_validation,
      **kwargs,
  )


def _get_config_name(
    builder_cls: Type[tfds.core.DatasetBuilder],
    config_kwarg: str | None,
    config_name: str | None,
    config_idx: int | None,
) -> str | tfds.core.BuilderConfig | None:
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
    if config_idx >= len(builder_cls.BUILDER_CONFIGS):
      raise ValueError(
          f'--config_idx {config_idx} greater than number of configs '
          f'{len(builder_cls.BUILDER_CONFIGS)} for {builder_cls.name}.'
      )
    else:
      # Use `config.name` to avoid
      # https://github.com/tensorflow/datasets/issues/2348
      return builder_cls.BUILDER_CONFIGS[config_idx].name
  else:  # No config defined
    return None
