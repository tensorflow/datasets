# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Downsampled Imagenet dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{DBLP:journals/corr/OordKK16,
  author    = {A{\"{a}}ron van den Oord and
               Nal Kalchbrenner and
               Koray Kavukcuoglu},
  title     = {Pixel Recurrent Neural Networks},
  journal   = {CoRR},
  volume    = {abs/1601.06759},
  year      = {2016},
  url       = {http://arxiv.org/abs/1601.06759},
  archivePrefix = {arXiv},
  eprint    = {1601.06759},
  timestamp = {Mon, 13 Aug 2018 16:46:29 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/OordKK16},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """\
Dataset with images of 2 resolutions (see config name for information on the resolution).
It is used for density estimation and generative modeling experiments.
"""

_DL_URL = "http://image-net.org/small/"

_DATA_OPTIONS = ["32x32", "64x64"]


class DownsampledImagenetConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Downsampled Imagenet."""

  @api_utils.disallow_positional_args
  def __init__(self, data=None, **kwargs):
    """Constructs a DownsampledImagenetConfig.

    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    super(DownsampledImagenetConfig, self).__init__(**kwargs)
    self.data = data


class DownsampledImagenet(tfds.core.GeneratorBasedBuilder):
  """Downsampled Imagenet dataset."""

  BUILDER_CONFIGS = [
      DownsampledImagenetConfig(  # pylint: disable=g-complex-comprehension
          name=config_name,
          description=(
              "A dataset consisting of Train and Validation images of " +
              config_name + " resolution."),
          version="1.0.0",
          supported_versions=[
              tfds.core.Version("1.0.0", experiments={
                  tfds.core.Experiment.S3: True}),
          ],
          data=config_name,
      ) for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
        }),
        supervised_keys=None,
        urls=["http://image-net.org/small/download.php"],
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    train_url = _DL_URL + "train_" + self.builder_config.name + ".tar"
    valid_url = _DL_URL + "valid_" + self.builder_config.name + ".tar"

    train_path, valid_path = dl_manager.download([
        train_url,
        valid_url,
    ])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                "archive": dl_manager.iter_archive(valid_path),
            }),
    ]

  def _generate_examples(self, archive):
    for fname, fobj in archive:
      record = {
          "image": fobj,
      }
      if self.version.implements(tfds.core.Experiment.S3):
        yield fname, record
      else:
        yield record
