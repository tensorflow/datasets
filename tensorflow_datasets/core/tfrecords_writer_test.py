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

"""Tests for tensorflow_datasets.core.tfrecords_writer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl.testing import absltest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import tfrecords_writer


class GetNumberShardsTest(testing.TestCase):

  def test_imagenet_train(self):
    size = 137<<30  # 137 GiB
    num_examples = 1281167
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 1024)

  def test_imagenet_evaluation(self):
    size = 6300 * (1<<20)  # 6.3 GiB
    num_examples = 50000
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 64)

  def test_verylarge_few_examples(self):
    size = 52<<30  # 52 GiB
    num_examples = 512
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 512)

  def test_xxl(self):
    size = 10<<40  # 10 TiB
    num_examples = 10**9  # 1G
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 11264)

  def test_xs(self):
    size = 100<<20  # 100 MiB
    num_examples = 100 * 10**3  # 100K
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 1)

  def test_m(self):
    size = 400<<20  # 499 MiB
    num_examples = 200 * 10**3  # 200K
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 4)


def _read_records(path):
  """Returns (files_names, list_of_records_in_each_file)."""
  fnames = sorted(tf.io.gfile.listdir(path))
  all_recs = []
  for fname in fnames:
    fpath = os.path.join(path, fname)
    recs = list(dataset_utils.as_numpy(tf.data.TFRecordDataset(fpath)))
    all_recs.append(recs)
  return fnames, all_recs


class WriterTest(testing.TestCase):

  @absltest.mock.patch.object(
      example_serializer, 'ExampleSerializer', testing.DummySerializer)
  def test_write(self):
    """Writes 8 records in 5 shards.

    Number of records is evenly distributed (2-1-2-1-2).
    """
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    writer = tfrecords_writer.Writer('some spec', path)
    to_write = [
        (1, b'a'), (2, b'b'),
        (3, b'c'),
        (4, b'd'), (5, b'e'),
        (6, b'f'),
        (7, b'g'), (8, b'h'),
    ]
    for key, record in to_write:
      writer.write(key, record)
    with absltest.mock.patch.object(tfrecords_writer, '_get_number_shards',
                                    return_value=5):
      shards_length = writer.finalize()
    self.assertEqual(shards_length, [2, 1, 2, 1, 2])
    written_files, all_recs = _read_records(self.tmp_dir)
    self.assertEqual(written_files,
                     ['foo.tfrecord-0000%s-of-00005' % i for i in range(5)])
    self.assertEqual(all_recs, [
        [b'f', b'c'], [b'a'], [b'd', b'g'], [b'h'], [b'b', b'e'],
    ])

if __name__ == '__main__':
  testing.test_main()
