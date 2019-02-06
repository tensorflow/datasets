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

"""Omniglot dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{lake2015human,
  title={Human-level concept learning through probabilistic program induction},
  author={Lake, Brenden M and Salakhutdinov, Ruslan and Tenenbaum, Joshua B},
  journal={Science},
  volume={350},
  number={6266},
  pages={1332--1338},
  year={2015},
  publisher={American Association for the Advancement of Science}
}
"""

_DESCRIPTION = """\
Omniglot data set for one-shot learning. This dataset contains 1623 different
handwritten characters from 50 different alphabets.
"""

_BASE_URL = "https://github.com/brendenlake/omniglot/"
_DL_URL = _BASE_URL + "raw/master/python/"
_DL_URLS = {
    "train": _DL_URL + "images_background.zip",
    "eval": _DL_URL + "images_evaluation.zip",
    "small1": _DL_URL + "images_background_small1.zip",
    "small2": _DL_URL + "images_background_small2.zip",
}

_NUM_CLASSES = 1623
_NUM_ALPHABETS = 50


class Omniglot(tfds.core.GeneratorBasedBuilder):
  """Omniglot dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(shape=(105, 105, 3), encoding_format="png"),
            "alphabet":
                tfds.features.ClassLabel(num_classes=_NUM_ALPHABETS),
            "alphabet_char_id":
                tf.int64,
            "label":
                tfds.features.ClassLabel(num_classes=_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        urls=[_BASE_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract(_DL_URLS)

    # Get all alphabets and labels
    alphabets, label_names = _get_names(extracted_dirs.values())
    self.info.features["alphabet"].names = sorted(alphabets)
    self.info.features["label"].names = label_names

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "directory": extracted_dirs["train"],
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={
                "directory": extracted_dirs["eval"],
            }),
        tfds.core.SplitGenerator(
            name="small1",
            num_shards=1,
            gen_kwargs={
                "directory": extracted_dirs["small1"],
            }),
        tfds.core.SplitGenerator(
            name="small2",
            num_shards=1,
            gen_kwargs={
                "directory": extracted_dirs["small2"],
            }),
    ]

  def _generate_examples(self, directory):
    for example in _walk_omniglot_dir(directory):
      alphabet, alphabet_char_id, label, image_path = example
      yield {
          "image": image_path,
          "alphabet": alphabet,
          "alphabet_char_id": alphabet_char_id,
          "label": label,
      }


def _walk_omniglot_dir(directory):
  """Walk an Omniglot directory and yield examples."""
  directory = os.path.join(directory, tf.io.gfile.listdir(directory)[0])
  alphabets = sorted(tf.io.gfile.listdir(directory))
  for alphabet in alphabets:
    alphabet_dir = os.path.join(directory, alphabet)
    characters = sorted(tf.io.gfile.listdir(alphabet_dir))
    for character in characters:
      character_id = int(character[len("character"):]) - 1
      character_dir = os.path.join(alphabet_dir, character)
      images = tf.io.gfile.listdir(character_dir)
      for image in images:
        label, _ = image.split("_")
        label = int(label) - 1
        image_path = os.path.join(character_dir, image)
        yield alphabet, character_id, label, image_path


def _get_names(dirs):
  """Get alphabet and label names, union across all dirs."""
  alphabets = set()
  label_names = {}
  for d in dirs:
    for example in _walk_omniglot_dir(d):
      alphabet, alphabet_char_id, label, _ = example
      alphabets.add(alphabet)
      label_name = "%s_%d" % (alphabet, alphabet_char_id)
      if label in label_names:
        assert label_names[label] == label_name
      else:
        label_names[label] = label_name
  label_names = [label_names[k] for k in sorted(label_names)]
  return alphabets, label_names
