# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""The Cosmos QA dataset."""

import csv
import json

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{huang-etal-2019-cosmos,
    title = "Cosmos {QA}: Machine Reading Comprehension with Contextual Commonsense Reasoning",
    author = "Huang, Lifu  and
      Le Bras, Ronan  and
      Bhagavatula, Chandra  and
      Choi, Yejin",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    year = "2019",
    url = "https://www.aclweb.org/anthology/D19-1243"
}
"""

_DESCRIPTION = """\
Cosmos QA is a large-scale dataset of 35.6K problems that require
 commonsense-based reading comprehension, formulated as multiple-choice
 questions. It focuses on reading between the lines over a diverse collection
 of people's everyday narratives, asking questions concerning on the likely
 causes or effects of events that require reasoning beyond the exact text
 spans in the context.
"""

_SPLIT_DOWNLOAD_URL = {
    'train':
        'https://raw.githubusercontent.com/wilburOne/cosmosqa/master/data/train.csv',
    'validation':
        'https://raw.githubusercontent.com/wilburOne/cosmosqa/master/data/valid.csv',
    'test':
        'https://raw.githubusercontent.com/wilburOne/cosmosqa/master/data/test.jsonl'
}


class CosmosQA(tfds.core.GeneratorBasedBuilder):
  """The Cosmos QA dataset."""
  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'context': tfds.features.Text(),
            'question': tfds.features.Text(),
            'answer0': tfds.features.Text(),
            'answer1': tfds.features.Text(),
            'answer2': tfds.features.Text(),
            'answer3': tfds.features.Text(),
            # Label indicates which of the answers is correct.
            'label': tfds.features.ClassLabel(names=['0', '1', '2', '3']),
            'id': tfds.features.Text(),
        }),
        # No default supervised_keys
        supervised_keys=None,
        homepage='https://wilburone.github.io/cosmos/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_paths = dl_manager.download(_SPLIT_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=split, gen_kwargs={'file_path': file_path})
        for split, file_path in file_paths.items()
    ]

  def _generate_examples(self, file_path):
    """This function returns the examples in the raw (text) form."""
    with tf.io.gfile.GFile(file_path) as f:
      # Test is in jsonl format whereas train and dev in tsv.
      if file_path.suffix == '.jsonl':
        for line in f:
          row = json.loads(line)
          row['label'] = -1
          yield row['id'], row
      else:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
          yield row['id'], row
