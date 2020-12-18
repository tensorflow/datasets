# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

r"""Generate kaokore data.

"""

import os

from absl import app
from absl import flags

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils
import tensorflow.compat.v2 as tf

tf.compat.v1.disable_eager_execution()

flags.DEFINE_string(
  'tfds_dir', py_utils.tfds_dir(), 'Path to tensorflow_datasets directory'
)
flags.DEFINE_integer('num', 4, 'Number of images to generate')

FLAGS = flags.FLAGS
_IMAGE_SIZE = 256


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, 'dummy_data')


def _generate_jpeg(example_id):
  jpeg = fake_data_utils.get_random_jpeg(height=_IMAGE_SIZE, width=_IMAGE_SIZE)
  filepath = os.path.join(_output_dir(), '{:08d}.jpg'.format(example_id))
  dirname = os.path.dirname(filepath)
  if not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  tf.io.gfile.copy(jpeg, filepath, overwrite=True)


def main():
  for i in range(FLAGS.num):
    _generate_jpeg(i)


if __name__ == '__main__':
  app.run(main)
