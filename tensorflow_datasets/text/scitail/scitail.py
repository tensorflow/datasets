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

"""scitail dataset."""

import csv

from etils import epath
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The SciTail dataset is an entailment dataset created from multiple-choice
science exams and web sentences. Each question and the correct answer choice
are converted into an assertive statement to form the hypothesis. Information
retrieval is used to obtain relevant text from a large text corpus of web
sentences, and these sentences are used as a premise P. The annotation of such
premise-hypothesis pair is crowdsourced as supports (entails) or not (neutral),
in order to create the SciTail dataset. The dataset contains 27,026 examples
with 10,101 examples with entails label and 16,925 examples with neutral label.
"""

_CITATION = """
@inproceedings{khot2018scitail,
    title={Scitail: A textual entailment dataset from science question answering},
    author={Khot, Tushar and Sabharwal, Ashish and Clark, Peter},
    booktitle={Proceedings of the 32th AAAI Conference on Artificial Intelligence (AAAI 2018)},
    url = "http://ai2-website.s3.amazonaws.com/publications/scitail-aaai-2018_cameraready.pdf",
    year={2018}
}
"""

_URL = 'http://data.allenai.org.s3.amazonaws.com/downloads/SciTailV1.1.zip'
_SCITAIL_DIR = 'SciTailV1.1'
_TSV_DIR = 'tsv_format'


class SciTail(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for scitail dataset."""

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
            'premise': tfds.features.Text(),
            'hypothesis': tfds.features.Text(),
            # Label indicates whether the premise entails or implies the
            # hypothesis.
            'label': tfds.features.ClassLabel(names=['entails', 'neutral']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://allenai.org/data/scitail',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Downloads the data and defines the splits
    data_dir = dl_manager.download_and_extract(_URL)

    # Returns the Dict[split names, Iterator[Key, Example]]
    return {
        tfds.Split.TRAIN:
            self._generate_examples(path=data_dir / _SCITAIL_DIR / _TSV_DIR /
                                    'scitail_1.0_train.tsv'),
        tfds.Split.VALIDATION:
            self._generate_examples(path=data_dir / _SCITAIL_DIR / _TSV_DIR /
                                    'scitail_1.0_dev.tsv'),
        tfds.Split.TEST:
            self._generate_examples(path=data_dir / _SCITAIL_DIR / _TSV_DIR /
                                    'scitail_1.0_test.tsv'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with epath.Path(path).open() as f:
      data = csv.reader(f, delimiter='\t')
      for id_, row in enumerate(data):
        yield id_, {'premise': row[0], 'hypothesis': row[1], 'label': row[2]}
