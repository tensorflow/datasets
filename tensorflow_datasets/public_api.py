# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Public API of tfds, without the registered dataset."""

# pylint: disable=unused-import,g-import-not-at-top,g-bad-import-order,wrong-import-position
from tensorflow_datasets.core import tf_compat
tf_compat.ensure_tf_install()

from tensorflow_datasets import core
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter as file_adapter
from tensorflow_datasets.core import units
from tensorflow_datasets.core.dataset_utils import as_numpy
from tensorflow_datasets.core.download import GenerateMode
from tensorflow_datasets.core.registered import builder
from tensorflow_datasets.core.registered import list_builders
from tensorflow_datasets.core.registered import load
from tensorflow_datasets.core.splits import percent
from tensorflow_datasets.core.splits import Split
from tensorflow_datasets.core.utils.gcs_utils import is_dataset_on_gcs
from tensorflow_datasets.core.utils.tqdm_utils import disable_progress_bar
from tensorflow_datasets.version import __version__


__all__ = [
    "core",
    "as_numpy",
    "download",
    "features",
    "file_adapter",
    "units",
    "GenerateMode",
    "builder",
    "list_builders",
    "load",
    "percent",
    "Split",
    "testing",
    "disable_progress_bar",
    "is_dataset_on_gcs",
]


def _import_testing():
  try:
    from tensorflow_datasets import testing  # pylint: disable=redefined-outer-name
    return testing
  except:
    raise   # pylint: disable=unreachable


testing = _import_testing()
