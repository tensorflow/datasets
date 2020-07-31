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

"""LJSpeech dataset."""

import os

import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{ljspeech17,
  author       = {Keith Ito},
  title        = {The LJ Speech Dataset},
  howpublished = {\\url{https://keithito.com/LJ-Speech-Dataset/}},
  year         = 2017
}
"""

_DESCRIPTION = """\
This is a public domain speech dataset consisting of 13,100 short audio clips of
a single speaker reading passages from 7 non-fiction books. A transcription is
provided for each clip. Clips vary in length from 1 to 10 seconds and have a
total length of approximately 24 hours.

The texts were published between 1884 and 1964, and are in the public domain.
The audio was recorded in 2016-17 by the LibriVox project and is also in the
public domain.
"""

_URL = "https://keithito.com/LJ-Speech-Dataset/"
_DL_URL = "https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2"


class Ljspeech(tfds.core.GeneratorBasedBuilder):
  """LJSpeech dataset."""

  VERSION = tfds.core.Version("1.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id": tf.string,
            "speech": tfds.features.Audio(sample_rate=22050),
            "text": tfds.features.Text(),
            "text_normalized": tfds.features.Text(),
        }),
        supervised_keys=("text_normalized", "speech"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(sample_rate=22050),
    )

  def _split_generators(self, dl_manager):
    extracted_dir = dl_manager.download_and_extract(_DL_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"directory": extracted_dir},
        ),
    ]

  def _generate_examples(self, directory):
    """Yields examples."""
    metadata_path = os.path.join(directory, "LJSpeech-1.1", "metadata.csv")
    with tf.io.gfile.GFile(metadata_path) as f:
      for line in f:
        line = line.strip()
        key, transcript, transcript_normalized = line.split("|")
        wav_path = os.path.join(directory, "LJSpeech-1.1", "wavs",
                                "%s.wav" % key)
        example = {
            "id": key,
            "speech": wav_path,
            "text": transcript,
            "text_normalized": transcript_normalized,
        }
        yield key, example
