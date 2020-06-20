"""Custom Translate Datasets Template"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from typing import Dict, List, Tuple, Set

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core.utils import version

class TranslateDataset(dataset_builder.DatasetBuilder):
  """Generic image classification dataset created from manual directory.

  The data directory should have the following structure:

  ```
  path/to/manual_dir/<dataset_name>/
    split_name/  # Ex: 'train'
      lang1.txt
      lang2.txt
    split_name/  # Ex: 'test'
      lang1.txt
      lang2.txt
      ...
  ```

  To use it:

  ```
  builder = tfds.TranslateDataset(root_dir='path/to/manual_dir/')
  print(builder.info)  # Splits, num examples,... are automatically calculated
  ds = builder.as_dataset(split='train', shuffle_files=True)
  ```

  """

  VERSION = version.Version('1.0.0')

  def __init__(self, root_dir: str):
    root_dir = os.path.expanduser(root_dir)
    self._languages_examples_dict, languages = _get_language_examples(root_dir)
    self._languages = sorted(list(languages))
    super(TranslateDataset, self).__init__()
    
    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = root_dir

    # Update DatasetInfo splits
    split_dict = split_lib.SplitDict(self.name)
    for split_name, examples in self._languages_examples_dict.items():
      split_dict.add(split_lib.SplitInfo(
          name=split_name,
          shard_lengths=[len(next(iter(examples.values())))],
        ))
    self.info.update_splits_if_different(split_dict)

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(
        builder=self,
        description='Generic image classification dataset.',
        features=features_lib.Translation(self._languages),
        # supervised_keys=(self.languages[0], self.languages[1]), # Support supervised?
    )

  def _download_and_prepare(self, **kwargs):
    raise NotImplementedError(
        'No need to call download_and_prepare function for {}.'.format(
            type(self).__name__))

  def download_and_prepare(self, **kwargs):
    return self._download_and_prepare()

  def _as_dataset(
      self,
      split,
      shuffle_files=False,
      decoders=None,
      read_config=None) -> tf.data.Dataset:
    """Generate dataset for given split"""
    del read_config # Unused (automatically created in `DatasetBuilder`)
    if decoders:
      raise NotImplementedError(
          '`decoders` is not supported with {}'.format(type(self).__name__))
    if split not in self.info.splits.keys():
      raise ValueError(
          'Unrecognized split {}. Subsplit API not yet supported for {}. '
          'Split name should be one of {}.'.format(
              split, type(self).__name__, list(self.info.splits.keys())))

    # Build the tf.data.Dataset object
    lang_example_dict = self._languages_examples_dict[split]
    ds = tf.data.Dataset.from_tensor_slices(lang_example_dict)
    if shuffle_files:
      ds = ds.shuffle(len(lang_example_dict))
    return ds


def _get_language_examples(
    root_dir: str
) -> Tuple[Dict[str, Dict[str, List[str]]], List[str]]:
  split_lang_examples = dict()
  languages = set()
  for split_name in _list_folders(root_dir):
    split_dir = os.path.join(root_dir, split_name)
    split_lang_examples[split_name] = {
        f[:-4]: _list_examples(os.path.join(split_dir, f))
        for f in tf.io.gfile.listdir(split_dir)
        if f.lower().endswith('.txt')
    }
    size = len(next(iter(split_lang_examples[split_name].values())))
    # One-to-One translation
    for lang, example in split_lang_examples[split_name].items():
      languages.add(lang)
      assert len(example) == size

  return split_lang_examples, languages


def _list_folders(root_dir: str) -> List[str]:
  return [
      f for f in tf.io.gfile.listdir(root_dir)
      if tf.io.gfile.isdir(os.path.join(root_dir, f))
  ]


def _list_examples(file: str) -> List[str]:
  with tf.io.gfile.GFile(file) as f:
    sentences = f.read().splitlines()
  return sentences
