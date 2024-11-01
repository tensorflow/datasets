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

"""Lazy import utils.

Please, use `etils.epy.lazy_imports` for lazy imports.
"""

from __future__ import annotations

import importlib

from etils import epy


def tf_error_callback(module_name: Exception):
  del module_name
  print("\n\n***************************************************************")
  print(
      "Failed to import TensorFlow. Please note that TensorFlow is not "
      "installed by default when you install TFDS. This allows you "
      "to choose to install either `tf-nightly` or `tensorflow`. "
      "Please install the most recent version of TensorFlow, by "
      "following instructions at https://tensorflow.org/install."
  )
  print("***************************************************************\n\n")


MIN_TF_VERSION = "2.1.0"

_ensure_tf_version_called = False


# Ensure TensorFlow version is sufficiently recent. This needs to happen after
# TensorFlow was imported, as it is referenced.
def ensure_tf_version(module_name: str):
  """Ensures TensorFlow version is sufficient."""
  # Only check the first time.
  global _ensure_tf_version_called
  if _ensure_tf_version_called:
    return
  _ensure_tf_version_called = True

  tf = importlib.import_module(module_name)
  tf_version = tf.__version__  # pytype: disable=attribute-error
  if tf_version < MIN_TF_VERSION:
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        f"version >= {MIN_TF_VERSION}; Detected an installation of version "
        f"{tf_version}. Please upgrade TensorFlow to proceed."
    )


def array_record_error_callback(module_name: Exception):
  del module_name
  print("\n\n***************************************************************")
  print(
      "Failed to import ArrayRecord. This probably means that you are running"
      " on macOS or Windows. ArrayRecord currently does not work for your"
      " infrastructure, because it uses Python bindings in C++. We are actively"
      " working on this issue. Thanks for your understanding."
  )
  print("***************************************************************\n\n")


def mlcroissant_error_callback(module_name: Exception):
  """Error callback for mlcroissant."""
  del module_name
  print("\n\n***************************************************************")
  print("Failed to import mlcroissant.")
  print('Please install mlcroissant using `pip install mlcroissant`.')
  print("***************************************************************\n\n")


def tf_agents_error_callback(module_name: Exception):
  del module_name
  print("\n\n***************************************************************")
  print("Failed to import tf_agents.")
  print('Please install tf_agents using `pip install tf_agents`.')
  print("***************************************************************\n\n")


def datasets_error_callback(module_name: Exception):
  """Error callback for datasets."""
  del module_name
  print("\n\n***************************************************************")
  print("Failed to import datasets.")
  print('Please install datasets using `pip install datasets`.')
  print("***************************************************************\n\n")


# pylint: disable=g-import-not-at-top,unused-import

with epy.lazy_imports(error_callback=mlcroissant_error_callback):
  import mlcroissant  # pytype: disable=import-error


with epy.lazy_imports():
  import apache_beam
  import pandas
  import psutil
  import pyarrow
  import promise
  from pyarrow import parquet
  import requests
  import tree


with epy.lazy_imports(
    error_callback=tf_error_callback, success_callback=ensure_tf_version
):
  import tensorflow  # pytype: disable=import-error

with epy.lazy_imports(error_callback=tf_agents_error_callback):
  import tf_agents  # pytype: disable=import-error

with epy.lazy_imports(error_callback=datasets_error_callback):
  import datasets  # pytype: disable=import-error
  import huggingface_hub  # pytype: disable=import-error

with epy.lazy_imports(error_callback=array_record_error_callback):
  from array_record.python import array_record_data_source
  from array_record.python import array_record_module
