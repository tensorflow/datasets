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

"""WikipediaToxicitySubtypes from Jigsaw Toxic Comment Classification Challenge."""

import csv
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{10.1145/3038912.3052591,
  author = {Wulczyn, Ellery and Thain, Nithum and Dixon, Lucas},
  title = {Ex Machina: Personal Attacks Seen at Scale},
  year = {2017},
  isbn = {9781450349130},
  publisher = {International World Wide Web Conferences Steering Committee},
  address = {Republic and Canton of Geneva, CHE},
  url = {https://doi.org/10.1145/3038912.3052591},
  doi = {10.1145/3038912.3052591},
  booktitle = {Proceedings of the 26th International Conference on World Wide Web},
  pages = {1391-1399},
  numpages = {9},
  keywords = {online discussions, wikipedia, online harassment},
  location = {Perth, Australia},
  series = {WWW '17}
}
"""

_DESCRIPTION = """
This version of the Wikipedia Toxicity Subtypes dataset provides access to the
primary toxicity label, as well the five toxicity subtype labels annotated by
crowd workers. The toxicity and toxicity subtype labels are binary values
(0 or 1) indicating whether the majority of annotators assigned that
attributes to the comment text.

The comments in this dataset come from an archive of Wikipedia talk pages
comments. These have been annotated by Jigsaw for toxicity, as well as a variety
of toxicity subtypes, including severe toxicity, obscenity, threatening
language, insulting language, and identity attacks. This dataset is a replica of
the data released for the Jigsaw Toxic Comment Classification Challenge on
Kaggle, with the training set unchanged, and the test dataset merged with the
test_labels released after the end of the competition. Test data not used for
scoring has been dropped. This dataset is released under CC0, as is the
underlying comment text.

See the Kaggle documentation or
https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more
details.
"""

_DOWNLOAD_URL = 'https://storage.googleapis.com/jigsaw-unintended-bias-in-toxicity-classification/wikipedia_toxicity_subtypes.zip'


class WikipediaToxicitySubtypes(tfds.core.GeneratorBasedBuilder):
  """Classification of 220K Wikipedia talk page comments for types of toxicity.

  This version of the Wikipedia Toxicity Subtypes dataset provides access to the
  primary toxicity label, as well the five toxicity subtype labels annotated by
  crowd workers. The toxicity and toxicity subtype labels are binary values
  (0 or 1) indicating whether the majority of annotators assigned that
  attributes to the comment text.

  See the Kaggle documentation or
  https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more
  details.
  """
  VERSION = tfds.core.Version('0.2.0')
  RELEASE_NOTES = {
      '0.2.0': 'Updated features for consistency with CivilComments dataset.',
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'text': tfds.features.Text(),
            'toxicity': tf.float32,
            'severe_toxicity': tf.float32,
            'obscene': tf.float32,
            'threat': tf.float32,
            'insult': tf.float32,
            'identity_attack': tf.float32,
        }),
        supervised_keys=('text', 'toxicity'),
        homepage='https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filename': os.path.join(dl_path, 'wikidata_train.csv')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'filename': os.path.join(dl_path, 'wikidata_test.csv')},
        ),
    ]

  def _generate_examples(self, filename):
    """Yields examples.

    Each example contains a text input and then six annotation labels.

    Args:
      filename: the path of the file to be read for this split.

    Yields:
      A dictionary of features, all floating point except the input text.
    """
    with tf.io.gfile.GFile(filename) as f:
      reader = csv.DictReader(f)
      for row in reader:
        example = {}
        example['text'] = row['comment_text']
        example['toxicity'] = float(row['toxic'])
        example['severe_toxicity'] = float(row['severe_toxic'])
        example['identity_attack'] = float(row['identity_hate'])
        for label in ['obscene', 'threat', 'insult']:
          example[label] = float(row[label])
        yield row['id'], example
