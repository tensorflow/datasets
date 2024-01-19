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

"""Tests for tensorflow_datasets.core.dataset_builder."""

import pathlib
from typing import Callable
from unittest import mock

import apache_beam as beam
from etils import epath
import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import utils


class DummyBeamDataset(dataset_builder.GeneratorBasedBuilder):
  VERSION = utils.Version('1.0.0')

  EXPECTED_METADATA = {
      'valid_1000': 1000,
      'valid_725': 725,
  }

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            'image': features.Image(shape=(16, 16, 1)),
            'label': features.ClassLabel(names=['dog', 'cat']),
            'id': tf.int32,
        }),
        supervised_keys=('x', 'x'),
        metadata=dataset_info.BeamMetadataDict(),
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {
        'train': self._generate_examples(num_examples=1000),
        'test': self._generate_examples(num_examples=725),
    }

  def _generate_examples(self, num_examples):
    """Generate examples as dicts."""
    examples = beam.Create(range(num_examples)) | beam.Map(_gen_example)

    # Can save int, str,... metadata but not `beam.PTransform`
    self.info.metadata[f'valid_{num_examples}'] = num_examples
    with pytest.raises(
        NotImplementedError, match="can't be used on `beam.PTransform`"
    ):
      self.info.metadata[f'invalid_{num_examples}'] = _compute_sum(examples)
    return examples


class CommonPipelineDummyBeamDataset(DummyBeamDataset):
  EXPECTED_METADATA = {
      'label_sum_1000': 500,
      'id_mean_1000': 499.5,
      'label_sum_725': 362,
      'id_mean_725': 362.0,
  }

  def _split_generators(self, dl_manager, pipeline):
    del dl_manager

    examples = pipeline | beam.Create(range(1000)) | beam.Map(_gen_example)

    # Wrap the pipeline inside a ptransform_fn to add `'label' >> ` to avoid
    # duplicated PTransform nodes names.
    generate_examples = beam.ptransform_fn(self._generate_examples)
    return {
        'train': examples | 'train' >> generate_examples(num_examples=1000),
        'test': examples | 'test' >> generate_examples(num_examples=725),
    }

  def _generate_examples(self, examples, num_examples):
    """Generate examples as dicts."""
    examples |= beam.Filter(lambda x: x[0] < num_examples)
    # Record metadata works for common PCollections
    self.info.metadata[f'id_mean_{num_examples}'] = _compute_mean(examples)
    self.info.metadata[f'label_sum_{num_examples}'] = _compute_sum(examples)
    return examples


def _gen_example(x):
  return (
      x,
      {
          'image': (np.ones((16, 16, 1)) * x % 255).astype(np.uint8),
          'label': x % 2,
          'id': x,
      },
  )


def _compute_sum(examples):
  return (
      examples | beam.Map(lambda x: x[1]['label']) | beam.CombineGlobally(sum)
  )


def _compute_mean(examples):
  return (
      examples
      | beam.Map(lambda x: x[1]['id'])
      | beam.CombineGlobally(beam.combiners.MeanCombineFn())
  )


def make_default_config():
  return download.DownloadConfig()


@pytest.mark.parametrize(
    'dataset_cls', [DummyBeamDataset, CommonPipelineDummyBeamDataset]
)
@pytest.mark.parametrize(
    'make_dl_config',
    [
        make_default_config,
    ],
)
def test_beam_datasets(
    tmp_path: pathlib.Path,
    dataset_cls: dataset_builder.GeneratorBasedBuilder,
    make_dl_config: Callable[[], download.DownloadConfig],
):
  dataset_name = dataset_cls.name

  builder = dataset_cls(data_dir=tmp_path)
  builder.download_and_prepare(download_config=make_dl_config())

  data_path = tmp_path / dataset_name / '1.0.0'
  assert data_path.exists()  # Dataset has been generated

  # Check number of shards/generated files
  _test_shards(
      data_path,
      pattern='%s-test.tfrecord-{:05}-of-{:05}' % dataset_name,
      # Liquid sharding is not guaranteed to always use the same number.
      num_shards=builder.info.splits['test'].num_shards,
  )
  _test_shards(
      data_path,
      pattern='%s-train.tfrecord-{:05}-of-{:05}' % dataset_name,
      num_shards=1,
  )

  ds = dataset_utils.as_numpy(builder.as_dataset())

  def get_id(ex):
    return ex['id']

  _assert_values_equal(
      sorted(list(ds['test']), key=get_id),
      sorted([_gen_example(i)[1] for i in range(725)], key=get_id),
  )
  _assert_values_equal(
      sorted(list(ds['train']), key=get_id),
      sorted([_gen_example(i)[1] for i in range(1000)], key=get_id),
  )

  assert builder.info.metadata == builder.EXPECTED_METADATA


def _test_shards(data_path, pattern, num_shards):
  assert num_shards >= 1
  shards_filenames = [pattern.format(i, num_shards) for i in range(num_shards)]
  assert all(data_path.joinpath(f).exists() for f in shards_filenames)


def _assert_values_equal(nested_lhs, nested_rhs):
  """assertAllEqual applied to a list of nested elements."""
  for dict_lhs, dict_rhs in zip(nested_lhs, nested_rhs):
    flat_lhs = tf.nest.flatten(dict_lhs)
    flat_rhs = tf.nest.flatten(dict_rhs)
    for lhs, rhs in zip(flat_lhs, flat_rhs):
      np.testing.assert_array_equal(lhs, rhs)


def test_read_tfrecord_beam():
  builder = DummyBeamDataset()
  with mock.patch.object(
      beam.io, 'ReadFromTFRecord'
  ) as mock_read, mock.patch.object(epath, 'Path') as mock_epath:
    file_pattern = '/a/b/*'
    mock_epath.return_value.expanduser.return_value = file_pattern
    mock_epath.return_value.glob.return_value = ['/a/b/c', '/a/b/d']
    builder.read_tfrecord_beam(file_pattern, validate=True)
    mock_epath.return_value.glob.assert_called_once_with('a/b/*')
    mock_read.assert_called_once_with(file_pattern=file_pattern, validate=True)
    info_proto = builder.info.as_proto
    assert len(info_proto.data_source_accesses) == 2
    assert info_proto.data_source_accesses[0].file_system.path == '/a/b/c'
    assert info_proto.data_source_accesses[1].file_system.path == '/a/b/d'
