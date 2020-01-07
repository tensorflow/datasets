"""Lung Cancer Data Set from UCI Machine Learning Repository"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{Hong:2020,
author = "Hong, Z. Q, and Yang, J. Y.",
year = "1991",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences" } 
"""

_DESCRIPTION = """
This data was used by Hong and Young to illustrate the power of the optimal discriminant plane even in ill-posed settings. Applying the KNN method in the resulting plane gave 77% accuracy. However, these results are strongly biased (See Aeberhard's second ref. above, or email to stefan '@' coral.cs.jcu.edu.au). Results obtained by Aeberhard et al. are :

RDA : 62.5%, KNN 53.1%, Opt. Disc. Plane 59.4%

The data described 3 types of pathological lung cancers. The Authors give no information on the individual variables nor on where the data was originally used.

Notes:
- In the original data 4 values for the fifth attribute were -1. These values have been changed to ? (unknown). (*)
- In the original data 1 value for the 39 attribute was 4. This value has been changed to ? (unknown). (*)
"""

_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/lung-cancer/lung-cancer.data'

class LungCancer(tfds.core.GeneratorBasedBuilder):
  """Lung Cancer Data Set from UCI Machine Learning Repository"""

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "label": tfds.features.ClassLabel(num_classes=3),
            "features": tfds.features.Tensor(shape=(56,), dtype=tf.uint8)
        }),
        supervised_keys=("label", "features"),
        homepage='https://archive.ics.uci.edu/ml/datasets/Lung+Cancer',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    data = dl_manager.download(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "file_path": data
            },
        ),
    ]

  def _generate_examples(self, file_path):
    """Yields examples."""
    with tf.io.gfile.GFile(file_path) as f:
      raw_data = csv.reader(f)
      for i, row in enumerate(raw_data):
        if '?' not in row and row != []:
          yield i, {
              "label": int(row[0])-1,
              "features": [int(x) for x in row[:-1]]
          }
