# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Summarizing abstract from covid19 publications."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, Iterator, List, Optional, Text, Tuple

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {CORD-19-research-challenge,
    author = "An AI challenge with AI2, CZI, MSR, Georgetown, NIH & The White House",
    title  = "COVID-19 Open Research Dataset Challenge (CORD-19)",
    month  = "april",
    year   = "2020",
    url    = "https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge"
}
"""

_HOMEPAGE = (
    "https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge"
)

_DESCRIPTION = """
CORD-19 is a resource of over 45,000 scholarly articles, including over 33,000
with full text, about COVID-19, SARS-CoV-2, and related coronaviruses.

To help organizing information in scientific literatures of COVID-19 through
abstractive summarization. This dataset parse those articles to pairs of
document and summaries of full_text-abstract or introduction-abstract.

Features includes strings of: abstract, full_text, sha (hash of pdf),
source_x (source of publication), title, doi (digital object identifier),
license, authors, publish_time, journal, url.
"""

_ABSTRACT = "abstract"
_BODY_TEXT = "body_text"
_SECTION = "section"
_TEXT = "text"
_SHA = "sha"
_ADDITIONAL_FEATURES = [
    _SHA,
    "source_x",
    "title",
    "doi",
    "license",
    "authors",
    "publish_time",
    "journal",
    "url",
]
_ALL_COLUMNS = [
    "cord_uid",
    "sha",
    "source_x",
    "title",
    "doi",
    "pmcid",
    "pubmed_id",
    "license",
    "abstract",
    "publish_time",
    "authors",
    "journal",
    "Microsoft Academic Paper ID",
    "WHO #Covidence",
    "has_full_text",
    "full_text_file",
    "url",
]


class Covid19sum(tfds.core.GeneratorBasedBuilder):
  """Covid19sum Dataset."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
    This dataset need to be manually downloaded through kaggle api:
    `kaggle datasets download allen-institute-for-ai/CORD-19-research-challenge`
    Place the downloaded zip file in the manual folder.
    """

  VERSION = tfds.core.Version("1.0.0")

  def _info(self) -> tfds.core.DatasetInfo:
    features = {k: tf.string for k in _ADDITIONAL_FEATURES + [_ABSTRACT]}
    features[_BODY_TEXT] = tfds.features.Sequence(
        tfds.features.FeaturesDict({_SECTION: np.str_, _TEXT: np.str_})
    )
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=(_BODY_TEXT, _ABSTRACT),
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    extracted_path = dl_manager.extract(
        os.path.join(dl_manager.manual_dir, "CORD-19-research-challenge.zip")
    )
    pd = tfds.core.lazy_imports.pandas
    df = pd.read_csv(
        os.path.join(extracted_path, "metadata.csv"),
        header=0,
        names=_ALL_COLUMNS,
    ).fillna("")
    data_paths = []
    for _, row in df.iterrows():
      file_dir = row["full_text_file"]
      if row["has_full_text"] and _has_abstract(row) and file_dir:
        d = {k: row[k] for k in _ADDITIONAL_FEATURES + [_ABSTRACT]}
        d["path"] = os.path.join(
            extracted_path, file_dir, file_dir, row[_SHA] + ".json"
        )
        data_paths.append(d)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"data_paths": data_paths},
        )
    ]

  def _generate_examples(
      self, data_paths: Optional[List[Dict[Text, Any]]] = None
  ) -> Iterator[Tuple[Any, Dict[Text, Any]]]:
    """Yields examples."""
    for d in data_paths:
      path = d.pop("path")
      if tf.io.gfile.exists(path):
        with tf.io.gfile.GFile(path, "rb") as f:
          data_dict = json.load(f)
          body_text = data_dict.get(_BODY_TEXT, [])
          if body_text:
            d[_BODY_TEXT] = [
                {k: s[k] for k in [_SECTION, _TEXT]} for s in body_text
            ]
            yield d[_SHA], d


def _has_abstract(example: Dict[Text, Any]) -> bool:
  abstract = example[_ABSTRACT]
  return abstract and abstract.lower() != "unknown"
