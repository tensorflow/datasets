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

"""Tests for beam_utils."""

import os
import pathlib
import textwrap

from tensorflow_datasets.core import beam_utils
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils


def test_read_from_tfds(
    dummy_dataset: dataset_builder.DatasetBuilder,
    tmp_path: pathlib.Path,
):
  import apache_beam as beam  # pylint: disable=g-import-not-at-top

  with beam.Pipeline() as pipeline:
    _ = (
        pipeline
        | beam_utils.ReadFromTFDS(dummy_dataset, split='train')
        | beam.Map(dataset_utils.as_numpy)
        | beam.io.WriteToText(os.fspath(tmp_path / 'out.txt')))

  assert (tmp_path /
          'out.txt-00000-of-00001').read_text() == textwrap.dedent("""\
      {'id': 0}
      {'id': 1}
      {'id': 2}
      """)
