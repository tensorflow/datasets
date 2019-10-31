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

"""BIGPATENT Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import json
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{sharma2019bigpatent,
    title={BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization},
    author={Eva Sharma and Chen Li and Lu Wang},
    year={2019},
    eprint={1906.03741},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

_DESCRIPTION = """
BIGPATENT, consisting of 1.3 million records of U.S. patent documents
along with human written abstractive summaries.
Each US patent application is filed under a Cooperative Patent Classification
(CPC) code. There are nine such classification categories:
A (Human Necessities), B (Performing Operations; Transporting),
C (Chemistry; Metallurgy), D (Textiles; Paper), E (Fixed Constructions),
F (Mechanical Engineering; Lightning; Heating; Weapons; Blasting),
G (Physics), H (Electricity), and
Y (General tagging of new or cross-sectional technology)

There are two features:
  - description: detailed description of patent.
  - summary: Patent abastract.

"""

_URL = "https://drive.google.com/uc?export=download&id=1J3mucMFTWrgAYa3LuBZoLRR3CzzYD3fa"

_DOCUMENT = "description"
_SUMMARY = "abstract"

_CPC_DESCRIPTION = {
    "a": "Human Necessities",
    "b": "Performing Operations; Transporting",
    "c": "Chemistry; Metallurgy",
    "d": "Textiles; Paper",
    "e": "Fixed Constructions",
    "f": "Mechanical Engineering; Lightning; Heating; Weapons; Blasting",
    "g": "Physics",
    "h": "Electricity",
    "y": "General tagging of new or cross-sectional technology"
}


class BigPatentConfig(tfds.core.BuilderConfig):
  """BuilderConfig for BigPatent."""

  @tfds.core.disallow_positional_args
  def __init__(self, cpc_codes=None, **kwargs):
    """BuilderConfig for Wikihow.

    Args:
      cpc_codes: str, cpc_codes
      **kwargs: keyword arguments forwarded to super.
    """
    super(BigPatentConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs)
    self.cpc_codes = cpc_codes


class BigPatent(tfds.core.GeneratorBasedBuilder):
  """BigPatent datasets."""

  BUILDER_CONFIGS = [
      BigPatentConfig(
          cpc_codes=list(_CPC_DESCRIPTION),
          name="all",
          description="Patents under all categories."),
  ] + [
      BigPatentConfig(  # pylint:disable=g-complex-comprehension
          cpc_codes=[k],
          name=k,
          description=("Patents under Cooperative Patent Classification (CPC)"
                       "{0}: {1}".format(k, v)),
      ) for k, v in sorted(_CPC_DESCRIPTION.items())
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text()
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://evasharma.github.io/bigpatent/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    split_types = ["train", "val", "test"]
    extract_paths = dl_manager.extract({
        k: os.path.join(dl_path, "bigPatentData", k + ".tar.gz")
        for k in split_types
    })
    extract_paths = {k: os.path.join(extract_paths[k], k) for k in split_types}

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": extract_paths["train"]},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": extract_paths["val"]},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": extract_paths["test"]},
        ),
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    for cpc_code in self.builder_config.cpc_codes:
      filenames = tf.io.gfile.glob(os.path.join(path, cpc_code, "*"))
      for filename in filenames:
        with tf.io.gfile.GFile(filename, "rb") as fin:
          fin = gzip.GzipFile(fileobj=fin)
          for row in fin:
            json_obj = json.loads(row)
            yield json_obj["publication_number"], {
                _DOCUMENT: json_obj[_DOCUMENT],
                _SUMMARY: json_obj[_SUMMARY]
            }
