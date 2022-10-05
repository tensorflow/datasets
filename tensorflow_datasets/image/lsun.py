# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""LSUN dataset.

Large scene understanding dataset.
"""

import io
import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

LSUN_SCENE_URL = "http://dl.yf.io/lsun/scenes/%s_%s_lmdb.zip"
LSUN_OBJECT_URL = "http://dl.yf.io/lsun/objects/%s.zip"

_CITATION = """\
@article{journals/corr/YuZSSX15,
  added-at = {2018-08-13T00:00:00.000+0200},
  author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
  biburl = {https://www.bibsonomy.org/bibtex/2446d4ffb99a5d7d2ab6e5417a12e195f/dblp},
  ee = {http://arxiv.org/abs/1506.03365},
  interhash = {3e9306c4ce2ead125f3b2ab0e25adc85},
  intrahash = {446d4ffb99a5d7d2ab6e5417a12e195f},
  journal = {CoRR},
  keywords = {dblp},
  timestamp = {2018-08-14T15:08:59.000+0200},
  title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop.},
  url = {http://dblp.uni-trier.de/db/journals/corr/corr1506.html#YuZSSX15},
  volume = {abs/1506.03365},
  year = 2015
}
"""

# From http://dl.yf.io/lsun/categories.txt minus "test"
_SCENES_CATEGORIES = [
    "classroom",
    "bedroom",
    "bridge",
    "church_outdoor",
    "conference_room",
    "dining_room",
    "kitchen",
    "living_room",
    "restaurant",
    "tower",
]

# From http://dl.yf.io/lsun/objects/
_OBJECTS_CATEGORIES = [
    "airplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "dining_table",
    "dog",
    "horse",
    "motorbike",
    "person",
    "potted_plant",
    "sheep",
    "sofa",
    "train",
    "tv-monitor",
]


def _make_lmdb_dataset(path):
  return tfds.core.lazy_imports.tensorflow_io.IODataset.from_lmdb(path)




class Lsun(tfds.core.GeneratorBasedBuilder):
  """Lsun dataset."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(  # pylint: disable=g-complex-comprehension
          name=category,
          description="Images of category %s" % category,
          version=tfds.core.Version("3.1.0"),
          release_notes={
              "3.0.0": "New split API (https://tensorflow.org/datasets/splits)",
              "3.1.0":
                  "Add builder config for missing `person` object category, "
                  "and add `id` to the feature dict",
          },
      ) for category in (_SCENES_CATEGORIES + _OBJECTS_CATEGORIES)
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Large scale images showing different objects "
                     "from given categories like bedroom, tower etc."),
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "image": tfds.features.Image(encoding_format="jpeg"),
        }),
        homepage="https://www.yf.io/p/lsun",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    if self.builder_config.name in _SCENES_CATEGORIES:
      extracted_dirs = dl_manager.download_and_extract({
          "train": LSUN_SCENE_URL % (self.builder_config.name, "train"),
          "val": LSUN_SCENE_URL % (self.builder_config.name, "val")
      })
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "extracted_dir":
                      extracted_dirs["train"],
                  "file_path":
                      "%s_%s_lmdb" % (self.builder_config.name, "train")
              }),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "extracted_dir": extracted_dirs["val"],
                  "file_path": "%s_%s_lmdb" % (self.builder_config.name, "val")
              }),
      ]
    else:
      extracted_dirs = dl_manager.download_and_extract({
          "train": LSUN_OBJECT_URL % self.builder_config.name,
      })
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "extracted_dir": extracted_dirs["train"],
                  "file_path": self.builder_config.name
              })
      ]

  def _generate_examples(self, extracted_dir, file_path):
    with tf.Graph().as_default():
      path = os.path.join(extracted_dir, file_path, "data.mdb")
      if not tf.io.gfile.exists(path):
        raise RuntimeError(f"Could not open file {path}!")
      dataset = _make_lmdb_dataset(path)
      for i, (id_bytes, jpeg_image) in enumerate(tfds.as_numpy(dataset)):
        record = {
            "id": id_bytes.decode("utf-8"),
            "image": io.BytesIO(jpeg_image),
        }
        yield i, record
