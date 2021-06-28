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

from typing import Any, Dict, Generator, List, Tuple
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

DeepMind Lab dataset has several levels from the challenging, partially
observable [Deepmind Lab suite](https://github.com/deepmind/lab). DeepMind Lab
dataset is collected by training distributed R2D2 by [Kapturowski et al., 2018]
(https://openreview.net/forum?id=r1lyTjAqYX) agents from scratch on individual
tasks. We recorded the experience across all actors during entire training runs
a few times for every task. The details of the dataset generation process is
described in [Gulcehre et al., 2021](https://arxiv.org/abs/2103.09575).

We release datasets for five different DeepMind Lab levels: `seekavoid_arena_01`,
`explore_rewards_few`, `explore_rewards_many`, `rooms_watermaze`,
`rooms_select_nonmatching_object`. We also release the snapshot datasets for
`seekavoid_arena_01` level that we generated the datasets from a trained R2D2
snapshot with different levels of epsilons for the epsilon-greedy algorithm
when evaluating the agent in the environment.

DeepMind Lab dataset is fairly large-scale. We recommend you to try it if you
are interested in large-scale offline RL models with memory.

"""

_CITATION = """
@article{gulcehre2021rbve,
    title={Regularized Behavior Value Estimation},
    author={{\\c{C}}aglar G{\\"{u}}l{\\c{c}}ehre and
               Sergio G{\\'{o}}mez Colmenarejo and
               Ziyu Wang and
               Jakub Sygnowski and
               Thomas Paine and
               Konrad Zolna and
               Yutian Chen and
               Matthew W. Hoffman and
               Razvan Pascanu and
               Nando de Freitas},
    year={2021},
    journal   = {CoRR},
    url       = {https://arxiv.org/abs/2103.09575},
    eprint={2103.09575},
    archivePrefix={arXiv},
}
"""

_HOMEPAGE = 'https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged'


def _get_files(prefix: str, num_shards: int) -> List[str]:
  return [
      tfds.core.as_path(f'{prefix}-{i:05d}-of-{num_shards:05d}')
      for i in range(num_shards)
  ]


class RLUBuilder(tfds.core.GeneratorBasedBuilder, skip_registration=True):
  """DatasetBuilder for RLU."""

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=self.get_features_dict(),
        supervised_keys=None,  # disabled
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def get_file_prefix(self):
    raise NotImplementedError()

  def num_shards(self):
    raise NotImplementedError()

  def get_features_dict(self):
    raise NotImplementedError()

  def tf_example_to_step_ds(self,
                            tf_example: tf.train.Example) -> Dict[str, Any]:
    """Create an episode from a TF example."""
    raise NotImplementedError()

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    del dl_manager

    paths = {
        'file_paths':
            _get_files(
                prefix=self.get_file_prefix(), num_shards=self.num_shards()),
    }
    return {
        'train': self._generate_examples(paths),
    }

  def _generate_examples(self, paths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    file_paths = paths['file_paths']

    def _generate_examples_one_file(
        path) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
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
        # The key of the episode is converted to string because int64 is not
        # supported as key.
        yield str(e['episode_id']), e

    return beam.Create(file_paths) | beam.FlatMap(_generate_examples_one_file)
