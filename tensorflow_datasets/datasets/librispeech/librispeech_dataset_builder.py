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

"""Librispeech dataset."""

from __future__ import annotations

import os
from typing import Iterable, List

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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
  """Librispeech dataset config."""

  def __init__(self, *args, lazy_decode: bool = False, **kwargs):
    super().__init__(*args, **kwargs)
    self.lazy_decode = lazy_decode


class Builder(tfds.core.GeneratorBasedBuilder):
  """Librispeech dataset."""

  VERSION = tfds.core.Version("2.1.2")
  RELEASE_NOTES = {
      "2.1.2": "Add 'lazy_decode' config.",
      "2.1.1": "Fix speech data type with dtype=tf.int16.",
  }
  MAX_SIMULTANEOUS_DOWNLOADS = 5  # in accordance with http://www.openslr.org
  BUILDER_CONFIGS = [
      LibrispeechConfig(
          name="default",
          description="Default dataset.",
          version=tfds.core.Version("2.1.1"),
      ),
      LibrispeechConfig(
          name="lazy_decode",
          description="Raw audio dataset.",
          lazy_decode=True,
          version=tfds.core.Version("2.1.2"),
      ),
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "speech": tfds.features.Audio(
                sample_rate=16000,
                dtype=np.int16,
                lazy_decode=self.builder_config.lazy_decode,
                file_format="flac",
            ),
            "text": tfds.features.Text(),
            "speaker_id": np.int64,
            "chapter_id": np.int64,
            "id": np.str_,
        }),
        supervised_keys=("speech", "text"),
        homepage=_URL,
        metadata=tfds.core.MetadataDict(
            sample_rate=16000,
        ),
    )

  def _populate_metadata(self, dirs: Iterable[epath.Path]):
    # All dirs contain the same metadata.
    directory = list(dirs)[0]
    self.info.metadata["speakers"] = self._read_metadata_file(
        directory / "LibriSpeech/SPEAKERS.TXT",
        ["speaker_id", "gender", "subset", "minutes", "name"],
    )
    self.info.metadata["chapters"] = self._read_metadata_file(
        directory / "LibriSpeech/CHAPTERS.TXT",
        [
            "chapter_id",
            "speaker_id",
            "minutes",
            "subset",
            "project_id",
            "book_id",
            "chapter_title",
            "project_title",
        ],
    )

  def _read_metadata_file(self, path: epath.Path, field_names: List[str]):
    metadata = {}
    with path.open() as f:
      for line in f:
        if line.startswith(";"):
          continue
        fields = line.split("|", len(field_names))
        metadata[int(fields[0])] = {
            k: v.strip() for k, v in zip(field_names[1:], fields[1:])
        }
    return metadata

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    extracted_dirs = dl_manager.download_and_extract(_DL_URLS)
    self._populate_metadata(extracted_dirs.values())
    splits = {
        split: self._generate_examples(directory)
        for split, directory in extracted_dirs.items()
    }
    return splits

  def _generate_examples(self, directory: epath.Path):
    """Generates examples as dicts."""
    transcripts_glob = os.path.join(directory, "LibriSpeech", "*/*/*/*.txt")
    transcripts_files = tf.io.gfile.glob(transcripts_glob)

    for transcript_file in transcripts_files:
      yield from _generate_librispeech_examples(transcript_file)


def _generate_librispeech_examples(transcript_file: str):
  """Generate examples from a Librispeech transcript file."""
  audio_dir = os.path.dirname(transcript_file)
  with tf.io.gfile.GFile(transcript_file) as f:
    for line in f:
      line = line.strip()
      key, transcript = line.split(" ", 1)
      audio_file = "%s.flac" % key
      speaker_id, chapter_id = [int(el) for el in key.split("-")[:2]]
      example = {
          "id": key,
          "speaker_id": speaker_id,
          "chapter_id": chapter_id,
          "speech": os.path.join(audio_dir, audio_file),
          "text": transcript,
      }
      yield key, example
