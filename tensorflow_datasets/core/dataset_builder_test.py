# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.dataset_builder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import test_utils

tf.enable_eager_execution()


def dummy_data_generator():
  for i in range(30):
    yield {"x": i}


class DummyDatasetSharedGenerator(dataset_builder.GeneratorBasedDatasetBuilder):

  @property
  def splits(self):
    return [
        self._split_files(split=dataset_builder.Split.TRAIN, num_shards=2),
        self._split_files(split=dataset_builder.Split.TEST, num_shards=1),
    ]

  def _dataset_split_generators(self):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    return [dataset_builder.SplitGenerator(generator_fn=dummy_data_generator,
                                           split_files=self.splits)]

  @property
  def _file_format_adapter(self):
    example_spec = {
        "x": tf.FixedLenFeature(tuple(), tf.int64),
    }
    return file_format_adapter.TFRecordExampleAdapter(example_spec)


class DatasetBuilderTest(tf.test.TestCase):

  def test_shared_generator(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()

      written_filepaths = [
          os.path.join(tmp_dir, fname)
          for fname in tf.gfile.ListDirectory(tmp_dir)
      ]
      expected_filepaths = []
      for split in builder.splits:
        expected_filepaths.extend(split.filepaths)
      self.assertEqual(sorted(expected_filepaths), sorted(written_filepaths))

      splits = [
          dataset_builder.Split.TRAIN, dataset_builder.Split.TEST
      ]
      datasets = [builder.as_dataset(split=split) for split in splits]
      data = [[el["x"].numpy() for el in dataset] for dataset in datasets]

      train_data, test_data = data
      self.assertEqual(20, len(train_data))
      self.assertEqual(10, len(test_data))
      self.assertEqual(list(range(30)), sorted(train_data + test_data))

  def test_load(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      dataset = registered.load(
          name="dummy_dataset_shared_generator",
          data_dir=tmp_dir,
          download=True,
          split=dataset_builder.Split.TRAIN)
      data = list(dataset)
      self.assertEqual(20, len(data))

  def test_numpy_iterator(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()
      items = []
      for item in builder.numpy_iterator(split=dataset_builder.Split.TRAIN):
        items.append(item)
      self.assertEqual(20, len(items))


if __name__ == "__main__":
  tf.test.main()
