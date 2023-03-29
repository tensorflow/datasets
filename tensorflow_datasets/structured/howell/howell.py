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

"""Demographic data from Kalahari !Kung San."""

from __future__ import annotations

import csv

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

URL = "https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/Howell1.csv"

_DESCRIPTION = """
Demographic data from Kalahari !Kung San people collected by Nancy Howell

Howell’s observations of the !Kung San were made by Howell in Botswana between
August 1967 and May 1969. Fuller descriptions of the region and the people
under study can be found in R. B. Lee and I. DeVore (eds), 1976, Kalahari
Hunter-Gatherers: Studies of the !Kung San and Their Neighbors, Harvard
University Press, Cambridge, Mass. And in N. Howell, 2000, Demography of the
Dobe !Kung, Aldine de Gruyter, New York.

Only columns on height, weight, age, and sex were kept. Rows with any
null values were dropped.

Number of instances: 544

Variables:

1. height in cm   (float)
2. weight in kg   (float)
3. age in years   (int)
4. male indicator (int)
"""

_CITATION = """
@ONLINE {
    author = "Howell, Nancy",
    title  = "Dobe !Kung Census of All Population.",
    year   = "2009",
    url    = "https://tspace.library.utoronto.ca/handle/1807/17973"
}
"""


class Howell(tfds.core.GeneratorBasedBuilder):
  """Demographic data from Kalahari !Kung San."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features_dict = {
        "height": tf.float32,
        "weight": tf.float32,
        "age": tf.float32,
        "male": tf.int32,
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # Set to `None` to disable
        homepage="https://tspace.library.utoronto.ca/handle/1807/10395",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    file_path = dl_manager.download_and_extract(URL)
    return {tfds.Split.TRAIN: self._generate_examples(file_path)}

  def _generate_examples(self, file_path):
    """Yields examples."""
    with file_path.open() as f:  # pytype: disable=attribute-error  # gen-stub-imports
      reader = csv.DictReader(f, delimiter=";")
      for index, row in enumerate(reader):
        example = dict(row.items())
        yield index, example
