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

"""The Multilingual Paraphrase Adversaries from Word Scrambling(PAWS) dataset."""

import csv
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_HOMEPAGE_URL = (
    "https://github.com/google-research-datasets/paws/tree/master/pawsx"
)
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


class Builder(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for multilingual paraphrase identification."""

  BUILDER_CONFIGS = [
      PawsXWikiConfig(  # pylint: disable=g-complex-comprehension
          name=l,
          description="Translated to " + l,
          version="1.0.0",
          language=l,
      )
      for l in _LANGUAGES
  ]

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "sentence1": tfds.features.Text(),
            "sentence2": tfds.features.Text(),
            # Label 0: Pair has different meaning, Label 1: Pair is a paraphrase
            "label": tfds.features.ClassLabel(names=_CLASS_LABELS),
        }),
        homepage=_HOMEPAGE_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract({"x-final": _DOWNLOAD_URL})
    # Name of the extracted folder is "x-final"
    base_path = os.path.join(dl_path["x-final"], "x-final")

    # Name of file for training for 'en' is different from other languages
    if self.builder_config.language == "en":
      training_path = os.path.join(
          base_path, self.builder_config.language, "train.tsv"
      )
    else:
      training_path = os.path.join(
          base_path, self.builder_config.language, "translated_train.tsv"
      )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": training_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": os.path.join(
                    base_path, self.builder_config.language, "test_2k.tsv"
                )
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "path": os.path.join(
                    base_path, self.builder_config.language, "dev_2k.tsv"
                )
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
    with epath.Path(path).open() as f:
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
