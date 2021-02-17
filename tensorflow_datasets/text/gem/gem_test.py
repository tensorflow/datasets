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

"""gem dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.gem import gem


class GemCommonGenTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['common_gen']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'data': 'common_gen',
  }


class GemCsRestaurantsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['cs_restaurants']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'cs_restaurants/train.jsonl',
      'validation': 'cs_restaurants/devel.jsonl',
      'test': 'cs_restaurants/test.jsonl',
  }


class GemDartTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['dart']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'dart/dart-v1.1.1-full-train.json',
      'validation': 'dart/dart-v1.1.1-full-dev.json',
      'test': 'dart/dart-v1.1.1-full-test.json',
  }


class GemE2ETest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['e2e_nlg']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'e2e_nlg/train-fixed.no-ol.csv',
      'validation': 'e2e_nlg/devel-fixed.no-ol.csv',
      'test': 'e2e_nlg/test-fixed.csv',
  }


class GemMLSumTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['mlsum_de', 'mlsum_es']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'mlsum',
      'validation': 'mlsum',
      'test': 'mlsum',
      'bad_ids': 'mlsum/gem_mlsum_bad_ids.json'
  }


class GemSchemaGuidedDialogTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['schema_guided_dialog']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'data': 'schema_guided_dialog',
  }


class GemTottoTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['totto']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'data': '',
  }


class GemWebNlgTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['web_nlg_en', 'web_nlg_ru']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'web_nlg/webnlg_ru_train.json',
      'validation': 'web_nlg/webnlg_ru_val.json',
      'test': 'web_nlg/webnlg_ru_test.json',
  }


class GemWikiAutoTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['wiki_auto_asset_turk']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test_turk': 1,  # Number of fake test examples.
      'test_asset': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'train': 'wiki_auto_asset_turk/train.tsv',
      'validation': 'wiki_auto_asset_turk/dev.tsv',
      'test_asset_0': 'wiki_auto_asset_turk/asset.test.simp.0',
      'test_asset_1': 'wiki_auto_asset_turk/asset.test.simp.1',
      'test_asset_2': 'wiki_auto_asset_turk/asset.test.simp.2',
      'test_asset_3': 'wiki_auto_asset_turk/asset.test.simp.3',
      'test_asset_4': 'wiki_auto_asset_turk/asset.test.simp.4',
      'test_asset_5': 'wiki_auto_asset_turk/asset.test.simp.5',
      'test_asset_6': 'wiki_auto_asset_turk/asset.test.simp.6',
      'test_asset_7': 'wiki_auto_asset_turk/asset.test.simp.7',
      'test_asset_8': 'wiki_auto_asset_turk/asset.test.simp.8',
      'test_asset_9': 'wiki_auto_asset_turk/asset.test.simp.9',
      'test_turk_0': 'wiki_auto_asset_turk/test.8turkers.tok.turk.0',
      'test_turk_1': 'wiki_auto_asset_turk/test.8turkers.tok.turk.1',
      'test_turk_2': 'wiki_auto_asset_turk/test.8turkers.tok.turk.2',
      'test_turk_3': 'wiki_auto_asset_turk/test.8turkers.tok.turk.3',
      'test_turk_4': 'wiki_auto_asset_turk/test.8turkers.tok.turk.4',
      'test_turk_5': 'wiki_auto_asset_turk/test.8turkers.tok.turk.5',
      'test_turk_6': 'wiki_auto_asset_turk/test.8turkers.tok.turk.6',
      'test_turk_7': 'wiki_auto_asset_turk/test.8turkers.tok.turk.7',
  }


class GemWikiLinguaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = [
      'wiki_lingua_es_en', 'wiki_lingua_ru_en', 'wiki_lingua_tr_en',
      'wiki_lingua_vi_en'
  ]
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'data': 'wiki_lingua',
  }


class GemXsumTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gem dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['xsum']
  DATASET_CLASS = gem.Gem
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake dev examples.
      'test': 1,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = {
      'data': 'xsum',
      'splits': 'xsum/gem_xsum_confidence_0.8.json'
  }


if __name__ == '__main__':
  tfds.testing.test_main()
