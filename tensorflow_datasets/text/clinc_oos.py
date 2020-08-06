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

"""clinc_oos dataset."""

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = 'https://github.com/jereliu/datasets/raw/master/clinc_oos.zip'

_CITATION = """
@inproceedings{larson-etal-2019-evaluation,
    title = "An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction",
    author = "Larson, Stefan  and
      Mahendran, Anish  and
      Peper, Joseph J.  and
      Clarke, Christopher  and
      Lee, Andrew  and
      Hill, Parker  and
      Kummerfeld, Jonathan K.  and
      Leach, Kevin  and
      Laurenzano, Michael A.  and
      Tang, Lingjia  and
      Mars, Jason",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1131",
    doi = "10.18653/v1/D19-1131",
    pages = "1311--1316",
}
"""

_DESCRIPTION = """
Task-oriented dialog systems need to know when a query falls outside their range of supported intents, but current text classification corpora only define label sets that cover every example. We introduce a new dataset that includes queries that are out-of-scope (OOS), i.e., queries that do not fall into any of the system's supported intents. This poses a new challenge because models cannot assume that every query at inference time belongs to a system-supported intent class. Our dataset also covers 150 intent classes over 10 domains, capturing the breadth that a production task-oriented agent must handle. It offers a way of more rigorously and realistically benchmarking text classification in task-driven dialog systems.
"""


class ClincOOS(tfds.core.GeneratorBasedBuilder):
  """CLINC Dataset for Intent Classification and Out-of-Scope (OOS) Detection.

  This dataset is for evaluating the performance of intent classification
  systems in the presence of "out-of-scope" queries. By "out-of-scope",
  we mean queries that do not fall into any of the system-supported intent
  classes. Most datasets include only data that is "in-scope".
  Our dataset includes both in-scope and out-of-scope data.

  This version of the CLINC OOS dataset contains 150 "in-scope" intents from
  10 domains. Each intent has 100 train, 20 validation, and 30 test samples.
  There are 100 train and validation out-of-scope samples, and 1000 out-of-scope
  test samples. It also contains labels for intent domain which are not included
  in the original dataset.
  """

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(clinc_oos): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'text': tfds.features.Text(),
            'intent': tf.int32,
            'domain': tf.int32,
            'intent_name': tfds.features.Text(),
            'domain_name': tfds.features.Text()
        }),
        supervised_keys=('text', 'intent'),
        homepage='https://github.com/clinc/oos-eval/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name='train',
            gen_kwargs={'filename': os.path.join(data_path, 'train.csv')},
        ),
        tfds.core.SplitGenerator(
            name='test',
            gen_kwargs={'filename': os.path.join(data_path, 'test.csv')},
        ),
        tfds.core.SplitGenerator(
            name='validation',
            gen_kwargs={'filename': os.path.join(data_path, 'val.csv')},
        ),
        tfds.core.SplitGenerator(
            name='train_oos',
            gen_kwargs={'filename': os.path.join(data_path, 'train_ood.csv')},
        ),
        tfds.core.SplitGenerator(
            name='test_oos',
            gen_kwargs={'filename': os.path.join(data_path, 'test_ood.csv')},
        ),
        tfds.core.SplitGenerator(
            name='validation_oos',
            gen_kwargs={'filename': os.path.join(data_path, 'val_ood.csv')},
        ),
    ]

  def _generate_examples(self, filename):
    """Yields examples."""
    with tf.io.gfile.GFile(filename) as f:
      reader = csv.DictReader(f)
      for row_id, row in enumerate(reader):
        example = {}
        example['text'] = row['text']
        example['intent'] = row['intent']
        example['domain'] = row['domain']
        example['intent_name'] = row['intent_name']
        example['domain_name'] = row['domain_name']

        yield row_id, example
