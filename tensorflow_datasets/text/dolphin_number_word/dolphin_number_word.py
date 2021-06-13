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

"""dolphin number word dataset."""

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DS_PATH = 'https://www.microsoft.com/en-us/research/uploads/prod/2016/02//dolphin-number_word_std.zip'

_DESCRIPTION = """
Dolphin Math Word Problem dataset (2015), as presented in https://www.microsoft.com/en-us/research/uploads/prod/2016/02//dolphin-sigmadolphin.datasets.pdf
"""

_CITATION = """
@inproceedings{inproceedings,
author = {Shi, Shuming and Wang, Yuehui and Lin, Chin-Yew and Liu, Xiaojiang and Rui, Yong},
year = {2015},
month = {09},
pages = {},
title = {Automatically Solving Number Word Problems by Semantic Parsing and Reasoning},
doi = {10.18653/v1/D15-1135}
}
"""


class DolphinNumberWord(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for dolphin_number_word problem dataset."""
  __count__ = 0

  VERSION = tfds.core.Version('0.0.2')
  RELEASE_NOTES = {
      '0.0.1': 'Initial release.',
      '0.0.2': 'RaggedTensor fix. Equations and Sources represented as a single'
               'string with components delimited by spaces',
      '0.0.3':
          'Reintroduced logic to handle edge-case involving examples without '
          'sources.'
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        # Per author's recommendation, we discard the ans_simple field.
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'index': tf.int32,
            'text': tfds.features.Text(),
            'sources': tfds.features.Text(),  # Flattened list of str.
            'equations': tfds.features.Text(),  # Flattened list of str.
            'ans': tfds.features.Text(),
        }),
        supervised_keys=('text', 'ans'),  # Alternatively text, ans.
        homepage='https://www.microsoft.com/en-us/research/project/sigmadolphin-2/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DS_PATH)
    return {
        'train': self._generate_examples(path, '.dev'),
        'test': self._generate_examples(path, '.test'),
    }

  def _generate_examples(self, json_paths, split):
    """Parses available JSON files in a given split, returns TF examples."""
    # Currently assume all files in archive are json-formatted.
    for file in json_paths.glob('*' + split + '*'):
      json_string = file.read_text()
      examples = json.loads(json_string)
      for e in examples:
        # Per author's recommendation, we discard the ans_simple field.
        e.pop('ans_simple')
        # 'equations' and 'sources' will be a RaggedTensor unless we flatten
        # them into a single string. RaggedTensors are not compatible with
        # t5 tasks.
        if 'sources' in e:
          e['sources'] = '  '.join(e['sources'])
        else:
          e['sources'] = ''
        e['equations'] = '  '.join(e['equations'])
        # Dataset appears to have duplicate entries, we add an internal
        # count to the provided entry's ID to bypass this error.
        e['id'] = e['id'] + str(self.__count__)
        self.__count__ += 1
        yield e['id'], e
