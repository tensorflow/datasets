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

"""WikipediaToxicitySubtypes from Jigsaw Toxic Comment Classification Challenge."""

import csv
import os

import tensorflow as tf
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

_SUBTYPES_HOMEPAGE = 'https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data'
_MULTILINGUAL_HOMEPAGE = 'https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data'

_COMMON_DESCRIPTION = """
The comments in this dataset come from an archive of Wikipedia talk page
comments. These have been annotated by Jigsaw for toxicity, as well as (for the
main config) a variety of toxicity subtypes, including severe toxicity,
obscenity, threatening language, insulting language, and identity attacks. This
dataset is a replica of the data released for the Jigsaw Toxic Comment
Classification Challenge and Jigsaw Multilingual Toxic Comment Classification
competition on Kaggle, with the test dataset merged with the test_labels
released after the end of the competitions. Test data not used for scoring has
been dropped. This dataset is released under CC0, as is the underlying comment
text.
"""

_SUBTYPES_DESCRIPTION = """
The comments in the WikipediaToxicitySubtypes config are from an archive of
English Wikipedia talk page comments which have been annotated by Jigsaw for
toxicity, as well as five toxicity subtype labels (severe toxicity, obscene,
threat, insult, identity_attack). The toxicity and toxicity subtype labels are
binary values (0 or 1) indicating whether the majority of annotators assigned
that attribute to the comment text. This config is a replica of the data
released for the Jigsaw Toxic Comment Classification Challenge on Kaggle, with
the test dataset joined with the test_labels released after the competition, and
test data not used for scoring dropped.

See the Kaggle documentation
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data
or https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more
details.
"""

_MULTILINGUAL_DESCRIPTION = """
The comments in the WikipediaToxicityMultilingual config here are from an
archive of non-English Wikipedia talk page comments annotated by Jigsaw for
toxicity, with a binary value (0 or 1) indicating whether the majority of
annotators rated the comment text as toxic. The comments in this config are in
multiple different languages (Turkish, Italian, Spanish, Portuguese, Russian,
and French). This config is a replica of the data released for the Jigsaw
Multilingual Toxic Comment Classification on Kaggle, with the test dataset
joined with the test_labels released after the competition.

See the Kaggle documentation
https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data
for more details.
"""

_DOWNLOAD_URL = 'https://storage.googleapis.com/jigsaw-unintended-bias-in-toxicity-classification/wikipedia_toxicity_subtypes_v0.3.zip'

TOXICITY_SUBTYPES = [
    'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack'
]


class WikipediaToxicityConfig(tfds.core.BuilderConfig):
  """Configuration for `WikipediaToxicitySubtypes`."""

  def __init__(self, name: str, description: str, multilingual: bool):
    super(WikipediaToxicityConfig, self).__init__(
        name=name, description=description)
    self.multilingual = multilingual


class WikipediaToxicitySubtypes(tfds.core.GeneratorBasedBuilder):
  """Classification of 295K Wikipedia talk page comments for types of toxicity.

  This version of the Wikipedia Toxicity Subtypes dataset provides access to the
  primary toxicity label annotated by crowd workers, with five additional
  toxicity subtype labels in the main config. The toxicity and toxicity subtype
  labels are binary values (0 or 1) indicating whether the majority of
  annotators assigned that attributes to the comment text.

  While the main config is entirely in English, the
  WikipediaToxicityMultilingual config provides validation and test splits with
  data in several non-English languages (tr, it, es, pt, ru, fr). This config
  provides access only to the primary toxicity label for each comment.
  """
  BUILDER_CONFIGS = [
      WikipediaToxicityConfig(
          name='EnglishSubtypes',
          description=_SUBTYPES_DESCRIPTION,
          multilingual=False),
      WikipediaToxicityConfig(
          name='Multilingual',
          description=_MULTILINGUAL_DESCRIPTION,
          multilingual=True),
  ]

  VERSION = tfds.core.Version('0.3.1')
  RELEASE_NOTES = {
      '0.3.1': ('Added a unique id for each comment. (For the Multilingual '
                'config, these are only unique within each split.)'),
      '0.3.0': 'Added WikipediaToxicityMultilingual config.',
      '0.2.0': 'Updated features for consistency with CivilComments dataset.',
  }

  def _info(self):
    description = _COMMON_DESCRIPTION
    homepage = _MULTILINGUAL_HOMEPAGE if self.builder_config.multilingual else _SUBTYPES_HOMEPAGE

    features = {
        'text': tfds.features.Text(),
        'id': tfds.features.Text(),
        'language': tfds.features.Text()
    }
    labels = ['toxicity']
    if not self.builder_config.multilingual:
      labels += TOXICITY_SUBTYPES

    for label in labels:
      features[label] = tf.float32

    return tfds.core.DatasetInfo(
        builder=self,
        description=description,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=('text', 'toxicity'),
        homepage=homepage,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    file_path_prefix = os.path.join(
        dl_path,
        'wikidata_' + 'multilingual_' * self.builder_config.multilingual)

    split_generators = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'filename': file_path_prefix + 'train.csv'},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'filename': file_path_prefix + 'test.csv'},
        ),
    ]

    if self.builder_config.multilingual:
      # Validation split instead of train for WikipediaToxicityMultilingual.
      split_generators[0] = tfds.core.SplitGenerator(
          name=tfds.Split.VALIDATION,
          gen_kwargs={'filename': file_path_prefix + 'validation.csv'})

    return split_generators

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
        example['id'] = row['id']
        example['language'] = row['lang']
        example['toxicity'] = float(row['toxic'])

        if not self.builder_config.multilingual:
          example['severe_toxicity'] = float(row['severe_toxic'])
          example['identity_attack'] = float(row['identity_hate'])
          for label in ['obscene', 'threat', 'insult']:
            example[label] = float(row[label])

        yield row['id'], example
