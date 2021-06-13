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

"""Dataset class for COIL-100 dataset."""

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_URL = "http://www.cs.columbia.edu/CAVE/databases/SLAM_coil-20_coil-100/coil-100/coil-100.zip"

_DESCRIPTION = ("""The dataset contains 7200 color images of 100 objects
(72 images per object). The objects have a wide variety of complex geometric and reflectance characteristics.
The objects were placed on a motorized turntable against a black background.
The turntable was rotated through 360 degrees to vary object pose with respect to a fxed color camera.
Images of the objects were taken at pose intervals of	5 degrees.This corresponds to
72 poses per object""")

_ANGLE_LABELS = [str(x) for x in range(0, 360, 5)]
_OBJECT_IDS = [f"obj{str(x)}" for x in range(1, 101)]

_IMAGE_SHAPE = (128, 128, 3)

_CITATION = """\
@article{nene1996columbia,
  title={Columbia object image library (coil-20)},
  author={Nene, Sameer A and Nayar, Shree K and Murase, Hiroshi and others},
  year={1996},
  publisher={Technical report CUCS-005-96}
}
"""


class Coil100(tfds.core.GeneratorBasedBuilder):
  """COIL-100 Image Dataset Class."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "Change features (`object_id` is now `ClassLabel`, rename "
               "`label` -> `angle_label`, add `angle`)",
      "1.0.0": "Initial release",
  }

  def _info(self):
    """Define Dataset Info."""

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "angle_label": tfds.features.ClassLabel(names=_ANGLE_LABELS),
            "object_id": tfds.features.ClassLabel(names=_OBJECT_IDS),
            "angle": tf.int64,
        }),
        supervised_keys=("image", "angle_label"),
        homepage="http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Define Splits."""
    path = dl_manager.download_and_extract(_URL)
    return {
        tfds.Split.TRAIN: self._generate_examples(path / "coil-100"),
    }

  def _generate_examples(self, data_dir_path):
    """Generate images and labels for splits."""
    for file_name in tf.io.gfile.listdir(data_dir_path):
      if file_name.endswith(".png"):
        image = os.path.join(data_dir_path, file_name)
        angle_label = file_name.split("_")[2].split(".")[0]
        object_id = file_name.split("_")[0]
        yield file_name, {
            "image": image,
            "angle_label": angle_label,
            "object_id": object_id,
            "angle": int(angle_label),
        }
