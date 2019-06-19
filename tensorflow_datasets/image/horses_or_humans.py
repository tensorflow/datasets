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

"""Horses or Humans dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@ONLINE {horses_or_humans,
author = "Laurence Moroney",
title = "Horses or Humans Dataset",
month = "feb",
year = "2019",
url = "http://laurencemoroney.com/horses-or-humans-dataset"
}
"""

_TRAIN_URL = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip"
_TEST_URL = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip"

_IMAGE_SIZE = 300
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)

_NAME_RE = re.compile(r"^(humans|horses)/[\w-]*\.png$")


class HorsesOrHumans(tfds.core.GeneratorBasedBuilder):
  """Horses or Humans dataset."""

  VERSION = tfds.core.Version("1.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.0.0", experiments={tfds.core.Experiment.S3: True}),
      tfds.core.Version("1.0.0"),
  ]
  # Version history:
  # 2.0.0: S3 (new shuffling, sharding and slicing mechanism).

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A large set of images of horses and humans.",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(
                names=["horses", "humans"]),
        }),
        supervised_keys=("image", "label"),
        urls=["http://laurencemoroney.com/horses-or-humans-dataset"],
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path)
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path)
            }),
    ]

  def _generate_examples(self, archive):
    """Generate horses or humans images and labels given the directory path.

    Args:
      archive: object that iterates over the zip.

    Yields:
      The image path and its corresponding label.
    """

    for fname, fobj in archive:
      res = _NAME_RE.match(fname)
      if not res:  # if anything other than .png; skip
        continue
      label = res.group(1).lower()
      record = {
          "image": fobj,
          "label": label,
      }
      if self.version.implements(tfds.core.Experiment.S3):
        yield fname, record
      else:
        yield record
