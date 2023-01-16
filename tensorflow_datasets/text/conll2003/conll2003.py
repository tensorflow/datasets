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

"""conll2003 dataset."""

from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder_utils as conll_lib
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The shared task of CoNLL-2003 concerns language-independent named entity
recognition and concentrates on four types of named entities: persons,
locations, organizations and names of miscellaneous entities that do not belong
to the previous three groups.
"""

_CITATION = """
@inproceedings{tjong-kim-sang-de-meulder-2003-introduction,
    title = "Introduction to the {C}o{NLL}-2003 Shared Task: Language-Independent Named Entity Recognition",
    author = "Tjong Kim Sang, Erik F.  and
      De Meulder, Fien",
    booktitle = "Proceedings of the Seventh Conference on Natural Language Learning at {HLT}-{NAACL} 2003",
    year = "2003",
    url = "https://www.aclweb.org/anthology/W03-0419",
    pages = "142--147",
}
"""


class Conll2003(tfds.dataset_builders.ConllDatasetBuilder):
  """DatasetBuilder for conll2003 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [conll_lib.CONLL_2003_CONFIG]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        description=_DESCRIPTION,
        homepage='https://www.aclweb.org/anthology/W03-0419/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        'https://data.deepai.org/conll2003.zip'
    )

    return {
        'train': self._generate_examples(path / 'train.txt'),
        'dev': self._generate_examples(path / 'valid.txt'),
        'test': self._generate_examples(path / 'test.txt'),
    }
