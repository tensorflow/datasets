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

"""The Paraphrase Adversaries from Word Scrambling(PAWS) dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@InProceedings{paws2019naacl,
  title = {{PAWS: Paraphrase Adversaries from Word Scrambling}},
  author = {Zhang, Yuan and Baldridge, Jason and He, Luheng},
  booktitle = {Proc. of NAACL},
  year = {2019}
}
"""

_DESCRIPTION = """Existing paraphrase identification datasets lack sentence pairs
that have high lexical overlap without being paraphrases.
Models trained on such data fail to distinguish pairs like flights
from New York to Florida and flights from Florida to New York.
This dataset contains 108,463 human-labeled and 656k noisily labeled pairs
that feature the importance of modeling structure, context, and word order information
for the problem of paraphrase identification.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries from Word Scrambling
at https://arxiv.org/abs/1904.01130

This corpus contains pairs generated from Wikipedia pages,
containing pairs that are generated from both word swapping and back translation methods.
All pairs have human judgements on both paraphrasing and fluency
and they are split into Train/Dev/Test sections.

All files are in the tsv format with four columns:

id	A unique id for each pair
sentence1	The first sentence
sentence2	The second sentence
(noisy_)label	(Noisy) label for each pair

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.
"""

_HOMEPAGE_URL = "https://github.com/google-research-datasets/paws"
_DOWNLOAD_URL = "https://storage.googleapis.com/paws/english/paws_wiki_labeled_final.tar.gz"

_CLASS_LABELS = ["different_meaning", "paraphrase"]


class PawsWiki(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for paraphrase identification."""

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
    dl_path = dl_manager.download_and_extract({"paws_wiki": _DOWNLOAD_URL})
    # Name of the extracted folder is "final"
    base_path = os.path.join(dl_path["paws_wiki"], "final")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(base_path, "train.tsv")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(base_path, "test.tsv")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": os.path.join(base_path, "dev.tsv")},
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
        key = row["id"]
        example = {
            "sentence1": row["sentence1"],
            "sentence2": row["sentence2"],
            "label": int(row["label"]),
        }
        yield key, example
