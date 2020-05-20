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
"""Code to build STL-10 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{coates2011stl10,
  title={{An Analysis of Single Layer Networks in Unsupervised Feature Learning}},
  author={Coates, Adam and Ng, Andrew and Lee, Honglak},
  booktitle={AISTATS},
  year={2011},
  note = {\\url{https://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf}},
}
"""

_DESCRIPTION = """\
The STL-10 dataset is an image recognition dataset for developing unsupervised
feature learning, deep learning, self-taught learning algorithms. It is inspired
by the CIFAR-10 dataset but with some modifications. In particular, each class
has fewer labeled training examples than in CIFAR-10, but a very large set of 
unlabeled examples is provided to learn image models prior to supervised
training. The primary challenge is to make use of the unlabeled data (which
comes from a similar but different distribution from the labeled data) to build
a useful prior. All images were acquired from labeled examples on ImageNet.
"""

URL = "http://ai.stanford.edu/~acoates/stl10/stl10_binary.tar.gz"
UNLABELLED = tfds.Split("unlabelled")


class Stl10(tfds.core.GeneratorBasedBuilder):
  """STL-10 dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(96, 96, 3)),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        homepage="http://ai.stanford.edu/~acoates/stl10/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    train_files = ["train_X.bin", "train_y.bin"]
    test_files = ["test_X.bin", "test_y.bin"]
    unlabeled_files = ["unlabeled_X.bin"]

    stl10_path = dl_manager.download_and_extract(URL)
    stl10_path = os.path.join(stl10_path, "stl10_binary/")

    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(stl10_path, f)

    # Adds the class names to the feature description.
    with tf.io.gfile.GFile(next(gen_filenames(["class_names.txt"])), "r") as f:
      class_names = [l.strip("\n") for l in f]
    self.info.features["label"].names = class_names

    # Define the splits
    splits = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepaths": gen_filenames(train_files)}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"filepaths": gen_filenames(test_files)}),
        tfds.core.SplitGenerator(
            name=UNLABELLED,
            gen_kwargs={"filepaths": gen_filenames(unlabeled_files)}),
    ]

    return splits

  def _generate_examples(self, filepaths):
    """Generate STL-10 examples as dicts.

    Args:
      filepaths (list[str]): The files to use to generate the data.

    Yields:
      The STL-10 examples, as defined in the dataset info features.
    """
    filepaths = list(filepaths)
    image_path = filepaths[0]
    label_path = filepaths[1] if len(filepaths) > 1 else None

    with tf.io.gfile.GFile(image_path, "rb") as f:
      images = np.frombuffer(f.read(), dtype=np.uint8)
      images = np.reshape(images, (-1, 3, 96, 96))
      images = np.transpose(images, (0, 3, 2, 1))

    if label_path:
      with tf.io.gfile.GFile(label_path, "rb") as f:
        labels = np.copy(np.frombuffer(f.read(), dtype=np.uint8))
        # Switch to zero-based indexing.
        labels -= 1
    else:
      labels = None

    for index, image in enumerate(images):
      yield index, {
          "image": image,
          "label": labels[index] if labels is not None else -1,
      }
