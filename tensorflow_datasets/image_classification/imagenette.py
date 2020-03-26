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

# Lint as: python3
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

_CITATION = """
@misc{imagenette,
  author    = "Jeremy Howard",
  title     = "imagenette",
  url       = "https://github.com/fastai/imagenette/"
}
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

Note: The v2 config correspond to the new 70/30 train/valid split (released
in Dec 6 2019).
"""

_LABELS_FNAME = "image_classification/imagenette_labels.txt"
_URL_PREFIX = "https://s3.amazonaws.com/fast-ai-imageclas/"


class ImagenetteConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagenette."""

  def __init__(self, size, base, **kwargs):
    super(ImagenetteConfig, self).__init__(
        # `320px-v2`,...
        name=size + ("-v2" if base == "imagenette2" else ""),
        description="{} variant.".format(size),
        version=tfds.core.Version("0.1.0"),
        **kwargs)
    # e.g. `imagenette2-320.tgz`
    self.dirname = base + {
        "full-size": "",
        "320px": "-320",
        "160px": "-160",
    }[size]


def _make_builder_configs():
  configs = []
  for base in ["imagenette2", "imagenette"]:
    for size in ["full-size", "320px", "160px"]:
      configs.append(ImagenetteConfig(base=base, size=size))
  return configs


class Imagenette(tfds.core.GeneratorBasedBuilder):
  """A smaller subset of 10 easily classified classes from Imagenet."""

  VERSION = tfds.core.Version("0.1.1")

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
    dirname = self.builder_config.dirname
    url = _URL_PREFIX + "{}.tgz".format(dirname)
    path = dl_manager.download_and_extract(url)
    train_path = os.path.join(path, dirname, "train")
    val_path = os.path.join(path, dirname, "val")

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
