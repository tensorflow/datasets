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

"""Tests for tensorflow_datasets.core.split_builder."""

import os
import pathlib

import apache_beam as beam
from tensorflow_datasets import testing
from tensorflow_datasets.core import split_builder as split_builder_lib


def _inc_placeholder_counter(x):
  beam.metrics.Metrics.counter('some_namespace', 'some_counter').inc()
  return x


def test_beam(tmp_path: pathlib.Path):
  """Test that `maybe_beam_pipeline` behave as `beam.Pipeline()`."""
  builder = testing.DummyMnist()
  split_builder = split_builder_lib.SplitBuilder(
      split_dict=builder.info.splits,
      features=builder.info.features,
      beam_options=None,
      beam_runner=None,
      max_examples_per_split=None,
  )

  path = tmp_path / 'out.txt'
  with split_builder.maybe_beam_pipeline() as pipeline_proxy:
    ptransform = (
        beam.Create(range(9))
        | beam.Map(lambda x: x * 10)
        | beam.Map(_inc_placeholder_counter)
        | beam.io.WriteToText(os.fspath(path), shard_name_template=''))
    _ = split_builder.beam_pipeline | ptransform
  result = pipeline_proxy.result
  # counters = metrics.get_metrics(result, 'some_namespace').counters
  mfilter = beam.metrics.MetricsFilter().with_namespaces(['some_namespace'])
  all_metrics = result.metrics().query(mfilter)
  counters = all_metrics['counters']
  assert counters[0].key.metric.name == 'some_counter'
  assert counters[0].committed == 9
  assert path.read_text() == '\n'.join(str(x * 10) for x in range(9)) + '\n'
