# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
"""netflix_shows dataset."""

import collections
import csv
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This dataset consists of TV shows and movies available on Netflix.
The dataset is collected from Flixable which is a third-party Netflix search engine.
Float and int missing values are replaced with -1,
string missing values are replaced with 'Unknown'.
"""

_CITATION = """
"""

RATING_CLASSES = [
    'Unknown', 'G', 'NC-17', 'NR', 'PG', 'PG-13', 'R', 'TV-14', 'TV-G', 'TV-MA',
    'TV-PG', 'TV-Y', 'TV-Y7', 'TV-Y7-FV', 'UR'
]


def convert_to_string(d):
  if not isinstance(d, str):
    if np.isnan(d):
      return "Unknown"
    else:
      return str(d)
  return "Unknown" if d == "" else d


def return_same(d):
  return d


FEATURE_DICT = collections.OrderedDict(
    [
        ("show_id", (tf.string, convert_to_string)),
        (
            "type", (
                tfds.features.ClassLabel(names=["TV Show", "Movie"]),
                convert_to_string
            )
        ),
        ("title", (tf.string, convert_to_string)),
        ("director", (tf.string, convert_to_string)),
        ("cast", (tf.string, convert_to_string)),
        ("country", (tf.string, convert_to_string)),
        ("date_added", (tf.string, convert_to_string)),
        ("release_year", (tf.int32, return_same)),
        (
            "rating",
            (tfds.features.ClassLabel(names=RATING_CLASSES), convert_to_string)
        ),
        ("duration", (tf.string, convert_to_string)),
        ("listed_in", (tf.string, convert_to_string)),
        ("description", (tf.string, convert_to_string)),
    ]
)


class NetflixShows(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for netflix_shows dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {
                "data":
                    {
                        name: dtype
                        for name, (dtype, func) in FEATURE_DICT.items()
                    }
            }
        ),
        supervised_keys=None,
        homepage='https://www.kaggle.com/shivamb/netflix-shows',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_kaggle_data("shivamb/netflix-shows")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": path / "netflix_titles.csv"}
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    with tf.io.gfile.GFile(path) as f:
      raw_data = csv.DictReader(f)
      for i, row in enumerate(raw_data):
        yield i, {
            "data":
                {
                    name: FEATURE_DICT[name][1](value)
                    for name, value in row.items()
                }
        }
