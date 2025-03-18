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

"""CoNNL dataset builders."""

from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder import ConllBuilderConfig
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder import ConllDatasetBuilder
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder_utils import CHUNK_TAGS
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder_utils import CONLL_2002_SEPARATOR
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder_utils import CONLL_2003_CONFIG
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder_utils import CONLL_2003_ORDERED_FEATURES
from tensorflow_datasets.core.dataset_builders.conll.conll_dataset_builder_utils import POS_TAGS
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder import ConllUBuilderConfig
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder import ConllUDatasetBuilder
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder_utils import get_universal_morphology_config
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder_utils import UNIVERSAL_DEPENDENCIES_FEATURES
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder_utils import UPOS
from tensorflow_datasets.core.dataset_builders.conll.conllu_dataset_builder_utils import XTREME_POS_FEATURES
