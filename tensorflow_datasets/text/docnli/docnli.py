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

"""DocNLI dataset."""

import json

import tensorflow_datasets.public_api as tfds

# Markdown description that will appear on the catalog page.
_DESCRIPTION = """
DocNLI is a large-scale dataset for document-level natural language inference
(NLI). DocNLI is transformed from a broad range of NLP problems and covers
multiple genres of text. The premises always stay in the document granularity,
whereas the hypotheses vary in length from single sentences to passages with
hundreds of words. In contrast to some existing sentence-level NLI datasets,
DocNLI has pretty limited artifacts.
"""

# BibTeX citation
_CITATION = """
@inproceedings{yin-etal-2021-docnli,
    title={DocNLI: A Large-scale Dataset for Document-level Natural Language Inference},
    author={Wenpeng Yin and Dragomir Radev and Caiming Xiong},
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
}
"""

# DocNLI url
_DOCNLI_URL = ('https://drive.google.com/uc?export=download&id='
               '16TZBTZcb9laNKxIvgbs5nOBgq3MhND5s')

_EXTRACT_PATH_TOKEN = 'DocNLI_dataset'


class DocNLI(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for docnli dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'premise':
                tfds.features.Text(),
            'hypothesis':
                tfds.features.Text(),
            # Label indicates whether the premise entails or implies the
            # hypothesis.
            'label':
                tfds.features.ClassLabel(names=['not_entailment', 'entailment']
                                        ),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://github.com/salesforce/DocNLI/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Downloads the data and defines the splits
    data_dir = dl_manager.download_and_extract(_DOCNLI_URL)

    # Returns the Dict[split names, Iterator[Key, Example]]
    return {
        tfds.Split.TRAIN:
            self._generate_examples(path=data_dir / _EXTRACT_PATH_TOKEN /
                                    'train.json'),
        tfds.Split.VALIDATION:
            self._generate_examples(path=data_dir / _EXTRACT_PATH_TOKEN /
                                    'dev.json'),
        tfds.Split.TEST:
            self._generate_examples(path=data_dir / _EXTRACT_PATH_TOKEN /
                                    'test.json'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # Yields (key, example) tuples from the dataset
    data = json.loads(path.read_text())
    for idx, row in enumerate(data):
      yield idx, {
          'premise': row['premise'],
          'hypothesis': row['hypothesis'],
          'label': row['label'],
      }
