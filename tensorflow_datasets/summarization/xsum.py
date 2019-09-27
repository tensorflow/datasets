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

"""XSum dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{Narayan2018DontGM,
  title={Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization},
  author={Shashi Narayan and Shay B. Cohen and Mirella Lapata},
  journal={ArXiv},
  year={2018},
  volume={abs/1808.08745}
}
"""

_DESCRIPTION = """
Extreme Summarization (XSum) Dataset.

There are two features:
  - document: Input news article.
  - summary: One sentence summary of the article.

This data need to manaully downloaded and processed as described in
https://github.com/EdinburghNLP/XSum/blob/master/XSum-Dataset/README.md.
The folder 'xsum-preprocessed' need to be put in manually downloaded folder.
"""

_URL = "https://raw.githubusercontent.com/EdinburghNLP/XSum/master/XSum-Dataset/XSum-TRAINING-DEV-TEST-SPLIT-90-5-5.json"

_DOCUMENT = "document"
_SUMMARY = "summary"


class Xsum(tfds.core.GeneratorBasedBuilder):
  """Extreme Summarization (XSum) Dataset."""

  # 2.0.0: use preprocessed (lowercased and noise reduction) instead of
  #        extracted data.
  VERSION = tfds.core.Version("2.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text(),
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        urls=["https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download(_URL)
    with tf.io.gfile.GFile(dl_path, "r") as json_file:
      split_ids = json.load(json_file)
    expected_counts = {k: len(v) for k, v in split_ids.items()}
    pattern = os.path.join(
        os.path.join(dl_manager.manual_dir, "xsum-preprocessed", "{0}",
                     "{1}.{0}"))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "document_path": pattern.format("document", "train"),
                "summary_path": pattern.format("summary", "train"),
                "expected_count": expected_counts["train"],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "document_path": pattern.format("document", "validation"),
                "summary_path": pattern.format("summary", "validation"),
                "expected_count": expected_counts["validation"],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "document_path": pattern.format("document", "test"),
                "summary_path": pattern.format("summary", "test"),
                "expected_count": expected_counts["test"],
            },
        ),
    ]

  def _generate_examples(self,
                         document_path=None,
                         summary_path=None,
                         expected_count=None):
    """Yields examples."""
    count = 0
    with tf.io.gfile.GFile(document_path) as document_f, tf.io.gfile.GFile(
        summary_path) as summary_f:
      for i, (document_line,
              summary_line) in enumerate(zip(document_f, summary_f)):
        count += 1
        yield i, {
            _DOCUMENT: document_line.strip(),
            _SUMMARY: summary_line.strip()
        }
    if count < expected_count:
      logging.warning("Actual count %d is less than expected count %d.", count,
                      expected_count)
