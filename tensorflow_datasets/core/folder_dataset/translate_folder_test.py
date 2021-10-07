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

"""Tests for Custom Translate Dataset."""
import os
from unittest import mock

from tensorflow_datasets.core.folder_dataset import translate_folder
import tensorflow_datasets.public_api as tfds

_EXAMPLE_DIR = os.path.join(tfds.testing.test_utils.fake_examples_dir(),
                            'translate_folder')

original_init = tfds.TranslateFolder.__init__
original_download_and_prepare = tfds.TranslateFolder.download_and_prepare


def new_init(self, root_dir=None, **kwargs):
  assert root_dir is None
  del kwargs
  original_init(self, root_dir=_EXAMPLE_DIR)


class TranslateFolderTests(tfds.testing.DatasetBuilderTestCase):
  """Translate dataset tests."""
  DATASET_CLASS = tfds.TranslateFolder
  SPLITS = {
      'train': 4,
      'test': 4,
      'val': 4,
  }

  @classmethod
  def setUpClass(cls):  # pylint:disable = invalid-name
    super().setUpClass()
    super(TranslateFolderTests, cls).setUpClass()
    cls.DATASET_CLASS.__init__ = new_init
    cls.DATASET_CLASS.download_and_prepare = mock.Mock(return_value=None)

  @classmethod
  def tearDownClass(cls):  # pylint:disable = invalid-name
    super().tearDownClass()
    cls.DATASET_CLASS.__init__ = original_init
    cls.DATASET_CLASS.download_and_prepare = original_download_and_prepare

  def test_registered(self):
    # Custom datasets shouldn't be registered
    self.assertNotIn(tfds.TranslateFolder.name, tfds.list_builders())


class TranslateFolderFunctionTest(tfds.testing.TestCase):
  """Tests for TranslateFolder functions."""

  def test_properties(self):
    file_contents = {
        'root_dir/lang1.train.txt': 'line1\nlang1',
        'root_dir/lang2.train.txt': 'line1\nlang2',
        'root_dir/lang3.train.txt': 'line1\nlang3',
        'root_dir/lang1.val.txt': 'line1\nline2\n\nline4',
        'root_dir/lang2.val.txt': 'line1\nline2\n\nline4',
        'root_dir/lang3.val.txt': 'line1\nline2\n\nline4',
        'root_dir/lang1.test.txt': 'line1',
        'root_dir/lang2.test.txt': 'line1',
    }

    with tfds.testing.MockFs() as fs:
      for file in file_contents:
        fs.add_file(file, file_contents[file])

      split_examples, langs = translate_folder._get_split_language_examples(
          'root_dir')
      builder = tfds.TranslateFolder(root_dir='root_dir')

      self.assertEqual(
          split_examples, {
              'train': {
                  'lang1': ['line1', 'lang1'],
                  'lang2': ['line1', 'lang2'],
                  'lang3': ['line1', 'lang3'],
              },
              'val': {
                  'lang1': ['line1', 'line2', '', 'line4'],
                  'lang2': ['line1', 'line2', '', 'line4'],
                  'lang3': ['line1', 'line2', '', 'line4'],
              },
              'test': {
                  'lang1': ['line1'],
                  'lang2': ['line1'],
              },
          })

      self.assertEqual(builder.info.splits['train'].num_examples, 2)
      self.assertEqual(builder.info.splits['val'].num_examples, 4)
      self.assertEqual(builder.info.splits['test'].num_examples, 1)

      expected_languages = [
          'lang1',
          'lang2',
          'lang3',
      ]

      self.assertEqual(expected_languages, langs)
      self.assertEqual(list(builder.info.features.keys()), expected_languages)


if __name__ == '__main__':
  tfds.testing.test_main()
