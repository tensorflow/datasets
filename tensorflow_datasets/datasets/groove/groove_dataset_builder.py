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

"""Groove Midi Dataset (GMD)."""

from __future__ import annotations

import collections
import copy
import csv
import io
import os

from absl import logging
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_PRIMARY_STYLES = [
    "afrobeat",
    "afrocuban",
    "blues",
    "country",
    "dance",
    "funk",
    "gospel",
    "highlife",
    "hiphop",
    "jazz",
    "latin",
    "middleeastern",
    "neworleans",
    "pop",
    "punk",
    "reggae",
    "rock",
    "soul",
]

_TIME_SIGNATURES = ["3-4", "4-4", "5-4", "5-8", "6-8"]

_DOWNLOAD_URL = "https://storage.googleapis.com/magentadata/datasets/groove/groove-v1.0.0.zip"
_DOWNLOAD_URL_MIDI_ONLY = "https://storage.googleapis.com/magentadata/datasets/groove/groove-v1.0.0-midionly.zip"


class GrooveConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Groove Dataset."""

  def __init__(
      self, split_bars=None, include_audio=True, audio_rate=16000, **kwargs
  ):
    """Constructs a GrooveConfig.

    Args:
      split_bars: int, number of bars to include per example using a sliding
        window across the raw data, or will not split if None.
      include_audio: bool, whether to include audio in the examples. If True,
        examples with missing audio will be excluded.
      audio_rate: int, sample rate to use for audio.
      **kwargs: keyword arguments forwarded to super.
    """
    name_parts = [("%dbar" % split_bars) if split_bars else "full"]
    if include_audio:
      name_parts.append("%dhz" % audio_rate)
    else:
      name_parts.append("midionly")

    super(GrooveConfig, self).__init__(
        name="-".join(name_parts),
        version=tfds.core.Version("2.0.1"),
        **kwargs,
    )
    self.split_bars = split_bars
    self.include_audio = include_audio
    self.audio_rate = audio_rate


class Builder(tfds.core.GeneratorBasedBuilder):
  """The Groove MIDI Dataset (GMD) of drum performances."""

  BUILDER_CONFIGS = [
      GrooveConfig(
          include_audio=False,
          description="Groove dataset without audio, unsplit.",
      ),
      GrooveConfig(
          include_audio=True, description="Groove dataset with audio, unsplit."
      ),
      GrooveConfig(
          include_audio=False,
          split_bars=2,
          description="Groove dataset without audio, split into 2-bar chunks.",
      ),
      GrooveConfig(
          include_audio=True,
          split_bars=2,
          description="Groove dataset with audio, split into 2-bar chunks.",
      ),
      GrooveConfig(
          include_audio=False,
          split_bars=4,
          description="Groove dataset without audio, split into 4-bar chunks.",
      ),
  ]

  def _info(self):
    features_dict = {
        "id": tf.string,
        "drummer": tfds.features.ClassLabel(
            names=["drummer%d" % i for i in range(1, 11)]
        ),
        "type": tfds.features.ClassLabel(names=["beat", "fill"]),
        "bpm": tf.int32,
        "time_signature": tfds.features.ClassLabel(names=_TIME_SIGNATURES),
        "style": {
            "primary": tfds.features.ClassLabel(names=_PRIMARY_STYLES),
            "secondary": tf.string,
        },
        "midi": tf.string,
    }
    if self.builder_config.include_audio:
      features_dict["audio"] = tfds.features.Audio(
          dtype=np.float32, sample_rate=self.builder_config.audio_rate
      )
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(features_dict),
        homepage="https://g.co/magenta/groove-dataset",
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    # Download data.
    data_dir = os.path.join(
        dl_manager.download_and_extract(
            _DOWNLOAD_URL
            if self._builder_config.include_audio  # pytype: disable=attribute-error  # always-use-return-annotations
            else _DOWNLOAD_URL_MIDI_ONLY
        ),
        "groove",
    )

    rows = collections.defaultdict(list)
    with tf.io.gfile.GFile(os.path.join(data_dir, "info.csv")) as f:
      reader = csv.DictReader(f)
      for row in reader:
        rows[row["split"]].append(row)

    return [
        tfds.core.SplitGenerator(  # pylint: disable=g-complex-comprehension
            name=split, gen_kwargs={"rows": split_rows, "data_dir": data_dir}
        )
        for split, split_rows in rows.items()
    ]

  def _generate_examples(self, rows, data_dir):
    split_bars = self._builder_config.split_bars  # pytype: disable=attribute-error  # always-use-return-annotations
    for row in rows:
      split_genre = row["style"].split("/")
      with tf.io.gfile.GFile(
          os.path.join(data_dir, row["midi_filename"]), "rb"
      ) as midi_f:
        midi = midi_f.read()
      audio = None
      if self._builder_config.include_audio:  # pytype: disable=attribute-error  # always-use-return-annotations
        if not row["audio_filename"]:
          # Skip examples with no audio.
          logging.warning("Skipping example with no audio: %s", row["id"])
          continue
        wav_path = os.path.join(data_dir, row["audio_filename"])
        audio = _load_wav(wav_path, self._builder_config.audio_rate)  # pytype: disable=attribute-error  # always-use-return-annotations

      example = {
          "id": row["id"],
          "drummer": row["drummer"],
          "type": row["beat_type"],
          "bpm": int(row["bpm"]),
          "time_signature": row["time_signature"],
          "style": {
              "primary": split_genre[0],
              "secondary": split_genre[1] if len(split_genre) == 2 else "",
          },
      }
      if not split_bars:
        # Yield full example.
        example["midi"] = midi
        if audio is not None:
          example["audio"] = audio
        yield example["id"], example
      else:
        # Yield split examples.
        bpm = int(row["bpm"])
        beats_per_bar = int(row["time_signature"].split("-")[0])
        bar_duration = 60 / bpm * beats_per_bar
        audio_rate = self._builder_config.audio_rate  # pytype: disable=attribute-error  # always-use-return-annotations

        pm = tfds.core.lazy_imports.pretty_midi.PrettyMIDI(io.BytesIO(midi))
        total_duration = pm.get_end_time()

        # Pad final bar if at least half filled.
        total_bars = int(round(total_duration / bar_duration))
        total_frames = int(total_bars * bar_duration * audio_rate)
        if audio is not None and len(audio) < total_frames:
          audio = np.pad(audio, [0, total_frames - len(audio)], "constant")

        for i in range(total_bars - split_bars + 1):
          time_range = [i * bar_duration, (i + split_bars) * bar_duration]

          # Split MIDI.
          pm_split = copy.deepcopy(pm)
          pm_split.adjust_times(time_range, [0, split_bars * bar_duration])
          pm_split.time_signature_changes = pm.time_signature_changes
          midi_split = io.BytesIO()
          pm_split.write(midi_split)
          example["midi"] = midi_split.getvalue()

          # Split audio.
          if audio is not None:
            example["audio"] = audio[
                int(time_range[0] * audio_rate) : int(
                    time_range[1] * audio_rate
                )
            ]

          example["id"] += ":%03d" % i
          yield example["id"], example


def _load_wav(path, sample_rate):
  with tf.io.gfile.GFile(path, "rb") as audio_f:
    audio_segment = (
        tfds.core.lazy_imports.pydub.AudioSegment.from_file(
            audio_f, format="wav"
        )
        .set_channels(1)
        .set_frame_rate(sample_rate)
    )
  audio = np.array(audio_segment.get_array_of_samples()).astype(np.float32)
  # Convert from int to float representation.
  audio /= 2 ** (8 * audio_segment.sample_width)
  return audio
