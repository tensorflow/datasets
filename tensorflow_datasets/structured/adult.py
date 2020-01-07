"""Prediction task is to determine whether a person makes over 50K a year."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tfds.core.lazy_imports.csv
import tfds.core.lazy_imports.collections
import tensorflow_datasets.public_api as tfds
import tensorflow as tf


_CITATION = """
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"}
"""


_DESCRIPTION = """
Listing of attributes:

>50K, <=50K.

age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines,
 Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti,
 Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
"""

CSV_COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "gender",
    "capital_gain", "capital_loss", "hours_per_week", "native_country",
    "income_bracket"
]

gender = tf.feature_column.categorical_column_with_vocabulary_list(
    "gender", ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])

race = tf.feature_column.categorical_column_with_vocabulary_list(
    "race", ["Female", "Male"])

education = tf.feature_column.categorical_column_with_vocabulary_list(
    "education", [
        "Bachelors", "HS-grad", "11th", "Masters", "9th",
        "Some-college", "Assoc-acdm", "Assoc-voc", "7th-8th",
        "Doctorate", "Prof-school", "5th-6th", "10th", "1st-4th",
        "Preschool", "12th"
    ])
marital_status = tf.feature_column.categorical_column_with_vocabulary_list(
    "marital_status", [
        "Married-civ-spouse", "Divorced", "Married-spouse-absent",
        "Never-married", "Separated", "Married-AF-spouse", "Widowed"
    ])
relationship = tf.feature_column.categorical_column_with_vocabulary_list(
    "relationship", [
        "Husband", "Not-in-family", "Wife", "Own-child", "Unmarried",
        "Other-relative"
    ])
workclass = tf.feature_column.categorical_column_with_vocabulary_list(
    "workclass", [
        "Self-emp-not-inc", "Private", "State-gov", "Federal-gov",
        "Local-gov", "?", "Self-emp-inc", "Without-pay", "Never-worked"
    ])

occupation = tf.feature_column.categorical_column_with_hash_bucket(
    "occupation", hash_bucket_size=1000)


native_country = tf.feature_column.categorical_column_with_hash_bucket(
    "native_country", hash_bucket_size=1000)

age = tf.feature_column.numeric_column("age")
fnlwgt = tf.feature_column.numeric_column("fnlwgt")
education_num = tf.feature_column.numeric_column("education_num")
capital_gain = tf.feature_column.numeric_column("capital_gain")
capital_loss = tf.feature_column.numeric_column("capital_loss")
hours_per_week = tf.feature_column.numeric_column("hours_per_week")

def gender_cat(d):
    return gender

def race_cat(d):
    return race

def education_cat(d):
    return education

def marital_status_cat(d):
    return marital_status

def relationship_cat(d):
    return relationship

def workclass_cat(d):
    return workclass

def cat_hash(a):
    return tf.feature_column.categorical_column_with_hash_bucket(a, hash_bucket_size=1000)

def numeric(a):
    return tf.feature_column.numeric_column(a)

def convert_to_label(d, dictionary):
    return dictionary[d]

CSV_COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "gender",
    "capital_gain", "capital_loss", "hours_per_week", "native_country",
    "income_bracket"
]


FEATURE_DICT = collections.OrderedDict([
    ("age", (tf.float32, numeric)),
    ("workclass", (tf.string, workclass_cat)),
    ("fnlwgt", (tf.float32, numeric)),
    ("education", (tf.string, education_cat)),
    ("education_num", (tf.float32, numeric)),
    ("marital_status", (tf.string, marital_status_cat)),
    ("occupation", (tf.string, cat_hash)),
    ("relationship", (tf.string, relationship_cat)),
    ("race", (tf.string, race_cat)),
    ("gender", (tf.string, gender_cat)),
    ("capital_gain", (tf.float32, numeric)),
    ("capital_loss", (tf.float32, numeric)),
    ("hours_per_week", (tf.float32, numeric)),
    ("native_country", (tf.string, cat_hash))
])

_INCOME_DICT = {'>50K' : 'below', ' <=50K' : 'above'}

_URL_TRAIN = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'

_URL_TEST = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test'

class Adult(tfds.core.GeneratorBasedBuilder):

  """Prediction task is to determine whether a person makes over 50K a year."""

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "income": tfds.features.ClassLabel(names=["below", "above"]),
            "features": {
                name: dtype
                for name, (dtype, func) in FEATURE_DICT.items()},
        }),
        )

  def _split_generators(self, dl_manager):

    train = dl_manager.download(_URL_TRAIN)
    test = dl_manager.download(_URL_TEST)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={

                "file_path": train
            }),

        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={

                "file_path": test

            }),
            ]

  def _generate_examples(self, file_path):

    with tf.io.gfile.GFile(file_path) as f:
          raw_data = csv.DictReader(f, fieldnames=CSV_COLUMNS)
          for i, row in enumerate(raw_data):
            income_val = row.pop("income_bracket")
            yield i, {
                "income": _INCOME_DICT[income_val],
                "features": {
                name: FEATURE_DICT[name][1](value)
                for name, value in row.items()
                }
            }

