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

"""openbookQA dataset."""

import json
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{mihaylov2018can,
  title={Can a suit of armor conduct electricity? a new dataset for open book question answering},
  author={Mihaylov, Todor and Clark, Peter and Khot, Tushar and Sabharwal, Ashish},
  journal={arXiv preprint arXiv:1809.02789},
  year={2018}
}
"""

_DESCRIPTION = """
The dataset contains 5,957 4-way multiple choice questions. Additionally, they
provide 5,167 crowd-sourced common knowledge facts, and an expanded version of
the train/dev/test questions where each question is associated with its
originating core fact, a human accuracy score, a clarity score, and an
anonymized crowd-worker ID.
"""


class Openbookqa(tfds.core.GeneratorBasedBuilder):
  """QA dataset with common knowledge facts."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'question': {
                'stem': tfds.features.Text(),
                'choice_A': tfds.features.Text(),
                'choice_B': tfds.features.Text(),
                'choice_C': tfds.features.Text(),
                'choice_D': tfds.features.Text(),
            },
            'fact1': tfds.features.Text(),
            'humanScore': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'clarity': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'turkIdAnonymized': tfds.features.Text(),
            'answerKey': tfds.features.ClassLabel(names=['A', 'B', 'C', 'D'])
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('question', 'answerKey'),
        # Homepage of the dataset for documentation
        homepage='https://leaderboard.allenai.org/open_book_qa/submissions/get-started',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    download_url = 'https://s3-us-west-2.amazonaws.com/ai2-website/data/OpenBookQA-V1-Sep2018.zip'
    dl_dir = dl_manager.download_and_extract(download_url)
    data_dir = os.path.join(dl_dir, 'OpenBookQA-V1-Sep2018/Data/Additional')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'train_complete.jsonl')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'dev_complete.jsonl')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'test_complete.jsonl')
            },
        ),
    ]

  def _generate_examples(self, data_dir, filepath):
    """Yields examples."""

    with tf.io.gfile.GFile(filepath) as f:
      for line in f:
        row = json.loads(line)
        question = {}
        question['stem'] = row['question']['stem']
        choices = row['question']['choices']
        question['choice_A'] = choices[0]['text']
        question['choice_B'] = choices[1]['text']
        question['choice_C'] = choices[2]['text']
        question['choice_D'] = choices[3]['text']

        yield row['id'], {
            'question': question,
            'fact1': row['fact1'],
            'humanScore': row['humanScore'],
            'clarity': row['clarity'],
            'turkIdAnonymized': row['turkIdAnonymized'],
            'answerKey': row['answerKey']
        }
