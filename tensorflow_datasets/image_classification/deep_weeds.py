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

"""Dataset class for DeepWeeds dataset."""

import csv
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://drive.google.com/uc?export=download&id=1xnK3B6K6KekDI55vwJ0vnc2IGoDga9cj"
_URL_LABELS = "https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/labels/labels.csv"

_DESCRIPTION = (
    """The DeepWeeds dataset consists of 17,509 images capturing eight different weed species native to Australia """
    """in situ with neighbouring flora.The selected weed species are local to pastoral grasslands across the state of Queensland."""
    """The images were collected from weed infestations at the following sites across Queensland: "Black River", "Charters Towers", """
    """ "Cluden", "Douglas", "Hervey Range", "Kelso", "McKinlay" and "Paluma"."""
)

_IMAGE_SHAPE = (256, 256, 3)

_CITATION = """\
 @article{DeepWeeds2019,
  author = {Alex Olsen and
    Dmitry A. Konovalov and
    Bronson Philippa and
    Peter Ridd and
    Jake C. Wood and
    Jamie Johns and
    Wesley Banks and
    Benjamin Girgenti and
    Owen Kenny and
    James Whinney and
    Brendan Calvert and
    Mostafa {Rahimi Azghadi} and
    Ronald D. White},
  title = {{DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning}},
  journal = {Scientific Reports},
  year = 2019,
  number = 2058,
  month = 2,
  volume = 9,
  issue = 1,
  day = 14,
  url = "https://doi.org/10.1038/s41598-018-38343-3",
  doi = "10.1038/s41598-018-38343-3"
}
"""


class DeepWeeds(tfds.core.GeneratorBasedBuilder):
  """DeepWeeds Image Dataset Class."""

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0": "Update download URL.",
      "2.0.0": "Fixes wrong labels in V1.",
  }

  def _info(self):
    """Define Dataset Info."""

    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=9),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/AlexOlsen/DeepWeeds",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Define Splits."""
    paths = dl_manager.download_and_extract({
        "image": _URL,
        "label": _URL_LABELS})

    return [
        tfds.core.SplitGenerator(
            name="train",
            gen_kwargs={
                "data_dir_path": paths["image"],
                "label_path": paths["label"],
            },
        ),
    ]

  def _generate_examples(self, data_dir_path, label_path):
    """Generate images and labels for splits."""

    with tf.io.gfile.GFile(label_path) as f:
      # Convert to list to reuse the iterator multiple times
      reader = list(csv.DictReader(f))

    # Extract the mapping int -> str and save the label name string to the
    # feature
    label_id_to_name = {int(row["Label"]): row["Species"] for row in reader}
    self.info.features["label"].names = [
        v for _, v in sorted(label_id_to_name.items())
    ]

    filename_to_label = {row["Filename"]: row["Species"] for row in reader}
    for file_name in tf.io.gfile.listdir(data_dir_path):
      yield file_name, {
          "image": os.path.join(data_dir_path, file_name),
          "label": filename_to_label[file_name]
      }
