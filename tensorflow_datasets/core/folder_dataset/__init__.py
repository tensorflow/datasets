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

"""Utils to load data comming from third party sources directly with TFDS."""

from tensorflow_datasets.core import registered

from tensorflow_datasets.core.folder_dataset.compute_split_utils import compute_split_info
from tensorflow_datasets.core.folder_dataset.compute_split_utils import compute_split_info_from_directory
from tensorflow_datasets.core.folder_dataset.write_metadata_utils import write_metadata

# Custom datasets cannot be instanciated through `tfds.load`
with registered.skip_registration():
  # pylint: disable=g-import-not-at-top
  from tensorflow_datasets.core.folder_dataset.image_folder import ImageFolder
  from tensorflow_datasets.core.folder_dataset.translate_folder import TranslateFolder
  # pylint: enable=g-import-not-at-top

__all__ = [
    "compute_split_info",
    "compute_split_info_from_directory",
    "ImageFolder",
    "TranslateFolder",
    "write_metadata",
]
