"""Database of character image features; try to identify the letter
	"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences" }
"""

_DESCRIPTION = """
The objective is to identify each of a large number of black-and-white rectangular pixel displays as one of the 26 capital letters in the English alphabet.
The character images were based on 20 different fonts and each letter within these 20 fonts was randomly distorted to produce a file of 20,000 unique stimuli. Each stimulus was converted into 16 primitive numerical attributes (statistical moments and edge counts) which were then scaled to fit into a range of integer values from 0 through 15. We typically train on the first 16000 items and then use the resulting model to predict the letter category for the remaining 4000. See the article cited above for more details.
"""

import csv
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

class LetterRecognition(tfds.core.GeneratorBasedBuilder):
  """Database of character image features; try to identify the letter"""

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "label": tfds.features.ClassLabel(names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']),
            "features": tfds.features.Tensor(shape=(16,), dtype=tf.int32)
        }),
        supervised_keys=("label", "features"),
        homepage='https://archive.ics.uci.edu/ml/datasets/Letter+Recognition',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    data = dl_manager.download("https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={

                "file_path": data
            },
        ),
    ]

  def _generate_examples(self, file_path):
    with tf.io.gfile.GFile(file_path) as f:
      raw_data = csv.reader(f)
      for i, row in enumerate(raw_data):
        yield i, {
            "label": str(row[0]),
            "features": [int(x) for x in row[1:]]
        }