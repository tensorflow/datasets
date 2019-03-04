# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Librispeech dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os

import tensorflow as tf

from tensorflow_datasets.core import api_utils
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
LibriSpeech is a corpus of approximately 1000 hours of read English speech of frequency 16 KHz, 
prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read
audiobooks from the LibriVox project, and has been carefully segmented and aligned.
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
_DATA_OPTIONS = ["clean100", "clean360", "all"]


# TODO(tfds): Better support compositional configuration
class LibrispeechConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Librispeech."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, data="clean100", **kwargs):
    """Constructs a LibrispeechConfig.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the text feature.
      data: `str`, one of `(clean100, clean360, all)`. `clean100` uses only the
        clean data without `train-clean-360`. `clean360` uses clean data with
        `train-clean-360`. `all` uses all the data.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)
    name = kwargs.get("name")
    if name is None:
      encoder_name = (
          text_encoder_config.name if text_encoder_config else "plain_text")
      data_name = data
      name = "%s_%s" % (data_name, encoder_name)
    kwargs["name"] = name

    description = kwargs.get("description")
    if description is None:
      if text_encoder_config:
        encoder_description = "Transcriptions use the %s" % (
            text_encoder_config.encoder_cls.__name__)
      else:
        encoder_description = "Transcriptions are in plain text."

      if data == "all":
        data_description = "Uses all data."
      else:
        data_description = ("Uses only clean data,%s including train-clean-360."
                            % ("" if data == "clean360" else " not"))

      description = "%s %s" % (data_description, encoder_description)
    kwargs["description"] = description

    super(LibrispeechConfig, self).__init__(**kwargs)
    self.text_encoder_config = text_encoder_config
    self.data = data

  @property
  def download_urls(self):
    urls = {
        tfds.Split.TRAIN: ["train_clean100"],
        tfds.Split.VALIDATION: ["dev_clean"],
        tfds.Split.TEST: ["test_clean"],
    }
    if self.data in ["all", "clean360"]:
      urls[tfds.Split.TRAIN].append("train_clean360")
    if self.data == "all":
      urls[tfds.Split.TRAIN].extend(["train_clean360", "train_other500"])
      urls[tfds.Split.VALIDATION].append("dev_other")
      urls[tfds.Split.TEST].append("test_other")

    urls = {
        split: [_DL_URLS[name] for name in names
               ] for split, names in urls.items()
    }
    return urls


def _make_builder_configs():
  """Make built-in Librispeech BuilderConfigs.

  Uses 4 text encodings (plain text, bytes, subwords with 8k vocab, subwords
  with 32k vocab) crossed with the data subsets (clean100, clean360, all).

  Returns:
    `list<tfds.audio.LibrispeechConfig>`
  """
  text_encoder_configs = [
      None,
      tfds.features.text.TextEncoderConfig(
          name="bytes", encoder=tfds.features.text.ByteTextEncoder()),
      tfds.features.text.TextEncoderConfig(
          name="subwords8k",
          encoder_cls=tfds.features.text.SubwordTextEncoder,
          vocab_size=2**13),
      tfds.features.text.TextEncoderConfig(
          name="subwords32k",
          encoder_cls=tfds.features.text.SubwordTextEncoder,
          vocab_size=2**15),
  ]
  version = "0.1.0"
  configs = []
  for text_encoder_config in text_encoder_configs:
    for data in _DATA_OPTIONS:
      config = LibrispeechConfig(
          version=version, text_encoder_config=text_encoder_config, data=data)
      configs.append(config)
  return configs


class Librispeech(tfds.core.GeneratorBasedBuilder):
  """Librispeech dataset."""

  BUILDER_CONFIGS = _make_builder_configs()

  IN_DEVELOPMENT = True

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "speech":
                tfds.features.Audio(),
            "text":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "speaker_id":
                tf.int64,
            "chapter_id":
                tf.int64,
        }),
        supervised_keys=("speech", "text"),
        urls=[_URL],
        citation=_CITATION,
    )

  def _vocab_text_gen(self, dirs):
    for example in self._generate_examples(dirs):
      yield example["text"]

  def _split_generators(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract(
        self.builder_config.download_urls)
    # Generate vocabulary from training data if SubwordTextEncoder configured
    self.info.features["text"].maybe_build_from_corpus(
        self._vocab_text_gen(extracted_dirs[tfds.Split.TRAIN]))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=100,
            gen_kwargs={
                "dirs": extracted_dirs[tfds.Split.TRAIN],
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=10,
            gen_kwargs={
                "dirs": extracted_dirs[tfds.Split.VALIDATION],
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs={
                "dirs": extracted_dirs[tfds.Split.TEST],
            }),
    ]

  def _generate_examples(self, dirs):
    for directory in dirs:
      for example in _walk_librispeech_dir(directory):
        yield {
            "speech": example.audio_file,
            "text": example.transcript,
            "speaker_id": example.speaker_id,
            "chapter_id": example.chapter_id,
        }


LibrispeechExample = collections.namedtuple(
    "_LibrispeechExample",
    ["speaker_id", "chapter_id", "audio_file", "transcript"])


def _walk_librispeech_dir(directory):
  """Walk a Librispeech directory and yield examples."""
  directory = os.path.join(directory, "LibriSpeech")
  for path, _, files in tf.io.gfile.walk(directory):
    if not files:
      continue

    transcript_file = [f for f in files if f.endswith(".txt")]
    if not transcript_file:
      continue
    assert len(transcript_file) == 1
    transcript_file, = transcript_file
    transcripts = {}
    with tf.io.gfile.GFile(os.path.join(path, transcript_file)) as f:
      for line in f:
        line = line.strip()
        key, transcript = line.split(" ", 1)
        transcripts[key] = transcript
    audio_files = [f for f in files if not f.endswith(".txt")]
    for audio_file in audio_files:
      assert audio_file.endswith(".flac")
      key = audio_file[:-len(".flac")]
      transcript = transcripts[key]
      speaker_id, chapter_id = [int(el) for el in key.split("-")[:2]]
      yield LibrispeechExample(
          speaker_id=speaker_id,
          chapter_id=chapter_id,
          audio_file=os.path.join(path, audio_file),
          transcript=transcript)
