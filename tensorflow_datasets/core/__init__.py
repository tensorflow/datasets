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

"""API to define datasets."""

# Allow to use `tfds.core.Path` in dataset implementation which seems more
# natural than having to import a third party module.
from etils.epath import Path

from tensorflow_datasets.core import community
from tensorflow_datasets.core.dataset_builder import BeamBasedBuilder
from tensorflow_datasets.core.dataset_builder import BuilderConfig
from tensorflow_datasets.core.dataset_builder import DatasetBuilder
from tensorflow_datasets.core.dataset_builder import GeneratorBasedBuilder

from tensorflow_datasets.core.dataset_info import BeamMetadataDict
from tensorflow_datasets.core.dataset_info import DatasetIdentity
from tensorflow_datasets.core.dataset_info import DatasetInfo
from tensorflow_datasets.core.dataset_info import Metadata
from tensorflow_datasets.core.dataset_info import MetadataDict

from tensorflow_datasets.core.example_serializer import ExampleSerializer

from tensorflow_datasets.core.file_adapters import FileFormat

from tensorflow_datasets.core.lazy_imports_lib import lazy_imports

from tensorflow_datasets.core.load import DatasetCollectionLoader

from tensorflow_datasets.core.naming import ShardedFileTemplate

from tensorflow_datasets.core.registered import DatasetNotFoundError

from tensorflow_datasets.core.sequential_writer import SequentialWriter

from tensorflow_datasets.core.split_builder import SplitGeneratorLegacy as SplitGenerator

from tensorflow_datasets.core.splits import ReadInstruction
from tensorflow_datasets.core.splits import Split
from tensorflow_datasets.core.splits import SplitDict
from tensorflow_datasets.core.splits import SplitInfo
from tensorflow_datasets.core.splits import SubSplitInfo

from tensorflow_datasets.core.utils import Experiment
from tensorflow_datasets.core.utils import gcs_path
from tensorflow_datasets.core.utils import lazy_imports_utils
from tensorflow_datasets.core.utils import tfds_path
from tensorflow_datasets.core.utils import Version
from tensorflow_datasets.core.utils.benchmark import BenchmarkResult
from tensorflow_datasets.core.utils.file_utils import add_data_dir
from tensorflow_datasets.core.utils.file_utils import as_path


def benchmark(*args, **kwargs):
  raise DeprecationWarning(
      "`tfds.core.benchmark` has been renamed to `tfds.benchmark`"
  )


__all__ = [
    "add_data_dir",
    "as_path",
    "BenchmarkResult",
    "BeamBasedBuilder",
    "BeamMetadataDict",
    "BuilderConfig",
    "DatasetBuilder",
    "DatasetCollectionLoader",
    "DatasetInfo",
    "DatasetIdentity",
    "DatasetNotFoundError",
    "Experiment",
    "FileFormat",
    "GeneratorBasedBuilder",
    "gcs_path",
    "lazy_imports",
    "Metadata",
    "MetadataDict",
    "Path",
    "ReadInstruction",
    "SequentialWriter",
    "ShardedFileTemplate",
    "SplitDict",
    "SplitGenerator",
    "SplitInfo",
    "tfds_path",
    "Version",
]
