# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
  with split_builder.maybe_beam_pipeline():
    ptransform = (
        beam.Create(range(9))
        | beam.Map(lambda x: x * 10)
        | beam.io.WriteToText(os.fspath(path), shard_name_template='')
    )
    _ = split_builder.beam_pipeline | ptransform

  assert path.read_text() == '\n'.join(str(x * 10) for x in range(9)) + '\n'
