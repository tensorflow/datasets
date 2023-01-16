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

"""BillSum Dataset."""

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_URL = "https://drive.google.com/uc?export=download&id=1g89WgFHMRbr4QrvA0ngh26PY081Nv3lx"

_DOCUMENT = "text"
_SUMMARY = "summary"


class Builder(tfds.core.GeneratorBasedBuilder):
  """BillSum Dataset."""

  # 2.0.0 data source updated to filter near duplicates.
  # 3.0.0  none of the test examples are 'near duplicates' of an example in the
  #   train set AND they dont have the same title, regardless of similarity.
  VERSION = tfds.core.Version("3.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text(),
            "title": tfds.features.Text(),
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/FiscalNote/BillSum",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": os.path.join(
                    dl_path, "us_train_data_final_OFFICIAL.jsonl"
                ),
                "key": "bill_id",
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": os.path.join(
                    dl_path, "us_test_data_final_OFFICIAL.jsonl"
                ),
                "key": "bill_id",
            },
        ),
        tfds.core.SplitGenerator(
            name="ca_test",
            gen_kwargs={
                "path": os.path.join(
                    dl_path, "ca_test_data_final_OFFICIAL.jsonl"
                ),
                "key": "external_id",
            },
        ),
    ]

  def _generate_examples(self, path=None, key=None):
    """Yields examples."""
    with epath.Path(path).open() as f:
      for line in f:
        # in us bills, json has fields:
        #   text, summary, title, bill_id, text_len, sum_len
        # in ca bills, json has fields:
        #   text, summary, title, external_id
        d = json.loads(line)
        yield d[key], {k: d[k] for k in [_DOCUMENT, _SUMMARY, "title"]}
