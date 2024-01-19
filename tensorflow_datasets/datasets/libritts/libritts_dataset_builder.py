# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from __future__ import annotations

import io
import os
import tarfile

import numpy as np
import six
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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


class Builder(tfds.core.BeamBasedBuilder):
  """LibriTTS dataset."""

  VERSION = tfds.core.Version("1.0.1")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "speech": tfds.features.Audio(file_format="wav", sample_rate=24000),
            "text_original": tfds.features.Text(),
            "text_normalized": tfds.features.Text(),
            "speaker_id": np.int64,
            "chapter_id": np.int64,
            "id": np.str_,
        }),
        supervised_keys=("text_normalized", "speech"),
        homepage=_URL,
        metadata=tfds.core.MetadataDict(
            sample_rate=24000,
        ),
    )

  def _populate_metadata(self, archive_paths):
    # All archives contain the same metadata.
    archive_path = list(archive_paths.values())[0]

    speaker_info = {}
    with tf.io.gfile.GFile(archive_path, "rb") as f:
      tarf = tarfile.open(mode="r:gz", fileobj=f)
      speakers_tsv = tarf.extractfile("LibriTTS/speakers.tsv")
      for n, line in enumerate(speakers_tsv):
        # Skip the first line which is just a header.
        if n == 0:
          continue
        fields = line.decode("utf-8").strip().split("\t")
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
    archives = dl_manager.download(_DL_URLS)
    self._populate_metadata(archives)
    splits = [
        tfds.core.SplitGenerator(name=k, gen_kwargs={"archive_path": v})
        for k, v in archives.items()
    ]
    return splits

  def _build_pcollection(self, pipeline, archive_path):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    return (
        pipeline
        | beam.Create([archive_path])
        | beam.FlatMap(_extract_libritts_data)
        | beam.Reshuffle()
        | "merge_transcripts_and_audio" >> beam.CombinePerKey(_merge_dicts)
    )


def _generate_transcripts(transcript_csv_file):
  """Generates partial examples from transcript CSV file."""
  for line in transcript_csv_file:
    key, text_original, text_normalized = line.decode("utf-8").split("\t")
    speaker_id, chapter_id = [int(el) for el in key.split("_")[:2]]
    example = {
        "text_normalized": text_normalized,
        "text_original": text_original,
        "speaker_id": speaker_id,
        "chapter_id": chapter_id,
        "id": key,
    }
    yield key, example


def _extract_libritts_data(archive_path):
  """Generate partial audio or transcript examples from a LibriTTS archive."""
  for path, contents in tfds.core.download.extractor.iter_tar(archive_path):
    if path.endswith(".trans.tsv"):
      for key, example in _generate_transcripts(contents):
        yield key, example
    elif path.endswith(".wav"):
      key = six.ensure_text(os.path.splitext(os.path.basename(path))[0])
      memfile = io.BytesIO(contents.read())
      example = {"speech": memfile}
      yield key, example


def _merge_dicts(dicts):
  merged = {}
  for d in dicts:
    merged.update(d)
  return merged
