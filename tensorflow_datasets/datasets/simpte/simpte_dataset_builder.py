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

"""simPTE dataset."""

from __future__ import annotations

import csv

import numpy as np
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for simPTE dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """
    Please download training data: sim_pte_train.csv and test data:
    sim_pte_test.csv to ~/tensorflow_datasets/downloads/manual/.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'y': np.int32,
            'treat': np.int32,
            'X1': np.float32,
            'X2': np.float32,
            'X3': np.float32,
            'X4': np.float32,
            'X5': np.float32,
            'X6': np.float32,
            'X7': np.float32,
            'X8': np.float32,
            'X9': np.float32,
            'X10': np.float32,
            'X11': np.float32,
            'X12': np.float32,
            'X13': np.float32,
            'X14': np.float32,
            'X15': np.float32,
            'X16': np.float32,
            'X17': np.float32,
            'X18': np.float32,
            'X19': np.float32,
            'X20': np.float32,
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=(
            {
                'X1': 'X1',
                'X2': 'X2',
                'X3': 'X3',
                'X4': 'X4',
                'X5': 'X5',
                'X6': 'X6',
                'X7': 'X7',
                'X8': 'X8',
                'X9': 'X9',
                'X10': 'X10',
                'X11': 'X11',
                'X12': 'X12',
                'X13': 'X13',
                'X14': 'X14',
                'X15': 'X15',
                'X16': 'X16',
                'X17': 'X17',
                'X18': 'X18',
                'X19': 'X19',
                'X20': 'X20',
                'treat': 'treat',
            },
            'y',
        ),
        homepage='https://rdrr.io/cran/uplift/man/sim_pte.html',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    train_path = dl_manager.manual_dir / 'sim_pte_train.csv'
    test_path = dl_manager.manual_dir / 'sim_pte_test.csv'

    return {
        'train': self._generate_examples(train_path),
        'test': self._generate_examples(test_path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:
      index = 0
      for row in csv.DictReader(f):
        # And yield (key, feature_dict)
        yield index, {
            'X1': row['X1'],
            'X2': row['X2'],
            'X3': row['X3'],
            'X4': row['X4'],
            'X5': row['X5'],
            'X6': row['X6'],
            'X7': row['X7'],
            'X8': row['X8'],
            'X9': row['X9'],
            'X10': row['X10'],
            'X11': row['X11'],
            'X12': row['X12'],
            'X13': row['X13'],
            'X14': row['X14'],
            'X15': row['X15'],
            'X16': row['X16'],
            'X17': row['X17'],
            'X18': row['X18'],
            'X19': row['X19'],
            'X20': row['X20'],
            'treat': row['treat'],
            'y': row['y'],
        }
        index += 1
