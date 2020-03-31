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
"""Healthy and unhealthy plant leaves dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{,
  author={Siddharth Singh Chouhan, Ajay Kaul, Uday Pratap Singh, Sanjeev
Jain},
  title={A Database of Leaf Images: Practice towards Plant Conservation with
Plant Pathology},
  howpublished={Mendeley Data},
  year={2019}
}
"""

_DESCRIPTION = """
This dataset consists of 4502 images of healthy and unhealthy plant leaves
divided into 22 categories by species and state of health. The images are in
high resolution JPG format.

There are no files with label prefix 0000, therefore label encoding is shifted
by one (e.g. file with label prefix 0001 gets encoded label 0).

Note: Each image is a separate download. Some might rarely fail, therefore make
sure to restart if that happens. An exception will be raised in case one of the
downloads repeatedly fails.

Dataset URL: https://data.mendeley.com/datasets/hb74ynkjcn/1
License: http://creativecommons.org/licenses/by/4.0
"""

# File name prefix to label mapping.
_LABEL_MAPPING = [
    ("0001", "Mango (P0) healthy"),
    ("0002", "Arjun (P1) healthy"),
    ("0003", "Alstonia Scholaris (P2) healthy"),
    ("0004", "Gauva (P3) healthy"),
    ("0005", "Jamun (P5) healthy"),
    ("0006", "Jatropha (P6) healthy"),
    ("0007", "Pongamia Pinnata (P7) healthy"),
    ("0008", "Basil (P8) healthy"),
    ("0009", "Pomegranate (P9) healthy"),
    ("0010", "Lemon (P10) healthy"),
    ("0011", "Chinar (P11) healthy"),
    ("0012", "Mango (P0) diseased"),
    ("0013", "Arjun (P1) diseased"),
    ("0014", "Alstonia Scholaris (P2) diseased"),
    ("0015", "Gauva (P3) diseased"),
    ("0016", "Bael (P4) diseased"),
    ("0017", "Jamun (P5) diseased"),
    ("0018", "Jatropha (P6) diseased"),
    ("0019", "Pongamia Pinnata (P7) diseased"),
    ("0020", "Pomegranate (P9) diseased"),
    ("0021", "Lemon (P10) diseased"),
    ("0022", "Chinar (P11) diseased"),
]
_URLS_FNAME = "image_classification/plant_leaves_urls.txt"
_MAX_DOWNLOAD_RETRY = 10


class DownloadRetryLimitReachedError(Exception):
  pass


class PlantLeaves(tfds.core.GeneratorBasedBuilder):
  """Healthy and unhealthy plant leaves dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    labels = list(zip(*_LABEL_MAPPING))[1]
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=labels)
        }),
        supervised_keys=("image", "label"),
        homepage="https://data.mendeley.com/datasets/hb74ynkjcn/1",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Batch download for this dataset is broken, therefore images have to be
    # downloaded independently from a list of urls.
    with tf.io.gfile.GFile(tfds.core.get_tfds_path(_URLS_FNAME)) as f:
      name_to_url_map = {
          os.path.basename(l.strip()): l.strip() for l in f.readlines()
      }
      retry_count = 0
      image_files = {}
      # We have to retry due to rare 504 HTTP errors. Downloads are cached,
      # therefore this shouldn't cause successful downloads to be retried.
      while True:
        try:
          image_files = dl_manager.download(name_to_url_map)
          break
        except tfds.download.DownloadError:
          retry_count += 1
          if retry_count == _MAX_DOWNLOAD_RETRY:
            raise DownloadRetryLimitReachedError(
                "Retry limit reached. Try downloading the dataset again.")
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={"image_files": image_files})
      ]

  def _generate_examples(self, image_files):
    """Yields examples."""
    label_map = {pattern: label for pattern, label in _LABEL_MAPPING}
    regexp = re.compile(r"^(\d\d\d\d)_.*\.JPG$")
    # Assigns labels to images based on label mapping.
    for original_fname, fpath in image_files.items():
      match = regexp.match(original_fname)
      if match and match.group(1) in label_map:
        label = label_map[match.group(1)]
        record = {
            "image": fpath,
            "image/filename": original_fname,
            "label": label,
        }
        yield original_fname, record
