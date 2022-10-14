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

"""Defines a config DatasetBuilder, reading metadata from config files."""

import inspect
import os
from typing import Any, Optional, Type

from etils import epath
from tensorflow_datasets import version
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_metadata
from tensorflow_datasets.core.utils import resource_utils


def _get_builder_datadir_path(builder_cls: Type[Any]) -> epath.Path:
  """Returns the path to ConfigBuilder data dir.

  Args:
    builder_cls: a Builder class.

  Returns:
    The path to directory where the config data files of `builders_cls` can be
    read from. e.g. "/usr/lib/[...]/tensorflow_datasets/datasets/foo".
  """
  dataset_module_path = inspect.getsourcefile(builder_cls)
  if dataset_module_path:
    # This convoluted way handles the scenario when python and data files are
    # not accessible at the same path (happens depending on Python packaging
    # methodology).
    tfds_root_path = epath.Path(inspect.getsourcefile(version)).parent
    dataset_pkg_path = os.fspath(epath.Path(dataset_module_path).parent)
    # `[1:]` to remove leading [anti]slash.
    dataset_pkg_relative_dir_path = dataset_pkg_path.replace(
        os.fspath(tfds_root_path), "")[1:]
  else:  # Inspect module couldn't get the sources.
    dataset_pkg_relative_dir_path = os.path.join(
        # `[1:-1]` to remove tensorflow_datasets prefix and builder suffix.
        *(builder_cls.__module__.split(".")[1:-1]))
  datadir_path = resource_utils.tfds_path(dataset_pkg_relative_dir_path)
  return datadir_path


class ConfigBasedBuilder:
  """Mixin defining metadata-related methods using configs files.

  See `dataset_metadata.py` module for details about supported config files.

  Until none of the modules defining datasets are imported from tfds __init__,
  we must be careful to NOT read config files at import time.
  """

  # If not set, pkg_dir_path is inferred. However, if user of class knows better
  # then this can be set directly before init, to avoid heuristic inferences.
  # Example: `imported_builder_cls` function in `registered.py` module sets it.
  pkg_dir_path: Optional[epath.Path] = None

  def __init_subclass__(cls, **kwargs):
    # Extract dataset name from package name: 1 package = 1 dataset!
    # We set the name before calling super, since RegisteredDataset otherwise
    # infer name from class name, which wouldn't be correct since all
    # `ConfigBasedBuilder`s are named `Builder`.
    cls.name = cls.__module__.rsplit(".", 2)[1]
    super().__init_subclass__(**kwargs)
    if cls.pkg_dir_path is None:
      cls.pkg_dir_path = _get_builder_datadir_path(cls)

  @classmethod
  def get_metadata(cls) -> dataset_metadata.DatasetMetadata:
    return dataset_metadata.load(cls.pkg_dir_path)

  def dataset_info_from_configs(self, **kwargs):
    """Returns the DatasetInfo using given kwargs anf config files.

    Sub-class should call this and add information not present in config files
    using kwargs directly passed to tfds.core.DatasetInfo object.

    Args:
      **kwargs: kw args to pass to DatasetInfo directly.
    """
    metadata = self.get_metadata()
    return dataset_info.DatasetInfo(
        builder=self,
        description=metadata.description,
        citation=metadata.citation,
        **kwargs)
