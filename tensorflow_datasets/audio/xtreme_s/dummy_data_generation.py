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

r"""Generate XTREME-S audio test data.

This does not create the TSV files.

"""

import os

from absl import app
from absl import flags
import tensorflow as tf
from tensorflow_datasets.core import utils
from tensorflow_datasets.testing import fake_data_utils

# In TF 2.0, eager execution is enabled by default
tf.compat.v1.disable_eager_execution()

_TFDS_DIR = flags.DEFINE_string("tfds_dir", str(utils.tfds_write_path()),
                                "Path to tensorflow_datasets directory")


def _output_dir():
  return os.path.join(_TFDS_DIR.value, "audio", "xtreme_s", "dummy_data",
                      "fleurs")


def _filepath(language: str, split: str, wav_name: str) -> str:
  return os.path.join(_output_dir(), language, "audio", split,
                      f"{wav_name}.wav")


def _make_wav_file(filepath: str):
  wav_file = fake_data_utils.get_random_wav_c1(duration=2, sample=16000)
  dirname = os.path.dirname(filepath)
  if not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  tf.io.gfile.copy(wav_file, filepath, overwrite=True)


def _generate_data():
  """Generate data examples."""

  # Several examples for Afrikaans.
  language = "af_za"
  for wav_name in ["train_1", "train_2", "train_3"]:
    filepath = _filepath(language=language, split="train", wav_name=wav_name)
    _make_wav_file(filepath)

  for wav_name in ["dev_1"]:
    filepath = _filepath(language=language, split="dev", wav_name=wav_name)
    _make_wav_file(filepath)

  for wav_name in ["test_1", "test_2"]:
    filepath = _filepath(language=language, split="test", wav_name=wav_name)
    _make_wav_file(filepath)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_data()


if __name__ == "__main__":
  app.run(main)
