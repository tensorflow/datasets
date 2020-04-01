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
"""NSynth Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The NSynth Dataset is an audio dataset containing ~300k musical notes, each
with a unique pitch, timbre, and envelope. Each note is annotated with three
additional pieces of information based on a combination of human evaluation
and heuristic algorithms: Source, Family, and Qualities.
"""

_FULL_DESCRIPTION = """\
Full NSynth Dataset is split into train, valid, and test sets, with no
instruments overlapping between the train set and the valid/test sets.
"""

_GANSYNTH_DESCRIPTION = """\
NSynth Dataset limited to acoustic instruments in the MIDI pitch interval
[24, 84]. Uses alternate splits that have overlap in instruments (but not exact
notes) between the train set and valid/test sets. This variant was originally
introduced in the ICLR 2019 GANSynth paper (https://arxiv.org/abs/1902.08710).
"""

_F0_AND_LOUDNESS_ADDENDUM = """\
This version additionally contains estimates for F0 using CREPE
(Kim et al., 2018) and A-weighted perceptual loudness in decibels. Both signals
are provided at a frame rate of 250Hz.
"""

# From http://proceedings.mlr.press/v70/engel17a.html
_CITATION = """\
@InProceedings{pmlr-v70-engel17a,
  title = 	 {Neural Audio Synthesis of Musical Notes with {W}ave{N}et Autoencoders},
  author = 	 {Jesse Engel and Cinjon Resnick and Adam Roberts and Sander Dieleman and Mohammad Norouzi and Douglas Eck and Karen Simonyan},
  booktitle = 	 {Proceedings of the 34th International Conference on Machine Learning},
  pages = 	 {1068--1077},
  year = 	 {2017},
  editor = 	 {Doina Precup and Yee Whye Teh},
  volume = 	 {70},
  series = 	 {Proceedings of Machine Learning Research},
  address = 	 {International Convention Centre, Sydney, Australia},
  month = 	 {06--11 Aug},
  publisher = 	 {PMLR},
  pdf = 	 {http://proceedings.mlr.press/v70/engel17a/engel17a.pdf},
  url = 	 {http://proceedings.mlr.press/v70/engel17a.html},
}
"""

_NUM_SECS = 4
_AUDIO_RATE = 16000  # 16 kHz
_F0_AND_LOUDNESS_RATE = 250  # 250 Hz
_CREPE_FRAME_SIZE = 1024
_LD_N_FFT = 2048
_LD_RANGE = 120.0
_REF_DB = 20.7  # White noise, amplitude=1.0, n_fft=2048

_INSTRUMENT_FAMILIES = [
    "bass", "brass", "flute", "guitar", "keyboard", "mallet", "organ", "reed",
    "string", "synth_lead", "vocal"
]
_INSTRUMENT_SOURCES = ["acoustic", "electronic", "synthetic"]
_QUALITIES = [
    "bright", "dark", "distortion", "fast_decay", "long_release", "multiphonic",
    "nonlinear_env", "percussive", "reverb", "tempo-synced"
]

_BASE_DOWNLOAD_PATH = "http://download.magenta.tensorflow.org/datasets/nsynth/nsynth-"

_SPLITS = ["train", "valid", "test"]


class NsynthConfig(tfds.core.BuilderConfig):
  """BuilderConfig for NSynth Dataset."""

  def __init__(self,
               gansynth_subset=False,
               estimate_f0_and_loudness=False,
               **kwargs):
    """Constructs a NsynthConfig.

    Args:
      gansynth_subset: bool, whether to use the subset of the dataset introduced
        in the ICLR 2019 GANSynth paper (Engel, et al. 2018). This subset uses
        acoustic-only instrument sources and limits the pitches to the interval
        [24, 84]. The train and test splits are also modified so that
        instruments (but not specific notes) overlap between them. See
        https://arxiv.org/abs/1902.08710 for more details.
      estimate_f0_and_loudness: bool, whether to estimate fundamental frequency
        (F0) and loudness for the audio (at 250 Hz) and add them to the set of
        features.
      **kwargs: keyword arguments forwarded to super.
    """
    name_parts = []
    if gansynth_subset:
      name_parts.append("gansynth_subset")
    else:
      name_parts.append("full")
    if estimate_f0_and_loudness:
      name_parts.append("f0_and_loudness")
    v230 = tfds.core.Version(
        "2.3.0", "New `loudness_db` feature in decibels (unormalized).")
    v231 = tfds.core.Version(
        "2.3.1", "F0 computed with normalization fix in CREPE.")
    v232 = tfds.core.Version(
        "2.3.2", "Use Audio feature.")
    super(NsynthConfig, self).__init__(
        name=".".join(name_parts),
        version=v232,
        supported_versions=[v231, v230],
        **kwargs)
    self.gansynth_subset = gansynth_subset
    self.estimate_f0_and_loudness = estimate_f0_and_loudness


