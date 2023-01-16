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

"""story_cloze dataset."""

from __future__ import annotations

import csv
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for story_cloze dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(name='2016', description='2018 year'),
      tfds.core.BuilderConfig(name='2018', description='2018 year'),
  ]
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Visit https://www.cs.rochester.edu/nlp/rocstories/ and fill out the google
  form to obtain the datasets. You will receive an email with the link to
  download the datasets. For the 2016 data, the validation and test file needs
  to be renamed to cloze_test_val__spring2016.csv and
  cloze_test_test__spring2016.csv respectively. For 2018 version, the validation
  and test file needs to be renamed to cloze_test_val__winter2018.csv and
  to cloze_test_test__winter2018.csv respectively. Move both these files
  to the manual directory.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'context': tfds.features.Text(),
            'endings': tfds.features.Sequence(tfds.features.Text()),
            'label': np.int32,
        }),
        supervised_keys=None,  # e.g. ('image', 'label')
        homepage='https://www.cs.rochester.edu/nlp/rocstories/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    if self.builder_config.name == '2016':
      file_postfix = 'spring2016'
    elif self.builder_config.name == '2018':
      file_postfix = 'winter2018'

    val_file = 'cloze_test_val__' + file_postfix + '.csv'
    test_file = 'cloze_test_test__' + file_postfix + '.csv'

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'filepath': os.path.join(dl_manager.manual_dir, val_file)
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'filepath': os.path.join(dl_manager.manual_dir, test_file)
            },
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with epath.Path(filepath).open() as f:
      reader = csv.DictReader(f)
      for row in reader:
        context = ' '.join([
            row['InputSentence1'],
            row['InputSentence2'],
            row['InputSentence3'],
            row['InputSentence4'],
        ])
        endings = [
            row['RandomFifthSentenceQuiz1'],
            row['RandomFifthSentenceQuiz2'],
        ]

        yield row['InputStoryid'], {
            'context': context,
            'endings': endings,
            'label': row.get('AnswerRightEnding', -1),
        }
