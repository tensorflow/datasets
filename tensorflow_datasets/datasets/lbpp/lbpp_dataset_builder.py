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

# Copyright 2024 Cohere and the current dataset script contributor.
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
# Author Note: Data loader is heavily inspired by the builder in
# https://github.com/google-research/google-research/tree/main/lbpp_dataset
"""Cohere Less Basic Python Problems. All columns decoded."""

import base64
import json
import pickle
import zlib

from tensorflow_datasets.core.utils.lazy_imports_utils import pandas as pd
import tensorflow_datasets.public_api as tfds


_HOMEPAGE = "https://aclanthology.org/2024.findings-emnlp.772/"

_VERSION = tfds.core.Version("2.0.0")

_COLUMNS = [
    "task_id",
    "language",
    "title",
    "instruction",
    "completion",
    "test_file",
    "test_list",
    "signature",
    "categories",
    "test_setup",
]

_LANGUAGES = ["python", "cpp", "go", "java", "js", "rust"]
_ALL_LANGUAGE_ALIASES = ["all", "multilingual"]
_LANGUAGE_ALIAS_MAP = {
    "default": "python",
    "javascript": "js",
}


def decode_str(str_to_decode: str):
  return json.loads(
      pickle.loads(
          zlib.decompress(base64.b64decode(str_to_decode.encode("utf-8")))
      )
  )


class LBPPConfig(tfds.core.BuilderConfig):
  """BuilderConfig."""

  def __init__(self, name, description, features, **kwargs):
    super(LBPPConfig, self).__init__(name=name, version=_VERSION, **kwargs)
    self.name = name
    self.description = description
    self.features = features


class Builder(tfds.core.GeneratorBasedBuilder):
  """Builder for LBPP dataset."""

  VERSION = _VERSION
  LICENSE = "apache-2.0"
  BUILDER_CONFIGS = [
      LBPPConfig(
          name="all", description="Multilingual LBPP", features=_COLUMNS
      ),
      LBPPConfig(
          name="multilingual",
          description="Multilingual LBPP",
          features=_COLUMNS,
      ),
      LBPPConfig(name="default", description="Python LBPP", features=_COLUMNS),
      LBPPConfig(name="python", description="Python LBPP", features=_COLUMNS),
      LBPPConfig(name="cpp", description="C++ LBPP", features=_COLUMNS),
      LBPPConfig(name="go", description="Go LBPP", features=_COLUMNS),
      LBPPConfig(name="java", description="Java LBPP", features=_COLUMNS),
      LBPPConfig(name="js", description="JavaScript LBPP", features=_COLUMNS),
      LBPPConfig(
          name="javascript", description="JavaScript LBPP", features=_COLUMNS
      ),
      LBPPConfig(name="rust", description="JavaScript LBPP", features=_COLUMNS),
  ]
  DEFAULT_CONFIG_NAME = "python"

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "task_id": tfds.features.Text(),
            "language": tfds.features.Text(),
            "title": tfds.features.Text(),
            "instruction": tfds.features.Text(),
            "completion": tfds.features.Text(),
            "test_file": tfds.features.Text(),
            "test_list": tfds.features.Sequence(tfds.features.Text()),
            "signature": tfds.features.Text(),
            "categories": tfds.features.Sequence(tfds.features.Text()),
            "test_setup": tfds.features.Text(),
        }),
        homepage=_HOMEPAGE,
        supervised_keys=None,
    )

  def _split_generators(self, dl_manager):
    # Map alias to actual language
    data_loading_name = _LANGUAGE_ALIAS_MAP.get(
        self.builder_config.name, self.builder_config.name
    )
    hf_url_prefix = (
        "https://huggingface.co/datasets/CohereForAI/lbpp/resolve/main/"
    )
    if data_loading_name in _ALL_LANGUAGE_ALIASES:
      # Download all languages
      download_targets = [
          f"{hf_url_prefix}{lang}/test.parquet" for lang in _LANGUAGES
      ]
    else:
      download_targets = [f"{hf_url_prefix}{data_loading_name}/test.parquet"]

    downloaded_files = dl_manager.download(download_targets)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepaths": downloaded_files,
            },
        )
    ]

  def _generate_examples(self, filepaths: list[str]):
    key = 0
    for filepath in filepaths:
      df = pd.read_parquet(filepath)
      for line in df.to_dict(orient="records"):
        yield key, {
            "task_id": line["task_id"],
            "language": line["language"],
            "title": line["title"],
            "instruction": line["instruction"],
            "completion": decode_str(line["completion"]),
            "test_file": decode_str(line["test_file"]),
            "test_list": decode_str(line["test_list"]),
            "signature": line["signature"] or "",
            "categories": line["categories"],
            "test_setup": decode_str(line["test_setup"]),
        }
        key += 1
