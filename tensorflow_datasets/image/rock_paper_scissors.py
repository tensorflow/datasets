# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

_TRAIN_URL = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps.zip"
_TEST_URL = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps-test-set.zip"

_IMAGE_SIZE = 300
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)

_NAME_RE = re.compile(r"^(rps|rps-test-set)/(rock|paper|scissors)/[\w-]*\.png$")


class RockPaperScissors(tfds.core.GeneratorBasedBuilder):
  """Rock, Paper, Scissors dataset."""

  VERSION = tfds.core.Version("1.0.0",
                              experiments={tfds.core.Experiment.S3: False})
  SUPPORTED_VERSIONS = [
      tfds.core.Version("3.0.0"),
      tfds.core.Version("2.0.0"),
  ]
  # Version history:
  # 3.0.0: S3 with new hashing function (different shuffle).
  # 2.0.0: S3 (new shuffling, sharding and slicing mechanism).

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
        urls=["http://laurencemoroney.com/rock-paper-scissors-dataset"],
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
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
      if self.version.implements(tfds.core.Experiment.S3):
        yield fname, record
      else:
        yield record
