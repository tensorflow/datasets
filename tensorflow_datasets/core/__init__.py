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

"""API to define datasets."""

from tensorflow_datasets.core.dataset_builder import BeamBasedBuilder
from tensorflow_datasets.core.dataset_builder import BuilderConfig
from tensorflow_datasets.core.dataset_builder import DatasetBuilder
from tensorflow_datasets.core.dataset_builder import GeneratorBasedBuilder

from tensorflow_datasets.core.dataset_info import DatasetInfo
from tensorflow_datasets.core.dataset_info import Metadata
from tensorflow_datasets.core.dataset_info import MetadataDict

from tensorflow_datasets.core.lazy_imports import lazy_imports

from tensorflow_datasets.core.splits import NamedSplit
from tensorflow_datasets.core.splits import SplitBase
from tensorflow_datasets.core.splits import SplitDict
from tensorflow_datasets.core.splits import SplitGenerator
from tensorflow_datasets.core.splits import SplitInfo
from tensorflow_datasets.core.utils import Experiment
from tensorflow_datasets.core.utils import get_tfds_path
from tensorflow_datasets.core.utils import Version

__all__ = [
    "lazy_imports",
    "BeamBasedBuilder",
    "BuilderConfig",
    "DatasetBuilder",
    "Experiment",
    "GeneratorBasedBuilder",
    "get_tfds_path",
    "DatasetInfo",
    "NamedSplit",
    "Metadata",
    "MetadataDict",
    "SplitBase",
    "SplitDict",
    "SplitGenerator",
    "SplitInfo",
    "Version",
]
