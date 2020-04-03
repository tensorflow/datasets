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
"""TED-LIUM speech recognition dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import numpy as np

import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled
at 16kHz. It contains about 118 hours of speech.

This is the TED-LIUM corpus release 1,
licensed under Creative Commons BY-NC-ND 3.0
(http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).
"""

_CITATION = """\
@inproceedings{rousseau2012tedlium,
  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus.},
  author={Rousseau, Anthony and Del{\\'e}glise, Paul and Est{\\`e}ve, Yannick},
  booktitle={Conference on Language Resources and Evaluation (LREC)},
  pages={125--129},
  year={2012}
}
"""

_URL = "https://www.openslr.org/7/"
_DL_URL = "http://www.openslr.org/resources/7/TEDLIUM_release1.tar.gz"


class Tedlium(tfds.core.BeamBasedBuilder):
  """TED-LIUM dataset release 1."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "speech":
                tfds.features.Audio(sample_rate=16000),
            "text":
                tfds.features.Text(),
            "speaker_id":
                tf.string,
            "gender":
                tfds.features.ClassLabel(names=["unknown", "female", "male"]),
            "id":
                tf.string,
        }),
        supervised_keys=("speech", "text"),
        homepage="https://www.openslr.org/7/",
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(sample_rate=16000,),
    )

  def _split_generators(self, dl_manager):
    extracted_dir = dl_manager.download_and_extract(_DL_URL)
    base_dir = os.path.join(extracted_dir, "TEDLIUM_release1")
    splits = []
    for split, dir_name in [(tfds.Split.TRAIN, "train"),
                            (tfds.Split.VALIDATION, "dev"),
                            (tfds.Split.TEST, "test")]:
      kwargs = {"directory": os.path.join(base_dir, dir_name)}
      splits.append(tfds.core.SplitGenerator(name=split, gen_kwargs=kwargs))
    return splits

  def _build_pcollection(self, pipeline, directory):
    beam = tfds.core.lazy_imports.apache_beam
    stm_files = tf.io.gfile.glob(os.path.join(directory, "stm", "*stm"))
    return (pipeline
            | beam.Create(stm_files)
            | beam.FlatMap(_generate_examples_from_stm_file))


def _generate_examples_from_stm_file(stm_path):
  """Generate examples from a TED-LIUM stm file."""
  stm_dir = os.path.dirname(stm_path)
  sph_dir = os.path.join(os.path.dirname(stm_dir), "sph")
  with tf.io.gfile.GFile(stm_path) as f:
    for line in f:
      line = line.strip()
      fn, channel, speaker, start, end, label, transcript = line.split(" ", 6)
      transcript = _maybe_trim_suffix(transcript)

      audio_file = "%s.sph" % fn
      samples = _extract_audio_segment(
          os.path.join(sph_dir, audio_file), int(channel), float(start),
          float(end))

      key = "-".join([speaker, start, end, label])
      example = {
          "speech": samples,
          "text": transcript,
          "speaker_id": speaker,
          "gender": _parse_gender(label),
          "id": key,
      }
      yield key, example


def _maybe_trim_suffix(transcript):
  # stm files for the train split contain a key (enclosed in parens) at the end.
  splits = transcript.rsplit(" ", 1)
  transcript = splits[0]
  if len(splits) > 1:
    suffix = splits[-1]
    if not suffix.startswith("("):
      transcript += " " + suffix
  return transcript


def _parse_gender(label_str):
  gender = re.split(",|_", label_str)[-1][:-1]
  # Fix inconsistencies in the data.
  if not gender:
    gender = -1  # Missing label.
  elif gender == "F":
    gender = "female"
  elif gender == "M":
    gender = "male"
  return gender


def _extract_audio_segment(sph_path, channel, start_sec, end_sec):
  """Extracts segment of audio samples (as an ndarray) from the given path."""
  with tf.io.gfile.GFile(sph_path, "rb") as f:
    segment = tfds.core.lazy_imports.pydub.AudioSegment.from_file(
        f, format="nistsphere")
  # The dataset only contains mono audio.
  assert segment.channels == 1
  assert channel == 1
  start_ms = int(start_sec * 1000)
  end_ms = int(end_sec * 1000)
  segment = segment[start_ms:end_ms]
  samples = np.array(segment.get_array_of_samples())
  return samples
