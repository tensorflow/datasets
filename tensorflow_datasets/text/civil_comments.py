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

"""CivilComments from Jigsaw Unintended Bias Kaggle Competition."""

import ast
import csv
import os

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# General (main) citation for CivilComments and CivilCommentsIdentities.
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

# Citation for CivilCommentsCovert.
_COVERT_CITATION = """
@inproceedings{lees-etal-2021-capturing,
    title = "Capturing Covertly Toxic Speech via Crowdsourcing",
    author = "Lees, Alyssa  and
      Borkan, Daniel  and
      Kivlichan, Ian  and
      Nario, Jorge  and
      Goyal, Tesh",
    booktitle = "Proceedings of the First Workshop on Bridging Human{--}Computer Interaction and Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.hcinlp-1.3",
    pages = "14--20"
}
"""

# Citation for CivilComments Toxic Spans.
_SPANS_CITATION = """
@inproceedings{pavlopoulos-etal-2021-semeval,
    title = "{S}em{E}val-2021 Task 5: Toxic Spans Detection",
    author = "Pavlopoulos, John  and Sorensen, Jeffrey  and Laugier, L{\'e}o and Androutsopoulos, Ion",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.6",
    doi = "10.18653/v1/2021.semeval-1.6",
    pages = "59--69",
}
"""

