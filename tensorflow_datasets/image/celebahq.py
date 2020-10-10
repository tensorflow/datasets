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

"""Celeba-HQ dataset."""

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{DBLP:journals/corr/abs-1710-10196,
  author    = {Tero Karras and
               Timo Aila and
               Samuli Laine and
               Jaakko Lehtinen},
  title     = {Progressive Growing of GANs for Improved Quality, Stability, and Variation},
  journal   = {CoRR},
  volume    = {abs/1710.10196},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.10196},
  archivePrefix = {arXiv},
  eprint    = {1710.10196},
  timestamp = {Mon, 13 Aug 2018 16:46:42 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10196},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """\
High-quality version of the CELEBA
dataset, consisting of 30000 images in 1024 x 1024 resolution.

Note: CelebAHQ dataset may contain potential bias. The fairness indicators
[example](https://github.com/tensorflow/fairness-indicators/blob/master/fairness_indicators/documentation/examples/Fairness_Indicators_TFCO_CelebA_Case_Study.ipynb)
goes into detail about several considerations to keep in mind while using the
CelebAHQ dataset.

WARNING: This dataset currently requires you to prepare images on your own.
"""


class CelebaHQConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CelebaHQ."""

  def __init__(self, *, resolution, **kwargs):
    """BuilderConfig for SQUAD.

    Args:
      resolution: Resolution of the image. Values supported: powers of 2 up to
        1024.
      **kwargs: keyword arguments forwarded to super.
    """
    v2 = tfds.core.Version("2.0.0")
    super(CelebaHQConfig, self).__init__(
        name="%d" % resolution,
        description=("CelebaHQ images in %d x %d resolution" %
                     (resolution, resolution)),
        version=v2,
        release_notes={
            "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
        },
        **kwargs)
    self.resolution = resolution
    self.file_name = "data%dx%d.tar" % (resolution, resolution)


class CelebAHq(tfds.core.GeneratorBasedBuilder):
  """Celeba_HQ Dataset."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain multiple tar files with images (data2x2.tar,
  data4x4.tar .. data1024x1024.tar).
  Detailed instructions are here:
  https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training
  """

  BUILDER_CONFIGS = [
      CelebaHQConfig(resolution=1024),
      CelebaHQConfig(resolution=512),
      CelebaHQConfig(resolution=256),
      CelebaHQConfig(resolution=128),
      CelebaHQConfig(resolution=64),
      CelebaHQConfig(resolution=32),
      CelebaHQConfig(resolution=16),
      CelebaHQConfig(resolution=8),
      CelebaHQConfig(resolution=4),
      CelebaHQConfig(resolution=2),
      CelebaHQConfig(resolution=1),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(self.builder_config.resolution,
                           self.builder_config.resolution, 3),
                    encoding_format="png"),
            "image/filename":
                tfds.features.Text(),
        },),
        homepage="https://github.com/tkarras/progressive_growing_of_gans",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    image_tar_file = os.path.join(dl_manager.manual_dir,
                                  self.builder_config.file_name)
    if not tf.io.gfile.exists(image_tar_file):
      # The current celebahq generation code depends on a concrete version of
      # pillow library and cannot be easily ported into tfds.
      msg = "You must download the dataset files manually and place them in: "
      msg += dl_manager.manual_dir
      msg += " as .tar files. See testing/test_data/fake_examples/celeb_a_hq "
      raise AssertionError(msg)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"archive": dl_manager.iter_archive(image_tar_file)},
        )
    ]

  def _generate_examples(self, archive):
    for fname, fobj in archive:
      record = {"image": fobj, "image/filename": fname}
      yield fname, record
