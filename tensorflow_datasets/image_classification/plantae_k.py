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

"""Healthy and unhealthy plant leaves dataset."""

import os
import re

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{,
  author={Vippon Preet Kour, Sakshi Arora},
  title={PlantaeK: A leaf database of native plants of Jammu and Kashmir},
  howpublished={Mendeley Data},
  year={2019}
}
"""

_DESCRIPTION = """
This dataset contains 2153 images of healthy and unhealthy plant leaves divided
16 categories by species and state of health. The images are in high resolution
JPG format.

Note: Each image is a separate download. Some might rarely fail, therefore make
sure to restart if that happens. An exception will be raised in case one of the
downloads repeatedly fails.

Dataset URL: https://data.mendeley.com/datasets/t6j2h22jpx/1
License: http://creativecommons.org/licenses/by/4.0
"""

# File name prefix to label mapping.
_LABEL_MAPPING = [
    ("apple_d", "APPLE DISEASED"),
    ("apple_h", "APPLE HEALTHY"),
    ("apricot_d", "APRICOT DISEASED"),
    ("apricot_h", "APRICOT HEALTHY"),
    ("cherry_d", "CHERRY DISEASED"),
    ("cherry_h", "CHERRY HEALTHY"),
    ("cranberry_d", "CRANBERRY DISEASED"),
    ("cranberry_h", "CRANBERRY HEALTHY"),
    ("grapes_d", "GRAPES DISEASED"),
    ("grapes_h", "GRAPES HEALTHY"),
    ("peach_d", "PEACH DISEASED"),
    ("peach_h", "PEACH HEALTHY"),
    ("pear_d", "PEAR DISEASED"),
    ("pear_h", "PEAR HEALTHY"),
    ("walnut_d", "WALNUT DISEASED"),
    # There's a bug in file naming. walnut_h* files are still diseased.
    ("walnut_h", "WALNUT DISEASED"),
    ("walnut-h", "WALNUT HEALTHY"),
]
_URLS_FNAME = "image_classification/plantae_k_urls.txt"
_MAX_DOWNLOAD_RETRY = 10


class DownloadRetryLimitReachedError(Exception):
  pass


class PlantaeK(tfds.core.GeneratorBasedBuilder):
  """Healthy and unhealthy plant leaves dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    labels = sorted(set(list(zip(*_LABEL_MAPPING))[1]))
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=labels)
        }),
        supervised_keys=("image", "label"),
        homepage="https://data.mendeley.com/datasets/t6j2h22jpx/1",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Batch download for this dataset is broken, therefore images have to be
    # downloaded independently from a list of urls.
    with tf.io.gfile.GFile(os.fspath(tfds.core.tfds_path(_URLS_FNAME))) as f:
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
    regexp = re.compile(r"^(\w+[-_][dh])\d+\.JPG$")
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
