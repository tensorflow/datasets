# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Imagenette: a subset of 10 easily classified classes from Imagenet.

(tench, English springer, cassette player, chain saw, church, French horn,
garbage truck, gas pump, golf ball, parachute)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

# TODO(imagenette): BibTeX citation
_CITATION = """
"""

_DESCRIPTION = """\
Imagenette is a subset of 10 easily classified classes from the Imagenet
dataset. It was originally prepared by Jeremy Howard of FastAI. The objective
behind putting together a small version of the Imagenet dataset was mainly
because running new ideas/algorithms/experiments on the whole Imagenet take a
lot of time.

This version of the dataset allows researchers/practitioners to quickly try out
ideas and share with others. The dataset comes in three variants:

  * Full size
  * 320 px
  * 160 px
This dataset consists of the Imagenette dataset {size} variant.
"""

_LABELS_FNAME = "image/imagenette_labels.txt"
_URL_PREFIX = "https://s3.amazonaws.com/fast-ai-imageclas"
_SIZES = ["full-size", "320px", "160px"]

_SIZE_TO_DIRNAME = {
    "full-size": "imagenette",
    "320px": "imagenette-320",
    "160px": "imagenette-160"
}


class ImagenetteConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagenette."""

  def __init__(self, size, **kwargs):
    super(ImagenetteConfig, self).__init__(
        version=tfds.core.Version("0.1.0"), **kwargs)
    self.size = size


def _make_builder_configs():
  configs = []
  for size in _SIZES:
    configs.append(
        ImagenetteConfig(
            name=size,
            size=size,
            description=_DESCRIPTION.format(size=size)))
  return configs


class Imagenette(tfds.core.GeneratorBasedBuilder):
  """A smaller subset of 10 easily classified classes from Imagenet."""

  VERSION = tfds.core.Version("0.1.0")
  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
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
      url = os.path.join(_URL_PREFIX, "imagenette%s.tgz" % size_str)
      path = dl_manager.download_and_extract(url)
      train_path = os.path.join(path, _SIZE_TO_DIRNAME[size], "train")
      val_path = os.path.join(path, _SIZE_TO_DIRNAME[size], "val")
    else:
      raise ValueError("Size not implemented!")

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
