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

"""NSynth Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import numpy as np
import tensorflow as tf
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
(Kim et al., 2018) and A-weighted perceptual loudness. Both signals are provided
at a frame rate of 250Hz.
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

_INSTRUMENT_FAMILIES = [
    "bass", "brass", "flute", "guitar", "keyboard", "mallet", "organ", "reed",
    "string", "synth_lead", "vocal"]
_INSTRUMENT_SOURCES = ["acoustic", "electronic", "synthetic"]
_QUALITIES = [
    "bright",
    "dark",
    "distortion",
    "fast_decay",
    "long_release",
    "multiphonic",
    "nonlinear_env",
    "percussive",
    "reverb",
    "tempo-synced"]

_BASE_DOWNLOAD_PATH = "http://download.magenta.tensorflow.org/datasets/nsynth/nsynth-"

_SPLITS = ["train", "valid", "test"]
_SPLIT_SHARDS = {
    "train": 512,
    "valid": 32,
    "test": 8,
}


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
    super(NsynthConfig, self).__init__(
        name=".".join(name_parts),
        version=tfds.core.Version(
            "1.1.0", experiments={tfds.core.Experiment.S3: False}),
        **kwargs)
    self.gansynth_subset = gansynth_subset
    self.estimate_f0_and_loudness = estimate_f0_and_loudness


class Nsynth(tfds.core.BeamBasedBuilder):
  """A large-scale and high-quality dataset of annotated musical notes."""
  BUILDER_CONFIGS = [
      NsynthConfig(description=_FULL_DESCRIPTION),
      NsynthConfig(
          gansynth_subset=True,
          description=_GANSYNTH_DESCRIPTION),
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
            tfds.features.Tensor(
                shape=(_AUDIO_RATE * _NUM_SECS,), dtype=tf.float32),
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
      f0_and_ld_shape = (_F0_AND_LOUDNESS_RATE * _NUM_SECS + 1,)
      features["f0"] = {
          "hz":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32),
          "midi":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32),
          "confidence":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32)
      }
      features["loudness"] = {
          "db":
              tfds.features.Tensor(shape=f0_and_ld_shape, dtype=tf.float32)
      }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage="https://g.co/magenta/nsynth-dataset",
        citation=_CITATION,
        metadata=tfds.core.BeamMetadataDict(),
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
      dl_urls["gansynth_splits"] = (
          _BASE_DOWNLOAD_PATH + "gansynth_splits.csv")
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
            num_shards=_SPLIT_SHARDS[split],
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
      return  {
          "id": features["note_str"].bytes_list.value[0],
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

    def _in_split(ex, split_ids):
      if not split_ids or tf.compat.as_text(ex["id"]) in split_ids:
        beam.metrics.Metrics.counter(split, "in-split").inc()
        return True
      return False

    def _estimate_f0(ex):
      """Estimate the fundamental frequency using CREPE and add to example."""
      ex = ex.copy()
      beam.metrics.Metrics.counter(split, "estimate-f0").inc()
      _, f0_hz, f0_confidence, _ = tfds.core.lazy_imports.crepe.predict(
          ex["audio"],
          sr=_AUDIO_RATE,
          viterbi=True,
          step_size=1000 / _F0_AND_LOUDNESS_RATE,
          verbose=0)
      f0_midi = tfds.core.lazy_imports.librosa.core.hz_to_midi(f0_hz)
      # Set -infs introduced by hz_to_midi to 0.
      f0_midi[f0_midi == -np.inf] = 0
      # Set nans to 0 in confidence.
      f0_confidence = np.nan_to_num(f0_confidence)
      ex["f0"] = {
          "hz": f0_hz.astype(np.float32),
          "midi": f0_midi.astype(np.float32),
          "confidence": f0_confidence.astype(np.float32),
      }
      return ex

    def _compute_loudness(ex):
      """Compute loudness and add to example."""
      ex = ex.copy()
      beam.metrics.Metrics.counter(split, "compute-loudness").inc()
      librosa = tfds.core.lazy_imports.librosa
      n_fft = 2048
      amin = 1e-15
      top_db = 200.0
      stft = librosa.stft(
          ex["audio"],
          n_fft=n_fft,
          hop_length=int(_AUDIO_RATE // _F0_AND_LOUDNESS_RATE))
      loudness_db = librosa.perceptual_weighting(
          np.abs(stft)**2,
          librosa.fft_frequencies(_AUDIO_RATE, n_fft=n_fft),
          amin=amin,
          top_db=top_db)
      # Average across freq in linear scale.
      mean_loudness_amp = np.mean(librosa.db_to_amplitude(loudness_db), axis=0)
      mean_loudness_db = librosa.amplitude_to_db(
          mean_loudness_amp,
          amin=amin,
          top_db=top_db)
      ex["loudness"] = {"db": mean_loudness_db.astype(np.float32)}
      return ex

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
          | beam.Map(_compute_loudness))
      if split == tfds.Split.TRAIN:
        # Output mean and variance of loudness for TRAIN split.
        loudness = examples | beam.Map(lambda x: np.mean(x["loudness"]["db"]))
        loudness_mean = (
            loudness
            | "loudness_mean" >> beam.combiners.Mean.Globally())
        loudness_variance = (
            loudness
            | beam.Map(lambda ld, ld_mean: (ld - ld_mean)**2,
                       ld_mean=beam.pvalue.AsSingleton(loudness_mean))
            | "loudness_variance" >> beam.combiners.Mean.Globally())
        self.info.metadata["loudness_db_mean"] = loudness_mean
        self.info.metadata["loudness_db_variance"] = loudness_variance

    return examples
