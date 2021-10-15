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

"""gov_report dataset."""

import itertools
import json
import os
from typing import Any, Dict, Iterable, Tuple

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Government report dataset consists of reports written by government research
 agencies including Congressional Research Service and U.S. Government
 Accountability Office.
"""

_CITATION = """
@inproceedings{
anonymous2022efficiently,
title={Efficiently Modeling Long Sequences with Structured State Spaces},
author={Anonymous},
booktitle={Submitted to The Tenth International Conference on Learning Representations },
year={2022},
url={https://openreview.net/forum?id=uYLFoz1vlAC},
note={under review}
}
"""

_HOMEPAGE = "https://gov-report-data.github.io/"
_URL = "https://drive.google.com/uc?export=download&id=1ik8uUVeIU-ky63vlnvxtfN2ZN-TUeov2"

_SUBSET_CRS = "crs"
_SUBSET_GAO = "gao"

_ID_KEY = "id"
_COMMON_KEYS = ("title", "released_date")
_CRS_KEYS = ("reports", "summary")
_GAO_KEYS = ("report", "highlight")
_GAO_ADDITIONAL_KEYS = ("url", "fastfact", "published_date")

_STYLE_DESCRIPTIONS = {
    "whitespace": "Structures flattened and joined by whitespace. "
                  "This is the format used by original paper",
    "html":
        "Structures flattened and joined by newline while add html tags. "
        "Tags are only added for secition_title in a format like <h2>xxx<h2>.",
    "json": "Structures represented as raw json.",
}


class GovReportConfig(tfds.core.BuilderConfig):
  """BuilderConfig for GovReportConfig."""

  def __init__(self,
               subset: str = "",
               style: str = "",
               supervised_keys: Tuple[str, str] = ("", ""),
               other_keys: Iterable[str] = (),
               description: str = "",
               **kwargs):
    super().__init__(
        name=f"{subset}_{style}",
        description=f"{description}\n{_STYLE_DESCRIPTIONS[style]}",
        **kwargs)
    self.subset = subset

    self.supervised_keys = supervised_keys
    self.other_keys = tuple(other_keys) + (_ID_KEY,)
    self.all_keys = supervised_keys + self.other_keys

    self.style = style
    self.separator = " " if style == "whitepsace" else "\n"


def _configs_for_style(style: str):
  return [
      GovReportConfig(
          subset=_SUBSET_CRS,
          style=style,
          description="CRS report with summary.",
          supervised_keys=_CRS_KEYS,
          other_keys=_COMMON_KEYS,
      ),
      GovReportConfig(
          subset=_SUBSET_GAO,
          style=style,
          description="GAO report with highlight",
          supervised_keys=_GAO_KEYS,
          other_keys=_COMMON_KEYS + _GAO_ADDITIONAL_KEYS,
      ),
  ]


class GovReport(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for gov_report dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }
  BUILDER_CONFIGS = list(
      itertools.chain.from_iterable(
          [_configs_for_style(style) for style in _STYLE_DESCRIPTIONS]))

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {k: tfds.features.Text() for k in self.builder_config.all_keys}),
        supervised_keys=self.builder_config.supervised_keys,
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)
    split_map = {
        tfds.Split.TRAIN: "train",
        tfds.Split.VALIDATION: "valid",
        tfds.Split.TEST: "test",
    }
    path = os.path.join(path, "gov-report")
    return {k: self._generate_examples(path, v) for k, v in split_map.items()}

  def _generate_examples(self, path: str, split: str):
    """Yields examples."""
    subset = self.builder_config.subset
    style = self.builder_config.style
    separator = self.builder_config.separator
    report_key, summary_key = self.builder_config.supervised_keys
    split_filename = os.path.join(path, "split_ids", f"{subset}_{split}.ids")
    with tf.io.gfile.GFile(split_filename) as f:
      for line in f:
        json_path = os.path.join(path, subset, f"{line.rstrip()}.json")
        with tf.io.gfile.GFile(json_path) as jf:
          d = json.load(jf)
          if style == "json":
            report = json.dumps(d[report_key])
          else:
            if subset == _SUBSET_CRS:
              report = _flatten_structure(d[report_key], separator, 1,
                                          style == "html")
            elif subset == _SUBSET_GAO:
              report = separator.join([
                  _flatten_structure(r, separator, 1, style == "html")
                  for r in d[report_key]
              ])
            else:
              raise ValueError("Unsupported subset.")

          if subset == _SUBSET_CRS:
            summary = separator.join(d[summary_key])
          elif subset == _SUBSET_GAO:
            summary = separator.join(
                sum([s["paragraphs"] for s in d[summary_key]], []))
          else:
            raise ValueError("Unsupported subset.")
          results = {report_key: report, summary_key: ""}
          results.update({
              k: separator.join(d[k]) if isinstance(d[k], list) else d[k]
              for k in self.builder_config.other_keys
          })
          yield d[_ID_KEY], results


def _flatten_structure(d: Dict[str, Any], separator: str, depth: int,
                       use_html: bool) -> str:
  """Recursively flatten the structure."""
  texts = []
  title = d["section_title"]
  if use_html:
    texts.append(f"<h{depth}>{title}</h{depth}>")
  else:
    texts.append(title)
  texts.extend(d["paragraphs"])
  texts.extend([
      _flatten_structure(s, separator, depth + 1, use_html)
      for s in d["subsections"]
  ])
  return separator.join(texts)
