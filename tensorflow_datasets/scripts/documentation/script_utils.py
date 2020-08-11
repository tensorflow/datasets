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

r"""Script utils for generating datasets figures and dataframes.
"""

import functools
import itertools
import traceback
from typing import List, Optional

from absl import logging

import tensorflow_datasets as tfds


# pylint: disable=logging-format-interpolation,logging-not-lazy


def log_exception(fn):
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


def get_full_names(datasets: Optional[List[str]] = None) -> List[str]:
  """List all builder names `ds/version` and `ds/config/version` to generate.

  Args:
    datasets: List of datasets from which get the builder names.

  Returns:
    builder_names: The builder names.
  """
  if datasets is None:
    return tfds.core.registered.list_full_names(
        current_version_only=True,
    )
  else:
    builder_names = list(itertools.chain.from_iterable([
        tfds.core.registered.single_full_names(builder_name)
        for builder_name in datasets
    ]))
    return builder_names
