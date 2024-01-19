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

r"""Script utils for generating datasets figures and dataframes."""

import concurrent.futures
import functools
import itertools
import multiprocessing
import os
import traceback
from typing import Any, Callable, List, Optional, TypeVar

from absl import app
from absl import logging
import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

# pylint: disable=logging-format-interpolation,logging-not-lazy,logging-fstring-interpolation

T = TypeVar('T')

_WORKER_COUNT_DATASETS = 10


def _log_exception(fn):
  """Logs the exceptions from a `ThreadPoolExecutor`."""

  @functools.wraps(fn)
  def decorated(*args, **kwargs):
    try:
      return fn(*args, **kwargs)
    except Exception:  # pylint: disable=broad-except
      err_str = traceback.format_exc()
      logging.error(f'Exception occurred for {args}, {kwargs}:\n' + err_str)
      raise

  return decorated


@_log_exception
def generate_and_save_artifact(
    full_name: str,
    *,
    dst_dir: tfds.typing.PathLike,
    overwrite: bool,
    file_extension: str,
    get_artifact_fn: Callable[[tf.data.Dataset, tfds.core.DatasetInfo], T],
    save_artifact_fn: Callable[[str, T], None],
) -> None:
  """Builds and saves the generated artifact for the dataset in dst_dir.

  Args:
    full_name: Name of the dataset to build `dataset`, `dataset/config`.
    dst_dir: Destination where the dataset will be saved (as
      `dataset-config-version`)
    overwrite: If True, recompute the image even if it exists.
    file_extension: File extension of the artifact (e.g. `.png`)
    get_artifact_fn: Function which extracts the dataset artifact to save.
    save_artifact_fn: Function which save the extracted artifact.
  """
  dst_filename = full_name.replace('/', '-') + file_extension
  dst_path = os.path.join(dst_dir, dst_filename)
  # If the file already exists, skip the generation
  if not overwrite and tf.io.gfile.exists(dst_path):
    logging.info(f'Skipping generation for {full_name} (already exists)')
    return

  logging.info(f'Generating for {full_name}...')
  # Load the dataset.
  builder_name, _, version = full_name.rpartition('/')
  builder = tfds.builder(f'{builder_name}:{version}')
  split_names = list(builder.info.splits.keys())
  if not split_names:
    logging.info(f'Dataset `{full_name}` not generated.')
    return
  elif 'train' in split_names:
    split = 'train'
  else:
    split = split_names[0]
  ds = builder.as_dataset(split=split, shuffle_files=False)
  if not tf.io.gfile.exists(dst_dir):
    tf.io.gfile.makedirs(dst_dir)
  try:
    artifact = get_artifact_fn(ds.take(10), builder.info)
  except Exception:  # pylint: disable=broad-except
    logging.info(f'Generation not supported for dataset `{full_name}`')
    return

  save_artifact_fn(dst_path, artifact)


def _get_full_names(datasets: Optional[List[str]] = None) -> List[str]:
  """Lists all builder names `ds/version` and `ds/config/version` to generate.

  Args:
    datasets: List of datasets from which get the builder names.

  Returns:
    builder_names: The builder names.
  """
  if datasets is None:
    return tfds.core.load.list_full_names(current_version_only=True)
  else:
    builder_names = list(
        itertools.chain.from_iterable(
            [
                tfds.core.load.single_full_names(builder_name)
                for builder_name in datasets
            ]
        )
    )
    return builder_names


def multi_process_map(
    worker_fn: Callable[..., None],
    datasets: Optional[List[str]] = None,
) -> None:
  """Applies the function for each given datasets.

  Args:
    worker_fn: Function called on each dataset version.
    datasets: List of all `dataset` names to generate. If None, visualization
      for all available datasets will be generated.
  """
  full_names = _get_full_names(datasets)
  logging.info(f'Generate figures for {len(full_names)} builders')
  with multiprocessing.Pool(_WORKER_COUNT_DATASETS) as tpool:
    list(tpool.map(worker_fn, full_names))


def multi_thread_map(
    worker_fn: Callable[..., None],
    datasets: Optional[List[str]] = None,
) -> None:
  """Applies the function for each given datasets.

  Args:
    worker_fn: Function called on each dataset version.
    datasets: List of all `dataset` names to generate. If None, visualization
      for all available datasets will be generated.
  """
  full_names = _get_full_names(datasets)
  with concurrent.futures.ThreadPoolExecutor(
      max_workers=_WORKER_COUNT_DATASETS,
  ) as executor:
    list(executor.map(worker_fn, full_names))


def multi_process_run(main: Callable[[Any], None]) -> None:
  """Same as `absl.app.run` but with special multiprocess flags."""
  app.run(main)
