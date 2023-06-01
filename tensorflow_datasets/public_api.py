# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

from tensorflow_datasets import core
from tensorflow_datasets import typing
from tensorflow_datasets.core import beam_utils as beam
from tensorflow_datasets.core import dataset_builders
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import deprecated
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import folder_dataset
from tensorflow_datasets.core import transform  # pylint: disable=unused-import
from tensorflow_datasets.core import visualization
from tensorflow_datasets.core.as_dataframe import as_dataframe
from tensorflow_datasets.core.dataset_utils import as_numpy
from tensorflow_datasets.core.download import GenerateMode
from tensorflow_datasets.core.folder_dataset import ImageFolder
from tensorflow_datasets.core.folder_dataset import TranslateFolder
from tensorflow_datasets.core.load import builder
from tensorflow_datasets.core.load import builder_cls
from tensorflow_datasets.core.load import data_source
from tensorflow_datasets.core.load import dataset_collection
from tensorflow_datasets.core.load import list_builders
from tensorflow_datasets.core.load import list_dataset_collections
from tensorflow_datasets.core.load import load
from tensorflow_datasets.core.read_only_builder import builder_from_directories
from tensorflow_datasets.core.read_only_builder import builder_from_directory
from tensorflow_datasets.core.splits import Split
from tensorflow_datasets.core.subsplits_utils import even_splits
from tensorflow_datasets.core.subsplits_utils import split_for_jax_process
from tensorflow_datasets.core.utils.benchmark import benchmark
from tensorflow_datasets.core.utils.gcs_utils import is_dataset_on_gcs
from tensorflow_datasets.core.utils.lazy_imports_utils import lazy_imports
from tensorflow_datasets.core.utils.read_config import ReadConfig
from tensorflow_datasets.core.utils.tqdm_utils import disable_progress_bar
from tensorflow_datasets.core.utils.tqdm_utils import display_progress_bar
from tensorflow_datasets.core.utils.tqdm_utils import enable_progress_bar
from tensorflow_datasets.core.visualization import show_examples
from tensorflow_datasets.core.visualization import show_statistics
from tensorflow_datasets.version import __version__

deprecated = core.utils.docs.deprecated(deprecated)

with lazy_imports():
  from tensorflow_datasets import testing  # pylint: disable=g-import-not-at-top
del lazy_imports

__all__ = [
    "as_dataframe",
    "as_numpy",
    "beam",
    "benchmark",
    "builder",
    "builder_cls",
    "builder_from_directory",
    "builder_from_directories",
    "core",
    "data_source",
    "dataset_builders",
    "dataset_collection",
    "decode",
    "deprecated",
    "disable_progress_bar",
    "display_progress_bar",
    "download",
    "enable_progress_bar",
    "even_splits",
    "features",
    "folder_dataset",
    "GenerateMode",
    "ImageFolder",
    "is_dataset_on_gcs",
    "list_builders",
    "list_dataset_collections",
    "load",
    "ReadConfig",
    "Split",
    "split_for_jax_process",
    "show_examples",
    "show_statistics",
    "testing",
    "transform",
    "TranslateFolder",
    "typing",
    "visualization",
    "__version__",
]
