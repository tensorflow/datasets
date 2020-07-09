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

"""Community public API."""

from tensorflow_datasets.core.community.dataset_spec import DatasetSource
from tensorflow_datasets.core.community.dataset_spec import DatasetSpec
from tensorflow_datasets.core.community.dataset_spec import GithubSource
from tensorflow_datasets.core.community.register import community_config_path
from tensorflow_datasets.core.community.register import COMMUNITY_EXPORTED_PATH
from tensorflow_datasets.core.community.register import default_register

__all__ = [
    'community_config_path',
    'COMMUNITY_EXPORTED_PATH',
    'DatasetSource',
    'DatasetSpec',
    'default_register',
    'GithubSource',
]
