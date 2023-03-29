# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""MIT Scene Parsing Benchmark (SceneParse150)."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_TRAIN_URL = {
    "images": (
        "http://sceneparsing.csail.mit.edu/data/ChallengeData2017/images.tar"
    ),
    "annotations": "http://sceneparsing.csail.mit.edu/data/ChallengeData2017/annotations_instance.tar",
}


class Builder(tfds.core.GeneratorBasedBuilder):
  """MIT Scene Parsing Benchmark dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(encoding_format="jpeg"),
            "annotation": tfds.features.Image(encoding_format="png"),
        }),
        supervised_keys=("image", "annotation"),
        homepage="http://sceneparsing.csail.mit.edu/",
    )

  def _split_generators(self, dl_manager):
    dl_paths = dl_manager.download_and_extract({
        "images": _TRAIN_URL["images"],
        "annotations": _TRAIN_URL["annotations"],
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": os.path.join(
                    dl_paths["images"], "images/training"
                ),
                "annotations_dir_path": os.path.join(
                    dl_paths["annotations"], "annotations_instance/training"
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": os.path.join(
                    dl_paths["images"], "images/validation"
                ),
                "annotations_dir_path": os.path.join(
                    dl_paths["annotations"], "annotations_instance/validation"
                ),
            },
        ),
    ]

  def _generate_examples(self, images_dir_path, annotations_dir_path):
    for image_file in tf.io.gfile.listdir(images_dir_path):
      # get the filename
      image_id = os.path.split(image_file)[1].split(".")[0]
      yield image_id, {
          "image": os.path.join(images_dir_path, "{}.jpg".format(image_id)),
          "annotation": os.path.join(
              annotations_dir_path, "{}.png".format(image_id)
          ),
      }
