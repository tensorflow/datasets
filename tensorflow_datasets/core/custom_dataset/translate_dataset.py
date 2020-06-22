"""Custom Translate Datasets Template"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
from typing import Dict, List, Tuple

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core.utils import version

# Dict of 'split_name'-> 'language' -> `List[text_data]`
SplitExampleDict = Dict[str, Dict[str, List[str]]]


class TranslateDataset(dataset_builder.DatasetBuilder):
  """Generic image classification dataset created from manual directory.

  The data directory should have the following structure:

  ```
  path/to/manual_dir/<dataset_name>/
    lang1.train.txt
    lang2.train.txt
    lang1.test.txt
    lang2.test.txt
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
    self._split_examples, self._languages = _get_split_language_examples(
        root_dir)
    super(TranslateDataset, self).__init__()

    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = root_dir

    # Update DatasetInfo splits
    split_dict = split_lib.SplitDict(self.name)
    for split_name, examples in self._split_examples.items():
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
      read_config=None
  ) -> tf.data.Dataset:
    """Generate dataset for given split"""
    del read_config  # Unused (automatically created in `DatasetBuilder`)
    if decoders:
      raise NotImplementedError(
          '`decoders` is not supported with {}'.format(type(self).__name__))
    if split not in self.info.splits.keys():
      raise ValueError(
          'Unrecognized split {}. Subsplit API not yet supported for {}. '
          'Split name should be one of {}.'.format(
              split, type(self).__name__, list(self.info.splits.keys())))

    # Build the tf.data.Dataset object
    lang_example_dict = self._split_examples[split]
    ds = tf.data.Dataset.from_tensor_slices(lang_example_dict)
    if shuffle_files:
      ds = ds.shuffle(len(lang_example_dict))
    return ds


def _get_split_language_examples(
    root_dir: str
) -> Tuple[SplitExampleDict, List[str]]:
  """Extract all split names and associated text data.

  Args:
    root_dir: The folder where the `lang.split.txt` are located

  Returns:
    split_examples: Mapping split_names -> language -> List[text_data]
    languages: The list of languages
  """
  split_examples = collections.defaultdict(dict)
  languages = set()
  files = tf.io.gfile.listdir(root_dir)
  for file in files:
    lang, split_name, _ = file.split('.')
    split_examples[split_name][lang] = _list_examples(
        os.path.join(root_dir, file))
    languages.add(lang)

    # One-to-One translation
    size = len(next(iter(split_examples[split_name].values())))
    assert all(len(ex) == size for ex in split_examples[split_name].values())

  return split_examples, sorted(languages)


def _list_examples(file: str) -> List[str]:
  with tf.io.gfile.GFile(file) as f:
    sentences = f.read().splitlines()
  return sentences
