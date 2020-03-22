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

"""UCI Adult Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import collections
import numpy as np

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
  @misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
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
def convert_to_int(d):
  return -1 if d == "?" else np.int32(d)

def convert_to_string(d):
  return d

COLUMNS = [
    "age", "work_class", "final_weight", "education", "education_num", \
    "marital_status", "occupation", "relationship", "race", "sex", \
    "capital_gain", "capital_loss", "hours_per_week", "native_country"
]

_WORK_CLASS_LABELS = [
    "State-gov", "Self-emp-not-inc", "Private", "Federal-gov", "Local-gov",\
    "Self-emp-inc", "Without-pay", "Never-worked", "?"
]

_EDUCATION_LABELS = [
    "Bachelors", "HS-grad", "11th", "Masters", "9th", "Some-college", \
    "Assoc-acdm", "Assoc-voc", "7th-8th", "Doctorate", "Prof-school", \
    "5th-6th", "10th", "1st-4th", "Preschool", "12th"
]

_MARITAL_LABELS = [
    "Never-married", "Married-civ-spouse", "Divorced", "Married-spouse-absent",\
    "Separated", "Married-AF-spouse", "Widowed"
]

_OCCUPATION_LABELS = [
    "Adm-clerical", "Exec-managerial", "Handlers-cleaners", "Prof-specialty", \
    "Other-service", "Sales", "Craft-repair", "Transport-moving", \
    "Farming-fishing", "Machine-op-inspct", "Tech-support", "Protective-serv", \
    "Armed-Forces", "Priv-house-serv", "?"
]

_RELATION_LABELS = [
    "Not-in-family", "Husband", "Wife", "Own-child", "Unmarried", \
    "Other-relative"
]

_RACE_LABELS = [
    "White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", \
    "Other"
]

_COUNTRY_LABELS = [
    "United-States", "Cuba", "Jamaica", "India", "Mexico", "South", \
    "Puerto-Rico", "Honduras", "England", "Canada", "Germany", "Iran", \
    "Philippines", "Italy", "Poland", "Columbia", "Cambodia", "Thailand", \
    "Ecuador", "Laos", "Taiwan", "Haiti", "Portugal", "Dominican-Republic", \
    "El-Salvador", "France", "Guatemala", "China", "Japan", "Yugoslavia", \
    "Peru", "Outlying-US(Guam-USVI-etc)", "Scotland", "Trinadad&Tobago", \
    "Greece", "Nicaragua", "Vietnam", "Hong", "Ireland", "Hungary", \
    "Holand-Netherlands", "?"
]

FEATURE_DICT = collections.OrderedDict([
    ("age", (tf.int32, convert_to_int)),
    ("work_class", (tfds.features.ClassLabel(names=_WORK_CLASS_LABELS),
                    convert_to_string)),

    ("final_weight", (tf.int32, convert_to_int)),
    ("education", (tfds.features.ClassLabel(names=_EDUCATION_LABELS),
                   convert_to_string)),

    ("education_num", (tf.int32, convert_to_int)),
    ("marital_status", (tfds.features.ClassLabel(names=_MARITAL_LABELS),
                        convert_to_string)),

    ("occupation", (tfds.features.ClassLabel(names=_OCCUPATION_LABELS),
                    convert_to_string)),

    ("relationship", (tfds.features.ClassLabel(names=_RELATION_LABELS),
                      convert_to_string)),

    ("race", (tfds.features.ClassLabel(names=_RACE_LABELS),
              convert_to_string)),

    ("sex", (tfds.features.ClassLabel(names=["Male", "Female"]),
             convert_to_string)),

    ("capital_gain", (tf.int32, convert_to_int)),
    ("capital_loss", (tf.int32, convert_to_int)),
    ("hours_per_week", (tf.int32, convert_to_int)),
    ("native_country", (tfds.features.ClassLabel(names=_COUNTRY_LABELS),
                        convert_to_string))
])

_URL_TRAIN = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
_URL_TEST = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"

class Adult(tfds.core.GeneratorBasedBuilder):
  """UCI Adult Dataset"""

  VERSION = tfds.core.Version(
      "0.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "prediction": tfds.features.ClassLabel(names=["<=50K", ">50K"]),
            "features": {
                name: dtype for name, (dtype, func) in FEATURE_DICT.items()
            }
        }),

        supervised_keys=("features", "prediction"),
        homepage='https://archive.ics.uci.edu/ml/datasets/Adult',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    files = dl_manager.download({
        "train_data": _URL_TRAIN,
        "test_data": _URL_TEST
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"file_path": files["train_data"]},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"file_path": files["test_data"]}
        )
    ]

  def _generate_examples(self, file_path):
    """Generate features and target given the directory path.
    Args:
      file_path: path where the csv file is stored
    Yields:
      The features and the target
    """
    with tf.io.gfile.GFile(file_path) as f:
      raw_data = csv.reader(f)
      for i, row in enumerate(raw_data):
        if len(row) == 15:
          prediction_val = row[-1].split('.')[0].strip()
          rec = dict(zip(COLUMNS, map(lambda x: x.strip(), row[:-1])))
          yield i, {
              "prediction": prediction_val,
              "features": {
                  name: FEATURE_DICT[name][1](value) for name, \
                        value in rec.items()
              }
          }
