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

"""GTZAN Music Speech dataset."""

import os
import re

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {Music Speech,
    author = "Tzanetakis, George",
    title  = "GTZAN Music/Speech Collection",
    year   = "1999",
    url    = "http://marsyas.info/index.html"
}
"""

_DESCRIPTION = """
The dataset was collected for the purposes of music/speech discrimination.
The dataset consists of 120 tracks, each 30 seconds long.
Each class (music/speech) has 60 examples.
The tracks are all 22050Hz Mono 16-bit audio files in .wav format.
"""

_DOWNLOAD_URL = "http://opihi.cs.uvic.ca/sound/music_speech.tar.gz"
_HOMEPAGE_URL = "http://marsyas.info/index.html"

_CLASS_LABELS = [
    "music",
    "speech"
]


class GTZANMusicSpeech(tfds.core.GeneratorBasedBuilder):
  """GTZANMusicSpeech Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "audio":
                tfds.features.Audio(
                    file_format="wav",
                    sample_rate=22050),
            "label": tfds.features.ClassLabel(names=_CLASS_LABELS),
            "audio/filename":
                tfds.features.Text(),
        }),
        supervised_keys=("audio", "label"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({"music_speech": _DOWNLOAD_URL})
    path = os.path.join(dl_paths["music_speech"], "music_speech")
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": path
            }),
    ]

  def _generate_examples(self, path):
    """Yields examples.

    Args:
       path: Path of the downloaded and extracted directory

    Yields:
       Next examples
    """

    #  The wav files are in directories named "{label}_wav"
    name_regex = re.compile(r"(.*)(speech|music)\_.*\/[\w-]*\.(wav)")

    for root, _, file_name in tf.io.gfile.walk(path):
      for fname in file_name:
        full_file_name = os.path.join(root, fname)
        res = name_regex.match(full_file_name)
        if not res:
          continue
        label = res.group(2)
        key = fname
        example = {
            "audio": full_file_name,
            "label": label,
            "audio/filename": fname,
        }
        yield key, example
