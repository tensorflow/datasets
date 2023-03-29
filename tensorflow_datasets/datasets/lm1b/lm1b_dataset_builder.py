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

"""The Language Model 1 Billion dataset."""
import os

from absl import logging
from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = (
    "http://www.statmt.org/lm-benchmark/"
    "1-billion-word-language-modeling-benchmark-r13output.tar.gz"
)
_TOP_LEVEL_DIR = "1-billion-word-language-modeling-benchmark-r13output"
_TRAIN_FILE_FORMAT = os.path.join(
    _TOP_LEVEL_DIR, "training-monolingual.tokenized.shuffled", "news.en-*"
)
_HELDOUT_FILE_FORMAT = os.path.join(
    _TOP_LEVEL_DIR,
    "heldout-monolingual.tokenized.shuffled",
    "news.en.heldout-*",
)


def _train_data_filenames(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _TRAIN_FILE_FORMAT))


def _test_data_filenames(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _HELDOUT_FILE_FORMAT))


class Builder(tfds.core.GeneratorBasedBuilder):
  """1 Billion Word Language Model Benchmark dataset."""

  VERSION = tfds.core.Version("1.1.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {
                "text": tfds.features.Text(),
            }
        ),
        supervised_keys=("text", "text"),
        homepage="http://www.statmt.org/lm-benchmark/",
    )

  def _split_generators(self, dl_manager):
    lm1b_path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    train_files = _train_data_filenames(lm1b_path)
    test_files = _test_data_filenames(lm1b_path)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"files": train_files}
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, gen_kwargs={"files": test_files}
        ),
    ]

  def _generate_examples(self, files):
    for filepath in files:
      logging.info("generating examples from = %s", filepath)
      with epath.Path(filepath).open() as f:
        for idx, line in enumerate(f):
          yield "%s_%d" % (os.path.basename(filepath), idx), {
              "text": line.strip(),
          }
