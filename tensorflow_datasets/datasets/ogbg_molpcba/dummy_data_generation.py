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

r"""Generate dummy molecular data.

"""
import collections
import itertools
import random
from typing import Iterable, Dict, Text, List

from absl import app
from absl import flags
from etils import epath
import numpy as np
import pandas as pd
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import resource_utils

# Command-line arguments.
flags.DEFINE_string('save_path', None, 'Path to save generated data to.')
flags.DEFINE_integer('num_graphs', 12, 'Number of graphs to create.')
flags.DEFINE_integer('seed', 7, 'Seed for random number generator.')
FLAGS = flags.FLAGS

# Type hints.
ArrayDict = Dict[Text, np.ndarray]
Path = epath.Path


def seed_prngs(seed: int):
  """Seed pseudo-random number generators."""
  np.random.seed(seed)
  random.seed(seed)


def generate_dummy_splits(num_graphs: int) -> ArrayDict:
  """Create simple train/validation/test split indices."""
  one_third_split = num_graphs // 3
  return {
      'train': np.arange(0, one_third_split),
      'valid': np.arange(one_third_split, 2 * one_third_split),
      'test': np.arange(2 * one_third_split, 3 * one_third_split),
  }


def generate_dummy_graphs(num_graphs: int) -> List[ArrayDict]:
  """Generates dummy graphs with random edges, features and label."""
  all_num_nodes = np.random.randint(low=8, high=11, size=num_graphs)
  all_num_edges = np.random.randint(low=10, high=30, size=num_graphs)
  return [
      generate_dummy_graph(num_nodes, num_edges)
      for (num_nodes, num_edges) in zip(all_num_nodes, all_num_edges)
  ]


def generate_dummy_graph(
    num_nodes: int,
    num_edges: int,
    node_feature_dim: int = 9,
    edge_feature_dim: int = 3,
    labels_dim: int = 128,
) -> ArrayDict:
  """Generates a dummy graph with random edges, features and label."""
  nodes = np.arange(num_nodes)
  node_features = np.random.standard_normal((num_nodes, node_feature_dim))

  possible_edge_indices = list(itertools.permutations(nodes, 2))
  edge_indices = np.array(random.choices(possible_edge_indices, k=num_edges))
  edge_features = np.random.standard_normal((num_edges, edge_feature_dim))

  labels = np.random.randint(low=0, high=3, size=(1, labels_dim))
  labels = labels.astype(np.float64)
  labels[labels == 2] = np.nan

  return {
      'labels': labels,
      'num_nodes': np.array([num_nodes]),
      'node_feat': node_features,
      'num_edges': np.array([num_edges]),
      'edge_feat': edge_features,
      'edge_index': edge_indices,
  }


def get_save_name(column: Text) -> Text:
  """Save file names for the different columns, according to OGB."""
  if column == 'labels':
    return 'graph-label.csv.gz'
  if column == 'num_nodes':
    return 'num-node-list.csv.gz'
  if column == 'node_feat':
    return 'node-feat.csv.gz'
  if column == 'num_edges':
    return 'num-edge-list.csv.gz'
  if column == 'edge_feat':
    return 'edge-feat.csv.gz'
  if column == 'edge_index':
    return 'edge.csv.gz'

  raise ValueError('Invalid column name.')


def combine_graph_data(graphs: Iterable[ArrayDict]) -> ArrayDict:
  """Flattens graph dictionaries into a common dictionary with the same keys."""
  graphs_dict = collections.defaultdict(list)
  for graph in graphs:
    for column, column_vals in graph.items():
      for val in column_vals:
        graphs_dict[column].append(val)
  return graphs_dict


def save_to_path(path: Path, graphs: Iterable[ArrayDict], splits: ArrayDict):
  """Save all generated data as OGB does."""

  # Combine all graph data into a single dictionary.
  graphs_dict = combine_graph_data(graphs)

  # Create directories for output.
  data_path = path / 'pcba/raw'
  data_path.mkdir(parents=True, exist_ok=True)

  split_path = path / 'pcba/split/scaffold'
  split_path.mkdir(parents=True, exist_ok=True)

  # Save each column as a separate compressed CSV file.
  for column, column_vals in graphs_dict.items():
    column_save_name = data_path / get_save_name(column)
    column_df = pd.DataFrame(column_vals)
    column_df.to_csv(
        column_save_name, compression='gzip', header=False, index=None
    )

  # Save each split as a separate compressed CSV file.
  for split, split_indices in splits.items():
    split_save_name = split_path / ('%s.csv.gz' % split)
    split_df = pd.DataFrame(split_indices)
    split_df.to_csv(
        split_save_name, compression='gzip', header=False, index=None
    )


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  # Seed random number generators.
  seed_prngs(FLAGS.seed)

  # Create graphs with dummy data.
  graphs = generate_dummy_graphs(FLAGS.num_graphs)
  splits = generate_dummy_splits(FLAGS.num_graphs)

  # Save them in the same way that OGB does.
  if FLAGS.save_path is None:
    save_path = (
        resource_utils.tfds_write_path() / 'graphs/ogbg_molpcba/dummy_data'
    )
  else:
    save_path = utils.to_write_path(FLAGS.save_path)
  save_to_path(save_path, graphs, splits)


if __name__ == '__main__':
  app.run(main)
