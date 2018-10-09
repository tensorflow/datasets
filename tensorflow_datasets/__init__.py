# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""`tensorflow_datasets` package.

`tensorflow_datasets` (`tfds`) defines a collection of datasets ready-to-use
with TensorFlow.

Each dataset is defined as a `tfds.DatasetBuilder`.
"""
# pylint: disable=g-multiple-import
from tensorflow_datasets.core.dataset_builder import DatasetBuilder
from tensorflow_datasets.core.dataset_builder import Split
from tensorflow_datasets.core.registered import builder, list_builders, load

# Imports for registration
import tensorflow_datasets.image.cifar
import tensorflow_datasets.image.mnist

from tensorflow.python.util.all_util import remove_undocumented

__all__ = [
    "DatasetBuilder",
    "Split",
    "builder",
    "list_builders",
    "load",
]

remove_undocumented(__name__, __all__)
