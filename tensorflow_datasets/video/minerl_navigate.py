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

"""Minerl Navigate Video dataset."""

import os
import json

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The MineRL dataset was crowd sourced by Guss et al. (2019) for reinforcement
learning applications. The dataset shows human players traveling to goal
coordinates in procedurally generated 3D worldsof the video game Minecraft,
traversing forests, mountains, villages, and oceans. To create a video
prediction dataset, we combined the human demonstrations for the `Navigate` and
`Navigate Extreme` tasks and split them into non-overlapping sequences of
length 500. The dataset contains 961 training videos and 225 test videos as
individual MP4 files. Additional metadata is stored in JSON format and contains
the actions taken by the players in the game and the angle between the forward
direction and the direction to the goal.
"""

_CITATION = """
@misc{saxena2021clockwork,
      title={Clockwork Variational Autoencoders},
      author={Vaibhav Saxena and Jimmy Ba and Danijar Hafner},
      year={2021},
      eprint={2102.09532},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
"""

_DOWNLOAD_URL = "https://archive.org/download/minerl_navigate/minerl_navigate.zip"

VIDEO_LEN = 500


class MinerlNavigate(tfds.core.GeneratorBasedBuilder):
  """MineRL Navigate Video Dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {
                "video":
                    tfds.features.Video(shape=(None, 64, 64, 3)),
                "actions":
                    tfds.features.FeaturesDict(
                        {
                            "attack":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "back":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "camera_x":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.float32
                                ),
                            "camera_y":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.float32
                                ),
                            "forward":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "jump":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "left":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "place":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "right":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "sneak":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                ),
                            "sprint":
                                tfds.features.Tensor(
                                    shape=(VIDEO_LEN,), dtype=tf.int32
                                )
                        }
                    )
            }
        ),
        supervised_keys=None,
        homepage="https://archive.org/details/minerl_navigate",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    return {
        "train": self._generate_examples(path / "minerl_navigate" / "train"),
        "test": self._generate_examples(path / "minerl_navigate" / "test"),
    }

  def _generate_examples(self, path):
    metadata = json.loads((path / "metadata.json").read_text())
    for f in path.glob("*.mp4"):
      key = str(os.path.basename(f))
      actions = {
          "attack": metadata[key]["attack"],
          "back": metadata[key]["back"],
          "camera_x": metadata[key]["camera_x"],
          "camera_y": metadata[key]["camera_y"],
          "forward": metadata[key]["forward"],
          "jump": metadata[key]["jump"],
          "left": metadata[key]["left"],
          "place": metadata[key]["place"],
          "right": metadata[key]["right"],
          "sneak": metadata[key]["sneak"],
          "sprint": metadata[key]["sprint"],
      }
      yield key, {
          "video": str(f.resolve()),
          "actions": actions,
      }
