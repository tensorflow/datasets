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

"""Stanford Online Products Dataset."""

import csv
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_LINK = "ftp://cs.stanford.edu/cs/cvgl/Stanford_Online_Products.zip"
_SPLITS = {tfds.Split.TRAIN: "Ebay_train", tfds.Split.TEST: "Ebay_test"}

_SUPER_CLASSES = [
    "bicycle",
    "cabinet",
    "chair",
    "coffee_maker",
    "fan",
    "kettle",
    "lamp",
    "mug",
    "sofa",
    "stapler",
    "table",
    "toaster",
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """Stanford Online Products Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        homepage="http://cvgl.stanford.edu/projects/lifted_struct/",
        features=tfds.features.FeaturesDict({
            "class_id": tfds.features.ClassLabel(num_classes=22634),
            "super_class_id/num": tfds.features.ClassLabel(
                num_classes=len(_SUPER_CLASSES)
            ),
            "super_class_id": tfds.features.ClassLabel(names=_SUPER_CLASSES),
            "image": tfds.features.Image(),
        }),
    )

  def _split_generators(self, dl_manager):
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_LINK)
    folder_path = os.path.join(dl_path, "Stanford_Online_Products")
    return [  # pylint:disable=g-complex-comprehension
        tfds.core.SplitGenerator(
            name=k,
            gen_kwargs={"file_path": os.path.join(folder_path, "%s.txt" % v)},
        )
        for k, v in _SPLITS.items()
    ]

  def _generate_examples(self, file_path):
    """Images of Product from the Data Directory.

    Args:
      file_path: str, path to the Ebay_(train/test/info).txt file. Having
        Columns ['class_id', 'super_class_id', 'path']

    Yields:
      Dataset examples.
    """
    with tf.io.gfile.GFile(file_path, "r") as file_:
      dataset = csv.DictReader(file_, delimiter=" ")
      for i, row in enumerate(dataset):
        yield i, {
            "class_id": int(row["class_id"]) - 1,
            "super_class_id/num": int(row["super_class_id"]) - 1,
            "super_class_id": _SUPER_CLASSES[int(row["super_class_id"]) - 1],
            "image": os.path.join(os.path.dirname(file_path), row["path"]),
        }
