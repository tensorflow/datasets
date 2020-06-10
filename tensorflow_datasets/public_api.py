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

# Lint as: python3
"""Public API of tfds, without the registered dataset."""

# pylint: disable=unused-import,g-import-not-at-top,g-bad-import-order,wrong-import-position
from tensorflow_datasets.core import tf_compat
tf_compat.ensure_tf_install()

from tensorflow_datasets import core
from tensorflow_datasets.core import download
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import features
from tensorflow_datasets.core import units
from tensorflow_datasets.core import visualization
from tensorflow_datasets.core.dataset_utils import as_numpy
from tensorflow_datasets.core.download import GenerateMode
from tensorflow_datasets.core.registered import builder
from tensorflow_datasets.core.registered import builder_cls
from tensorflow_datasets.core.registered import list_builders
from tensorflow_datasets.core.registered import load
from tensorflow_datasets.core.splits import Split
from tensorflow_datasets.core.utils.gcs_utils import is_dataset_on_gcs
from tensorflow_datasets.core.utils.read_config import ReadConfig
from tensorflow_datasets.core.utils.tqdm_utils import disable_progress_bar
from tensorflow_datasets.core.visualization import show_examples
from tensorflow_datasets.core.visualization import show_statistics
from tensorflow_datasets.version import __version__

with core.registered.skip_registration():
  # We import testing namespace but without registering the tests datasets
  # (e.g. DummyMnist,...).
  from tensorflow_datasets import testing


__all__ = [
    "core",
    "as_numpy",
    "decode",
    "download",
    "features",
    "units",
    "GenerateMode",
    "builder",
    "builder_cls",
    "list_builders",
    "load",
    "ReadConfig",
    "Split",
    "testing",
    "disable_progress_bar",
    "is_dataset_on_gcs",
    "show_examples",
    "show_statistics",
    "visualization",
    "__version__",
]
