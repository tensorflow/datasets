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

"""CLEVR dataset."""

import collections
import json
import os

import tensorflow.compat.v2 as tf
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

_BASE_URL = "https://cs.stanford.edu/people/jcjohns/clevr/"
_DOWNLOAD_URL = "https://dl.fbaipublicfiles.com/clevr/CLEVR_v1.0.zip"


class CLEVR(tfds.core.GeneratorBasedBuilder):
  """CLEVR dataset."""

  VERSION = tfds.core.Version("3.1.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("3.0.0"),
  ]
  RELEASE_NOTES = {
      "3.1.0": "Add question/answer text.",
  }

  def _info(self):
    features = {
        "image":
            tfds.features.Image(),
        "file_name":
            tfds.features.Text(),
        "objects":
            tfds.features.Sequence({
                "color":
                    tfds.features.ClassLabel(names=[
                        "gray", "blue", "brown", "yellow", "red", "green",
                        "purple", "cyan"
                    ]),
                "material":
                    tfds.features.ClassLabel(names=["rubber", "metal"]),
                "shape":
                    tfds.features.ClassLabel(
                        names=["cube", "sphere", "cylinder"]),
                "size":
                    tfds.features.ClassLabel(names=["small", "large"]),
                "rotation":
                    tfds.features.Tensor(shape=(), dtype=tf.float32),
                "3d_coords":
                    tfds.features.Tensor(shape=(3,), dtype=tf.float32),
                "pixel_coords":
                    tfds.features.Tensor(shape=(3,), dtype=tf.float32),
            })
    }
    if self.version > "3.0.0":
      features["question_answer"] = tfds.features.Sequence({
          "question": tfds.features.Text(),
          "answer": tfds.features.Text(),
      })
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage=_BASE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    images_path_dir = os.path.join(path, "CLEVR_v1.0/images")
    questions_path_dir = os.path.join(path, "CLEVR_v1.0/questions")
    scenes_path_dir = os.path.join(path, "CLEVR_v1.0/scenes")

    splits = []
    for split_name in ["train", "val", "test"]:
      name_map = {
          "train": tfds.Split.TRAIN,
          "val": tfds.Split.VALIDATION,
          "test": tfds.Split.TEST,
      }
      splits.append(
          tfds.core.SplitGenerator(
              name=name_map[split_name],
              gen_kwargs={
                  "images_dir_path":
                      os.path.join(images_path_dir, split_name),
                  "question_file":
                      os.path.join(
                          questions_path_dir,
                          "CLEVR_{}_questions.json".format(split_name)),
                  "scenes_description_file":
                      os.path.join(scenes_path_dir,
                                   "CLEVR_{}_scenes.json".format(split_name)),
              },
          ))

    return splits

  def _generate_examples(self, images_dir_path, question_file,
                         scenes_description_file):
    image_paths = sorted([
        os.path.join(images_dir_path, filename)
        for filename in tf.io.gfile.listdir(images_dir_path)
    ])

    with tf.io.gfile.GFile(question_file) as f:
      questions_json = json.load(f)
    questions = collections.defaultdict(list)
    for q in questions_json["questions"]:
      questions[q["image_filename"]].append({
          "question": q["question"],
          "answer": q.get("answer", ""),  # Test set do not have answer.
      })

    if tf.io.gfile.exists(scenes_description_file):
      with tf.io.gfile.GFile(scenes_description_file) as f:
        scenes_json = json.load(f)
    else:
      # if annotation file does not exist, we create empty annotations
      scenes_json = {"scenes": [{"objects": []}] * len(image_paths)}

    attrs = [
        "color", "material", "shape", "size", "rotation", "pixel_coords",
        "3d_coords"
    ]
    for image_path, scene in zip(image_paths, scenes_json["scenes"]):
      objects = scene["objects"]
      fname = os.path.basename(image_path)
      record = {
          "image": image_path,
          "file_name": fname,
          "question_answer": questions[fname],
          "objects": [{attr: obj[attr] for attr in attrs} for obj in objects]  # pylint: disable=g-complex-comprehension
      }
      yield fname, record
