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

import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import test_utils

tf.enable_eager_execution()


class DummyTFRecordBuilder(dataset_builder.GeneratorBasedDatasetBuilder):

  def _dataset_split_generators(self):
    def zero_to_thirty():
      for i in range(30):
        yield {"x": i, "y": -i, "z": tf.compat.as_text(str(i))}

    def thirty_to_forty():
      for i in range(30, 40):
        yield {"x": i, "y": -i, "z": tf.compat.as_text(str(i))}

    zero_to_thirty_splits = [
        self._split_files(split=dataset_builder.Split.TRAIN, num_shards=2),
        self._split_files(split=dataset_builder.Split.VALIDATION, num_shards=1)
    ]
    thirty_to_forty_splits = [
        self._split_files(split=dataset_builder.Split.TEST, num_shards=1)
    ]
    return [
        dataset_builder.SplitGenerator(generator_fn=zero_to_thirty,
                                       split_files=zero_to_thirty_splits),
        dataset_builder.SplitGenerator(generator_fn=thirty_to_forty,
                                       split_files=thirty_to_forty_splits),
    ]

  @property
  def _file_format_adapter(self):
    example_spec = {
        "x": tf.FixedLenFeature(tuple(), tf.int64),
        "y": tf.FixedLenFeature(tuple(), tf.int64),
        "z": tf.FixedLenFeature(tuple(), tf.string),
    }
    return file_format_adapter.TFRecordExampleAdapter(example_spec)


class DummyCSVBuilder(DummyTFRecordBuilder):

  @property
  def _file_format_adapter(self):
    return file_format_adapter.CSVAdapter(
        feature_types={"x": tf.int32, "y": tf.int32, "z": tf.string})


class FileFormatAdapterTest(tf.test.TestCase):

  def _test_generator_based_builder(self, builder_cls):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = builder_cls(data_dir=tmp_dir)
      builder.download_and_prepare()
      train_dataset = builder.as_dataset(split=dataset_builder.Split.TRAIN)
      valid_dataset = builder.as_dataset(split=dataset_builder.Split.VALIDATION)
      test_dataset = builder.as_dataset(split=dataset_builder.Split.TEST)

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

  def setUp(self):
    self.example_dict = {"a": 1, "b": ["foo", "bar"], "c": [2.0]}

    def generator():
      for _ in range(3):
        yield self.example_dict

    self.generator = generator

  def test_dict_to_example(self):
    example = file_format_adapter._dict_to_tf_example(self.example_dict)
    feature = example.features.feature
    self.assertEqual([1], list(feature["a"].int64_list.value))
    self.assertEqual([b"foo", b"bar"], list(feature["b"].bytes_list.value))
    self.assertEqual([2.0], list(feature["c"].float_list.value))

  def test_convert_to_example_generator(self):
    wrapped = file_format_adapter._generate_tf_examples(self.generator())
    expected = file_format_adapter._dict_to_tf_example(self.example_dict)
    wrapped_examples = list(wrapped)
    self.assertEqual(3, len(wrapped_examples))
    for serialized_example in wrapped_examples:
      example = tf.train.Example()
      example.ParseFromString(serialized_example)
      self.assertEqual(expected, example)


if __name__ == "__main__":
  tf.test.main()
