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

"""MathQA dataset."""

import json
import os
import re

from etils import epath
import tensorflow_datasets.public_api as tfds

_URL = 'https://math-qa.github.io/data/MathQA.zip'

_FEATURES = [
    'Problem',
    'Rationale',
    'options',
    'correct',
    'annotated_formula',
    'linear_formula',
    'category',
    'correct_option',
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for math_qa dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {k: tfds.features.Text() for k in _FEATURES}
        ),
        supervised_keys=None,
        homepage='https://math-qa.github.io/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)
    return {
        tfds.Split.TRAIN: self._generate_examples(
            os.path.join(path, 'train.json')
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            os.path.join(path, 'dev.json')
        ),
        tfds.Split.TEST: self._generate_examples(
            os.path.join(path, 'test.json')
        ),
    }

  def _generate_examples(self, filename: str):
    """Yields examples."""
    with epath.Path(filename).open() as f:
      for i, ex in enumerate(json.load(f)):
        ex['correct_option'] = extract_answer_text(ex['options'], ex['correct'])
        yield i, ex


def extract_answer_text(options_text: str, answer_tag: str):
  """Extracts correct answer's text from all options.

  Args:
    options_text: all options as text in various format.
    answer_tag: correct answers tag a, b, c, ...

  Returns:
    parsed option text corresponding to the correct answer.
  """
  if options_text.startswith('[') and options_text.endswith(']'):
    options = eval(options_text)  # pylint: disable = eval-used
    options = [re.sub('[abcde] \\)', '', x).strip() for x in options]
  else:
    options = re.split('[abcde] \\)', options_text)
    if options[0]:
      raise ValueError(f'Expects first segment to be empty in {options}.')
    options = [x.strip().rstrip(',').strip() for x in options[1:]]
  correct_id = ord(answer_tag) - ord('a')
  if correct_id >= len(options):
    raise ValueError(f'Ill parsed dictionary {options} from {options_text}.')
  return options[correct_id]
