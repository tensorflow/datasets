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

"""Geirhos conflict stimulus set."""

import os
import re

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{
  geirhos2018imagenettrained,
  title={ImageNet-trained {CNN}s are biased towards texture; increasing shape
         bias improves accuracy and robustness.},
  author={Robert Geirhos and Patricia Rubisch and Claudio Michaelis and
          Matthias Bethge and Felix A. Wichmann and Wieland Brendel},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://openreview.net/forum?id=Bygh9j09KX},
}
"""

_DESCRIPTION = """\
Shape/texture conflict stimuli from "ImageNet-trained CNNs are biased towards \
texture; increasing shape bias improves accuracy and robustness."

Note that, although the dataset source contains images with matching shape and
texture and we include them here, they are ignored for most evaluations in the
original paper.
"""

_BASE_URL = "https://github.com/rgeirhos/texture-vs-shape"
_DOWNLOAD_URL = "https://github.com/rgeirhos/texture-vs-shape/archive/1b69c6a445c3348927139edb30a5134521fd4b03.zip"
_IMAGENET_MAPPING_URL = "https://raw.githubusercontent.com/rgeirhos/generalisation-humans-DNNs/5bbe08f6821e1eb2bdbe98acebf3586d36be00ab/16-class-ImageNet/MSCOCO_to_ImageNet_category_mapping.txt"
_DATA_DIR_PATH = "texture-vs-shape-1b69c6a445c3348927139edb30a5134521fd4b03/stimuli/style-transfer-preprocessed-512"

_CLASSES = [
    "airplane", "bear", "bicycle", "bird", "boat", "bottle", "car", "cat",
    "chair", "clock", "dog", "elephant", "keyboard", "knife", "oven", "truck"
]
_IMAGENET_LABELS_FNAME = "image_classification/imagenet2012_labels.txt"


class GeirhosConflictStimuli(tfds.core.GeneratorBasedBuilder):
  """Shape/Texture conflict ."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    """Define dataset info."""

    imagenet_names_file = tfds.core.tfds_path(_IMAGENET_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(),
            "shape_label":
                tfds.features.ClassLabel(names=_CLASSES),
            "shape_imagenet_labels":
                tfds.features.Sequence(
                    tfds.features.ClassLabel(names_file=imagenet_names_file)),
            "texture_label":
                tfds.features.ClassLabel(names=_CLASSES),
            "texture_imagenet_labels":
                tfds.features.Sequence(
                    tfds.features.ClassLabel(names_file=imagenet_names_file)),
            "file_name":
                tfds.features.Text(),
        }),
        supervised_keys=("image", "shape_label"),
        homepage=_BASE_URL,
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    """Define splits."""

    dl_paths = dl_manager.download_and_extract({
        "texture_vs_shape": _DOWNLOAD_URL,
        "imagenet_mapping": _IMAGENET_MAPPING_URL
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "data_dir_path":
                    os.path.join(dl_paths["texture_vs_shape"], _DATA_DIR_PATH),
                "imagenet_mapping_path":
                    dl_paths["imagenet_mapping"]
            },
        ),
    ]

  def _generate_examples(self, data_dir_path, imagenet_mapping_path):
    """Generate images and labels for splits."""
    # Read ImageNet mapping.
    imagenet_names = set(self.info.features["shape_imagenet_labels"].names)

    with tf.io.gfile.GFile(imagenet_mapping_path) as f:
      mapping_txt = f.read()
    mapping = {}
    for match in re.finditer(r"([a-z]+)\s*=\s*\[([^\]]+)\]", mapping_txt):
      mapping[match.group(1)] = list(
          sorted(
              imagenet_names.intersection(
                  re.sub(r"\s", "", match.group(2)).split(","))))

    # Process images.
    for shape_class_name in tf.io.gfile.listdir(data_dir_path):
      class_dir_path = os.path.join(data_dir_path, shape_class_name)
      for image_name in tf.io.gfile.listdir(class_dir_path):
        image = os.path.join(class_dir_path, image_name)
        texture_class_name = re.search("-([a-z]+)", image_name).group(1)  # pytype: disable=attribute-error
        yield image_name, {
            "image": image,
            "file_name": image_name,
            "shape_label": shape_class_name,
            "shape_imagenet_labels": mapping[shape_class_name],
            "texture_label": texture_class_name,
            "texture_imagenet_labels": mapping[texture_class_name]
        }
