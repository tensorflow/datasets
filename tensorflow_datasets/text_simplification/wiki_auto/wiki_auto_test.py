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

"""wiki_auto dataset."""

import sys
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text_simplification.wiki_auto import wiki_auto

sys.path.insert(0, '.')


class WikiAutoTestMANUAL(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_auto dataset for manual configuration."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['manual']
  DATASET_CLASS = wiki_auto.WikiAuto

  DL_EXTRACT_RESULT = {
      'train': 'manual/1.0.0/train.tsv',
      'dev': 'manual/1.0.0/dev.tsv',
      'test': 'manual/1.0.0/test.tsv',
  }
  SPLITS = {
      'train': 5,
      'dev': 5,
      'test': 5,
  }


class WikiAutoTestAUTO(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_auto dataset for auto configuration."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['auto']
  DATASET_CLASS = wiki_auto.WikiAuto

  DL_EXTRACT_RESULT = {
      'part1': 'auto/1.0.0/wiki-auto-part-1-data.json',
      'part2': 'auto/1.0.0/wiki-auto-part-2-data.json',
  }
  SPLITS = {
      'part1': 1,
      'part2': 1,
  }


class WikiAutoTestAUTOACL(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_auto dataset for auto_acl configuration."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['auto_acl']
  DATASET_CLASS = wiki_auto.WikiAuto

  DL_EXTRACT_RESULT = {
      'normal': 'auto_acl/1.0.0/train.dst',
      'simple': 'auto_acl/1.0.0/train.src',
  }
  SPLITS = {'full': 5}


class WikiAutoTestAUTOACLNOSPLIT(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_auto dataset for auto_acl configuration."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['auto_full_no_split']
  DATASET_CLASS = wiki_auto.WikiAuto

  DL_EXTRACT_RESULT = {
      'normal': 'auto_full_no_split/1.0.0/train.dst',
      'simple': 'auto_full_no_split/1.0.0/train.src',
  }
  SPLITS = {'full': 5}


class WikiAutoTestAUTOACLWITHSPLIT(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_auto dataset for auto_acl configuration."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['auto_full_with_split']
  DATASET_CLASS = wiki_auto.WikiAuto

  DL_EXTRACT_RESULT = {
      'normal': 'auto_full_with_split/1.0.0/train.dst',
      'simple': 'auto_full_with_split/1.0.0/train.src',
  }
  SPLITS = {'full': 5}


if __name__ == '__main__':
  tfds.testing.test_main()
