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

"""Caltech images dataset."""

import os
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{FeiFei2004LearningGV,
  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},
  author={Li Fei-Fei and Rob Fergus and Pietro Perona},
  journal={Computer Vision and Pattern Recognition Workshop},
  year={2004},
}
"""
_DESCRIPTION = """\
Caltech-101 consists of pictures of objects belonging to 101 classes, plus
one `background clutter` class. Each image is labelled with a single object.
Each class contains roughly 40 to 800 images, totalling around 9k images.
Images are of variable sizes, with typical edge lengths of 200-300 pixels.
This version contains image-level labels only. The original dataset also
contains bounding boxes.
"""
_LABELS_FNAME = "image_classification/caltech101_labels.txt"
_URL = "http://www.vision.caltech.edu/Image_Datasets/Caltech101/"
_IMAGES_FNAME = "101_ObjectCategories.tar.gz"
_TRAIN_POINTS_PER_CLASS = 30


class Caltech101(tfds.core.GeneratorBasedBuilder):
  """Caltech-101."""

  VERSION = tfds.core.Version(
      "3.0.0", "New split API (https://tensorflow.org/datasets/splits)")

  def _info(self):
    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names_file=names_file),
            "image/file_name": tfds.features.Text(),  # E.g. 'image_0001.jpg'.
        }),
        supervised_keys=("image", "label"),
        homepage=_URL,
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(os.path.join(_URL, _IMAGES_FNAME))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": path,
                "is_train_split": True,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": path,
                "is_train_split": False,
            }),
    ]

  def _generate_examples(self, images_dir_path, is_train_split):
    """Generates images and labels given the image directory path.

    As is usual for this dataset, 30 random examples from each class are added
    to the train split, and the remainder are added to the test split.

    Args:
      images_dir_path: path to the directory where the images are stored.
      is_train_split: bool, if true, generates the train split, else generates
        the test split.

    Yields:
      The image path, and its corresponding label and filename.

    Raises:
      ValueError: If too few points are present to create the train set for any
        class.
    """
    # Sets random seed so the random partitioning of files is the same when
    # called for the train and test splits.
    numpy_original_state = np.random.get_state()
    np.random.seed(1234)

    parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
    walk_dir = os.path.join(images_dir_path, parent_dir)
    dirs = tf.io.gfile.listdir(walk_dir)

    for d in dirs:
      # Each directory contains all the images from a single class.
      if tf.io.gfile.isdir(os.path.join(walk_dir, d)):
        for full_path, _, fnames in tf.io.gfile.walk(os.path.join(walk_dir, d)):

          # _TRAIN_POINTS_PER_CLASS datapoints are sampled for the train split,
          # the others constitute the test split.
          if _TRAIN_POINTS_PER_CLASS > len(fnames):
            raise ValueError("Fewer than {} ({}) points in class {}".format(
                _TRAIN_POINTS_PER_CLASS, len(fnames), d))
          train_fnames = np.random.choice(fnames, _TRAIN_POINTS_PER_CLASS,
                                          replace=False)
          test_fnames = set(fnames).difference(train_fnames)
          fnames_to_emit = train_fnames if is_train_split else test_fnames

          for image_file in fnames_to_emit:
            if image_file.endswith(".jpg"):
              image_path = os.path.join(full_path, image_file)
              record = {
                  "image": image_path,
                  "label": d.lower(),
                  "image/file_name": image_file,
              }
              yield "%s/%s" % (d, image_file), record
    # Resets the seeds to their previous states.
    np.random.set_state(numpy_original_state)
