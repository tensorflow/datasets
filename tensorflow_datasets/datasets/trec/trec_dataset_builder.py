# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""The Text REtrieval Conference (TREC) Question Classification dataset."""

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URLs = {
    "train": "http://cogcomp.org/Data/QA/QC/train_5500.label",
    "test": "http://cogcomp.org/Data/QA/QC/TREC_10.label",
}

_COARSE_LABELS = ["DESC", "ENTY", "ABBR", "HUM", "NUM", "LOC"]

_FINE_LABELS = [
    "manner",
    "cremat",
    "animal",
    "exp",
    "ind",
    "gr",
    "title",
    "def",
    "date",
    "reason",
    "event",
    "state",
    "desc",
    "count",
    "other",
    "letter",
    "religion",
    "food",
    "country",
    "color",
    "termeq",
    "city",
    "body",
    "dismed",
    "mount",
    "money",
    "product",
    "period",
    "substance",
    "sport",
    "plant",
    "techmeth",
    "volsize",
    "instru",
    "abb",
    "speed",
    "word",
    "lang",
    "perc",
    "code",
    "dist",
    "temp",
    "symbol",
    "ord",
    "veh",
    "weight",
    "currency",
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """TREC Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "label-coarse": tfds.features.ClassLabel(names=_COARSE_LABELS),
            "label-fine": tfds.features.ClassLabel(names=_FINE_LABELS),
            "text": tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage="https://cogcomp.seas.upenn.edu/Data/QA/QC/",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    dl_files = dl_manager.download_and_extract(_URLs)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": dl_files["train"],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepath": dl_files["test"],
            },
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""

    with tf.io.gfile.GFile(filepath, "rb") as f:
      for id_, row in enumerate(f):
        # One non-ASCII byte: sisterBADBYTEcity. We replace it with a space
        label, _, text = (
            row.replace(b"\xf0", b" ").strip().decode().partition(" ")
        )
        coarse_label, _, fine_label = label.partition(":")
        yield id_, {
            "label-coarse": coarse_label,
            "label-fine": fine_label,
            "text": text,
        }
