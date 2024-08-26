# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Tests for beam_utils."""

import os
import pathlib
from typing import Optional

import pytest
from tensorflow_datasets.core import beam_utils
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils


@pytest.mark.parametrize(
    'split, workers_per_shard, expected_result',
    [
        ('train', 1, "{'id': 0}\n{'id': 1}\n{'id': 2}\n"),
        ('train', 2, "{'id': 0}\n{'id': 1}\n{'id': 2}\n"),
        ('train', 100, "{'id': 0}\n{'id': 1}\n{'id': 2}\n"),
        ('train[:2]', 1, "{'id': 0}\n{'id': 1}\n"),
        ('train[1:]', 1, "{'id': 1}\n{'id': 2}\n"),
    ],
)
def test_read_from_tfds(
    dummy_dataset: dataset_builder.DatasetBuilder,
    tmp_path: pathlib.Path,
    split: str,
    workers_per_shard: Optional[int],
    expected_result: str,
):
  import apache_beam as beam  # pylint: disable=g-import-not-at-top

  with beam.Pipeline() as pipeline:
    _ = (
        pipeline
        | beam_utils.ReadFromTFDS(
            dummy_dataset, split=split, workers_per_shard=workers_per_shard
        )
        | beam.Map(dataset_utils.as_numpy)
        # Post numpy2, we don't get `{'id': 0}` but
        # `{'id': np.int64(0)}`
        | beam.Map(lambda x: {'id': int(x['id'])})
        | beam.io.WriteToText(os.fspath(tmp_path / 'out.txt'))
    )

  assert (tmp_path / 'out.txt-00000-of-00001').read_text() == expected_result


@pytest.mark.parametrize(
    'split, expected_implemented_with_batchsize',
    [
        ('train', True),
        ('train[:2]', False),
        ('train[1:]', False),
    ],
)
def test_subsplit_failure_with_batch_size(
    dummy_dataset: dataset_builder.DatasetBuilder,
    tmp_path: pathlib.Path,
    split,
    expected_implemented_with_batchsize,
):
  implemented_with_batchsize = True
  try:
    import apache_beam as beam  # pylint: disable=g-import-not-at-top

    with beam.Pipeline() as pipeline:
      _ = (
          pipeline
          | beam_utils.ReadFromTFDS(dummy_dataset, split=split, batch_size=2)
          | beam.Map(dataset_utils.as_numpy)
          | beam.io.WriteToText(os.fspath(tmp_path / 'out.txt'))
      )

  except NotImplementedError:
    implemented_with_batchsize = False
  assert implemented_with_batchsize == expected_implemented_with_batchsize
