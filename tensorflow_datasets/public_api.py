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

"""Public API of tfds, without the registered dataset."""

import types

# pylint: disable=unused-import,g-import-not-at-top,g-bad-import-order,wrong-import-position
from tensorflow_datasets.core import tf_compat
tf_compat.ensure_tf_install()

from tensorflow_datasets import core
from tensorflow_datasets.core import folder_dataset
from tensorflow_datasets.core import download
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import features
from tensorflow_datasets.core import units
from tensorflow_datasets.core import visualization
from tensorflow_datasets.core.as_dataframe import as_dataframe
from tensorflow_datasets.core.folder_dataset import ImageFolder
from tensorflow_datasets.core.folder_dataset import TranslateFolder
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

deprecated = types.ModuleType("deprecated")
deprecated.text = features.text


__all__ = [
    "as_dataframe",
    "as_numpy",
    "core",
    "deprecated",
    "folder_dataset",
    "builder",
    "builder_cls",
    "decode",
    "disable_progress_bar",
    "download",
    "features",
    "GenerateMode",
    "ImageFolder",
    "is_dataset_on_gcs",
    "list_builders",
    "load",
    "ReadConfig",
    "Split",
    "show_examples",
    "show_statistics",
    "testing",
    "TranslateFolder",
    "units",
    "visualization",
    "__version__",
]
