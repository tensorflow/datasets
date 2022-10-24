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

r"""Generate yesno data.

"""

import os
import random

from absl import app
from absl import flags
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

NUMBER_OF_EXAMPLES = 1


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, "audio", "yesno", "dummy_data")


def _get_file_name():
  """Returns file name of audio file."""
  # Example of audio file name: 0_0_1_1_0_1_0_0.wav
  file_name = str(random.randint(0, 1))
  for _ in range(7):  # Range is 7 as the first label is added on initialization
    file_name += "_"
    file_name += str(random.randint(0, 1))
  return file_name


def _generate_data():
  """Generate data examples."""
  for _ in range(NUMBER_OF_EXAMPLES):
    wav_file = fake_data_utils.get_random_wav_c1(duration=6, sample=8000)
    filename = _get_file_name()
    filepath = os.path.join(_output_dir(), "waves_yesno",
                            "{}.wav".format(filename))
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
