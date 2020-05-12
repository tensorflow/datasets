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
"""Rock, Paper, Scissors dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@ONLINE {rps,
author = "Laurence Moroney",
title = "Rock, Paper, Scissors Dataset",
month = "feb",
year = "2019",
url = "http://laurencemoroney.com/rock-paper-scissors-dataset"
}
"""

_TRAIN_URL = "https://storage.googleapis.com/download.tensorflow.org/data/rps.zip"
_TEST_URL = "https://storage.googleapis.com/download.tensorflow.org/data/rps-test-set.zip"

_IMAGE_SIZE = 300
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)

_NAME_RE = re.compile(
    r"^(rps|rps-test-set)(?:/|\\)(rock|paper|scissors)(?:/|\\)[\w-]*\.png$"
)


class RockPaperScissors(tfds.core.GeneratorBasedBuilder):
  """Rock, Paper, Scissors dataset."""

  VERSION = tfds.core.Version(
      "3.0.0", "New split API (https://tensorflow.org/datasets/splits)")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="Images of hands playing rock, paper, scissor game.",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(
                names=["rock", "paper", "scissors"]),
        }),
        supervised_keys=("image", "label"),
        homepage="http://laurencemoroney.com/rock-paper-scissors-dataset",
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path),
            }),
    ]

  def _generate_examples(self, archive):
    """Generate rock, paper or scissors images and labels given the directory path.

    Args:
      archive: object that iterates over the zip.

    Yields:
      The image path and its corresponding label.
    """

    for fname, fobj in archive:
      res = _NAME_RE.match(fname)
      if not res:  # if anything other than .png; skip
        continue
      label = res.group(2).lower()
      record = {
          "image": fobj,
          "label": label,
      }
      yield fname, record
