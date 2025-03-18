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

"""openbookQA dataset."""

import json
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """QA dataset with common knowledge facts."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'question': {
                'stem': tfds.features.Text(),
                'choice_A': tfds.features.Text(),
                'choice_B': tfds.features.Text(),
                'choice_C': tfds.features.Text(),
                'choice_D': tfds.features.Text(),
            },
            'fact1': tfds.features.Text(),
            'humanScore': tfds.features.Tensor(shape=(), dtype=np.float32),
            'clarity': tfds.features.Tensor(shape=(), dtype=np.float32),
            'turkIdAnonymized': tfds.features.Text(),
            'answerKey': tfds.features.ClassLabel(names=['A', 'B', 'C', 'D']),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('question', 'answerKey'),
        # Homepage of the dataset for documentation
        homepage='https://leaderboard.allenai.org/open_book_qa/submissions/get-started',
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
                'filepath': os.path.join(data_dir, 'train_complete.jsonl'),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'dev_complete.jsonl'),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'test_complete.jsonl'),
            },
        ),
    ]

  def _generate_examples(self, data_dir, filepath):
    """Yields examples."""

    with epath.Path(filepath).open() as f:
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
            'answerKey': row['answerKey'],
        }