# Citation for CivilComments Context.
_CONTEXT_CITATION = """
@misc{pavlopoulos2020toxicity,
    title={Toxicity Detection: Does Context Really Matter?},
    author={John Pavlopoulos and Jeffrey Sorensen and Lucas Dixon and Nithum Thain and Ion Androutsopoulos},
    year={2020}, eprint={2006.00998}, archivePrefix={arXiv}, primaryClass={cs.CL}
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
extended this dataset by adding additional labels for toxicity, identity
mentions, as well as covert offensiveness. This data set is an exact replica of
the data released for the Jigsaw Unintended Bias in Toxicity Classification
Kaggle challenge. This dataset is released under CC0, as is the underlying
comment text.

For comments that have a parent_id also in the civil comments data, the
text of the previous comment is provided as the "parent_text" feature. Note
that the splits were made without regard to this information, so using previous
comments may leak some information. The annotators did not have access to the
parent text when making the labels.
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

_CC_COVERT_DESCRIPTION = """
The CivilCommentsCovert set is a subset of CivilCommentsIdentities with ~20% of
the train and test splits further annotated for covert offensiveness, in
addition to the toxicity and identity labels. Raters were asked to categorize
comments as one of explicitly, implicitly, not, or not sure if offensive, as
well as whether it contained different types of covert offensiveness. The full
annotation procedure is detailed in a forthcoming paper at
https://sites.google.com/corp/view/hciandnlp/accepted-papers.
"""

_CC_SPANS_DESCRIPTION = """
The CivilComments Toxic Spans are a subset of CivilComments that is
labeled at the span level - the indices of all character (unicode codepoints)
boundaries that were tagged as toxic by a majority of the annotators is
returned in a 'spans' feature.
"""

_CC_CONTEXT_DESCRIPTION = """
The CivilComments in Context is a subset of CivilComments that was
labeled by making available to the labelers the parent_text. It includes
a contextual_toxicity feature.
"""

_DOWNLOAD_URL = 'https://storage.googleapis.com/jigsaw-unintended-bias-in-toxicity-classification/civil_comments_v1.2.zip'

IDENTITY_LABELS = [
    'male', 'female', 'transgender', 'other_gender', 'heterosexual',
    'homosexual_gay_or_lesbian', 'bisexual', 'other_sexual_orientation',
    'christian', 'jewish', 'muslim', 'hindu', 'buddhist', 'atheist',
    'other_religion', 'black', 'white', 'asian', 'latino',
    'other_race_or_ethnicity', 'physical_disability',
    'intellectual_or_learning_disability', 'psychiatric_or_mental_illness',
    'other_disability'
]

COVERT_LABELS = [
    'explicitly_offensive', 'implicitly_offensive', 'not_sure_offensive',
    'not_offensive', 'covert_humor', 'covert_obfuscation',
    'covert_emoticons_emojis', 'covert_sarcasm', 'covert_microaggression',
    'covert_masked_harm', 'covert_political'
]


def _labels(mode):
  """Return the list of label features appropriate for the mode."""
  if mode == 'spans':
    return ['spans']
  labels = [
      'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult',
      'identity_attack', 'sexual_explicit'
  ]
  if mode in ['identity', 'covert']:
    labels += IDENTITY_LABELS
  if mode == 'covert':
    labels += COVERT_LABELS
  if mode == 'context':
    labels += ['contextual_toxicity']
  return labels


def _parse_common(row):
  """Parse common elements to TF Example from CSV row for non-spans mode."""
  example = {}
  example['id'] = row['id']
  example['text'] = row['comment_text']
  example['parent_text'] = row['parent_text']
  parent_id = row['parent_id'] or 0
  example['parent_id'] = int(float(parent_id))
  example['article_id'] = int(row['article_id'])
  return example


def _parse_row_as_example(row, mode):
  """Parse elements to TF Example, as appropriate for specified mode."""
  example = _parse_common(row)
  for label in _labels(mode):
    if not row[label]:
      return
    example[label] = float(row[label])
  return example


def _parse_spans_row_as_example(row):
  """Parse elements to TF Example for toxic spans mode."""
  example = _parse_common(row)
  example['spans'] = np.array(ast.literal_eval(row['spans']), dtype=np.int32)
  return example


class CivilCommentsConfig(tfds.core.BuilderConfig):
  """Configuration for `CivilComments`."""

  def __init__(self, name, description, mode):
    super(CivilCommentsConfig, self).__init__(
        name=name, description=description)
    self.mode = mode


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
          name='CivilComments', description=_CC_DESCRIPTION, mode='base'),
      CivilCommentsConfig(
          name='CivilCommentsIdentities',
          description=_CC_IDENTITIES_DESCRIPTION,
          mode='identity'),
      CivilCommentsConfig(
          name='CivilCommentsCovert',
          description=_CC_COVERT_DESCRIPTION,
          mode='covert'),
      CivilCommentsConfig(
          name='CivilCommentsToxicSpans',
          description=_CC_SPANS_DESCRIPTION,
          mode='spans'),
      CivilCommentsConfig(
          name='CivilCommentsInContext',
          description=_CC_CONTEXT_DESCRIPTION,
          mode='context'),
  ]

  VERSION = tfds.core.Version('1.2.2')
  RELEASE_NOTES = {
      '1.2.2': 'Update to reflect context only having a train split.',
      '1.2.1': 'Fix incorrect formatting in context splits.',
      '1.2.0': 'Add toxic spans, context, and parent comment text features.',
      '1.1.3': 'Corrected id types from float to string.',
      '1.1.2': 'Added separate citation for CivilCommentsCovert dataset.',
      '1.1.1': 'Added CivilCommentsCovert config with correct checksum.',
      '1.1.0': 'Added CivilCommentsCovert config.',
      '1.0.1': 'Added a unique id for each comment.',
      '1.0.0': 'Initial full release.',
  }

  def _info(self):
    mode = self.builder_config.mode
    citation = {
        'base': _CITATION,
        'identity': _CITATION,
        'covert': _COVERT_CITATION,
        'spans': _SPANS_CITATION,
        'context': _CONTEXT_CITATION
    }[mode]
    features = {
        'text': tfds.features.Text(),
        'id': tf.string,
        'parent_text': tfds.features.Text(),
        'parent_id': tf.int32,
        'article_id': tf.int32,
    }
    if mode == 'spans':
      features['spans'] = tfds.features.Tensor(shape=(None,), dtype=tf.int32)
      supervised_value = 'spans'
    else:
      for label in _labels(mode):
        features[label] = tf.float32
      supervised_value = 'toxicity'

    return tfds.core.DatasetInfo(
        builder=self,
        description=_COMMON_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        # The supervised_keys version is very impoverished.
        supervised_keys=('text', supervised_value),
        homepage='https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data',
        citation=citation,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    mode = self.builder_config.mode
    filename = os.path.join(dl_path, 'civil_comments.csv')

    splits = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filename': filename,
                'mode': mode,
                'split': 'train',
            },
        )
    ]

    if mode != 'covert' and mode != 'context':
      # Covert and context do not have validation split.
      validation_split_generator = tfds.core.SplitGenerator(
          name=tfds.Split.VALIDATION,
          gen_kwargs={
              'filename': filename,
              'mode': mode,
              'split': 'test_public',
          },
      )
      splits.append(validation_split_generator)

    if mode != 'context':
      # Context has only a train split.
      test_split_generator = tfds.core.SplitGenerator(
          name=tfds.Split.TEST,
          gen_kwargs={
              'filename': filename,
              'mode': mode,
              'split': 'test_private',
          },
      )
      splits.append(test_split_generator)
    return splits

  def _generate_examples(self, filename, mode, split):
    """Yields examples.

    Each example contains a text input followed by several toxicity subtype
    scores, identity labels if include_identity_labels is True, and covert
    offensiveness labels if include_covert_labels is True.

    Args:
      filename: the path of the file to be read for this split.
      mode: the specifc data subset and features to yield.
      split: the split to extract, one of train, public_test, private_test.

    Yields:
      A dictionary of features, depending upon the mode.
    """
    with tf.io.gfile.GFile(filename) as f:
      reader = csv.DictReader(f)
      for row in reader:
        if mode == 'spans':
          if row['spans_split'] == split:
            example = _parse_spans_row_as_example(row)
            yield row['id'], example
        else:
          if row['split'] == split:
            example = _parse_row_as_example(row, mode)
            if example:
              yield row['id'], example
