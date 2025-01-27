# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

import io
import os
import re
import zipfile

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
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

_URL = (
    "https://download.microsoft.com/download/3/E/1/"
    "3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
)
_NUM_CORRUPT_IMAGES = 1738
_DESCRIPTION = (
    "A large set of images of cats and dogs. "
    f"There are {_NUM_CORRUPT_IMAGES} corrupted images that are dropped."
)

_NAME_RE = re.compile(r"^PetImages[\\/](Cat|Dog)[\\/]\d+\.jpg$")


class CatsVsDogs(tfds.core.GeneratorBasedBuilder):
  """Cats vs Dogs."""

  VERSION = tfds.core.Version("4.0.1")
  RELEASE_NOTES = {
      "4.0.0": "New split API (https://tensorflow.org/datasets/splits)",
      "4.0.1": (
          "Recoding images in generator to fix corrupt JPEG data warnings"
          " (https://github.com/tensorflow/datasets/issues/2188)"
      ),
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
        homepage=(
            "https://www.microsoft.com/en-us/download/details.aspx?id=54765"
        ),
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
            },
        ),
    ]

  def _generate_examples(self, archive):
    """Generate Cats vs Dogs images and labels given a directory path."""
    num_skipped = 0
    for fname, fobj in archive:
      norm_fname = os.path.normpath(fname)
      res = _NAME_RE.match(norm_fname)
      if not res:  # README file, ...
        continue
      label = res.group(1).lower()
      if tf.compat.as_bytes("JFIF") not in fobj.peek(10):
        num_skipped += 1
        continue

      # Some images caused 'Corrupt JPEG data...' messages during training or
      # any other iteration recoding them once fixes the issue (discussion:
      # https://github.com/tensorflow/datasets/issues/2188).
      # Those messages are now displayed when generating the dataset instead.
      img_data = fobj.read()
      img_tensor = tf.image.decode_image(img_data)
      img_recoded = tf.io.encode_jpeg(img_tensor)

      # Converting the recoded image back into a zip file container.
      buffer = io.BytesIO()
      with zipfile.ZipFile(buffer, "w") as new_zip:
        new_zip.writestr(norm_fname, img_recoded.numpy())
      new_fobj = zipfile.ZipFile(buffer).open(norm_fname)

      record = {
          "image": new_fobj,
          "image/filename": norm_fname,
          "label": label,
      }
      yield norm_fname, record

    if num_skipped != _NUM_CORRUPT_IMAGES:
      raise ValueError(
          f"Expected {_NUM_CORRUPT_IMAGES} corrupt images, but found"
          f" {num_skipped}."
      )
    logging.warning("%d images were corrupted and were skipped", num_skipped)
