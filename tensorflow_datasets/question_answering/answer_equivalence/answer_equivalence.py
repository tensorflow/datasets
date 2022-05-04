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

"""answer_equivalence dataset."""

import json
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The Answer Equivalence Dataset contains human ratings on model predictions from
several models on the SQuAD dataset. The ratings establish whether the predicted
answer is 'equivalent' to the gold answer (taking into account both question and
context).

More specifically, by 'equivalent' we mean that the predicted answer contains at
least the same information as the gold answer and does not add superfluous
information. The dataset contains annotations for:
  * predictions from BiDAF on SQuAD dev
  * predictions from XLNet on SQuAD dev
  * predictions from Luke on SQuAD dev
  * predictions from Albert on SQuAD training, dev and test examples
"""

_CITATION = """
@article{bulian-etal-2022-tomayto,
      title={Tomayto, Tomahto. Beyond Token-level Answer Equivalence for Question Answering Evaluation},
      author={Jannis Bulian and Christian Buck and Wojciech Gajewski and Benjamin Boerschinger and Tal Schuster},
      year={2022},
      eprint={2202.07654},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""


class AnswerEquivalence(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for answer_equivalence dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'qid': tfds.features.Text(),
            'gold_index': tf.int32,
            'context': tfds.features.Text(),
            'question': tfds.features.Text(),
            'reference': tfds.features.Text(),
            'candidate': tfds.features.Text(),
            'score': tf.float32,
            'question_1': tfds.features.ClassLabel(names=['no', 'yes', 'null']),
            'question_2': tfds.features.ClassLabel(names=['no', 'yes', 'null']),
            'question_3': tfds.features.ClassLabel(names=['no', 'yes', 'null']),
            'question_4': tfds.features.ClassLabel(names=['no', 'yes', 'null']),
        }),
        supervised_keys=None,
        homepage='https://github.com/google-research-datasets/answer-equivalence-dataset',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    homepage = 'https://raw.githubusercontent.com/google-research-datasets/answer-equivalence-dataset/main/v1/'
    archive = {
        'train': os.path.join(homepage, 'train.jsonl'),
        'ae_dev': os.path.join(homepage, 'ae_dev.jsonl'),
        'ae_test': os.path.join(homepage, 'ae_test.jsonl'),
        'dev_xlnet': os.path.join(homepage, 'dev_by_system/dev_xlnet.jsonl'),
        'dev_luke': os.path.join(homepage, 'dev_by_system/dev_luke.jsonl'),
        'dev_bidaf': os.path.join(homepage, 'dev_by_system/dev_bidaf.jsonl')
    }

    paths = dl_manager.download_and_extract(archive)

    return {
        split: self._generate_examples(path) for split, path in paths.items()
    }

  def _generate_examples(self, filepath):
    """Yields examples."""
    with tf.io.gfile.GFile(filepath) as fin:
      for i, line in enumerate(fin):
        data = json.loads(line)
        sample_id = data['qid'] + f'_{i}'
        sample = {
            'qid': data['qid'],
            'gold_index': data['gold_index'],
            'context': data['context'],
            'question': data['question'],
            'reference': data['reference'],
            'candidate': data['candidate'],
            'score': data['score'],
        }
        for j in range(4):
          sample[f'question_{j+1}'] = data['raw_rating'][j]
        yield sample_id, sample
