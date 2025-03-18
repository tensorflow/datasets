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

"""Utils functions."""

import enum
from etils import epy


class DownloadError(Exception):
  pass


class GenerateMode(epy.StrEnum):
  """`Enum` for how to treat pre-existing downloads and data.

  The default mode is `REUSE_DATASET_IF_EXISTS`, which will reuse both
  raw downloads and the prepared dataset if they exist.

  The generations modes:

  |                                    | Downloads | Dataset | Metadata |
  | -----------------------------------|-----------|---------|----------|
  | `REUSE_DATASET_IF_EXISTS` (default)| Reuse     | Reuse   | Reuse    |
  | `UPDATE_DATASET_INFO`              | Reuse     | Reuse   | Fresh    |
  | `REUSE_CACHE_IF_EXISTS`            | Reuse     | Fresh   | Fresh    |
  | `FORCE_REDOWNLOAD`                 | Fresh     | Fresh   | Fresh    |

  UPDATE_DATASET_INFO only regenerates DatasetInfo metadata which is directly
  coming from the Builder metadata, and not directly used to prepare the data
  or computed from the downloaded or prepared data.
  This means that `description`, `config_tags`, etc. will be updated, but
  `download_size`, `schema`, `splits`, `disable_shuffling`, `file_format` will
  not be updated.
  UPDATE_DATASET_INFO will fail if the data has never been prepared.
  """

  REUSE_DATASET_IF_EXISTS = enum.auto()
  UPDATE_DATASET_INFO = enum.auto()
  REUSE_CACHE_IF_EXISTS = enum.auto()
  FORCE_REDOWNLOAD = enum.auto()

  @property
  def force_download(self) -> bool:
    return self == GenerateMode.FORCE_REDOWNLOAD

  @property
  def overwrite_dataset(self) -> bool:
    return self in [
        GenerateMode.REUSE_CACHE_IF_EXISTS,
        GenerateMode.FORCE_REDOWNLOAD,
    ]


class ComputeStatsMode(enum.Enum):
  """Mode to decide if dynamic dataset info fields should be computed or not.

  Mode can be:

  * AUTO: Compute the DatasetInfo dynamic fields only if they haven't been
    restored from GCS.
  * FORCE: Always recompute DatasetInfo dynamic  fields, even if they are
    already present
  * SKIP: Ignore the dataset dynamic field computation (whether they already
    exist or not)
  """

  AUTO = 'auto'
  FORCE = 'force'
  SKIP = 'skip'
