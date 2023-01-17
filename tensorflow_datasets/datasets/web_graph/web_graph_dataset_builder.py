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

"""web_graph dataset."""

from __future__ import annotations

import dataclasses
import os
import textwrap
from typing import List

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


@dataclasses.dataclass
class WebGraphConfig(tfds.core.BuilderConfig):
  """Palmer Penguins dataset builder config."""

  # Basename of the file hosting the data.
  subfolder: str = ''
  num_shards: int = 1


def filename(subfolder: str, name: str):
  full_name = os.path.join(subfolder, name)
  return os.fspath(tfds.core.Path(full_name))


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for web_graph dataset."""

  VERSION = tfds.core.Version('1.0.0')
  WEB_GRAPH_HOMEPAGE = 'gs://gresearch/web_graph/'
  SHARDS = None
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      WebGraphConfig(
          name='sparse',
          subfolder='web_graph_min_10',
          num_shards=1000,
          description=textwrap.dedent(
              """\
              WebGraph-sparse contains around 30B edges and around 365M nodes.
              """
          ),
      ),
      WebGraphConfig(
          name='dense',
          subfolder='web_graph_min_50',
          num_shards=1000,
          description=textwrap.dedent(
              """\
              WebGraph-dense contains around 22B edges and around 136.5M nodes.
              """
          ),
      ),
      WebGraphConfig(
          name='de-sparse',
          subfolder='web_graph_tld_de_min_10',
          num_shards=100,
          description=textwrap.dedent(
              """\
              WebGraph-de-sparse contains around 1.19B edges and around 19.7M
              nodes.
              """
          ),
      ),
      WebGraphConfig(
          name='de-dense',
          subfolder='web_graph_tld_de_min_50',
          num_shards=100,
          description=textwrap.dedent(
              """\
              WebGraph-de-dense contains around 0.82B edges and around 5.7M
              nodes.
              """
          ),
      ),
      WebGraphConfig(
          name='in-sparse',
          subfolder='web_graph_tld_in_min_10',
          num_shards=10,
          description=textwrap.dedent(
              """\
              WebGraph-de-sparse contains around 0.14B edges and around 1.5M
              nodes.
              """
          ),
      ),
      WebGraphConfig(
          name='in-dense',
          subfolder='web_graph_tld_in_min_50',
          num_shards=10,
          description=textwrap.dedent(
              """\
              WebGraph-de-dense contains around 0.12B edges and around 0.5M
              nodes.
              """
          ),
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'row_tag': np.int64,
            'col_tag': tfds.features.Sequence(np.int64),
            'gt_tag': tfds.features.Sequence(np.int64),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://arxiv.org/abs/2112.02194',
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager, pipeline
  ):
    """Returns SplitGenerators."""
    del dl_manager

    subfolder = os.path.join(
        self.WEB_GRAPH_HOMEPAGE, self.builder_config.subfolder
    )
    shards = self.SHARDS or self.builder_config.num_shards

    train_files = [
        filename(subfolder, f'train.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    train_t_files = [
        filename(subfolder, f'train.transpose.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    test_files = [
        filename(subfolder, f'test.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    return {
        'train': self._generate_examples(pipeline, train_files, split='train'),
        'train_t': self._generate_examples(
            pipeline, train_t_files, split='train_t'
        ),
        'test': self._generate_examples(pipeline, test_files, split='test'),
    }

  def _generate_examples(self, pipeline, files, split: str):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _get_int_feature(
        example: tf.train.Example, feature_name: str
    ) -> List[int]:
      return example.features.feature[feature_name].int64_list.value

    def _process_example(example: bytes, is_test=False):
      example = tf.train.Example.FromString(example)
      row_tag = _get_int_feature(example, 'row_tag')[0]
      col_tag = np.array(_get_int_feature(example, 'col_tag'), dtype=np.int64)
      if is_test:
        gt_tag = _get_int_feature(example, 'gt_tag')
      else:
        gt_tag = []
      gt_tag = np.array(gt_tag, dtype=np.int64)
      return_dict = {'row_tag': row_tag, 'col_tag': col_tag, 'gt_tag': gt_tag}
      return row_tag, return_dict

    return (
        pipeline
        | f'{split}_create' >> beam.Create(files)
        | f'{split}_read' >> beam.io.tfrecordio.ReadAllFromTFRecord()
        | f'{split}_process' >> beam.Map(_process_example, split == 'test')
    )
