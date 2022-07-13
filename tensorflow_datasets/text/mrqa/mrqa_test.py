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

"""mrqa datasets."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.mrqa import mrqa


class MRQASQuADTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for squad dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['squad']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'squad/train.jsonl',
      'validation': 'squad/validation.jsonl',
  }


class MRQANewsQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for news_qa dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['news_qa']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'news_qa/train.jsonl',
      'validation': 'news_qa/validation.jsonl',
  }


class MRQATriviaQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for trivia_qa dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['trivia_qa']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'trivia_qa/train.jsonl',
      'validation': 'trivia_qa/validation.jsonl',
  }


class MRQASearchQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for search_qa dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['search_qa']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'search_qa/train.jsonl',
      'validation': 'search_qa/validation.jsonl',
  }


class MRQAHotpotQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for hotpot_qa dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['hotpot_qa']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'hotpot_qa/train.jsonl',
      'validation': 'hotpot_qa/validation.jsonl',
  }


class MRQANaturalQuestionsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'train': 9,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions/train.jsonl',
      'validation': 'natural_questions/validation.jsonl',
  }


class MRQABioASQTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for bio_asq dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['bio_asq']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'bio_asq/test.jsonl',
  }


class MRQADROPTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for drop dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['drop']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'drop/test.jsonl',
  }


class MRQADuoRCTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for duo_rc dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['duo_rc']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'duo_rc/test.jsonl',
  }


class MRQARACETest(tfds.testing.DatasetBuilderTestCase):
  """Tests for race dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['race']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'race/test.jsonl',
  }


class MRQARelationExtractionTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for relation_extraction dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['relation_extraction']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'relation_extraction/test.jsonl',
  }


class MRQATextbookQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for textbook_qa dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['textbook_qa']
  DATASET_CLASS = mrqa.MRQA
  SPLITS = {
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'test': 'textbook_qa/test.jsonl',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
