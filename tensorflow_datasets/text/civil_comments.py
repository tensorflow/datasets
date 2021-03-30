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

"""CivilComments from Jigsaw Unintended Bias Kaggle Competition."""

import csv
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{DBLP:journals/corr/abs-1903-04561,
  author    = {Daniel Borkan and
               Lucas Dixon and
               Jeffrey Sorensen and
               Nithum Thain and
               Lucy Vasserman},
  title     = {Nuanced Metrics for Measuring Unintended Bias with Real Data for Text
               Classification},
  journal   = {CoRR},
  volume    = {abs/1903.04561},
  year      = {2019},
  url       = {http://arxiv.org/abs/1903.04561},
  archivePrefix = {arXiv},
  eprint    = {1903.04561},
  timestamp = {Sun, 31 Mar 2019 19:01:24 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1903-04561},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_COMMON_DESCRIPTION = """
This version of the CivilComments Dataset provides access to the primary
seven labels that were annotated by crowd workers, the toxicity and other
tags are a value between 0 and 1 indicating the fraction of annotators that
assigned these attributes to the comment text.

The other tags are only available for a fraction of the input examples. They
are currently ignored for the main dataset; the CivilCommentsIdentities set
includes those labels, but only consists of the subset of the data with them.
The other attributes that were part of the original CivilComments release are
included only in the raw data. See the Kaggle documentation for more details
about the available features.

The comments in this dataset come from an archive of the Civil Comments
platform, a commenting plugin for independent news sites. These public comments
were created from 2015 - 2017 and appeared on approximately 50 English-language
news sites across the world. When Civil Comments shut down in 2017, they chose
to make the public comments available in a lasting open archive to enable future
research. The original data, published on figshare, includes the public comment
text, some associated metadata such as article IDs, timestamps and
commenter-generated "civility" labels, but does not include user ids. Jigsaw
extended this dataset by adding additional labels for toxicity and identity
mentions. This data set is an exact replica of the data released for the
Jigsaw Unintended Bias in Toxicity Classification Kaggle challenge. This
dataset is released under CC0, as is the underlying comment text.
"""

_CC_DESCRIPTION = """

The CivilComments set here includes all the data, but only the basic seven
labels (toxicity, severe_toxicity, obscene, threat, insult, identity_attack, and
sexual_explicit).
"""

_CC_IDENTITIES_DESCRIPTION = """
The CivilCommentsIdentities set here includes an extended set of identity labels
in addition to the basic seven labels. However, it only includes the subset
(roughly a quarter) of the data with all these features.
"""

_DOWNLOAD_URL = 'https://storage.googleapis.com/jigsaw-unintended-bias-in-toxicity-classification/civil_comments.zip'

IDENTITY_LABELS = [
    'male', 'female', 'transgender', 'other_gender', 'heterosexual',
    'homosexual_gay_or_lesbian', 'bisexual', 'other_sexual_orientation',
    'christian', 'jewish', 'muslim', 'hindu', 'buddhist', 'atheist',
    'other_religion', 'black', 'white', 'asian', 'latino',
    'other_race_or_ethnicity', 'physical_disability',
    'intellectual_or_learning_disability', 'psychiatric_or_mental_illness',
    'other_disability'
]


class CivilCommentsConfig(tfds.core.BuilderConfig):
  """Configuration for `CivilComments`."""

  def __init__(self, name, description, include_identity_labels):
    super(CivilCommentsConfig, self).__init__(
        name=name, description=description, version=tfds.core.Version('1.0.1'))
    self.include_identity_labels = include_identity_labels


class CivilComments(tfds.core.GeneratorBasedBuilder):
  """Classification and tagging of 2M comments on news sites.

  This version of the CivilComments Dataset provides access to the primary
  seven labels that were annotated by crowd workers, the toxicity and other
  tags are a value between 0 and 1 indicating the fraction of annotators that
  assigned these attributes to the comment text.

  The other tags are only available for a fraction of the input examples. They
  are currently ignored for the main dataset; the CivilCommentsIdentities set
  includes those labels, but only consists of the subset of the data with them.
  The other attributes that were part of the original CivilComments release are
  included only in the raw data. See the Kaggle documentation for more details
  about the available features.
  """

  BUILDER_CONFIGS = [
      CivilCommentsConfig(
          name='CivilComments',
          description=_CC_DESCRIPTION,
          include_identity_labels=False),
      CivilCommentsConfig(
          name='CivilCommentsIdentities',
          description=_CC_IDENTITIES_DESCRIPTION,
          include_identity_labels=True),
  ]

  def _info(self):
    features = {'text': tfds.features.Text()}
    labels = [
        'id', 'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult',
        'identity_attack', 'sexual_explicit'
    ]
    if self.builder_config.include_identity_labels:
      labels += IDENTITY_LABELS

    for label in labels:
      features[label] = tf.float32

    return tfds.core.DatasetInfo(
        builder=self,
        description=_COMMON_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        # The supervised_keys version is very impoverished.
        supervised_keys=('text', 'toxicity'),
        homepage='https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filename':
                    os.path.join(dl_path, 'train.csv'),
                'toxicity_label':
                    'target',
                'include_identity_labels':
                    self.builder_config.include_identity_labels,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'filename':
                    os.path.join(dl_path, 'test_public_expanded.csv'),
                'toxicity_label':
                    'toxicity',
                'include_identity_labels':
                    self.builder_config.include_identity_labels,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'filename':
                    os.path.join(dl_path, 'test_private_expanded.csv'),
                'toxicity_label':
                    'toxicity',
                'include_identity_labels':
                    self.builder_config.include_identity_labels,
            },
        ),
    ]

  def _parse_row_as_example(self, row, toxicity_label, other_labels):
    example = {}
    example['id'] = row['id']
    example['text'] = row['comment_text']
    example['toxicity'] = float(row[toxicity_label])

    for label in other_labels:
      if not row[label] and label in IDENTITY_LABELS:
        return
      example[label] = float(row[label])
    return example

  def _generate_examples(self, filename, toxicity_label,
                         include_identity_labels):
    """Yields examples.

    Each example contains a text input followed by several toxicity subtype
    scores and identity labels if include_identity_labels is True.

    Args:
      filename: the path of the file to be read for this split.
      toxicity_label: indicates 'target' or 'toxicity' to capture the variation
        in the released labels for this dataset.
      include_identity_labels: Whether to include the additional extended set of
        identity labels. In this case, only those examples with values for all
        labels are yielded.

    Yields:
      A dictionary of features, all floating point except the input text.
    """
    labels = [
        'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack',
        'sexual_explicit'
    ]
    if include_identity_labels:
      labels += IDENTITY_LABELS

    with tf.io.gfile.GFile(filename) as f:
      reader = csv.DictReader(f)
      for row in reader:
        example = self._parse_row_as_example(row, toxicity_label, labels)
        if example:
          yield row['id'], example
