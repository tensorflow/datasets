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

r"""Generate gtzan music speech data.

"""

import os

from absl import app
from absl import flags
import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

# In TF 2.0, eager execution is enabled by default
tf.compat.v1.disable_eager_execution()

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, "audio", "gtzan_music_speech",
                      "dummy_data")


def _generate_data():
  """Generate data examples."""
  wav_file = fake_data_utils.get_random_wav_c1(duration=1, sample=22050)
  filepath = os.path.join(_output_dir(), "music_speech", "speech_wav",
                          "{}.wav".format("test"))
  dirname = os.path.dirname(filepath)
  if not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  tf.io.gfile.copy(wav_file, filepath, overwrite=True)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_data()


if __name__ == "__main__":
  app.run(main)
