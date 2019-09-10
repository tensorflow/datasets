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
from tensorflow_datasets.testing import fake_data_utils
import os

flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data', 'fake_examples',
                      'ade20k', 'ADEChallengeData2016',
                      '{data}', '{split}', '{filename}')


def main(argv):
  del argv
  out = _output_dir()
  for split in ('training', 'validation'):
    jpg = fake_data_utils.get_random_jpeg(height=2, width=2)
    png = fake_data_utils.get_random_png(height=2, width=2, channels=1)
    example_id = 'fake_{}'.format(split)
    os.rename(jpg, out.format(
        data='images', split=split, filename='{}.jpg'.format(example_id)))
    os.rename(
        png, out.format(
        data='annotations', split=split, filename='{}.png'.format(example_id)))



if __name__ == '__main__':
  app.run(main)
