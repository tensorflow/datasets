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
"""Breast Cancer Wisconsin dataset."""

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

BCWD_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

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
Features are computed from a digitized image of a fine needle aspirate (FNA)
of a breast mass. They describe characteristics of the cell nuclei present in
the image. The goal of the dataset is to predict whether the cancer in the cell
is benign or malignant. The attribute information is as follows:
#  Attribute                     Domain
   -- -----------------------------------------
   1. Sample code number            id number
   2. Clump Thickness               1 - 10
   3. Uniformity of Cell Size       1 - 10
   4. Uniformity of Cell Shape      1 - 10
   5. Marginal Adhesion             1 - 10
   6. Single Epithelial Cell Size   1 - 10
   7. Bare Nuclei                   1 - 10
   8. Bland Chromatin               1 - 10
   9. Normal Nucleoli               1 - 10
  10. Mitoses                       1 - 10
  11. Class:                        Benign or Malignant
  For this dataset, 0 represents benign and 1 represents malignant
  """


def convert_to_int(number):
  return -1 if number == "?" else np.int8(number)


COLUMNS = ["clump_thickness", "uniformity_of_cell_size",
           "uniformity_of_cell_shape", "marginal_adhesion",
           "single_epithelial_cell_size", "bare_nuclei", "bland_chromatin",
           "normal_nucleoli", "mitoses"]


FEATURES = tfds.features.FeaturesDict({
    "clump_thickness": tf.int8,
    "uniformity_of_cell_size": tf.int8,
    "uniformity_of_cell_shape": tf.int8,
    "marginal_adhesion": tf.int8,
    "single_epithelial_cell_size": tf.int8,
    "bare_nuclei": tf.int8,
    "bland_chromatin": tf.int8,
    "normal_nucleoli": tf.int8,
    "mitoses": tf.int8
})


class BreastCancer(tfds.core.GeneratorBasedBuilder):
  """Breast Cancer Wisconsin dataset."""

  VERSION = tfds.core.Version("0.0.1")
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "features": FEATURES,
            "label": tfds.features.ClassLabel(names=['Benign', 'Malignant'])
        }),
        supervised_keys=("features", "label"),
        homepage="https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Generate Splits"""
    bcwd_file = dl_manager.download(BCWD_URL)
    all_lines = tf.io.gfile.GFile(bcwd_file).read().split("\n")
    records = [l.split(",") for l in all_lines if l]

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"records": records}),
    ]

  def _generate_examples(self, records):
    for i, row in enumerate(records):
      label = row[-1]
      #the 0 label represents 2 in the original dataset(benig & 1 represents
      # 4(malignant)
      label = 0 if label == 2 else 1
      dict_values = dict(zip(COLUMNS, map(lambda x: x.strip(), row[:-1])))
      yield i, {
          "label": label,
          "features": {
              name: convert_to_int(value) for name, value in dict_values.items()
          }
      }
