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

"""Dmlab dataset."""

from __future__ import annotations

import io
import os

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://storage.googleapis.com/dmlab-vtab/dmlab.tar.gz"


class Dmlab(tfds.core.GeneratorBasedBuilder):
  """Dmlab dataset."""

  VERSION = tfds.core.Version("2.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=r"""
        The Dmlab dataset contains frames observed by the agent acting in the
        DeepMind Lab environment, which are annotated by the distance between
        the agent and various objects present in the environment. The goal is to
        is to evaluate the ability of a visual model to reason about distances
        from the visual input in 3D environments. The Dmlab dataset consists of
        360x480 color images in 6 classes. The classes are
        {close, far, very far} x {positive reward, negative reward}
        respectively.""",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(
                shape=(360, 480, 3), encoding_format="jpeg"
            ),
            "filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=6),
        }),
        homepage="https://github.com/google-research/task_adaptation",
        citation=r"""@article{zhai2019visual,
        title={The Visual Task Adaptation Benchmark},
        author={Xiaohua Zhai and Joan Puigcerver and Alexander Kolesnikov and
               Pierre Ruyssen and Carlos Riquelme and Mario Lucic and
               Josip Djolonga and Andre Susano Pinto and Maxim Neumann and
               Alexey Dosovitskiy and Lucas Beyer and Olivier Bachem and
               Michael Tschannen and Marcin Michalski and Olivier Bousquet and
               Sylvain Gelly and Neil Houlsby},
                              year={2019},
                              eprint={1910.04867},
                              archivePrefix={arXiv},
                              primaryClass={cs.CV},
                              url = {https://arxiv.org/abs/1910.04867}
                          }""",
        supervised_keys=("image", "label"),
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": path,
                "split_name": "train",
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "images_dir_path": path,
                "split_name": "validation",
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": path,
                "split_name": "test",
            },
        ),
    ]

  def _parse_single_image(self, example_proto):
    """Parses single video from the input tfrecords.

    Args:
      example_proto: tfExample proto with a single video.

    Returns:
      dict with all frames, positions and actions.
    """

    feature_map = {
        "image": tf.io.FixedLenFeature(shape=[], dtype=tf.string),
        "filename": tf.io.FixedLenFeature(shape=[], dtype=tf.string),
        "label": tf.io.FixedLenFeature(shape=[], dtype=tf.int64),
    }

    parse_single = tf.io.parse_single_example(example_proto, feature_map)

    return parse_single

  def _generate_examples(self, images_dir_path, split_name):
    path_glob = os.path.join(
        images_dir_path, "dmlab-{}.tfrecord*".format(split_name)
    )
    files = tf.io.gfile.glob(path_glob)

    logging.info("Reading data from %s.", ",".join(files))
    with tf.Graph().as_default():
      ds = tf.data.TFRecordDataset(files)
      ds = ds.map(
          self._parse_single_image,
          num_parallel_calls=tf.data.experimental.AUTOTUNE,
      )
      iterator = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
      with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        try:
          while True:
            result = sess.run(iterator)
            yield result["filename"], {
                "image": io.BytesIO(result["image"]),
                "filename": result["filename"],
                "label": result["label"],
            }

        except tf.errors.OutOfRangeError:
          return
