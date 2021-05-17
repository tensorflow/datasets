# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import os

from absl import logging
import numpy as np
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

DATA_URL = "http://rail.eecs.berkeley.edu/datasets/bair_robot_pushing_dataset_v0.tar"

# There are exactly 30 frames in each video.
FRAMES_PER_VIDEO = 30
IMG_SHAPE = (64, 64, 3)

_CITATION = """\
@misc{1710.05268,
  Author = {Frederik Ebert and Chelsea Finn and Alex X. Lee and Sergey Levine},
  Title = {Self-Supervised Visual Planning with Temporal Skip Connections},
  Year = {2017},
  Eprint = {arXiv:1710.05268},
}
"""


class BairRobotPushingSmall(tfds.core.GeneratorBasedBuilder):
  """Robot pushing dataset from BAIR (Small 64x64 version)."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    # The Bair dataset consist of a sequence of frames (video) with associated
    # metadata (action and position)
    features = tfds.features.Sequence(
        {
            "image_main":
                tfds.features.Image(shape=IMG_SHAPE),
            "image_aux1":
                tfds.features.Image(shape=IMG_SHAPE),
            "action":
                tfds.features.Tensor(shape=(4,), dtype=tf.float32),
            "endeffector_pos":
                tfds.features.Tensor(shape=(3,), dtype=tf.float32),
        },
        length=FRAMES_PER_VIDEO)

    return tfds.core.DatasetInfo(
        builder=self,
        description="This data set contains roughly 44,000 examples of robot "
        "pushing motions, including one training set (train) and "
        "two test sets of previously seen (testseen) and unseen "
        "(testnovel) objects. This is the small 64x64 version.",
        features=features,
        homepage="https://sites.google.com/view/sna-visual-mpc/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    files = dl_manager.download_and_extract(DATA_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filedir": os.path.join(files, "softmotion30_44k", "train"),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filedir": os.path.join(files, "softmotion30_44k", "test"),
            }),
    ]

  def _generate_examples(self, filedir):
    logging.info("Reading data from %s.", filedir)
    files = tf.io.gfile.listdir(filedir)
    logging.info("%d files found.", len(files))

    # For each file
    for filename in sorted(tf.io.gfile.listdir(filedir)):
      filepath = os.path.join(filedir, filename)

      # For each video inside the file
      for video_id, example_str in enumerate(
          tf.compat.v1.io.tf_record_iterator(filepath)):
        example = tf.train.SequenceExample.FromString(example_str)

        # Merge all frames together
        all_frames = []
        for frame_id in range(FRAMES_PER_VIDEO):
          # Extract all features from the original proto context field
          frame_feature = {  # pylint: disable=g-complex-comprehension
              out_key: example.context.feature[in_key.format(frame_id)]  # pylint: disable=g-complex-comprehension
              for out_key, in_key in [
                  ("image_main", "{}/image_main/encoded"),
                  ("image_aux1", "{}/image_aux1/encoded"),
                  ("endeffector_pos", "{}/endeffector_pos"),
                  ("action", "{}/action"),
              ]
          }

          # Decode float
          for key in ("endeffector_pos", "action"):
            values = frame_feature[key].float_list.value
            frame_feature[key] = [values[i] for i in range(len(values))]

          # Decode images (from encoded string)
          for key in ("image_main", "image_aux1"):
            img = frame_feature[key].bytes_list.value[0]  # pytype: disable=attribute-error
            img = np.frombuffer(img, dtype=np.uint8)
            img = np.reshape(img, IMG_SHAPE)
            frame_feature[key] = img

          all_frames.append(frame_feature)

        # Encode the sequence (list) of frames (feature dicts)
        # yield [
        #     {'action': [...], 'image_main': img_frame0, ...},  # Frame 0
        #     {'action': [...], 'image_main': img_frame1, ...},  # Frame 1
        #     ...,
        # ]
        yield "%s_%s" % (filename, video_id), all_frames
