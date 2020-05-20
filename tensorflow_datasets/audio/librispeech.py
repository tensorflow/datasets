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
"""Librispeech dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{panayotov2015librispeech,
  title={Librispeech: an ASR corpus based on public domain audio books},
  author={Panayotov, Vassil and Chen, Guoguo and Povey, Daniel and Khudanpur, Sanjeev},
  booktitle={Acoustics, Speech and Signal Processing (ICASSP), 2015 IEEE International Conference on},
  pages={5206--5210},
  year={2015},
  organization={IEEE}
}
"""

_DESCRIPTION = """\
LibriSpeech is a corpus of approximately 1000 hours of read English speech with sampling rate of 16 kHz,
prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read
audiobooks from the LibriVox project, and has been carefully segmented and aligned.87
"""

_URL = "http://www.openslr.org/12"
_DL_URL = "http://www.openslr.org/resources/12/"
_DL_URLS = {
    "dev_clean": _DL_URL + "dev-clean.tar.gz",
    "dev_other": _DL_URL + "dev-other.tar.gz",
    "test_clean": _DL_URL + "test-clean.tar.gz",
    "test_other": _DL_URL + "test-other.tar.gz",
    "train_clean100": _DL_URL + "train-clean-100.tar.gz",
    "train_clean360": _DL_URL + "train-clean-360.tar.gz",
    "train_other500": _DL_URL + "train-other-500.tar.gz",
}


class LibrispeechConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Librispeech."""

  @tfds.core.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """Constructs a LibrispeechConfig.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the text feature.
      **kwargs: keyword arguments forwarded to super.
    """
    name = kwargs.get("name")
    if name is None:
      name = (text_encoder_config.name if text_encoder_config else "plain_text")
    kwargs["name"] = name

    description = kwargs.get("description")
    if description is None:
      if text_encoder_config:
        description = "Transcriptions use the %s" % (
            text_encoder_config.encoder_cls.__name__)
      else:
        description = "Transcriptions are in plain text."
    kwargs["description"] = description

    super(LibrispeechConfig, self).__init__(**kwargs)
    self.text_encoder_config = text_encoder_config


def _make_builder_configs():
  """Make built-in Librispeech BuilderConfigs.

  Uses 3 text encodings (plain_text, subwords with 8k vocab, subwords with 32k
  vocab).

  Returns:
    `list<tfds.audio.LibrispeechConfig>`
  """
  text_encoder_configs = [
      None,
      tfds.features.text.TextEncoderConfig(
          name="subwords8k",
          encoder_cls=tfds.features.text.SubwordTextEncoder,
          vocab_size=2**13),
      tfds.features.text.TextEncoderConfig(
          name="subwords32k",
          encoder_cls=tfds.features.text.SubwordTextEncoder,
          vocab_size=2**15),
  ]
  configs = []
  for text_encoder_config in text_encoder_configs:
    config = LibrispeechConfig(
        version=tfds.core.Version("1.1.0"),
        text_encoder_config=text_encoder_config)
    configs.append(config)
  return configs


class Librispeech(tfds.core.BeamBasedBuilder):
  """Librispeech dataset."""

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "speech":
                tfds.features.Audio(sample_rate=16000),
            "text":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "speaker_id":
                tf.int64,
            "chapter_id":
                tf.int64,
            "id":
                tf.string,
        }),
        supervised_keys=("speech", "text"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(sample_rate=16000,),
    )

  def _vocab_text_gen(self, dirs):
    for directory in dirs:
      for _, example in _generate_librispeech_examples(directory):
        yield example["text"]

  def _populate_metadata(self, dirs):
    # All dirs contain the same metadata.
    directory = list(dirs.values())[0]
    self.info.metadata["speakers"] = self._read_metadata_file(
        os.path.join(directory, "LibriSpeech/SPEAKERS.TXT"),
        ["speaker_id", "gender", "subset", "minutes", "name"])
    self.info.metadata["chapters"] = self._read_metadata_file(
        os.path.join(directory, "LibriSpeech/CHAPTERS.TXT"), [
            "chapter_id", "speaker_id", "minutes", "subset", "project_id",
            "book_id", "chapter_title", "project_title"
        ])

  def _read_metadata_file(self, path, field_names):
    metadata = {}
    with tf.io.gfile.GFile(path) as f:
      for line in f:
        if line.startswith(";"):
          continue
        fields = line.split("|", len(field_names))
        metadata[int(fields[0])] = {
            k: v.strip() for k, v in zip(field_names[1:], fields[1:])
        }
    return metadata

  def _split_generators(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract(_DL_URLS)
    # Generate vocabulary from training data if SubwordTextEncoder configured.
    all_train_dirs = [
        v for k, v in extracted_dirs.items() if k.startswith("train")
    ]
    self.info.features["text"].maybe_build_from_corpus(
        self._vocab_text_gen(all_train_dirs))
    self._populate_metadata(extracted_dirs)
    splits = [tfds.core.SplitGenerator(name=k, gen_kwargs={"directory": v})
              for k, v in extracted_dirs.items()]
    return splits

  def _build_pcollection(self, pipeline, directory):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    return (pipeline
            | beam.Create([directory])
            | beam.FlatMap(_generate_librispeech_examples)
            | beam.Reshuffle())


def _generate_librispeech_examples(directory):
  """Generate examples from a Librispeech directory."""
  transcripts_glob = os.path.join(directory, "LibriSpeech", "*/*/*/*.txt")
  for transcript_file in tf.io.gfile.glob(transcripts_glob):
    path = os.path.dirname(transcript_file)
    with tf.io.gfile.GFile(os.path.join(path, transcript_file)) as f:
      for line in f:
        line = line.strip()
        key, transcript = line.split(" ", 1)
        audio_file = "%s.flac" % key
        speaker_id, chapter_id = [int(el) for el in key.split("-")[:2]]
        example = {
            "id": key,
            "speaker_id": speaker_id,
            "chapter_id": chapter_id,
            "speech": os.path.join(path, audio_file),
            "text": transcript
        }
        yield key, example
