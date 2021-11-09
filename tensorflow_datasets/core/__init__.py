# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
# Ensure TensorFlow is importable and its version is sufficiently recent. This
# needs to happen before anything else, since the imports below will try to
# import tensorflow, too.
from tensorflow_datasets.core import tf_compat

tf_compat.ensure_tf_install()

# pylint:disable=g-import-not-at-top

from tensorflow_datasets.core import community  # pylint: disable=g-bad-import-order
from tensorflow_datasets.core.dataset_builder import BeamBasedBuilder
from tensorflow_datasets.core.dataset_builder import BuilderConfig
from tensorflow_datasets.core.dataset_builder import DatasetBuilder
from tensorflow_datasets.core.dataset_builder import GeneratorBasedBuilder

from tensorflow_datasets.core.dataset_info import BeamMetadataDict
from tensorflow_datasets.core.dataset_info import DatasetInfo
from tensorflow_datasets.core.dataset_info import Metadata
from tensorflow_datasets.core.dataset_info import MetadataDict

from tensorflow_datasets.core.file_adapters import FileFormat

from tensorflow_datasets.core.lazy_imports_lib import lazy_imports

from tensorflow_datasets.core.read_only_builder import builder_from_directory

from tensorflow_datasets.core.registered import DatasetNotFoundError

from tensorflow_datasets.core.split_builder import SplitGeneratorLegacy as SplitGenerator

from tensorflow_datasets.core.splits import Split
from tensorflow_datasets.core.splits import SplitDict
from tensorflow_datasets.core.splits import SplitInfo
from tensorflow_datasets.core.splits import SubSplitInfo

from tensorflow_datasets.core.tfrecords_reader import ReadInstruction

from tensorflow_datasets.core.utils import Experiment
from tensorflow_datasets.core.utils import gcs_path
from tensorflow_datasets.core.utils import tfds_path
from tensorflow_datasets.core.utils import Version
from tensorflow_datasets.core.utils.benchmark import BenchmarkResult
from tensorflow_datasets.core.utils.file_utils import add_data_dir
from tensorflow_datasets.core.utils.generic_path import as_path
from tensorflow_datasets.core.utils.type_utils import PathLike
from tensorflow_datasets.core.utils.type_utils import ReadOnlyPath
from tensorflow_datasets.core.utils.type_utils import ReadWritePath


def benchmark(*args, **kwargs):
  raise DeprecationWarning(
      "`tfds.core.benchmark` has been renamed to `tfds.benchmark`")


__all__ = [
    "add_data_dir",
    "as_path",
    "BenchmarkResult",
    "BeamBasedBuilder",
    "BeamMetadataDict",
    "BuilderConfig",
    "builder_from_directory",
    "DatasetBuilder",
    "DatasetInfo",
    "DatasetNotFoundError",
    "Experiment",
    "FileFormat",
    "GeneratorBasedBuilder",
    "gcs_path",
    "lazy_imports",
    "Metadata",
    "MetadataDict",
    "PathLike",
    "ReadInstruction",
    "ReadOnlyPath",
    "ReadWritePath",
    "SplitDict",
    "SplitGenerator",
    "SplitInfo",
    "tfds_path",
    "Version",
]
