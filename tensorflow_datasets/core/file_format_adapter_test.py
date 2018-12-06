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

"""Tests for tensorflow_datasets.core.file_format_adapter."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import test_utils

tf.enable_eager_execution()


class DummyTFRecordBuilder(dataset_builder.GeneratorBasedDatasetBuilder):

  def _split_generators(self, dl_manager):
    return [
        splits.SplitGenerator(
            name=[splits.Split.TRAIN, splits.Split.VALIDATION],
            num_shards=[2, 1],
            gen_kwargs={"range_": range(30)}),
        splits.SplitGenerator(
            name=splits.Split.TEST,
            num_shards=1,
            gen_kwargs={"range_": range(30, 40)}),
    ]

  def _generate_examples(self, range_):
    for i in range_:
      yield self.info.features.encode_example({
          "x": i,
          "y": np.array([-i]).astype(np.int64)[0],
          "z": tf.compat.as_text(str(i))
      })

  def _info(self):
    return dataset_info.DatasetInfo(
        features=features.FeaturesDict({
            "x": tf.int64,
            "y": tf.int64,
            "z": tf.string,
        }),
    )


class DummyCSVBuilder(DummyTFRecordBuilder):

  @property
  def _file_format_adapter(self):
    file_adapter_cls = file_format_adapter.CSVAdapter
    serialized_info = self.info.features.get_serialized_info()
    return file_adapter_cls(serialized_info)


class FileFormatAdapterTest(tf.test.TestCase):

  def _test_generator_based_builder(self, builder_cls):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = builder_cls(data_dir=tmp_dir)
      builder.download_and_prepare()
      train_dataset = builder.as_dataset(split=splits.Split.TRAIN)
      valid_dataset = builder.as_dataset(split=splits.Split.VALIDATION)
      test_dataset = builder.as_dataset(split=splits.Split.TEST)

      def validate_dataset(dataset, min_val, max_val, test_range=False):
        els = []
        for el in dataset:
          x, y, z = el["x"].numpy(), el["y"].numpy(), el["z"].numpy()
          self.assertEqual(-x, y)
          self.assertEqual(x, int(z))
          self.assertGreaterEqual(x, min_val)
          self.assertLess(x, max_val)
          els.append(x)
        if test_range:
          self.assertEqual(list(range(min_val, max_val)), sorted(els))

      validate_dataset(train_dataset, 0, 30)
      validate_dataset(valid_dataset, 0, 30)
      validate_dataset(test_dataset, 30, 40, True)

  def test_tfrecords(self):
    self._test_generator_based_builder(DummyTFRecordBuilder)

  def test_csv(self):
    self._test_generator_based_builder(DummyCSVBuilder)


class TFRecordUtilsTest(tf.test.TestCase):

  def test_dict_to_example(self):
    example = file_format_adapter._dict_to_tf_example({
        "a": 1,
        "b": ["foo", "bar"],
        "c": [2.0],
    })
    feature = example.features.feature
    self.assertEqual([1], list(feature["a"].int64_list.value))
    self.assertEqual([b"foo", b"bar"], list(feature["b"].bytes_list.value))
    self.assertEqual([2.0], list(feature["c"].float_list.value))


if __name__ == "__main__":
  tf.test.main()
