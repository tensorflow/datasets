"""Tests for Custom Translate Dataset."""
import os
import mock

# from tensorflow_datasets.core.custom_dataset import translate_dataset
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
  def setUpClass(cls): # pylint:disable = invalid-name
    super().setUpClass()
    super(TranslateDatasetTests, cls).setUpClass()
    cls.DATASET_CLASS.__init__ = new_init
    cls.DATASET_CLASS.download_and_prepare = mock.Mock(return_value=None)

  @classmethod
  def tearDownClass(cls): # pylint:disable = invalid-name
    super().tearDownClass()
    cls.DATASET_CLASS.__init__ = original_init
    cls.DATASET_CLASS.download_and_prepare = original_download_and_prepare

  def test_registered(self):
    # Custom datasets shouldn't be registered
    self.assertNotIn(tfds.TranslateDataset.name, tfds.list_builders())

# TODO: Add function tests and fake directory tests

if __name__ == '__main__':
  tfds.testing.test_main()
