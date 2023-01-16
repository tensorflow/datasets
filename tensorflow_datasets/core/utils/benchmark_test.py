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

"""Tests for tensorflow_datasets.core.utils.benchmark."""

import pytest

import tensorflow as tf
from tensorflow_datasets.core.utils import benchmark


@pytest.mark.parametrize(
    'ds, num_iter, batch_size, expected_num_examples',
    [
        (tf.data.Dataset.range(10), 10, 1, 10),
        (tf.data.Dataset.range(10), 5, 1, 5),
        (tf.data.Dataset.range(10), 10, 2, 20),
        (range(10), 10, 1, 10),
        (range(10), 10, 2, 20),
    ],
)
def test_raw_benchmark(ds, num_iter, batch_size, expected_num_examples):
  result = benchmark.raw_benchmark(ds, num_iter=num_iter, batch_size=batch_size)
  assert isinstance(result, benchmark.RawBenchmarkResult)
  assert result.num_examples == expected_num_examples
  assert result.end_time > result.start_time
  assert result.end_time >= result.first_batch_time


def test_benchmark():
  # Works with tf.data.Dataset
  ds = tf.data.Dataset.range(10)
  result = benchmark.benchmark(ds)
  assert isinstance(result, benchmark.BenchmarkResult)

  # Works with other iterators
  result = benchmark.benchmark(range(10))
  assert isinstance(result, benchmark.BenchmarkResult)


def test_benchmark_empty():
  # len() == 0
  with pytest.raises(ValueError, match='Cannot benchmark dataset with 0 elem'):
    benchmark.benchmark([])

  # len() == 1
  result = benchmark.benchmark([1])
  assert isinstance(result, benchmark.BenchmarkResult)
