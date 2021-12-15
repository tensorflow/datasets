# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""GZTAN dataset."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{tzanetakis_essl_cook_2001,
author    = "Tzanetakis, George and Essl, Georg and Cook, Perry",
title     = "Automatic Musical Genre Classification Of Audio Signals",
url       = "http://ismir2001.ismir.net/pdf/tzanetakis.pdf",
publisher = "The International Society for Music Information Retrieval",
year      = "2001"
}
"""

_DESCRIPTION = """
The dataset consists of 1000 audio tracks each 30 seconds long.
It contains 10 genres, each represented by 100 tracks.
The tracks are all 22050Hz Mono 16-bit audio files in .wav format.

The genres are:

* blues
* classical
* country
* disco
* hiphop
* jazz
* metal
* pop
* reggae
* rock

"""

_DOWNLOAD_URL = "http://opihi.cs.uvic.ca/sound/genres.tar.gz"
_HOMEPAGE_URL = "http://marsyas.info/index.html"

_CLASS_LABELS = [
    "blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop",
    "reggae", "rock"
]


class GTZAN(tfds.core.GeneratorBasedBuilder):
  """GTZAN Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "audio": tfds.features.Audio(file_format="wav", sample_rate=22050),
            "label": tfds.features.ClassLabel(names=_CLASS_LABELS),
            "audio/filename": tfds.features.Text(),
        }),
        supervised_keys=("audio", "label"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({"genres": _DOWNLOAD_URL})
    path = os.path.join(dl_paths["genres"], "genres")
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"path": path}),
    ]

  def _generate_examples(self, path):
    """Yields examples.

    Args:
       path: Path of the downloaded and extracted directory

    Yields:
       Next examples
    """
    for root, _, file_name in tf.io.gfile.walk(path):
      for fname in file_name:
        if fname.endswith(".wav"):  # select only .wav files
          # Each .wav file has name in the format of <genre>.<number>.wav
          label = fname.split(".")[0]
          key = fname
          example = {
              "audio": os.path.join(root, fname),
              "label": label,
              "audio/filename": fname,
          }
          yield key, example