class Nsynth(tfds.core.BeamBasedBuilder):
  """A large-scale and high-quality dataset of annotated musical notes."""
  BUILDER_CONFIGS = [
      NsynthConfig(description=_FULL_DESCRIPTION),
      NsynthConfig(gansynth_subset=True, description=_GANSYNTH_DESCRIPTION),
      NsynthConfig(
          gansynth_subset=True,
          estimate_f0_and_loudness=True,
          description=_GANSYNTH_DESCRIPTION + _F0_AND_LOUDNESS_ADDENDUM),
  ]

  def _info(self):
    features = {
        "id":
            tf.string,
        "audio":
            tfds.features.Audio(
                shape=(_AUDIO_RATE * _NUM_SECS,),
                dtype=tf.float32,
                sample_rate=_AUDIO_RATE,
            ),
        "pitch":
            tfds.features.ClassLabel(num_classes=128),
        "velocity":
            tfds.features.ClassLabel(num_classes=128),
        "instrument": {
            # We read the list of labels in _split_generators.
            "label": tfds.features.ClassLabel(num_classes=1006),
            "family": tfds.features.ClassLabel(names=_INSTRUMENT_FAMILIES),
            "source": tfds.features.ClassLabel(names=_INSTRUMENT_SOURCES),
        },
        "qualities": {quality: tf.bool for quality in _QUALITIES},
    }
    if self.builder_config.estimate_f0_and_loudness:
      f0_and_ld_shape = (_F0_AND_LOUDNESS_RATE * _NUM_SECS,)
      features["f0"] = {
          "hz":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32),
          "midi":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32),
          "confidence":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32)
      }
      features["loudness"] = {
          "db": tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32)
      }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage="https://g.co/magenta/nsynth-dataset",
        citation=_CITATION,
        metadata=tfds.core.BeamMetadataDict(sample_rate=_AUDIO_RATE,),
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""

    dl_urls = {}
    dl_urls["examples"] = {
        split: _BASE_DOWNLOAD_PATH + "%s.tfrecord.tar" % split
        for split in _SPLITS
    }
    dl_urls["instrument_labels"] = (
        _BASE_DOWNLOAD_PATH + "instrument_labels.txt")
    if self.builder_config.gansynth_subset:
      dl_urls["gansynth_splits"] = (_BASE_DOWNLOAD_PATH + "gansynth_splits.csv")
    dl_paths = dl_manager.download_and_extract(dl_urls)

    with tf.io.gfile.GFile(dl_paths["instrument_labels"]) as f:
      instrument_labels = f.read().strip().splitlines()
    self.info.features["instrument"]["label"].names = instrument_labels

    split_ids = {s: set() for s in _SPLITS}
    split_dirs = {s: [dl_paths["examples"][s]] for s in _SPLITS}
    if self.builder_config.gansynth_subset:
      # Generator needs to see all original splits for each new split.
      split_dirs = {s: dl_paths["examples"].values() for s in _SPLITS}
      with tf.io.gfile.GFile(dl_paths["gansynth_splits"]) as f:
        reader = csv.DictReader(f)
        for row in reader:
          split_ids[row["split"]].add(row["id"])

    return [
        tfds.core.SplitGenerator(  # pylint: disable=g-complex-comprehension
            name=split,
            gen_kwargs={
                "tfrecord_dirs": split_dirs[split],
                "ids": split_ids[split],
                "split": split,
            })
        for split in _SPLITS
    ]

  def _build_pcollection(self, pipeline, tfrecord_dirs, ids, split):
    """Build PCollection of examples for split."""
    beam = tfds.core.lazy_imports.apache_beam

    def _emit_base_example(ex):
      """Maps an input example to a TFDS example."""
      beam.metrics.Metrics.counter(split, "base-examples").inc()
      features = ex.features.feature
      id_ = features["note_str"].bytes_list.value[0]
      return id_, {
          "id":
              id_,
          "audio":
              np.array(features["audio"].float_list.value, dtype=np.float32),
          "pitch":
              features["pitch"].int64_list.value[0],
          "velocity":
              features["velocity"].int64_list.value[0],
          "instrument": {
              "label":
                  tf.compat.as_text(
                      features["instrument_str"].bytes_list.value[0]),
              "family":
                  tf.compat.as_text(
                      features["instrument_family_str"].bytes_list.value[0]),
              "source":
                  tf.compat.as_text(
                      features["instrument_source_str"].bytes_list.value[0])
          },
          "qualities": {
              q: features["qualities"].int64_list.value[i]
              for (i, q) in enumerate(_QUALITIES)
          }
      }

    def _in_split(id_ex, split_ids):
      unused_id, ex = id_ex
      if not split_ids or tf.compat.as_text(ex["id"]) in split_ids:
        beam.metrics.Metrics.counter(split, "in-split").inc()
        return True
      return False

    def _estimate_f0(id_ex):
      """Estimate the fundamental frequency using CREPE and add to example."""
      id_, ex = id_ex
      beam.metrics.Metrics.counter(split, "estimate-f0").inc()

      audio = ex["audio"]

      # Copied from magenta/ddsp/spectral_ops.py
      # Pad end so that `num_frames = _NUM_SECS * _F0_AND_LOUDNESS_RATE`.
      hop_size = _AUDIO_RATE / _F0_AND_LOUDNESS_RATE
      n_samples = len(audio)
      n_frames = _NUM_SECS * _F0_AND_LOUDNESS_RATE
      n_samples_padded = (n_frames - 1) * hop_size + _CREPE_FRAME_SIZE
      n_padding = (n_samples_padded - n_samples)
      assert n_padding % 1 == 0
      audio = np.pad(audio, (0, int(n_padding)), mode="constant")
      crepe_step_size = 1000 / _F0_AND_LOUDNESS_RATE  # milliseconds

      _, f0_hz, f0_confidence, _ = tfds.core.lazy_imports.crepe.predict(
          audio,
          sr=_AUDIO_RATE,
          viterbi=True,
          step_size=crepe_step_size,
          center=False,
          verbose=0)
      f0_midi = tfds.core.lazy_imports.librosa.core.hz_to_midi(f0_hz)
      # Set -infs introduced by hz_to_midi to 0.
      f0_midi[f0_midi == -np.inf] = 0
      # Set nans to 0 in confidence.
      f0_confidence = np.nan_to_num(f0_confidence)
      ex = dict(ex)
      ex["f0"] = {
          "hz": f0_hz.astype(np.float32),
          "midi": f0_midi.astype(np.float32),
          "confidence": f0_confidence.astype(np.float32),
      }
      return id_, ex

    def _calc_loudness(id_ex):
      """Compute loudness, add to example (ref is white noise, amplitude=1)."""
      id_, ex = id_ex
      beam.metrics.Metrics.counter(split, "compute-loudness").inc()

      audio = ex["audio"]

      # Copied from magenta/ddsp/spectral_ops.py
      # Get magnitudes.
      hop_size = int(_AUDIO_RATE // _F0_AND_LOUDNESS_RATE)

      # Add padding to the end
      n_samples_initial = int(audio.shape[-1])
      n_frames = int(np.ceil(n_samples_initial / hop_size))
      n_samples_final = (n_frames - 1) * hop_size + _LD_N_FFT
      pad = n_samples_final - n_samples_initial
      audio = np.pad(audio, ((0, pad),), "constant")

      librosa = tfds.core.lazy_imports.librosa
      spectra = librosa.stft(
          audio, n_fft=_LD_N_FFT, hop_length=hop_size, center=False).T

      # Compute power
      amplitude = np.abs(spectra)
      amin = 1e-20  # Avoid log(0) instabilities.
      power_db = np.log10(np.maximum(amin, amplitude))
      power_db *= 20.0

      # Perceptual weighting.
      frequencies = librosa.fft_frequencies(sr=_AUDIO_RATE, n_fft=_LD_N_FFT)
      a_weighting = librosa.A_weighting(frequencies)[np.newaxis, :]
      loudness = power_db + a_weighting

      # Set dynamic range.
      loudness -= _REF_DB
      loudness = np.maximum(loudness, -_LD_RANGE)

      # Average over frequency bins.
      mean_loudness_db = np.mean(loudness, axis=-1)

      ex = dict(ex)
      ex["loudness"] = {"db": mean_loudness_db.astype(np.float32)}
      return id_, ex

    examples = (
        pipeline
        | beam.Create([os.path.join(dir_, "*") for dir_ in tfrecord_dirs])
        | beam.io.tfrecordio.ReadAllFromTFRecord(
            coder=beam.coders.ProtoCoder(tf.train.Example))
        | beam.Map(_emit_base_example)
        | beam.Filter(_in_split, split_ids=ids))
    if self.builder_config.estimate_f0_and_loudness:
      examples = (
          examples
          | beam.Reshuffle()
          | beam.Map(_estimate_f0)
          | beam.Map(_calc_loudness))

    return examples
