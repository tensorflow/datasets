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

"""Historical phenological data for cherry tree flowering at Kyoto City."""

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

URL = 'https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/cherry_blossoms.csv'

_DESCRIPTION = """
Historical phenological data for cherry tree flowering at Kyoto City.

This data was collected from diaries and chronicles dating back to the 9th
century. Data from the 9th to the 14th century were collected by Aono and Saito
(2010;  International Journal of Biometeorology, 54, 211-219), while the 15th
to 21st  century were collected by Aono and Kazui (2008; International Journal
of  Climatology, 28, 905-914).

All dates are expressed in the Gregorian calendar.


Number of instances: 1216

Variables:

1. year: Year CE  (int)
2. doy: Day of year of first bloom. Day 89 is April 1. Day 119 is May 1. (float)
3. temp: March temperature estimate (float)
4. temp_upper: Upper 95% bound for estimate (float)
5. temp_lower: Lower 95% bound for estimate (float)
"""

_CITATION = """
@ONLINE {
    author = "Aono, Yasuyuki",
    title  = "Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions)",
    year   = "2012",
    url    = "http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/"
}
"""


class CherryBlossoms(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for cherry_blossoms dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features_dict = {
        'year': tf.int32,
        'doy': tf.float32,
        'temp': tf.float32,
        'temp_upper': tf.float32,
        'temp_lower': tf.float32,
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # Set to `None` to disable
        homepage='http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(URL)
    return {tfds.Split.TRAIN: self._generate_examples(path)}

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:  # pytype: disable=attribute-error  # gen-stub-imports
      reader = csv.DictReader(f, delimiter=';')
      for index, row in enumerate(reader):
        example = {k: v.replace('NA', 'nan') for k, v in row.items()}
        yield index, example
