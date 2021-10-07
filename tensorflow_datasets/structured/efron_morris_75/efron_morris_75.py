# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""efron_morris_75 dataset."""
import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

URL = 'https://raw.githubusercontent.com/pymc-devs/pymc-examples/main/examples/data/efron-morris-75-data.tsv'

_DESCRIPTION = """
The batting averages of 18 Major League Baseball players through their first 45
at-bats of the 1970 season, along with their batting average for the remainder
the season.

The data has been modified from the table in the paper, as used for case studies
using Stan and PyMC3, by  adding columns explicitly listing the number of
at-bats early in the season, as well as at-bats and hits for the full season.
"""

_CITATION = r"""
@article{efron1975data,
  title={Data analysis using Stein's estimator and its generalizations},
  author={Efron, Bradley and Morris, Carl},
  journal={Journal of the American Statistical Association},
  volume={70},
  number={350},
  pages={311--319},
  year={1975},
  publisher={Taylor \& Francis}
}
"""


class EfronMorris75(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for efron_morris_75 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features_dict = {
        'FirstName': tf.string,
        'LastName': tf.string,
        'At-Bats': tf.int32,
        'Hits': tf.int32,
        'BattingAverage': tf.float32,
        'RemainingAt-Bats': tf.int32,
        'RemainingAverage': tf.float32,
        'SeasonAt-Bats': tf.int32,
        'SeasonHits': tf.int32,
        'SeasonAverage': tf.float32,
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # Set to `None` to disable
        citation=_CITATION)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(URL)
    return {tfds.Split.TRAIN: self._generate_examples(path)}

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:
      reader = csv.DictReader(f, delimiter='\t')
      for index, row in enumerate(reader):
        example = dict(row.items())
        yield index, example
