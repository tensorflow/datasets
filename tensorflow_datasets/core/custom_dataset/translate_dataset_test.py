"""Tests for Custom Translate Dataset."""
import os
import mock

from tensorflow_datasets.core.custom_dataset import translate_dataset
import tensorflow_datasets.public_api as tfds

_EXAMPLE_DIR = os.path.join(
    tfds.testing.test_utils.fake_examples_dir(), 'translate_dataset')

original_init = tfds.TranslateDataset.__init__
original_download_and_prepare = tfds.TranslateDataset.download_and_prepare


def new_init(self, root_dir=None, **kwargs):
  assert root_dir is None
  del kwargs
  original_init(self, root_dir=_EXAMPLE_DIR)


class TranslateDatasetTests(tfds.testing.DatasetBuilderTestCase):
  """Translate dataset tests."""
  DATASET_CLASS = tfds.TranslateDataset
  SPLITS = {
      'train': 4,
      'test': 4,
      'val': 4,
  }

  @classmethod
  def setUpClass(cls):  # pylint:disable = invalid-name
    super().setUpClass()
    super(TranslateDatasetTests, cls).setUpClass()
    cls.DATASET_CLASS.__init__ = new_init
    cls.DATASET_CLASS.download_and_prepare = mock.Mock(return_value=None)

  @classmethod
  def tearDownClass(cls):  # pylint:disable = invalid-name
    super().tearDownClass()
    cls.DATASET_CLASS.__init__ = original_init
    cls.DATASET_CLASS.download_and_prepare = original_download_and_prepare

  def test_registered(self):
    # Custom datasets shouldn't be registered
    self.assertNotIn(tfds.TranslateDataset.name, tfds.list_builders())


class TranslateDatasetFunctionTest(tfds.testing.TestCase):
  """Tests for TranslateDataset functions."""

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

      split_examples, langs = translate_dataset._get_split_language_examples(
          'root_dir')
      builder = tfds.TranslateDataset(root_dir='root_dir')

      self.assertEqual(split_examples, {
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
      self.assertEqual(builder.info.features.languages, expected_languages)


if __name__ == '__main__':
  tfds.testing.test_main()
