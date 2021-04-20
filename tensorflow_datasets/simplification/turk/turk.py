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

"""Turk dataset for tuning and evaluating text simplification models focused on lexical paraphrasing."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
 @article{Xu-EtAl:2016:TACL,
 author = {Wei Xu and Courtney Napoles and Ellie Pavlick and Quanze Chen and Chris Callison-Burch},
 title = {Optimizing Statistical Machine Translation for Text Simplification},
 journal = {Transactions of the Association for Computational Linguistics},
 volume = {4},
 year = {2016},
 url = {https://cocoxu.github.io/publications/tacl2016-smt-simplification.pdf},
 pages = {401--415}
 }
}
"""

_DESCRIPTION = """\
TURK is a dataset for evaluating sentence simplification systems that focus on lexical paraphrasing,
as described in "Optimizing Statistical Machine Translation for Text Simplification". The corpus is composed 
of 2000 validation and 359 test original sentences that were each simplified 8 times by different annotators.
"""

_HOMEPAGE = "https://github.com/cocoxu/simplification"

_LICENSE = "GNU General Public License v3.0"

_URL_LIST = [
  (
    "test.8turkers.tok.norm",
    "https://raw.githubusercontent.com/cocoxu/simplification/master/data/turkcorpus/test.8turkers.tok.norm",
  ),
  (
    "tune.8turkers.tok.norm",
    "https://raw.githubusercontent.com/cocoxu/simplification/master/data/turkcorpus/tune.8turkers.tok.norm",
  ),
]
_URL_LIST += [
  (
    f"{spl}.8turkers.tok.turk.{i}",
    f"https://raw.githubusercontent.com/cocoxu/simplification/master/data/turkcorpus/{spl}.8turkers.tok.turk.{i}",
  )
  for spl in ["tune", "test"]
  for i in range(8)
]

_URLs = dict(_URL_LIST)


class Turk(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Turk dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
    "1.0.0": "Initial release.",
  }

  BUILDER_CONFIGS = [
    tfds.core.BuilderConfig(
      name="simplification",
      version=VERSION,
      description="A set of sentences with 8 human simplifications for each.",
    )
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = tfds.features.FeaturesDict(
      {
        "original": tfds.features.Text(),
        "simplifications": tfds.features.Sequence(tfds.features.Text()),
      }
    )
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=features,
      supervised_keys=None,
      homepage=_HOMEPAGE,
      citation=_CITATION,
    )


  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(_URLs)
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.VALIDATION,
        gen_kwargs={"filepaths": data_dir, "split": "valid"},
      ),
      tfds.core.SplitGenerator(
        name=tfds.Split.TEST,
        gen_kwargs={"filepaths": data_dir, "split": "test"},
      ),
    ]


  def _generate_examples(self, filepaths, split):
    """Yields examples."""
    if split == "valid":
      split = "tune"
    files = [tf.io.gfile.GFile(filepaths[f"{split}.8turkers.tok.norm"])] + [
      tf.io.gfile.GFile(filepaths[f"{split}.8turkers.tok.turk.{i}"])
      for i in range(8)
    ]
    for id_, lines in enumerate(zip(*files)):
      yield id_, {
        "original": lines[0].strip(),
        "simplifications": [line.strip() for line in lines[1:]],
      }
