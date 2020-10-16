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
"""credit_card_fraud dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import pandas as pd
import collections
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {kagglemachinelearninggroupulb2016,
    author = "Kaggle and Machine Learning Group - ULB",
    title  = "Credt Card Fraud Detection",
    month  = "mar",
    year   = "2016",
    url    = "https://www.kaggle.com/mlg-ulb/creditcardfraud"}

@CONFERENCE {andreadalpozzolooliviercaelenreida.johnsongianlucabontempi2015,
    author       = "Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi",
    title        = "Calibrating Probability with Undersampling for Unbalanced Classification",
    year         = "2015",
    address      = "Cape Town, South Africa",
    month        = "dec",
    organization = "IEEE Symposium Series on Computational Intelligence (SSCI)"}
"""

_DESCRIPTION = """
The datasets contains transactions made by credit cards in September 2013 by european cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.
"""

_URL = "https://www.openml.org/data/get_csv/1673544/phpKo8OWT"

FEATURES = collections.OrderedDict([
    ('Time', tf.float64),
    ('V1', tf.float64),
    ('V2', tf.float64),
    ('V3', tf.float64),
    ('V4', tf.float64),
    ('V5', tf.float64),
    ('V6', tf.float64),
    ('V7', tf.float64),
    ('V8', tf.float64),
    ('V9', tf.float64),
    ('V10', tf.float64),
    ('V11', tf.float64),
    ('V12', tf.float64),
    ('V13', tf.float64),
    ('V14', tf.float64),
    ('V15', tf.float64),
    ('V16', tf.float64),
    ('V17', tf.float64),
    ('V18', tf.float64),
    ('V19', tf.float64),
    ('V20', tf.float64),
    ('V21', tf.float64),
    ('V22', tf.float64),
    ('V23', tf.float64),
    ('V24', tf.float64),
    ('V25', tf.float64),
    ('V26', tf.float64),
    ('V27', tf.float64),
    ('V28', tf.float64),
    ('Amount', tf.float64),
])

class CreditCardFraud(tfds.core.GeneratorBasedBuilder):
  """Classification task for determining fraudulent or genuine credit card behaviour"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "Class":
                tfds.features.ClassLabel(names = ["'0'","'1'"]),
            "features" :
                {name: dtype for name,dtype in FEATURES.items()}
        }),
        supervised_keys=("Class","features"),
        # Homepage of the dataset for documentation
        homepage='https://www.kaggle.com/mlg-ulb/creditcardfraud',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data = dl_manager.download(_URL)
    #There are no predeffined validation/test set available for this dataset
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'file_path' : data},
        ),
    ]

  def _generate_examples(self, file_path):
    """Yields examples.

    Args:
    file_path : file path corresponding to the csv data file"""
    with tf.io.gfile.GFile(file_path) as f:
      raw_data = csv.DictReader(f)
      for i, row in enumerate(raw_data):
        yield i, {
            'Class': row.pop('Class'),
            'features': {name: value for name, value in row.items()},
        }
