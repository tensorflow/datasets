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

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The NSynth Dataset is an audio dataset containing ~300k musical notes, each
with a unique pitch, timbre, and envelope. Each note is annotated with three
additional pieces of information based on a combination of human evaluation
and heuristic algorithms:
 -Source: The method of sound production for the note's instrument.
 -Family: The high-level family of which the note's instrument is a member.
 -Qualities: Sonic qualities of the note.

The dataset is split into train, valid, and test sets, with no instruments
overlapping between the train set and the valid/test sets.
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

_SAMPLE_LENGTH = 64000  # 4 seconds * 16000 samples / second


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
    "train": 64,
    "valid": 4,
    "test": 1,
}


class Nsynth(tfds.core.GeneratorBasedBuilder):
  """A large-scale and high-quality dataset of annotated musical notes."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id":
                tf.string,
            "audio":
                tfds.features.Tensor(shape=(_SAMPLE_LENGTH,), dtype=tf.float32),
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
        }),
        urls=["https://g.co/magenta/nsynth-dataset"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    dl_urls = {
        split: _BASE_DOWNLOAD_PATH + "%s.tfrecord" % split for split in _SPLITS
    }
    dl_urls["instrument_labels"] = (_BASE_DOWNLOAD_PATH +
                                    "instrument_labels.txt")
    dl_paths = dl_manager.download_and_extract(dl_urls)

    instrument_labels = tf.io.gfile.GFile(dl_paths["instrument_labels"],
                                          "r").read().strip().split("\n")
    self.info.features["instrument"]["label"].names = instrument_labels

    return [
        tfds.core.SplitGenerator(  # pylint: disable=g-complex-comprehension
            name=split,
            num_shards=_SPLIT_SHARDS[split],
            gen_kwargs={"path": dl_paths[split]}) for split in _SPLITS
    ]

  def _generate_examples(self, path):

    reader = tf.compat.v1.io.tf_record_iterator(path)
    for example_str in reader:
      example = tf.train.Example.FromString(example_str)
      features = example.features.feature
      yield {
          "id":
              features["note_str"].bytes_list.value[0],
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
