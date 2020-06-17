"""Custom Translate Datasets Template"""

import os

import tensorflow.compat.v2 as tf
from tensorflow_datasets import core


class TranslateDataset(core.DatasetBuilder):
  """Generic image classification dataset created from manual directory.

  The data directory should have the following structure:

  ```
  path/to/manual_dir/<dataset_name>/
    split_name/  # Ex: 'train'
      lang1.txt
      lang2.txt
      lang3.txt
    split_name/  # Ex: 'test'
      lang1.txt
      lang2.txt
      ...
  ```

  To use it:

  ```
  builder = tfds.TranslateDataset(root_dir='path/to/manual_dir/')
  print(builder.info)  # Splits, num examples,... are automatically calculated
  ds = builder.as_dataset(split='split_name', shuffle_files=True)
  ```

  """

  VERSION = core.Version('2.0.0')

  def __init__(self, root_dir):
    root_dir = os.path.expanduser(root_dir)
    super(TranslateDataset, self).__init__(
        data_dir=root_dir, version=str(self.VERSION), config=None)

    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = root_dir

    languages_examples_dict = _get_language_examples()
    self.languages = languages_examples_dict.keys()

    # TODO: Update self.info

  def _info(self):
    return core.DatasetInfo(
        builder=self,
        description='Generic image classification dataset.',
        features=core.features.Translation(self.languages),
        # supervised_keys=(self.languages[0], self.languages[1]), Support supervised?
    )

  def _download_and_prepare(_):
    raise NotImplementedError('No need to call download_and_prepare function.')

  def download_and_prepare(_):
    raise NotImplementedError('No need to call download_and_prepare function.')

  def _process_ds(self, path, label):
    pass

  def _as_dataset(
      self,
      split,
      shuffle_files=False,
      decoders=None,
      read_config=None):
    """Generate dataset for given split"""

    pass


def _get_language_examples():
  return dict()

def _list_files(root_dir):
  return []