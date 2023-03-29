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

"""NEWSROOM Dataset."""

import json
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DOCUMENT = "text"
_SUMMARY = "summary"
_ADDITIONAL_TEXT_FEATURES = [
    "title",
    "url",
    "date",
    "density_bin",
    "coverage_bin",
    "compression_bin",
]
_ADDITIONAL_FLOAT_FEATURES = [
    "density",
    "coverage",
    "compression",
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """NEWSROOM Dataset."""

  VERSION = tfds.core.Version("1.0.0")
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You should download the dataset from https://summari.es/download/
  The webpage requires registration.
  After downloading, please put dev.jsonl, test.jsonl and train.jsonl
  files in the manual_dir.
  """

  def _info(self):
    features = {
        k: tfds.features.Text()
        for k in [_DOCUMENT, _SUMMARY] + _ADDITIONAL_TEXT_FEATURES
    }
    features.update(
        {
            k: tfds.features.Tensor(shape=[], dtype=np.float32)
            for k in _ADDITIONAL_FLOAT_FEATURES
        }
    )
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(features),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://summari.es",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "input_file": os.path.join(dl_manager.manual_dir, "train.jsonl")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "input_file": os.path.join(dl_manager.manual_dir, "dev.jsonl")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "input_file": os.path.join(dl_manager.manual_dir, "test.jsonl")
            },
        ),
    ]

  def _generate_examples(self, input_file=None):
    """Yields examples."""
    with epath.Path(input_file).open() as f:
      for i, line in enumerate(f):
        d = json.loads(line)
        # fields are "url", "archive", "title", "date", "text",
        #  "compression_bin", "density_bin", "summary", "density",
        #  "compression', "coverage", "coverage_bin",
        yield i, {
            k: d[k]
            for k in [_DOCUMENT, _SUMMARY]
            + _ADDITIONAL_TEXT_FEATURES
            + _ADDITIONAL_FLOAT_FEATURES
        }
