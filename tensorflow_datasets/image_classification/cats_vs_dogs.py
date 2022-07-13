# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Cats vs Dogs dataset."""

import re

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@Inproceedings (Conference){asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization,
author = {Elson, Jeremy and Douceur, John (JD) and Howell, Jon and Saul, Jared},
title = {Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization},
booktitle = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
year = {2007},
month = {October},
publisher = {Association for Computing Machinery, Inc.},
url = {https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/},
edition = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
}
"""

_URL = ("https://download.microsoft.com/download/3/E/1/"
        "3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip")
_NUM_CORRUPT_IMAGES = 1738
_DESCRIPTION = (("A large set of images of cats and dogs. "
                 "There are %d corrupted images that are dropped.") %
                _NUM_CORRUPT_IMAGES)

_NAME_RE = re.compile(r"^PetImages[\\/](Cat|Dog)[\\/]\d+\.jpg$")


class CatsVsDogs(tfds.core.GeneratorBasedBuilder):
  """Cats vs Dogs."""

  VERSION = tfds.core.Version("4.0.0")
  RELEASE_NOTES = {
      "4.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),  # eg 'PetImages/Dog/0.jpg'
            "label": tfds.features.ClassLabel(names=["cat", "dog"]),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.microsoft.com/en-us/download/details.aspx?id=54765",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(path),
            }),
    ]

  def _generate_examples(self, archive):
    """Generate Cats vs Dogs images and labels given a directory path."""
    num_skipped = 0
    for fname, fobj in archive:
      res = _NAME_RE.match(fname)
      if not res:  # README file, ...
        continue
      label = res.group(1).lower()
      if tf.compat.as_bytes("JFIF") not in fobj.peek(10):
        num_skipped += 1
        continue
      record = {
          "image": fobj,
          "image/filename": fname,
          "label": label,
      }
      yield fname, record

    if num_skipped != _NUM_CORRUPT_IMAGES:
      raise ValueError("Expected %d corrupt images, but found %d" %
                       (_NUM_CORRUPT_IMAGES, num_skipped))
    logging.warning("%d images were corrupted and were skipped", num_skipped)
