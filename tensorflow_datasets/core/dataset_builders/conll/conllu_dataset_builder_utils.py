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

"""Utils for ConllUDatasetBuilder.

This file contains list of reusable tags which are commonly used in CoNLL-U
based datasets.
"""
import collections
from typing import Optional, OrderedDict

from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features.class_label_feature import ClassLabel
from tensorflow_datasets.core.features.sequence_feature import Sequence
from tensorflow_datasets.core.features.text_feature import Text

# Universal part-of-speech tags.
UPOS = (
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CCONJ",
    "DET",
    "INTJ",
    "NOUN",
    "NUM",
    "PART",
    "PRON",
    "PROPN",
    "PUNCT",
    "SCONJ",
    "SYM",
    "VERB",
    "X",
    "_",
)

# Used by universal dependencies datasets.
UNIVERSAL_DEPENDENCIES_FEATURES = collections.OrderedDict({
    "idx": Text(),
    "tokens": Sequence(Text()),
    "lemmas": Sequence(Text()),
    "upos": Sequence(ClassLabel(names=UPOS)),
    "xpos": Sequence(Text()),
    "feats": Sequence(Text()),
    "head": Sequence(Text()),
    "deprel": Sequence(Text()),
    "deps": Sequence(Text()),
    "misc": Sequence(Text()),
    "text": Text(),
})

# Used for the xtreme's UD implementation.
XTREME_POS_FEATURES = collections.OrderedDict({
    "tokens": Sequence(Text()),
    "upos": Sequence(ClassLabel(names=UPOS)),
})


def get_universal_morphology_config(
    language: str,
    features: OrderedDict[str, feature_lib.FeatureConnector],
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> conllu_dataset_builder.ConllUBuilderConfig:
  """Returns a populated Universal Morphology ConllUBuilderConfig.

  Args:
    language: The language of the data used to generate the ConllUBuilderConfig.
    features:  An OrderedDict specifying the features names and their type.
    name: Optional config name. If not given, will be set to be the same as the
      given language.
    description: Optional config description.

  Returns:
    A populated `ConllUBuilderConfig` for a Universal Morphology dataset.
  """
  return conllu_dataset_builder.ConllUBuilderConfig(
      name=name or language,
      description=description or None,
      features=features,
      language=language,
  )
