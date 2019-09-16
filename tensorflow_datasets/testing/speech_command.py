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

r"""Generate fake data for ade20k dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import zipfile

from absl import app
from absl import flags

from tensorflow_datasets.core.utils import py_utils
import os
import numpy as np
import tensorflow as tf

flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "speech_command")

def generate_audio_file(filename):
  with tf.io.gfile.GFile(filename, "wb") as f:
    f.write(np.random.uniform(-1,1, size=(16000)).tobytes())
    f.write(np.random.randint(35, dtype=np.int).tobytes())
    f.write(b'0a2b400e')

def main(_):
  generate_audio_file(os.path.join(_output_dir(), 'generated_example'))



if __name__ == '__main__':
  app.run(main)