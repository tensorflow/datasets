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

# Lint as: python3

"""Adult UCI Dataset"""

# gfile cannot be imported directly `from tensorflow.io import gfile`
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
gfile = tf.io.gfile


ADULT_TRAIN_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
ADULT_TEST_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"

_CITATION = """\
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information
               and Computer Sciences"
}
"""

_DESCRIPTION = """\
The dataset contains various information of adults.
The purpose of the dataset is to predict whether the
person earns more than $50K/year or not. The extraction
was done by Barry Becker from the 1994 Census database.
A set of reasonably clean records was extracted using
the following conditions: ((AAGE>16) && (AGI>100) &&
(AFNLWGT>1)&& (HRSWK>0)). The data set contains 48842
instances containing 14 attributes each. It is
also known as "Census Income" dataset. Following are the various
attributes:
1) Age
2) Workclass
3) Final Weight
4) Education
5) Education-Num
6) Marital Status
7) Occupation
8) Relationship
9) Race
10) Sex
11) Capital Gain
12) Capital Loss
13) Hours Per Week
14) Native Country
15) Prediction (Output)
"""


class Adult(tfds.core.GeneratorBasedBuilder):
  """Adult UCI Dataset"""
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "features": tfds.features.Tensor(shape=(14,), dtype=tf.string),
            "prediction": tfds.features.ClassLabel(names=["<=50K", ">50K"]),
        }),
        supervised_keys=("features", "prediction"),
        homepage="https://archive.ics.uci.edu/ml/datasets/adult",
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    """Generate Splits"""
    train_file = dl_manager.download(ADULT_TRAIN_URL)
    all_lines = tf.io.gfile.GFile(train_file).read().split("\n")
    train_records = [l for l in all_lines if l]

    train_file = dl_manager.download(ADULT_TEST_URL)
    all_lines = tf.io.gfile.GFile(train_file).read().split("\n")
    test_records = [l for l in all_lines if l][1:]

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"records": train_records}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"records": test_records}),
    ]

  def _generate_examples(self, records):
    """Generate examples given the records"""
    for i, row in enumerate(records):
      elems = row.split(",")
      yield i, {
          "features": [e.strip() for e in elems[:-1]],
          "prediction": elems[-1].split('.')[0].strip(),
      }
