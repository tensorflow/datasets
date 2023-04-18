# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""TensorFlow compatibility utilities."""

import functools
import os
from typing import Optional

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def get_single_element(ds):
  """Calls `tf.data.Dataset.get_single_element`."""
  if hasattr(ds, "get_single_element"):  # tf 2.6 and above
    return ds.get_single_element()
  else:
    return tf.data.experimental.get_single_element(ds)


def _get_option_deterministic_field() -> str:
  if hasattr(tf.data.Options(), "deterministic"):
    return "deterministic"
  return "experimental_deterministic"


def get_option_deterministic(options) -> Optional[bool]:
  """Returns the option whether the output should be in deterministic order."""
  return getattr(options, _get_option_deterministic_field())


def set_option_deterministic(options, value: bool) -> None:
  setattr(options, _get_option_deterministic_field(), value)


def _make_pathlike_fn(fn, nb_path_arg=1):
  """Wrap the function in a PathLike-compatible function."""

  @functools.wraps(fn)
  def new_fn(*args, **kwargs):
    # Normalize PathLike objects
    args = tuple(os.fspath(arg) for arg in args[:nb_path_arg])
    return fn(*args, **kwargs)

  return new_fn
