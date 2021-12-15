# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """Story Cloze Test is a new commonsense reasoning framework
for evaluating story understanding, story generation, and script learning.
This test requires a system to choose the correct ending to a four-sentence
story.
"""

_CITATION = """@inproceedings{sharma-etal-2018-tackling,
    title = "Tackling the Story Ending Biases in The Story Cloze Test",
    author = "Sharma, Rishi  and
      Allen, James  and
      Bakhshandeh, Omid  and
      Mostafazadeh, Nasrin",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P18-2119",
    doi = "10.18653/v1/P18-2119",
    pages = "752--757",
    abstract = "The Story Cloze Test (SCT) is a recent framework for evaluating story comprehension and script learning. There have been a variety of models tackling the SCT so far. Although the original goal behind the SCT was to require systems to perform deep language understanding and commonsense reasoning for successful narrative understanding, some recent models could perform significantly better than the initial baselines by leveraging human-authorship biases discovered in the SCT dataset. In order to shed some light on this issue, we have performed various data analysis and analyzed a variety of top performing models presented for this task. Given the statistics we have aggregated, we have designed a new crowdsourcing scheme that creates a new SCT dataset, which overcomes some of the biases. We benchmark a few models on the new dataset and show that the top-performing model on the original SCT dataset fails to keep up its performance. Our findings further signify the importance of benchmarking NLP systems on various evolving test sets.",
}
"""


class StoryCloze(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for story_cloze dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(name='2016', description='2018 year'),
      tfds.core.BuilderConfig(name='2018', description='2018 year')
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
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'context': tfds.features.Text(),
            'endings': tfds.features.Sequence(tfds.features.Text()),
            'label': tf.int32,
        }),
        supervised_keys=None,  # e.g. ('image', 'label')
        homepage='https://www.cs.rochester.edu/nlp/rocstories/',
        citation=_CITATION,
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
    with tf.io.gfile.GFile(filepath) as f:
      reader = csv.DictReader(f)
      for row in reader:
        context = ' '.join([
            row['InputSentence1'], row['InputSentence2'], row['InputSentence3'],
            row['InputSentence4']
        ])
        endings = [
            row['RandomFifthSentenceQuiz1'], row['RandomFifthSentenceQuiz2']
        ]

        yield row['InputStoryid'], {
            'context': context,
            'endings': endings,
            'label': row.get('AnswerRightEnding', -1),
        }
