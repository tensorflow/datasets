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
"""Healthy and unhealthy citrus fruits and leaves dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{rauf2019citrus,
  title={A citrus fruits and leaves dataset for detection and classification of
citrus diseases through machine learning},
  author={Rauf, Hafiz Tayyab and Saleem, Basharat Ali and Lali, M Ikram Ullah
and Khan, Muhammad Attique and Sharif, Muhammad and Bukhari, Syed Ahmad Chan},
  journal={Data in brief},
  volume={26},
  pages={104340},
  year={2019},
  publisher={Elsevier}
}
"""

_DESCRIPTION = """
The original citrus dataset contains 759 images of healthy and unhealthy citrus
fruits and leaves. However, for now we only export 594 images of citrus leaves
with the following labels: Black Spot, Canker, Greening, and Healthy. The
exported images are in PNG format and have 256x256 pixels.

NOTE: Leaf images with Melanose label were dropped due to very small count and
other non-leaf images being present in the same directory.

Dataset URL: https://data.mendeley.com/datasets/3f83gxmv57/2
License: http://creativecommons.org/licenses/by/4.0
"""

_URL = "https://data.mendeley.com/datasets/3f83gxmv57/2/files/6f809085-8c29-49f7-afbc-f90854fd45dc/Citrus.zip"
_LEAVES_LABELS = ["Black spot", "canker", "greening", "healthy"]


class CitrusLeaves(tfds.core.GeneratorBasedBuilder):
  """Subset of the citrus dataset with just leaves."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=_LEAVES_LABELS)
        }),
        supervised_keys=("image", "label"),
        homepage="https://data.mendeley.com/datasets/3f83gxmv57/2",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"datapath": path})
    ]

  def _generate_examples(self, datapath):
    """Yields examples based on the passed split index."""
    for label in _LEAVES_LABELS:
      # The real dataset has spaces in directories (label names), which causes
      # fake data test to fail due objfs not handling whitespace in paths. The
      # solution is to replace spaces with underscores in fake data directories
      # and then not care whether a character is a space or an underscore.
      fuzzy_label = label.replace(" ", "[_ ]")
      glob_path = os.path.join(datapath, "Citrus/Leaves", fuzzy_label, "*.png")
      for fpath in tf.io.gfile.glob(glob_path):
        fname = os.path.basename(fpath)
        record = {
            "image": fpath,
            "image/filename": fname,
            "label": label,
        }
        yield "{}/{}".format(label, fname), record
