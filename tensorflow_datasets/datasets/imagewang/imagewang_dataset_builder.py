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

# -*- coding: utf-8 -*-
"""Imagewang contains Imagenette and Imagewoof combined."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION_SHORT = """\
Imagewang contains Imagenette and Imagewoof combined.
"""

_LABELS_FNAME = "image_classification/imagewang_labels.txt"
_URL_PREFIX = "https://s3.amazonaws.com/fast-ai-imageclas"
_SIZES = ["full-size", "320px", "160px"]

_SIZE_TO_DIRNAME = {
    "full-size": "imagewang",
    "320px": "imagewang-320",
    "160px": "imagewang-160",
}


class ImagewangConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagewang."""

  def __init__(self, size, **kwargs):
    super(ImagewangConfig, self).__init__(
        version=tfds.core.Version("2.0.0"), **kwargs
    )
    self.size = size


def _make_builder_configs():
  configs = []
  for size in _SIZES:
    configs.append(
        ImagewangConfig(name=size, size=size, description=_DESCRIPTION_SHORT)
    )
  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """Imagewang contains Imagenette and Imagewoof combined."""

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/fastai/imagenette",
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
