# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Custom Translate Datasets Template."""

from __future__ import annotations

import collections
import os
from typing import Dict, List, Tuple

from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core.utils import version
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

# Dict of 'split_name'-> 'language' -> `List[text_data]`
SplitExampleDict = Dict[str, Dict[str, List[str]]]


class TranslateFolder(dataset_builder.DatasetBuilder):
  """Generic text translation dataset created from manual directory.

  The directory content should be as followed:

  ```
  path/to/my_data/
    lang1.train.txt
    lang2.train.txt
    lang1.test.txt
    lang2.test.txt
    ...
  ```

  Each files should have one example per line. Line order should match between
  files.

  To use it:

  ```
  builder = tfds.TranslateFolder(root_dir='path/to/my_data/')
  print(builder.info)  # Splits, num examples,... are automatically calculated
  ds = builder.as_dataset(split='train', shuffle_files=True)
  ```

  Note: All examples from all splits are loaded in memory in `__init__`.
  """

  VERSION = version.Version('1.0.0')

  def __init__(self, root_dir: str):
    # Extract the splits, examples
    root_dir = os.path.expanduser(root_dir)
    self._split_examples, self._languages = _get_split_language_examples(
        root_dir
    )

    super(TranslateFolder, self).__init__()
    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = root_dir

    # Update DatasetInfo splits
    split_infos = [
        split_lib.SplitInfo(  # pylint: disable=g-complex-comprehension
            name=split_name,
            shard_lengths=[len(next(iter(examples.values())))],
            num_bytes=0,
        )
        for split_name, examples in self._split_examples.items()
    ]
    split_dict = split_lib.SplitDict(split_infos)
    self.info.set_splits(split_dict)

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(
        builder=self,
        description='Generic text translation dataset.',
        features=features_lib.FeaturesDict(
            {lang: features_lib.Text() for lang in self._languages}
        ),
    )

  def _download_and_prepare(self, **kwargs):  # pytype: disable=signature-mismatch  # overriding-parameter-count-checks
    raise NotImplementedError(
        'No need to call download_and_prepare function for {}.'.format(
            type(self).__name__
        )
    )

  def download_and_prepare(self, **kwargs):
    return self._download_and_prepare()

  def _as_dataset(
      self, split, shuffle_files=False, decoders=None, read_config=None
  ) -> tf.data.Dataset:
    """Generate dataset for given split."""
    del read_config  # Unused (automatically created in `DatasetBuilder`)
    if decoders:
      raise NotImplementedError(
          '`decoders` is not supported with {}'.format(type(self).__name__)
      )
    if split not in self.info.splits.keys():
      raise ValueError(
          'Unrecognized split {}. Subsplit API not yet supported for {}. '
          'Split name should be one of {}.'.format(
              split, type(self).__name__, list(self.info.splits.keys())
          )
      )

    # Build the tf.data.Dataset object
    lang_example_dict = self._split_examples[split]
    ds = tf.data.Dataset.from_tensor_slices(lang_example_dict)
    if shuffle_files:
      ds = ds.shuffle(len(lang_example_dict))
    return ds


def _get_split_language_examples(
    root_dir: str,
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
        os.path.join(root_dir, file)
    )
    languages.add(lang)

  # One-to-One translation
  for split, examples in split_examples.items():
    num_examples = {lang: len(ex) for lang, ex in examples.items()}
    if len(set(num_examples.values())) != 1:
      raise ValueError(
          'Num examples for split {} do not match: {}'.format(
              split, num_examples
          )
      )

  return split_examples, sorted(languages)


def _list_examples(file: str) -> List[str]:
  with epath.Path(file).open() as f:
    sentences = f.read().splitlines()
  return sentences
