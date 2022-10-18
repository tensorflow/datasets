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

"""The Paraphrase Adversaries from Word Scrambling(PAWS) dataset."""

import csv
import os
from typing import Dict

from etils import epath
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
_LABELED_FINAL = "labeled_final"  # default subset
_LABELED_SWAP = "labeled_swap"
_UNLABELED_FINAL = "unlabeled_final"
_RAW_MAPPING = "raw_and_mapping"
_DOWNLOAD_URLS = {
    _LABELED_FINAL:
        "https://storage.googleapis.com/paws/english/paws_wiki_labeled_final.tar.gz",
    _LABELED_SWAP:
        "https://storage.googleapis.com/paws/english/paws_wiki_labeled_swap.tar.gz",
    _UNLABELED_FINAL:
        "https://storage.googleapis.com/paws/english/paws_wiki_unlabeled_final.tar.gz",
    _RAW_MAPPING:
        "https://storage.googleapis.com/paws/english/wiki_raw_and_mapping.tar.gz",
}
_EXTRACTED_FOLDERS = {
    _LABELED_FINAL: "final",
    _LABELED_SWAP: "swap",
    _UNLABELED_FINAL: "unlabeled/final",
}
_SUBSET_SPLITS = {
    _LABELED_FINAL: ["train", "dev", "test"],
    _LABELED_SWAP: ["train"],
    _UNLABELED_FINAL: ["train", "dev"],
}
_SPLIT_MAPPINGS = {
    "train": tfds.Split.TRAIN,
    "dev": tfds.Split.VALIDATION,
    "test": tfds.Split.TEST,
}

_CLASS_LABELS = ["different_meaning", "paraphrase"]


class PawsWikiConfig(tfds.core.BuilderConfig):
  """Configuration Class for PAWS Wiki."""

  def __init__(self, tokenized: bool = True, subset: str = "", **kwargs):
    super().__init__(
        name=f"{subset}_{'tokenized' if tokenized else 'raw'}",
        description=f"Subset: {subset} tokenized: {tokenized}",
        **kwargs)
    self.subset = subset
    self.tokenized = tokenized


class PawsWiki(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for paraphrase identification."""
  VERSION = tfds.core.Version("1.1.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial version.",
      "1.1.0": "Adds configs to different subset and support raw text.",
  }
  BUILDER_CONFIGS = [
      PawsWikiConfig(  # pylint: disable=g-complex-comprehension
          subset=subset,
          tokenized=tokenized,
      ) for tokenized, subset in [
          (True, _LABELED_FINAL),
          (False, _LABELED_FINAL),
          (True, _LABELED_SWAP),
          (False, _LABELED_SWAP),
          (True, _UNLABELED_FINAL),
      ]
  ]

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
    dl_paths = dl_manager.download_and_extract(_DOWNLOAD_URLS)
    subset = self.builder_config.subset
    labels_path = os.path.join(dl_paths[subset], _EXTRACTED_FOLDERS[subset])

    if self.builder_config.tokenized:
      mappings_path = ""
      tags2texts = {}
    else:
      mapping_base_dir = os.path.join(dl_paths[_RAW_MAPPING],
                                      "wiki_raw_and_mapping")
      mappings_path = os.path.join(mapping_base_dir, f"{subset}_mapping")
      swap_path = os.path.join(mapping_base_dir, "input_swap_wiki_50k.tsv")
      backtransl_path = os.path.join(mapping_base_dir,
                                     "input_backtransl_wiki_with_swap_id.tsv")
      tags2texts = {}
      with epath.Path(swap_path).open() as f:
        reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        # tsv file format: id  sentence1  sentence2
        for row in reader:
          tags2texts[f"{row['id']}_1"] = row["sentence1"]
          tags2texts[f"{row['id']}_2"] = row["sentence2"]

      with epath.Path(backtransl_path).open() as f:
        reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        # tsv file format: id  sentence1  sentence2  swap_id
        for row in reader:
          tags2texts[f"{row['id']}_2"] = row["sentence2"]

    return [  # pylint: disable=g-complex-comprehension
        tfds.core.SplitGenerator(
            name=_SPLIT_MAPPINGS[split],
            gen_kwargs={
                "labels_path": os.path.join(labels_path, f"{split}.tsv"),
                "mappings_path": os.path.join(mappings_path, f"{split}.tsv"),
                "tags2texts": tags2texts,
            },
        ) for split in _SUBSET_SPLITS[subset]
    ]

  def _generate_examples(
      self,
      labels_path: str,
      mappings_path: str,
      tags2texts: Dict[str, str],
  ):
    """Yeilds Examples.

    Args:
      labels_path: The file path for ids, tokenized texts and labels.
      mappings_path: The file path for ids and mapping tags.
      tags2texts: The dictionary of mapping tags to raw texts.

    Yields:
      Generator yielding the next examples
    """
    if tags2texts:
      # uses mapping tags to create dataset with raw texts.
      with epath.Path(labels_path).open() as f:
        # tsv file format: id  sentence1  sentence2  label
        labels = list(csv.DictReader(f, delimiter="\t"))
      with epath.Path(mappings_path).open() as f:
        # tsv file format: id  mapping1  mapping2
        tags = list(csv.DictReader(f, delimiter="\t"))
      if len(labels) != len(tags):
        raise ValueError("Expect same number of labels and mapping tags. "
                         f"Got {len(labels)} vs {len(tags)} instead.")
      for label_ex, tag_ex in zip(labels, tags):
        if label_ex["id"] != tag_ex["id"]:
          raise ValueError(
              "Expect matched id as key from labels file and mappings file. "
              f"Got {label_ex['id']} vs {tag_ex['id']} instead.")
        key = label_ex["id"]
        example = {
            "sentence1": tags2texts[tag_ex["mapping1"]],
            "sentence2": tags2texts[tag_ex["mapping2"]],
            "label": int(label_ex["label"]),
        }
        yield key, example
    else:
      # creates dataset with tokenized texts.
      with epath.Path(labels_path).open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        # tsv file format: id  sentence1  sentence2 label
        for row in reader:
          key = row["id"]
          label_str = "noisy_label" if self.builder_config.subset == _UNLABELED_FINAL else "label"
          example = {
              "sentence1": row["sentence1"],
              "sentence2": row["sentence2"],
              "label": int(row[label_str]),
          }
          yield key, example
