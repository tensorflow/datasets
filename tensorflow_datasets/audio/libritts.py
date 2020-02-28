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

"""LibriTTS dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{zen2019libritts,
  title = {LibriTTS: A Corpus Derived from LibriSpeech for Text-to-Speech},
  author = {H. Zen and V. Dang and R. Clark and Y. Zhang and R. J. Weiss and Y. Jia and Z. Chen and Y. Wu},
  booktitle = {Proc. Interspeech},
  month = sep,
  year = {2019},
  doi = {10.21437/Interspeech.2019-2441},
}
"""

_DESCRIPTION = """\
LibriTTS is a multi-speaker English corpus of approximately 585 hours of read
English speech at 24kHz sampling rate, prepared by Heiga Zen with the assistance
of Google Speech and Google Brain team members. The LibriTTS corpus is designed
for TTS research. It is derived from the original materials (mp3 audio files
from LibriVox and text files from Project Gutenberg) of the LibriSpeech corpus.
The main differences from the LibriSpeech corpus are listed below:

1. The audio files are at 24kHz sampling rate.
2. The speech is split at sentence breaks.
3. Both original and normalized texts are included.
4. Contextual information (e.g., neighbouring sentences) can be extracted.
5. Utterances with significant background noise are excluded.
"""

_URL = "http://www.openslr.org/60"
_DL_URL = "http://www.openslr.org/resources/60/"
_DL_URLS = {
    "dev_clean": _DL_URL + "dev-clean.tar.gz",
    "dev_other": _DL_URL + "dev-other.tar.gz",
    "test_clean": _DL_URL + "test-clean.tar.gz",
    "test_other": _DL_URL + "test-other.tar.gz",
    "train_clean100": _DL_URL + "train-clean-100.tar.gz",
    "train_clean360": _DL_URL + "train-clean-360.tar.gz",
    "train_other500": _DL_URL + "train-other-500.tar.gz",
}


class Libritts(tfds.core.BeamBasedBuilder):
  """LibriTTS dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "speech": tfds.features.Audio(),
            "text_original": tfds.features.Text(),
            "text_normalized": tfds.features.Text(),
            "speaker_id": tf.int64,
            "chapter_id": tf.int64,
            "id": tf.string,
        }),
        supervised_keys=("text_normalized", "speech"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(sample_rate=24000,),
    )

  def _populate_metadata(self, dirs):
    # All dirs contain the same metadata.
    directory = list(dirs.values())[0]

    speaker_info = {}
    path = os.path.join(directory, "LibriTTS/speakers.tsv")
    with tf.io.gfile.GFile(path) as f:
      for n, line in enumerate(f):
        # Skip the first line which is just a header.
        if n == 0:
          continue
        fields = line.strip().split("\t")
        if len(fields) == 3:
          # Some lines are missing the final field, so leave it blank.
          fields.append("")
        id_str, gender, subset, name = fields
        speaker_info[int(id_str)] = {
            "gender": gender,
            "subset": subset,
            "name": name,
        }
    self.info.metadata["speakers"] = speaker_info

  def _split_generators(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract(_DL_URLS)
    self._populate_metadata(extracted_dirs)
    splits = [tfds.core.SplitGenerator(name=k, gen_kwargs={"directory": v})
              for k, v in extracted_dirs.items()]
    return splits

  def _build_pcollection(self, pipeline, directory):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    return (pipeline
            | beam.Create([directory])
            | beam.FlatMap(_generate_libritts_examples)
            | beam.Reshuffle())


def _generate_libritts_examples(directory):
  """Generate examples from a LibriTTS directory."""
  transcripts_glob = os.path.join(directory, "LibriTTS", "*/*/*/*.trans.tsv")
  for transcript_file in tf.io.gfile.glob(transcripts_glob):
    path = os.path.dirname(transcript_file)
    with tf.io.gfile.GFile(os.path.join(path, transcript_file)) as f:
      for line in f:
        key, text_original, text_normalized = line.split("\t")
        audio_file = "%s.wav" % key
        speaker_id, chapter_id = [int(el) for el in key.split("_")[:2]]
        example = {
            "speech": os.path.join(path, audio_file),
            "text_normalized": text_normalized,
            "text_original": text_original,
            "speaker_id": speaker_id,
            "chapter_id": chapter_id,
            "id": key,
        }
        yield key, example
