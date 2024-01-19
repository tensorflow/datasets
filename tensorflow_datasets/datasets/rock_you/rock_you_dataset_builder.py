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

"""The rockyou dataset."""

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"


class Builder(tfds.core.GeneratorBasedBuilder):
  """This dataset contains passwords that were leaked or stolen from from various sites."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {
                "password": tfds.features.Text(),
            }
        ),
        supervised_keys=None,
        homepage="https://wiki.skullsecurity.org/Passwords",
    )

  def _split_generators(self, dl_manager):
    dl_path = dl_manager.download(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name="train",
            gen_kwargs={
                "path": dl_path,
            },
        )
    ]

  def _generate_examples(self, path):
    with tf.io.gfile.GFile(path, "rb") as f:
      blines = f.readlines()

    for i, bline in enumerate(blines):
      yield i, {
          "password": bline.strip(),
      }
