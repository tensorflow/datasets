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

"""ProteinNet dataset."""

from __future__ import annotations

import os
from typing import Dict, Iterator, List, Optional, Sequence, Tuple, Union
import urllib

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_Example = Dict[str, Union[int, str, np.ndarray, List]]
_ExampleIterator = Iterator[Tuple[str, _Example]]
_PROTEINNET_HOMEPAGE = 'https://github.com/aqlaboratory/proteinnet'

_LINES_PER_ENTRY = 33


def _parse_array(lines: Sequence[str]) -> np.ndarray:
  """Parse lines of tab-separated numbers into an array."""
  lines = [x.split('\t') for x in lines]
  return np.array(lines, dtype=np.float32)


def _parse_mask(line: str) -> np.ndarray:
  """Parse a string of `+` and `-` into a bool array."""
  return np.array([ch == '+' for ch in line], dtype=bool)


def _read_entry(fin: tf.io.gfile.GFile) -> Optional[Tuple[str, _Example]]:
  """Read an example from an input file.

  Args:
    fin: Input file object for reading dataset entries.

  Returns:
    The read exmple and its name, or None in cases of EOF.

  Raises:
    Exception: In case entry format is incorect.
  """
  lines = []
  for _ in range(_LINES_PER_ENTRY):
    line = fin.readline().strip()
    lines.append(line)

  if all(not line for line in lines):  # EOF?
    return None

  # Check structure.
  if (
      lines[0] != '[ID]'
      or lines[2] != '[PRIMARY]'
      or lines[4] != '[EVOLUTIONARY]'
      or lines[26] != '[TERTIARY]'
      or lines[30] != '[MASK]'
      or lines[32]
  ):
    raise ValueError('Incorrect data formatting.')
  lines = lines[:-1]  # Discard last empty (spacer) line.

  # The transposes below is required because TFDS allows unknown tensor
  # dimensions only in the first axis.
  key = lines[1]
  example = {
      'id': key,
      'primary': list(lines[3]),
      'evolutionary': _parse_array(lines[5:26]).transpose(),
      'tertiary': _parse_array(lines[27:30]).transpose(),
      'mask': _parse_mask(lines[31]),
      'length': len(lines[3]),
  }
  return key, example


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for the ProteinNet dataset."""

  URL = (
      'https://sharehost.hms.harvard.edu/sysbio/alquraishi/proteinnet'
      '/human_readable/'
  )
  FILES = {
      'casp7': 'casp7.tar.gz',
      'casp8': 'casp8.tar.gz',
      'casp9': 'casp9.tar.gz',
      'casp10': 'casp10.tar.gz',
      'casp11': 'casp11.tar.gz',
      'casp12': 'casp12.tar.gz',
  }
  THRESHOLDS = [30, 50, 70, 90, 95, 100]
  AMINOACIDS = [
      'A',
      'C',
      'D',
      'E',
      'F',
      'G',
      'H',
      'I',
      'K',
      'L',
      'M',
      'N',
      'P',
      'Q',
      'R',
      'S',
      'T',
      'V',
      'W',
      'Y',
  ]

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(name='casp7'),
      tfds.core.BuilderConfig(name='casp8'),
      tfds.core.BuilderConfig(name='casp9'),
      tfds.core.BuilderConfig(name='casp10'),
      tfds.core.BuilderConfig(name='casp11'),
      tfds.core.BuilderConfig(name='casp12'),
  ]

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'primary': tfds.features.Sequence(
                tfds.features.ClassLabel(names=self.AMINOACIDS)
            ),
            'evolutionary': tfds.features.Tensor(
                shape=(None, 21), dtype=np.float32
            ),
            'tertiary': tfds.features.Tensor(shape=(None, 3), dtype=np.float32),
            'mask': tfds.features.Tensor(shape=(None,), dtype=np.bool_),
            'length': tfds.features.Tensor(shape=(), dtype=np.int32),
        }),
        supervised_keys=('primary', 'tertiary'),
        homepage=_PROTEINNET_HOMEPAGE,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> Dict[Union[str, tfds.Split], _ExampleIterator]:
    """Returns SplitGenerators."""
    name = self.builder_config.name  # Configurable dataset (config) name.
    path = dl_manager.download_and_extract(
        urllib.parse.urljoin(self.URL, self.FILES[name])
    )

    splits = {
        tfds.Split.VALIDATION: self._generate_examples(
            os.path.join(path, name, 'validation')
        ),
        tfds.Split.TEST: self._generate_examples(
            os.path.join(path, name, 'testing')
        ),
    }
    for threshold in self.THRESHOLDS:  # Train splits.
      split_path = os.path.join(path, name, f'training_{threshold}')
      splits[f'train_{threshold}'] = self._generate_examples(split_path)
    return splits

  def _generate_examples(self, filename: str) -> _ExampleIterator:
    """Yields examples."""
    with tf.io.gfile.GFile(filename, mode='r') as fin:
      while True:
        example = _read_entry(fin)
        if example is None:
          break
        yield example
