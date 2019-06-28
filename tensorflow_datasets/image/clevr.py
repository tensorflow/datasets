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

"""CLEVR dataset."""

import json
import os

import tensorflow as tf

import tensorflow_datasets.public_api as tfds


_DESCRIPTION = """\
CLEVR is a diagnostic dataset that tests a range of visual reasoning abilities.
It contains minimal biases and has detailed annotations describing the kind of
reasoning each question requires.
"""


_CITATION = """\
@inproceedings{johnson2017clevr,
  title={{CLEVR}: A diagnostic dataset for compositional language and elementary visual reasoning},
  author={Johnson, Justin and Hariharan, Bharath and van der Maaten, Laurens and Fei-Fei, Li and Lawrence Zitnick, C and Girshick, Ross},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2017}
}
"""

_NUM_SHARDS = 128

_BASE_URL = "https://cs.stanford.edu/people/jcjohns/clevr/"
_DOWNLOAD_URL = "https://dl.fbaipublicfiles.com/clevr/CLEVR_v1.0.zip"


class CLEVR(tfds.core.GeneratorBasedBuilder):
  """CLEVR dataset."""

  VERSION = tfds.core.Version("1.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.0.0", experiments={tfds.core.Experiment.S3: True}),
      tfds.core.Version("1.0.0"),
  ]
  # Version history:
  # 2.0.0: S3 (new shuffling, sharding and slicing mechanism).

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "file_name": tfds.features.Text(),
            "objects": tfds.features.Sequence({
                "color": tfds.features.ClassLabel(names=["gray", "blue",
                                                         "brown", "yellow",
                                                         "red", "green",
                                                         "purple", "cyan"]),
                "material": tfds.features.ClassLabel(names=["rubber", "metal"]),
                "shape": tfds.features.ClassLabel(names=["cube", "sphere",
                                                         "cylinder"]),
                "size": tfds.features.ClassLabel(names=["small", "large"]),
                "rotation": tfds.features.Tensor(shape=(), dtype=tf.float32),
                "3d_coords": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
                "pixel_coords": tfds.features.Tensor(shape=(3,),
                                                     dtype=tf.float32),
            })
        }),
        urls=[_BASE_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    images_path_dir = os.path.join(path, "CLEVR_v1.0/images")
    scenes_path_dir = os.path.join(path, "CLEVR_v1.0/scenes")

    splits = []
    for split_name in ["train", "val", "test"]:
      name_map = {"train": "train", "val": "validation", "test": "test"}
      splits.append(tfds.core.SplitGenerator(
          name=name_map[split_name],
          num_shards=_NUM_SHARDS,
          gen_kwargs={
              "images_dir_path": os.path.join(images_path_dir, split_name),
              "scenes_description_file": os.path.join(
                  scenes_path_dir, "CLEVR_{}_scenes.json".format(split_name)),
              },
          ))

    return splits

  def _generate_examples(self, images_dir_path, scenes_description_file):
    image_paths = sorted([os.path.join(images_dir_path, filename)
                          for filename in tf.io.gfile.listdir(images_dir_path)])

    if tf.io.gfile.exists(scenes_description_file):
      scenes_json = json.load(tf.io.gfile.GFile(scenes_description_file))
    else:
      # if annotation file does not exist, we create empty annotations
      scenes_json = {"scenes": [{"objects": []}] * len(image_paths)}

    attrs = ["color", "material", "shape", "size",
             "rotation", "pixel_coords", "3d_coords"]
    for image_path, scene in zip(image_paths, scenes_json["scenes"]):
      objects = scene["objects"]
      fname = os.path.basename(image_path)
      record = {
          "image": image_path,
          "file_name": fname,
          "objects": [{attr: obj[attr] for attr in attrs} for obj in objects]  # pylint: disable=g-complex-comprehension
      }
      if self.version.implements(tfds.core.Experiment.S3):
        yield fname, record
      else:
        yield record
