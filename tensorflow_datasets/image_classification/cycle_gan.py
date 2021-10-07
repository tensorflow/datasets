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

"""CycleGAN dataset."""

import os

import tensorflow as tf

import tensorflow_datasets.public_api as tfds

# From https://arxiv.org/abs/1703.10593
_CITATION = """\
@article{DBLP:journals/corr/ZhuPIE17,
  author    = {Jun{-}Yan Zhu and
               Taesung Park and
               Phillip Isola and
               Alexei A. Efros},
  title     = {Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial
               Networks},
  journal   = {CoRR},
  volume    = {abs/1703.10593},
  year      = {2017},
  url       = {http://arxiv.org/abs/1703.10593},
  archivePrefix = {arXiv},
  eprint    = {1703.10593},
  timestamp = {Mon, 13 Aug 2018 16:48:06 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuPIE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DL_URL = "https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/"

# "ae_photos" : Not added because trainA and trainB are missing.
_DATA_OPTIONS = [
    "apple2orange", "summer2winter_yosemite", "horse2zebra", "monet2photo",
    "cezanne2photo", "ukiyoe2photo", "vangogh2photo", "maps", "cityscapes",
    "facades", "iphone2dslr_flower"
]

_DL_URLS = {name: _DL_URL + name + ".zip" for name in _DATA_OPTIONS}


class CycleGANConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CycleGAN."""

  def __init__(self, *, data=None, **kwargs):
    """Constructs a CycleGANConfig.

    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    super(CycleGANConfig, self).__init__(**kwargs)
    self.data = data


class CycleGAN(tfds.core.GeneratorBasedBuilder):
  """CycleGAN dataset."""

  BUILDER_CONFIGS = [
      CycleGANConfig(  # pylint: disable=g-complex-comprehension
          name=config_name,
          version=tfds.core.Version("2.0.0"),
          release_notes={
              "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
          },
          data=config_name,
      ) for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A dataset consisting of images from two classes A and "
        "B (For example: horses/zebras, apple/orange,...)",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=["A", "B"]),
        }),
        supervised_keys=("image", "label"),
        homepage="https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    url = _DL_URLS[self.builder_config.name]
    data_dirs = dl_manager.download_and_extract(url)

    path_to_dataset = os.path.join(data_dirs, tf.io.gfile.listdir(data_dirs)[0])

    train_a_path = os.path.join(path_to_dataset, "trainA")
    train_b_path = os.path.join(path_to_dataset, "trainB")
    test_a_path = os.path.join(path_to_dataset, "testA")
    test_b_path = os.path.join(path_to_dataset, "testB")

    return [
        tfds.core.SplitGenerator(
            name="trainA", gen_kwargs={
                "path": train_a_path,
                "label": "A",
            }),
        tfds.core.SplitGenerator(
            name="trainB", gen_kwargs={
                "path": train_b_path,
                "label": "B",
            }),
        tfds.core.SplitGenerator(
            name="testA", gen_kwargs={
                "path": test_a_path,
                "label": "A",
            }),
        tfds.core.SplitGenerator(
            name="testB", gen_kwargs={
                "path": test_b_path,
                "label": "B",
            }),
    ]

  def _generate_examples(self, path, label):
    images = tf.io.gfile.listdir(path)

    for image in images:
      record = {
          "image": os.path.join(path, image),
          "label": label,
      }
      yield image, record
