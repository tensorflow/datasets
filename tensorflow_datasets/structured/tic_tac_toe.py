"""Binary classification task on possible configurations of tic-tac-toe game"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import tensorflow.compat.v2 as tf
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
This database encodes the complete set of possible board configurations at the end of tic-tac-toe games, where "x" is assumed to have played first. The target concept is "win for x" (i.e., true when "x" has one of 8 possible ways to create a "three-in-a-row").
Interestingly, this raw database gives a stripped-down decision tree algorithm (e.g., ID3) fits. However, the rule-based CN2 algorithm, the simple IB1 instance-based learning algorithm, and the CITRE feature-constructing decision tree algorithm perform well on it.
"""

class TicTacToe(tfds.core.GeneratorBasedBuilder):
  """Binary classification task on possible configurations of tic-tac-toe game"""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "label": tfds.features.ClassLabel(names=["negative", "positive"]),
            "features": tfds.features.Sequence(ClassLabel(names=["b", "x", "o"]), length=3*3)
        }),
        supervised_keys=("label", "features"),
        homepage='https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    data = dl_manager.download("https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data")
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
            "label": str(row[-1]),
            "features": [convert(x) for x in row[:-1]]
        }

