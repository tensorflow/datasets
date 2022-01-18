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

"""Test dataset builder without TFDV."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets as tfds

tf.compat.v1.enable_eager_execution()


class BuilderNoStatsTest(tfds.testing.TestCase):

  def test_no_tfdv_dir(self):
    with tfds.testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = tfds.testing.DummyMnist(data_dir=tmp_dir)
      builder.download_and_prepare()  # tfdv not present. Statistics skipped.

      # Statistics skipped
      num_examples = int(builder.info.splits['train'].statistics.num_examples)
      self.assertEqual(num_examples, 0)


if __name__ == '__main__':
  tfds.testing.test_main()
