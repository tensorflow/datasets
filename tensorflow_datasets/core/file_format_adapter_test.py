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

"""Tests for tensorflow_datasets.core.file_format_adapter."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import utils

tf.compat.v1.enable_eager_execution()


class DummyTFRecordBuilder(dataset_builder.GeneratorBasedBuilder):

  VERSION = utils.Version("0.0.0")

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
      yield {
          "x": i,
          "y": np.array([-i]).astype(np.int64)[0],
          "z": tf.compat.as_text(str(i))
      }

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
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


class FileFormatAdapterTest(testing.TestCase):

  def _test_generator_based_builder(self, builder_cls):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
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


class TFRecordUtilsTest(testing.TestCase):

  def test_dicts_to_sequence_example(self):
    context_dict = {
        "a": 1,
        "a2": np.array(1),
        "b": ["foo", "bar"],
    }
    sequence_dict = {
        "w": [["foo"], ["foo", "bar"]],
        "x": [1, 2, 3],
        "y": np.array([2., 3., 4., 5.]),
        "z": [[1, 2], [3, 4, 5]],
    }
    seq_ex = file_format_adapter._dicts_to_tf_sequence_example(
        context_dict, sequence_dict)
    context = seq_ex.context.feature
    self.assertEqual([1], list(context["a"].int64_list.value))
    self.assertEqual([1], list(context["a2"].int64_list.value))
    self.assertEqual([b"foo", b"bar"], list(context["b"].bytes_list.value))
    seq = seq_ex.feature_lists.feature_list
    self.assertEqual(
        [[b"foo"], [b"foo", b"bar"]],
        [list(el.bytes_list.value) for el in seq["w"].feature])
    self.assertEqual(
        [[el] for el in [1, 2, 3]],
        [list(el.int64_list.value) for el in seq["x"].feature])
    self.assertAllClose(
        [[el] for el in [2., 3., 4., 5.]],
        [list(el.float_list.value) for el in seq["y"].feature])
    self.assertEqual(
        [[1, 2], [3, 4, 5]],
        [list(el.int64_list.value) for el in seq["z"].feature])

  def test_dict_to_example(self):
    example = file_format_adapter._dict_to_tf_example({
        "a": 1,
        "a2": np.array(1),
        "b": ["foo", "bar"],
        "b2": np.array(["foo", "bar"]),
        "c": [2.0],
        "c2": np.array([2.0]),
        # Empty values supported when type is defined
        "d": np.array([], dtype=np.int32),
        # Support for byte strings
        "e": np.zeros(2, dtype=np.uint8).tobytes(),
        "e2": [np.zeros(2, dtype=np.uint8).tobytes()] * 2,
    })
    feature = example.features.feature
    self.assertEqual([1], list(feature["a"].int64_list.value))
    self.assertEqual([1], list(feature["a2"].int64_list.value))
    self.assertEqual([b"foo", b"bar"], list(feature["b"].bytes_list.value))
    self.assertEqual([b"foo", b"bar"], list(feature["b2"].bytes_list.value))
    self.assertEqual([2.0], list(feature["c"].float_list.value))
    self.assertEqual([2.0], list(feature["c2"].float_list.value))
    self.assertEqual([], list(feature["d"].int64_list.value))
    self.assertEqual([b"\x00\x00"], list(feature["e"].bytes_list.value))
    self.assertEqual([b"\x00\x00", b"\x00\x00"],
                     list(feature["e2"].bytes_list.value))

    with self.assertRaisesWithPredicateMatch(ValueError, "received an empty"):
      # Raise error if an undefined empty value is given
      file_format_adapter._dict_to_tf_example({
          "empty": [],
      })

    with self.assertRaisesWithPredicateMatch(ValueError, "not support type"):
      # Raise error if an unsupported dtype is given
      file_format_adapter._dict_to_tf_example({
          "wrong_type": np.zeros(shape=(5,), dtype=np.complex64),
      })


if __name__ == "__main__":
  testing.test_main()
