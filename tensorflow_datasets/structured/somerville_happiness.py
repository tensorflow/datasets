"""Somerville Happiness Survey Data Set from UCI Machine Learning Repository"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{Waldemar:2020 ,
author = "Waldemar W. Koczkodaj",
year = "2015",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
}
"""

_DESCRIPTION = """It is a case of supervised learning with the use of Receiver Operating Characteristic (ROC) to 
select the minimal set of attributes preserving or increasing predictability of the data.

Attribute Information:

D = decision attribute (D) with values 0 (unhappy) and 1 (happy) 
X1 = the availability of information about the city services 
X2 = the cost of housing 
X3 = the overall quality of public schools 
X4 = your trust in the local police 
X5 = the maintenance of streets and sidewalks 
X6 = the availability of social community events 

Attributes X1 to X6 have values 1 to 5.
"""
_FEELING = ["happy", "unhappy"]

_FEELING_DICT = {"1": "happy", "0": "unhappy"}

def check_input(d):
  if d <= 5:
    return d

FEATURE_DICT = collections.OrderedDict([
    ("X1", (tf.int32, check_input)),
    ("X2", (tf.int32, check_input)),
    ("X3", (tf.int32, check_input)),
    ("X4", (tf.int32, check_input)),
    ("X5", (tf.int32, check_input)),
    ("X6", (tf.int32, check_input))
])

_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00479/SomervilleHappinessSurvey2015.csv'

class SomervilleHappiness(tfds.core.GeneratorBasedBuilder):
  
  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        
        features=tfds.features.FeaturesDict({
           "feeling": tfds.features.ClassLabel(names=_FEELING),
           "features": {name: dtype
                         for name, (dtype, func) in FEATURE_DICT.items()}
        }),
        supervised_keys=("features", "feeling"),
        urls='https://archive.ics.uci.edu/ml/datasets/Somerville+Happiness+Survey',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
              'file_path': path,
            },
        ),
    ]

  def _generate_examples(self, file_path):
    with open(file_path, newline='', encoding='utf-16') as f:
      reader = csv.DictReader(f, quoting=csv.QUOTE_NONE)
      for i, row in enumerate(reader):
        yield i, {
               "feeling": _FEELING_DICT['1'],
               "features": row,
          }
