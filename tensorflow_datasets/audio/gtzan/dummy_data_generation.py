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

r"""Generate gtzan data.

"""

import os
import random

from absl import app
from absl import flags
from tensorflow_datasets.audio.gtzan import gtzan
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, "audio", "gtzan", "dummy_data")


def _generate_data():
  """Generate data examples."""
  # pylint: disable=protected-access
  labels = tfds.features.ClassLabel(names=gtzan._CLASS_LABELS).names  # pytype: disable=module-attr
  # pylint: enable=protected-access
  wav_file = fake_data_utils.get_random_wav_c1(duration=30, sample=22050)
  # .wav file has name in the format of <genre>.<number>.wav
  label = random.choice(labels)
  random_number_for_filename = random.randint(0, 99)
  filename = "{}.{:05d}".format(label, random_number_for_filename)
  filepath = os.path.join(_output_dir(), "genres", label,
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
