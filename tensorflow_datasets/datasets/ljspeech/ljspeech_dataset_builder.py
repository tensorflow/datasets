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

"""LJSpeech dataset."""

from __future__ import annotations

import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_URL = "https://keithito.com/LJ-Speech-Dataset/"
_DL_URL = "https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2"


class Builder(tfds.core.GeneratorBasedBuilder):
  """LJSpeech dataset."""

  VERSION = tfds.core.Version("1.1.1")
  RELEASE_NOTES = {
      "1.1.1": "Fix speech data type with dtype=tf.int16.",
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "id": np.str_,
            "speech": tfds.features.Audio(sample_rate=22050, dtype=np.int16),
            "text": tfds.features.Text(),
            "text_normalized": tfds.features.Text(),
        }),
        supervised_keys=("text_normalized", "speech"),
        homepage=_URL,
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
    with epath.Path(metadata_path).open() as f:
      for line in f:
        line = line.strip()
        key, transcript, transcript_normalized = line.split("|")
        wav_path = os.path.join(
            directory, "LJSpeech-1.1", "wavs", "%s.wav" % key
        )
        example = {
            "id": key,
            "speech": wav_path,
            "text": transcript,
            "text_normalized": transcript_normalized,
        }
        yield key, example
