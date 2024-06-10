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

"""Healthy and unhealthy plant leaves dataset."""

import os

import tensorflow_datasets.public_api as tfds

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

_DOWNLOAD_URL = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/hb74ynkjcn-1.zip"


class DownloadRetryLimitReachedError(Exception):
  pass


class Builder(tfds.core.GeneratorBasedBuilder):
  """Healthy and unhealthy plant leaves dataset."""

  VERSION = tfds.core.Version("0.1.1")
  RELEASE_NOTES = {
      "0.1.0": "Initial release.",
      "0.1.1": "Fix checksum error.",
  }

  def _info(self):
    labels = list(zip(*_LABEL_MAPPING))[1]
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=labels),
        }),
        supervised_keys=("image", "label"),
        homepage="https://data.mendeley.com/datasets/hb74ynkjcn/1",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Batch download for this dataset is broken, therefore images have to be
    # downloaded independently from a list of urls.
    archive_path = dl_manager.download(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"archive": dl_manager.iter_archive(archive_path)},
        )
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    for filename, fobj in archive:
      if not filename.endswith(".JPG"):
        continue
      fname_split = filename.split(os.path.sep)
      label = fname_split[-3] + " " + fname_split[-2]
      record = {
          "image": fobj,
          "image/filename": fname_split[-1],
          "label": label,
      }
      yield fname_split[-1], record
