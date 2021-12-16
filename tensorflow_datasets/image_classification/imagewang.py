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

# -*- coding: utf-8 -*-
"""Imagewang contains Imagenette and Imagewoof combined."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{imagewang,
  author    = "Jeremy Howard",
  title     = "Imagewang",
  url       = "https://github.com/fastai/imagenette/"
}
"""

_DESCRIPTION = """\
Imagewang contains Imagenette and Imagewoof combined
Image网 (pronounced "Imagewang"; 网 means "net" in Chinese) contains Imagenette
and Imagewoof combined, but with some twists that make it into a tricky
semi-supervised unbalanced classification problem:

* The validation set is the same as Imagewoof (i.e. 30% of Imagewoof images);
  there are no Imagenette images in the validation set (they're all in the
  training set)
* Only 10% of Imagewoof images are in the training set!
* The remaining are in the unsup ("unsupervised") directory, and you can not
  use their labels in training!
* It's even hard to type and hard to say!

The dataset comes in three variants:

  * Full size
  * 320 px
  * 160 px

This dataset consists of the Imagenette dataset {size} variant.
"""

_DESCRIPTION_SHORT = """\
Imagewang contains Imagenette and Imagewoof combined.
"""

_LABELS_FNAME = "image_classification/imagewang_labels.txt"
_URL_PREFIX = "https://s3.amazonaws.com/fast-ai-imageclas"
_SIZES = ["full-size", "320px", "160px"]

_SIZE_TO_DIRNAME = {
    "full-size": "imagewang",
    "320px": "imagewang-320",
    "160px": "imagewang-160"
}


class ImagewangConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagewang."""

  def __init__(self, size, **kwargs):
    super(ImagewangConfig, self).__init__(
        version=tfds.core.Version("2.0.0"), **kwargs)
    self.size = size


def _make_builder_configs():
  configs = []
  for size in _SIZES:
    configs.append(
        ImagewangConfig(name=size, size=size, description=_DESCRIPTION_SHORT))
  return configs


class Imagewang(tfds.core.GeneratorBasedBuilder):
  """Imagewang contains Imagenette and Imagewoof combined."""

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names_file=names_file)
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/fastai/imagenette",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    size = self.builder_config.size
    if size in _SIZES:
      size_str = "" if size == "full-size" else "-" + size[:-2]
      url = "/".join([_URL_PREFIX, "imagewang%s.tgz" % size_str])
      path = dl_manager.download_and_extract(url)
      train_path = os.path.join(path, _SIZE_TO_DIRNAME[size], "train")
      val_path = os.path.join(path, _SIZE_TO_DIRNAME[size], "val")
    else:
      raise ValueError("size must be one of %s" % _SIZES)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "datapath": train_path,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "datapath": val_path,
            },
        ),
    ]

  def _generate_examples(self, datapath):
    """Yields examples."""
    for label in tf.io.gfile.listdir(datapath):
      for fpath in tf.io.gfile.glob(os.path.join(datapath, label, "*.JPEG")):
        fname = os.path.basename(fpath)
        record = {
            "image": fpath,
            "label": label,
        }
        yield fname, record
