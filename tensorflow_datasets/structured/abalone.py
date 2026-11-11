"""Abalone Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import collections
import csv
import numpy as np

_CITATION = """\
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences" }
"""

_DESCRIPTION = """\
Predicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age. Further information, such as weather patterns and location (hence food availability) may be required to solve the problem.

From the original data examples with missing values were removed (the majority having the predicted value missing), and the ranges of the continuous values have been scaled for use with an ANN (by dividing by 200).
"""


def return_same(d):
  return d

def return_float(d):
  return np.float32(d)

FEATURE_DICT = collections.OrderedDict([
  ("Sex", (tfds.features.ClassLabel(names=["M", "F", "I"]), return_same)),
  ("Length", (tf.float32, return_float)),
  ("Diameter", (tf.float32, return_float)),
  ("Height", (tf.float32, return_float)),
  ("Whole weight", (tf.float32, return_float)),
  ("Shucked weight", (tf.float32, return_float)),
  ("Viscera weight", (tf.float32, return_float)),
  ("Shell weight", (tf.float32, return_float))
])

_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
_HOMEPAGE_URL = "https://archive.ics.uci.edu/ml/datasets/Abalone"

class Abalone(tfds.core.GeneratorBasedBuilder):
  """Abalone age prediction dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
        "age": tfds.features.Tensor(shape=[], dtype=tf.float32),
        "features": {name: dtype
         for name, (dtype, func) in FEATURE_DICT.items()}
        }),
      supervised_keys=("features", "age"),
      homepage=_HOMEPAGE_URL,
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    abalone_file = dl_manager.download(_URL)
    all_lines = tf.io.gfile.GFile(abalone_file).read().split("\n")
    records = [l for l in all_lines if l]
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        gen_kwargs={"file_path": abalone_file})]

  def _generate_examples(self, file_path):
    """Yields examples."""
    with tf.io.gfile.GFile(file_path) as f:
      raw_data = csv.DictReader(f, fieldnames=["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "age"])
      for i, row in enumerate(raw_data):
        age_val = row.pop("age")
        yield i, {
          "age": age_val,
          "features": {
            name: FEATURE_DICT[name][1](value)
            for name, value in row.items()
            }
        }
