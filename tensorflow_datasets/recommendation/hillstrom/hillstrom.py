# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Hillstrom dataset."""

from __future__ import annotations

import csv

import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This dataset contains 64,000 customers who last purchased within twelve months. The customers were involved in an e-mail test.

1. 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.
2. 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.
3. 1/3 were randomly chosen to not receive an e-mail campaign.

During a period of two weeks following the e-mail campaign, results were tracked.
The task is to tell the world if the Mens or Womens e-mail campaign was successful.
"""

_CITATION = """
@article{entryhillstrom,
  title={Hillstrom’s MineThatData Email Analytics Challenge},
  author={ENTRY, WINNING}
}
"""


class Hillstrom(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'history': np.float32,
            'zip_code': tfds.features.Text(),
            'segment': tfds.features.Text(),
            'recency': np.int64,
            'history_segment': tfds.features.Text(),
            'mens': np.int64,
            'womens': np.int64,
            'newbie': np.int64,
            'channel': tfds.features.Text(),
            'visit': np.int64,
            'conversion': np.int64,
            'spend': np.float32,
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=(
            {
                'history': 'history',
                'zip_code': 'zip_code',
                'segment': 'segment',
                'recency': 'recency',
                'mens': 'mens',
                'womens': 'womens',
                'newbie': 'newbie',
                'channel': 'channel',
            },
            'visit',
        ),
        homepage='https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        'http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv'
    )

    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:
      index = 0
      for row in csv.DictReader(f):
        # And yield (key, feature_dict)
        yield index, {
            'recency': row['recency'],
            'history_segment': row['history_segment'],
            'mens': row['mens'],
            'womens': row['womens'],
            'newbie': row['newbie'],
            'channel': row['channel'],
            'segment': row['segment'],
            'visit': row['visit'],
            'conversion': row['conversion'],
            'spend': row['spend'],
            'history': row['history'],
            'zip_code': row['zip_code'],
        }
        index += 1
