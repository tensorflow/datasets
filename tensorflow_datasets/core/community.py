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

"""Community utils."""

from tensorflow_datasets.core import utils


# Community datasets are parsed from the config files and exported on GCS
COMMUNITY_EXPORTED_PATH = utils.gcs_path('community-datasets-list.tsv')


def community_config_path() -> str:
  """Returns the community config path."""
  # Is dynamically loaded as it is only required by specific scripts so may
  # not always be present.
  return utils.get_tfds_path('community-datasets.toml')
