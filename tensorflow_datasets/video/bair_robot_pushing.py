# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Berkeley (BAIR) robot pushing dataset.

Self-Supervised Visual Planning with Temporal Skip Connections
Frederik Ebert, Chelsea Finn, Alex X. Lee, and Sergey Levine.
https://arxiv.org/abs/1710.05268
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

DATA_URL = (
    "http://rail.eecs.berkeley.edu/datasets/bair_robot_pushing_dataset_v0.tar")

# There are exactly 30 frames in each video.
FRAMES_PER_VIDEO = 30


class BairRobotPushing(tfds.core.GeneratorBasedBuilder):
  """Robot pushing dataset from BAIR."""

  def _split_generators(self, dl_manager):
    files = dl_manager.download_and_extract(DATA_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "split_name": "train",
                "filedir": os.path.join(files, "softmotion30_44k/train"),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=4,
            gen_kwargs={
                "split_name": "test",
                "filedir": os.path.join(files, "softmotion30_44k/test"),
            }),
    ]

  def _info(self):
    nb_frames = FRAMES_PER_VIDEO
    features = tfds.features.FeaturesDict({
        "video_main": tfds.features.Video(shape=(nb_frames, 64, 64, 3)),
        "video_aux1": tfds.features.Video(shape=(nb_frames, 64, 64, 3)),
        "action": tfds.features.Tensor(shape=(nb_frames, 4), dtype=tf.float32),
        "endeffector_pos": tfds.features.Tensor(
            shape=(nb_frames, 3), dtype=tf.float32),
    })
    return tfds.core.DatasetInfo(
        name=self.name,
        description="This data set contains roughly 59,000 examples of robot "
        "pushing motions, including one training set (train) and "
        "two test sets of previously seen (testseen) and unseen "
        "(testnovel) objects.",
        version="0.1.0",
        features=features,
        urls=["https://sites.google.com/site/brainrobotdata/home/push-dataset"],
        size_in_bytes=30.0 * tfds.units.GiB,
        citation="Unsupervised Learning for Physical Interaction through Video "
        " Prediction. Chelsea Finn, Ian Goodfellow, Sergey Levine",
    )

  def _parse_single_video(self, example_proto):
    """Parses single video from the input tfrecords.

    Args:
      example_proto: tfExample proto with a single video.
    Returns:
      dict with all frames, positions and actions.
    """
    features_base = {
        "action": tf.FixedLenFeature([4], tf.float32),
        "image_aux1/encoded": tf.FixedLenFeature((), tf.string),
        "image_main/encoded": tf.FixedLenFeature((), tf.string),
        "endeffector_pos": tf.FixedLenFeature([3], tf.float32),
    }
    features = {}
    for frame in range(FRAMES_PER_VIDEO):
      for key, value in features_base.items():
        features["%d/%s" % (frame, key)] = value

    parsed = tf.parse_single_example(example_proto, features)
    # Decode images from string to uint8 tensor (64, 64, 3).
    for frame in range(FRAMES_PER_VIDEO):
      for key in ["image_main/encoded", "image_aux1/encoded"]:
        parsed["%d/%s" % (frame, key)] = tf.cast(
            tf.reshape(
                tf.decode_raw(parsed["%d/%s" % (frame, key)], tf.uint8),
                (64, 64, 3)), dtype=tf.uint8)
    return parsed

  def _generate_examples(self, split_name, filedir):
    tf.logging.info("Reading data from %s.", filedir)
    files = tf.gfile.ListDirectory(filedir)
    tf.logging.info("Split %s: files found: %d.", split_name, len(files))
    with tf.Graph().as_default():
      ds = tf.data.TFRecordDataset([
          os.path.join(filedir, x) for x in files
      ])
      ds = ds.map(self._parse_single_video,
                  num_parallel_calls=tf.data.experimental.AUTOTUNE)
      iterator = ds.make_one_shot_iterator().get_next()
      with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        try:
          while True:
            video = sess.run(iterator)
            yield self.info.features.encode_example({
                "video_main":
                    np.array([
                        video["%d/image_main/encoded" % i]
                        for i in range(FRAMES_PER_VIDEO)
                    ]),
                "video_aux1":
                    np.array([
                        video["%d/image_aux1/encoded" % i]
                        for i in range(FRAMES_PER_VIDEO)
                    ]),
                "action":
                    np.array([
                        video["%d/action" % i] for i in range(FRAMES_PER_VIDEO)
                    ]),
                "endeffector_pos":
                    np.array([
                        video["%d/endeffector_pos" % i]
                        for i in range(FRAMES_PER_VIDEO)
                    ]),
            })

        except tf.errors.OutOfRangeError:
          # End of file.
          return
