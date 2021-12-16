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

"""Module including definitions for all RLU datasets."""

import os

from typing import Any, Dict, Generator, List, Tuple
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

"""


_HOMEPAGE = 'https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged'


def filename(prefix: str, num_shards: int, shard_id: int):
  return os.fspath(
      tfds.core.as_path(f'{prefix}-{shard_id:05d}-of-{num_shards:05d}'))


def get_files(prefix: str, num_shards: int) -> List[str]:
  return [filename(prefix, num_shards, i) for i in range(num_shards)]  # pytype: disable=bad-return-type  # gen-stub-imports


class RLUBuilder(tfds.core.GeneratorBasedBuilder, skip_registration=True):
  """DatasetBuilder for RLU."""

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION + self.get_description(),
        features=self.get_features_dict(),
        supervised_keys=None,  # disabled
        homepage=_HOMEPAGE,
        citation=self.get_citation(),
    )

  def get_file_prefix(self):
    raise NotImplementedError()

  def get_citation(self):
    raise NotImplementedError

  def get_description(self):
    raise NotImplementedError()

  def num_shards(self):
    raise NotImplementedError()

  def get_features_dict(self):
    raise NotImplementedError()

  def get_episode_id(self, episode):
    # The key of the episode is converted to string because int64 is not
    # supported as key.
    return str(episode['episode_id'])

  def tf_example_to_step_ds(self,
                            tf_example: tf.train.Example) -> Dict[str, Any]:
    """Create an episode from a TF example."""
    raise NotImplementedError()

  def get_splits(self):
    paths = {
        'file_paths':
            get_files(
                prefix=self.get_file_prefix(), num_shards=self.num_shards()),
    }
    return {
        'train': self._generate_examples(paths),
    }

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    del dl_manager

    return self.get_splits()

  def generate_examples_one_file(
      self, path) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    """Yields examples from one file."""
    # Dataset of tf.Examples containing full episodes.
    example_ds = tf.data.TFRecordDataset(
        filenames=str(path), compression_type='GZIP')
    # Dataset of episodes, each represented as a dataset of steps.
    episode_ds = example_ds.map(
        self.tf_example_to_step_ds,
        num_parallel_calls=tf.data.experimental.AUTOTUNE)
    episode_ds = tfds.as_numpy(episode_ds)
    for e in episode_ds:
      yield self.get_episode_id(e), e

  def _generate_examples(self, paths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    file_paths = paths['file_paths']

    return beam.Create(file_paths) | beam.FlatMap(
        self.generate_examples_one_file)
