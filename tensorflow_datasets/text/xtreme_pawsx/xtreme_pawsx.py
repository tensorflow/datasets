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

"""The Multilingual Paraphrase Adversaries from Word Scrambling(PAWS) dataset."""

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{hu2020xtreme,
      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},
      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},
      journal   = {CoRR},
      volume    = {abs/2003.11080},
      year      = {2020},
      archivePrefix = {arXiv},
      eprint    = {2003.11080}
}"""

_DESCRIPTION = """
This dataset contains machine translations of the English PAWS training
data. The translations are provided by the XTREME benchmark and cover the following
languages:

* French
* Spanish
* German
* Chinese
* Japanese
* Korean

For further details on PAWS, see the  papers:
PAWS: Paraphrase Adversaries from Word Scrambling
at https://arxiv.org/abs/1904.01130
and
PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification
at  https://arxiv.org/abs/1908.11828

For details related to XTREME, please refer to:
XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization
at https://arxiv.org/abs/2003.11080
"""

_XTREME_TRANSLATIONS_FORMAT = "https://storage.googleapis.com/xtreme_translations/PAWSX/translate-train/en-{0}-translated.tsv"

_CLASS_LABELS = ["different_meaning", "paraphrase"]

_LANGUAGES = ["de", "es", "fr", "ja", "ko", "zh"]


class XtremePawsxConfig(tfds.core.BuilderConfig):
  """Configuration Class for PAWS - X Dataset."""

  def __init__(self, *, language, **kwargs):
    if language not in _LANGUAGES:
      raise ValueError("language must be one of {}".format(list(_LANGUAGES)))

    super(XtremePawsxConfig, self).__init__(**kwargs)
    self.language = language


class XtremePawsx(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for multilingual paraphrase identification."""
  BUILDER_CONFIGS = [
      XtremePawsxConfig(  # pylint: disable=g-complex-comprehension
          name=l,
          description="Translated to " + l,
          version="1.0.0",
          language=l,
      ) for l in _LANGUAGES
  ]

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "sentence1": tfds.features.Text(),
            "sentence2": tfds.features.Text(),
            # Label 0: Pair has different meaning, Label 1: Pair is a paraphrase
            "label": tfds.features.ClassLabel(names=_CLASS_LABELS),
        }),
        homepage="https://github.com/google-research/xtreme",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(
        _XTREME_TRANSLATIONS_FORMAT.format(self.builder_config.language))
    return {"train": self._generate_examples(dl_path)}

  def _generate_examples(self, path):
    """Yeilds Examples.

    Args:
      path: The path of the file to be read for this split

    Yields:
      Generator yielding the next examples
    """
    counter = 0
    with tf.io.gfile.GFile(path) as f:
      reader = csv.DictReader(
          f,
          delimiter="\t",
          fieldnames=[
              "en_sentence1", "en_sentence2", "sentence1", "sentence2", "label"
          ])

      # tsv file format: id  sentence1  sentence2 label
      for row in reader:
        # Some rows in the files have been wrongly populated
        if row["label"] in ("0", "1"):
          counter += 1
          example = {
              "sentence1": row["sentence1"],
              "sentence2": row["sentence2"],
              "label": int(row["label"]),
          }
          yield counter, example
