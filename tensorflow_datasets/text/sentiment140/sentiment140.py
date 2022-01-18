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

"""Sentiment 140 Dataset."""

import codecs
import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {Sentiment140,
    author = "Go, Alec and Bhayani, Richa and Huang, Lei",
    title  = "Twitter Sentiment Classification using Distant Supervision",
    year   = "2009",
    url    = "http://help.sentiment140.com/home"
}
"""

_DESCRIPTION = """
Sentiment140 allows you to discover the sentiment of a brand, product, or topic on Twitter.

The data is a CSV with emoticons removed. Data file format has 6 fields:

0. the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
1. the id of the tweet (2087)
2. the date of the tweet (Sat May 16 23:58:44 UTC 2009)
3. the query (lyx). If there is no query, then this value is NO_QUERY.
4. the user that tweeted (robotickilldozr)
5. the text of the tweet (Lyx is cool)

For more information, refer to the paper
Twitter Sentiment Classification with Distant Supervision at
https://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf
"""

_DOWNLOAD_URL = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
_HOMEPAGE_URL = "http://help.sentiment140.com/home"


class Sentiment140(tfds.core.GeneratorBasedBuilder):
  """Sentiment140 Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "polarity": tf.int32,
            "date": tfds.features.Text(),
            "query": tfds.features.Text(),
            "user": tfds.features.Text(),
            "text": tfds.features.Text(),
        }),
        supervised_keys=("text", "polarity"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path":
                    os.path.join(dl_paths,
                                 "training.1600000.processed.noemoticon.csv")
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": os.path.join(dl_paths, "testdata.manual.2009.06.14.csv")
            }),
    ]

  def _generate_examples(self, path):
    """Yeilds Examples.

    Args:
      path: The path of the file to be read for this split

    Yields:
      Generator yielding the next examples
    """
    with tf.io.gfile.GFile(path, mode="rb") as f:
      reader = csv.reader(codecs.iterdecode(f, "ISO-8859-1"))
      for index, row in enumerate(reader):
        # The values in the csv file do not have titles for columns
        # Certain rows have the same id
        key = "{}_{}".format(index, row[1])  # ID of the tweet
        example = {
            "polarity": row[0],
            "date": row[2],
            "query": row[3],
            "user": row[4],
            "text": row[5],
        }
        yield key, example
