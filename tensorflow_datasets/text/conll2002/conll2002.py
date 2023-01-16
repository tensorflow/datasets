# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""conll2002 dataset."""
import collections

from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder
from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder_utils as conll_lib
from tensorflow_datasets.core.features.class_label_feature import ClassLabel
from tensorflow_datasets.core.features.sequence_feature import Sequence
from tensorflow_datasets.core.features.text_feature import Text
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The shared task of CoNLL-2002 concerns language-independent named entity
recognition. The types of named entities include: persons, locations,
organizations and names of miscellaneous entities that do not belong to the
previous three groups. The participants of the shared task were offered training
and test data for at least two languages. Information sources other than the
training data might have been used in this shared task.
"""

_CITATION = """
@inproceedings{tjong-kim-sang-2002-introduction,
    title = "Introduction to the {C}o{NLL}-2002 Shared Task: Language-Independent Named Entity Recognition",
    author = "Tjong Kim Sang, Erik F.",
    booktitle = "{COLING}-02: The 6th Conference on Natural Language Learning 2002 ({C}o{NLL}-2002)",
    year = "2002",
    url = "https://aclanthology.org/W02-2024",
}
"""

_URL = "https://raw.githubusercontent.com/teropa/nlp/master/resources/corpora/conll2002/"

ES_POS_TAGS = (
    "AO",
    "AQ",
    "CC",
    "CS",
    "DA",
    "DE",
    "DD",
    "DI",
    "DN",
    "DP",
    "DT",
    "Faa",
    "Fat",
    "Fc",
    "Fd",
    "Fe",
    "Fg",
    "Fh",
    "Fia",
    "Fit",
    "Fp",
    "Fpa",
    "Fpt",
    "Fs",
    "Ft",
    "Fx",
    "Fz",
    "I",
    "NC",
    "NP",
    "P0",
    "PD",
    "PI",
    "PN",
    "PP",
    "PR",
    "PT",
    "PX",
    "RG",
    "RN",
    "SP",
    "VAI",
    "VAM",
    "VAN",
    "VAP",
    "VAS",
    "VMG",
    "VMI",
    "VMM",
    "VMN",
    "VMP",
    "VMS",
    "VSG",
    "VSI",
    "VSM",
    "VSN",
    "VSP",
    "VSS",
    "Y",
    "Z",
)

NL_POS_TAGS = (
    "Adj",
    "Adv",
    "Art",
    "Conj",
    "Int",
    "Misc",
    "N",
    "Num",
    "Prep",
    "Pron",
    "Punc",
    "V",
)

ES_CONFIG = conll_dataset_builder.ConllBuilderConfig(
    name="es",
    separator=conll_lib.CONLL_2002_SEPARATOR,
    ordered_features=collections.OrderedDict({
        "tokens": Sequence(Text()),
        "pos": Sequence(ClassLabel(names=ES_POS_TAGS)),
        "ner": Sequence(ClassLabel(names=conll_lib.NER_TAGS)),
    }),
)

NL_CONFIG = conll_dataset_builder.ConllBuilderConfig(
    name="nl",
    separator=conll_lib.CONLL_2002_SEPARATOR,
    ordered_features=collections.OrderedDict({
        "tokens": Sequence(Text()),
        "pos": Sequence(ClassLabel(names=NL_POS_TAGS)),
        "ner": Sequence(ClassLabel(names=conll_lib.NER_TAGS)),
    }),
)


class Conll2002(tfds.dataset_builders.ConllDatasetBuilder):
  """DatasetBuilder for conll2002 dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }
  BUILDER_CONFIGS = [ES_CONFIG, NL_CONFIG]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        description=_DESCRIPTION,
        homepage="https://aclanthology.org/W02-2024/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    file_name = "esp" if self.builder_config.name == ES_CONFIG.name else "ned"
    urls_to_download = {
        "train": f"{_URL}{file_name}.train",
        "dev": f"{_URL}{file_name}.testa",
        "test": f"{_URL}{file_name}.testb",
    }

    dl_paths = dl_manager.download(urls_to_download)

    return {
        "train": self._generate_examples(dl_paths["train"]),
        "dev": self._generate_examples(dl_paths["dev"]),
        "test": self._generate_examples(dl_paths["test"]),
    }
