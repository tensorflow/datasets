# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """@InProceedings{pawsx2019emnlp,
  title = {{PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification}},
  author = {Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},
  booktitle = {Proc. of EMNLP},
  year = {2019}
}"""

_DESCRIPTION = """
This dataset contains 23,659 human translated PAWS evaluation pairs and
296,406 machine translated training pairs in six typologically distinct languages:

* French
* Spanish
* German
* Chinese
* Japanese
* Korean

For further details, see the accompanying paper:
PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification
at  https://arxiv.org/abs/1908.11828

Similar to PAWS Dataset, examples are split into Train/Dev/Test sections.
All files are in the tsv format with four columns:

id	A unique id for each pair
sentence1	The first sentence
sentence2	The second sentence
(noisy_)label	(Noisy) label for each pair

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.
"""

_HOMEPAGE_URL = "https://github.com/google-research-datasets/paws/tree/master/pawsx"
_DOWNLOAD_URL = "https://storage.googleapis.com/paws/pawsx/x-final.tar.gz"

_CLASS_LABELS = ["different_meaning", "paraphrase"]

_LANGUAGES = ["de", "en", "es", "fr", "ja", "ko", "zh"]


class PawsXWikiConfig(tfds.core.BuilderConfig):
  """Configuration Class for PAWS - X Dataset."""

  def __init__(self, *, language, **kwargs):
    if language not in _LANGUAGES:
      raise ValueError("language must be one of {}".format(list(_LANGUAGES)))

    super(PawsXWikiConfig, self).__init__(**kwargs)
    self.language = language


class PawsXWiki(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for multilingual paraphrase identification."""
  BUILDER_CONFIGS = [
      PawsXWikiConfig(  # pylint: disable=g-complex-comprehension
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
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract({"x-final": _DOWNLOAD_URL})
    # Name of the extracted folder is "x-final"
    base_path = os.path.join(dl_path["x-final"], "x-final")

    # Name of file for training for 'en' is different from other languages
    if self.builder_config.language == "en":
      training_path = os.path.join(base_path, self.builder_config.language,
                                   "train.tsv")
    else:
      training_path = os.path.join(base_path, self.builder_config.language,
                                   "translated_train.tsv")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": training_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path":
                    os.path.join(base_path, self.builder_config.language,
                                 "test_2k.tsv")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "path":
                    os.path.join(base_path, self.builder_config.language,
                                 "dev_2k.tsv")
            },
        ),
    ]

  def _generate_examples(self, path):
    """Yeilds Examples.

    Args:
      path: The path of the file to be read for this split

    Yields:
      Generator yielding the next examples
    """
    with tf.io.gfile.GFile(path) as f:
      reader = csv.DictReader(f, delimiter="\t")
      # tsv file format: id  sentence1  sentence2 label
      for row in reader:
        # Some rows in the files have been wrongly populated
        if row["label"] in ("0", "1"):
          key = row["id"]
          example = {
              "sentence1": row["sentence1"],
              "sentence2": row["sentence2"],
              "label": int(row["label"]),
          }
          yield key, example
