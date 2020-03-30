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
"""Cifar-10.1 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds


_CITATION = """\
@article{recht2018cifar10.1,
  author = {Benjamin Recht and Rebecca Roelofs and Ludwig Schmidt and Vaishaal Shankar},
  title = {Do CIFAR-10 Classifiers Generalize to CIFAR-10?},
  year = {2018},
  note = {\\url{https://arxiv.org/abs/1806.00451}},
}

@article{torralba2008tinyimages, 
  author = {Antonio Torralba and Rob Fergus and William T. Freeman}, 
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title = {80 Million Tiny Images: A Large Data Set for Nonparametric Object and Scene Recognition}, 
  year = {2008}, 
  volume = {30}, 
  number = {11}, 
  pages = {1958-1970}
}
"""

_DESCRIPTION = """\
The CIFAR-10.1 dataset is a new test set for CIFAR-10. CIFAR-10.1 contains roughly 2,000 new test images 
that were sampled after multiple years of research on the original CIFAR-10 dataset. The data collection 
for CIFAR-10.1 was designed to minimize distribution shift relative to the original dataset. We describe 
the creation of CIFAR-10.1 in the paper "Do CIFAR-10 Classifiers Generalize to CIFAR-10?". 
The images in CIFAR-10.1 are a subset of the TinyImages dataset. 
There are currently two versions of the CIFAR-10.1 dataset: v4 and v6.
"""

_DL_URL_IMAGES = "https://github.com/modestyachts/CIFAR-10.1/blob/master/datasets/cifar10.1_{}_data.npy?raw=true"
_DL_URL_LABELS = "https://github.com/modestyachts/CIFAR-10.1/blob/master/datasets/cifar10.1_{}_labels.npy?raw=true"

_DATA_OPTIONS = ["v4", "v6"]


class Cifar10_1Config(tfds.core.BuilderConfig):  # pylint: disable=invalid-name
  """BuilderConfig for Cifar-10.1."""

  @tfds.core.disallow_positional_args
  def __init__(self, data=None, **kwargs):
    """Constructs a Cifar10_1Config.

    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)
    kwargs.setdefault("name", data)
    super(Cifar10_1Config, self).__init__(**kwargs)
    self.data = data


class Cifar10_1(tfds.core.GeneratorBasedBuilder):  # pylint: disable=invalid-name
  """Cifar-10.1 dataset."""

  BUILDER_CONFIGS = [
      Cifar10_1Config(
          description=(
              "It is the first version of our dataset on which we tested any classifier. As mentioned above, this "
              "makes the v4 dataset independent of the classifiers we evaluate. The numbers reported in the main "
              "sections of our paper use this version of the dataset. It was built from the top 25 TinyImages "
              "keywords for each class, which led to a slight class imbalance. The largest difference is that ships "
              "make up only 8% of the test set instead of 10%. v4 contains 2,021 images."
          ),
          version=tfds.core.Version("1.0.0"),
          data="v4",
      ),
      Cifar10_1Config(
          description=(
              "It is derived from a slightly improved keyword allocation that is exactly class balanced. This version "
              "of the dataset corresponds to the results in Appendix D of our paper. v6 contains 2,000 images."
          ),
          version=tfds.core.Version("1.0.0"),
          data="v6",
      )
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(32, 32, 3)),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/modestyachts/CIFAR-10.1",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    image_url = _DL_URL_IMAGES.format(self.builder_config.data)
    label_url = _DL_URL_LABELS.format(self.builder_config.name)

    image_path, label_path = dl_manager.download([
        image_url,
        label_url,
    ])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "image_path": image_path,
                "label_path": label_path,
            }),
    ]

  def _generate_examples(self, image_path, label_path):
    with tf.io.gfile.GFile(image_path, "rb") as f:
      images = np.load(f)
    with tf.io.gfile.GFile(label_path, "rb") as f:
      labels = np.load(f)
    for i, (image, label) in enumerate(zip(images, labels)):
      record = {
          "image": image,
          "label": label,
      }
      yield i, record
