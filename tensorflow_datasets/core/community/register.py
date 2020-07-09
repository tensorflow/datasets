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

"""Community datasets register."""

import functools
import json
from typing import Dict

import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import dataset_spec


# Community datasets are parsed from the config files and exported on GCS
COMMUNITY_EXPORTED_PATH = utils.gcs_path('community-datasets-list.jsonl')


def community_config_path() -> str:
  """Returns the community config path."""
  # Is dynamically loaded as it is only required by specific scripts so may
  # not always be present.
  return utils.get_tfds_path('community-datasets.toml')


class DatasetSpecRegister:
  """Cache of all dynamically registered datasets.

  * Dynamically load and cache the list of registered datasets
  * Fault-tolerent if the register can't be loaded (e.g. offline mode)

  """

  def __init__(self, register_path: str):
    """Constructor.

    Args:
      register_path: File containing the registered dataset specs
    """
    # Should use pathlib-like GFile API instead.
    self._register_path = register_path

  def is_available(self) -> bool:
    """Returns `False` if the register can't be reached (e.g. offline)."""
    try:
      return tf.io.gfile.exists(self._register_path)
    except:  # pylint: disable=bare-except
      return False

  # TODO(py3.8): Use `@functools.cached_property`
  @property
  @functools.lru_cache()
  def dataset_specs(self) -> Dict[str, dataset_spec.DatasetSpec]:
    """Returns and cache all available specs.

    Returns:
      Mapping `namespace/ds_name` -> `DatasetSpec`
    """
    with tf.io.gfile.GFile(self._register_path, 'r') as f:
      lines = f.read().splitlines()

    all_ds_specs = [
        dataset_spec.DatasetSpec.from_json(json.loads(l)) for l in lines
    ]
    return {ds_spec.cannonical_name: ds_spec for ds_spec in all_ds_specs}


# Default MLDS public register
# In the future, could allow to user to set-up their own register (e.g
# private company can fetch dataset from their private code-base)
default_register: DatasetSpecRegister = DatasetSpecRegister(
    COMMUNITY_EXPORTED_PATH
)
