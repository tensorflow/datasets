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

"""Base class for building a TFDS dataset from RLDS data."""

import dataclasses
import os
from typing import Any, Dict, Generator, List, Optional, Tuple

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rlds import envlogger_reader


@dataclasses.dataclass
class DatasetConfig(tfds.core.BuilderConfig):
  """Configuration of the RLDS dataset.

  Attributes:
    description: string describing the dataset config.
    overall_description: string describing the dataset.
    homepage: URL hosting dataset information.
    citation: Citation for the dataset.
    observation_info: spec of the observation expressed as a TFDS feature.
    action_info: spec of the action expressed as a TFDS feature.
    reward_info: spec of the reward expressed as a TFDS feature.
    discount_info: spec of the discount expressed as a TFDS feature.
    step_metadata_info: spec of the step metadata expresses as a dictionary of
      'feature_name': TFDS feature. Can be an empty dictionary.
    episode_metadata_info: spec of the episode metadata expresses as a
      dictionary of 'feature_name': TFDS feature. Can be an empty dictionary.
    supervised_keys: Supervised keys to be used is `as_supervised=True` in
      `builder.as_dataset`. See `tfds.core.DatasetInfo` for details.
  """
  description: str = ''
  overall_description: str = ''
  homepage: str = ''
  citation: str = ''
  observation_info: Optional[tfds.typing.FeatureConnectorArg] = None
  action_info: Optional[tfds.features.FeatureConnector] = None
  reward_info: Optional[tfds.features.FeatureConnector] = None
  discount_info: Optional[tfds.features.FeatureConnector] = None
  step_metadata_info: Optional[Dict[str, tfds.features.FeatureConnector]] = None
  episode_metadata_info: Optional[Dict[str,
                                       tfds.features.FeatureConnector]] = None
  supervised_keys: Optional[Tuple[Any]] = None


def build_info(ds_config: DatasetConfig,
               builder: tfds.core.DatasetBuilder) -> tfds.core.DatasetInfo:
  """Returns the dataset metadata."""
  step_metadata = ds_config.step_metadata_info
  if step_metadata is None:
    step_metadata = {}
  episode_metadata = ds_config.episode_metadata_info
  if episode_metadata is None:
    episode_metadata = {}
  return tfds.core.DatasetInfo(
      builder=builder,
      description=ds_config.overall_description,
      features=tfds.features.FeaturesDict({
          'steps':
              tfds.features.Dataset({
                  'observation': ds_config.observation_info,
                  'action': ds_config.action_info,
                  'reward': ds_config.reward_info,
                  'is_terminal': tf.bool,
                  'is_first': tf.bool,
                  'is_last': tf.bool,
                  'discount': ds_config.discount_info,
                  **step_metadata,
              }),
          **episode_metadata,
      }),
      supervised_keys=ds_config.supervised_keys,
      homepage=ds_config.homepage,
      citation=ds_config.citation,
  )


def get_log_paths(root_dir: str) -> List[str]:
  """Returns the paths of environment logs under a (set of) directories.

  We assume that a sub-directory with metadata.riegeli file contains the logs.

  Args:
    root_dir: Root directory to search for log paths.

  Returns:
    A list of paths that contain the environment logs.

  Raises:
    ValueError if the specified pattern matches a non-directory.
  """
  paths = []
  if not tf.io.gfile.isdir(root_dir):
    raise ValueError(f'{root_dir} is not a directory.')
  for path, _, files in tf.io.gfile.walk(root_dir):
    if 'metadata.riegeli' in files:
      paths.append(path)
  return paths


def generate_examples(path):
  """Yields examples."""
  # TODO(sabela): Consider adding the option of passing a filter to remove
  # some of the episodes.
  tag_dirs = get_log_paths(path.resolve())
  for tag_dir in tag_dirs:
    yield from _generate_examples_from_log_path(tag_dir)


def generate_beam_examples(path):
  """Yields examples using Beam."""
  beam = tfds.core.lazy_imports.apache_beam

  tag_dirs = get_log_paths(path.resolve())
  return beam.Create(tag_dirs) | beam.FlatMap(_generate_examples_from_log_path)


def _generate_examples_from_log_path(
    log_path: str) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
  """Yields examples from a directory containing log files.

  Args:
    log_path: Path of the directory containing the log files.

  Yields:
    a unique example ID and dictionary pair for each episode.
  """
  envlogger = tfds.core.lazy_imports.envlogger
  logging.info('Processing directory %s.', log_path)
  counter = 0
  # TFDS suggests using the basename to avoid having the user path in the key.
  key_prefix = os.path.basename(log_path)
  with envlogger.Reader(log_path) as reader:
    for episode_dict in envlogger_reader.generate_episodes(reader):
      # The example ID should be unique.
      episode_id = counter
      if 'episode_id' in episode_dict:
        episode_id = episode_dict['episode_id']
      yield f'{key_prefix}/{episode_id}', episode_dict
      counter += 1
