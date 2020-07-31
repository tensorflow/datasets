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

"""Commonsense Explanations (CoS-E) Dataset."""

import json
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Nie2019AdversarialNA,
    title = "Adversarial NLI: A New Benchmark for Natural Language Understanding",
    author = "Nie, Yixin and
      Williams, Adina and
      Dinan, Emily  and
      Bansal, Mohit and
      Weston, Jason and
      Kiela, Douwe",
      year="2019",
    url ="https://arxiv.org/abs/1910.14599"
}
"""

_DESCRIPTION = """
Adversarial NLI (ANLI) is a large-scale NLI benchmark dataset, collected via an
iterative, adversarial human-and-model-in-the-loop procedure.
"""

_ANLI_URL = "https://dl.fbaipublicfiles.com/anli/anli_v0.1.zip"

EXTRACT_PATH_TOKEN = "anli_v0.1"

VERSION = tfds.core.Version("0.1.0")


class AnliConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Anli."""

  def __init__(self, *, round_dir=None, **kwargs):
    """BuilderConfig for Anli.

    Args:
      round_dir: str. The directory for the Anli round to read.
      **kwargs: keyword arguments forwarded to super.
    """
    super(AnliConfig, self).__init__(
        version=VERSION,
        **kwargs)
    self.round_dir = round_dir


class Anli(tfds.core.GeneratorBasedBuilder):
  """ANLI: Adversarial NLI corpus."""

  BUILDER_CONFIGS = [
      AnliConfig(
          name="r1",
          description="Round One",
          round_dir="R1",
      ),
      AnliConfig(
          name="r2",
          description="Round Two",
          round_dir="R2",
      ),
      AnliConfig(
          name="r3",
          description="Round Three",
          round_dir="R3",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "uid": tfds.features.Text(),
            "context": tfds.features.Text(),
            "hypothesis": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=["e", "n", "c"]),
        }),
        supervised_keys=None,
        homepage="https://github.com/facebookresearch/anli",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    dl_dir = dl_manager.download_and_extract(_ANLI_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepath": os.path.join(
                    dl_dir, EXTRACT_PATH_TOKEN, self._builder_config.round_dir,
                    "test.jsonl")
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": os.path.join(
                dl_dir, EXTRACT_PATH_TOKEN, self._builder_config.round_dir,
                "dev.jsonl")}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": os.path.join(
                    dl_dir, EXTRACT_PATH_TOKEN, self._builder_config.round_dir,
                    "train.jsonl")
            })
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with tf.io.gfile.GFile(filepath) as f:
      for line in f:
        element = json.loads(line)
        yield element["uid"], {
            "uid": element["uid"],
            "context": element["context"],
            "hypothesis": element["hypothesis"],
            "label": element["label"],
        }
