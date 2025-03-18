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

"""Imagenette: a subset of 10 easily classified classes from Imagenet.

(tench, English springer, cassette player, chain saw, church, French horn,
garbage truck, gas pump, golf ball, parachute)
"""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_LABELS_FNAME = "image_classification/imagenette_labels.txt"
_URL_PREFIX = "https://s3.amazonaws.com/fast-ai-imageclas/"


class ImagenetteConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagenette."""

  def __init__(self, size, base, **kwargs):
    super(ImagenetteConfig, self).__init__(
        # `320px-v2`,...
        name=size + ("-v2" if base == "imagenette2" else ""),
        description="{} variant.".format(size),
        **kwargs,
    )
    # e.g. `imagenette2-320.tgz`
    self.dirname = (
        base
        + {
            "full-size": "",
            "320px": "-320",
            "160px": "-160",
        }[size]
    )


def _make_builder_configs():
  configs = []
  for base in ["imagenette2", "imagenette"]:
    for size in ["full-size", "320px", "160px"]:
      configs.append(ImagenetteConfig(base=base, size=size))
  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """A smaller subset of 10 easily classified classes from Imagenet."""

  VERSION = tfds.core.Version("1.0.0")

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(encoding_format="jpeg"),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/fastai/imagenette",
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
