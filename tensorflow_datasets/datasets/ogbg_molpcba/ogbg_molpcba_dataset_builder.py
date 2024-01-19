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

"""ogbg_molpcba dataset."""

from typing import Dict, Text, Tuple

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

# Type hints.
ArrayDict = Dict[Text, np.ndarray]
Path = epath.Path

# URL.
_OGB_URL = 'https://ogb.stanford.edu/docs/graphprop'
_DOWNLOAD_URL = (
    'https://snap.stanford.edu/ogb/data/graphproppred/csv_mol_download/pcba.zip'
)

# File containing the names of individual tasks.
_TASKS_FNAME = 'datasets/ogbg_molpcba/tasks.txt'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for ogbg_molpcba dataset."""

  VERSION = tfds.core.Version('0.1.3')
  RELEASE_NOTES = {
      '0.1.0': 'Initial release of experimental API.',
      '0.1.1': 'Exposes the number of edges in each graph explicitly.',
      '0.1.2': 'Add metadata field for GraphVisualizer.',
      '0.1.3': 'Add metadata field for names of individual tasks.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # Read the individual task names.
    tasks_file = tfds.core.tfds_path(_TASKS_FNAME)
    tasks = tasks_file.read_text().splitlines()

    # Specify the tfds.core.DatasetInfo object
    return self.dataset_info_from_configs(
        # We mimic the features of the OGB platform-agnostic DataLoader.
        features=tfds.features.FeaturesDict({
            'num_nodes': tfds.features.Tensor(shape=(None,), dtype=np.int64),
            'node_feat': tfds.features.Tensor(
                shape=(None, 9), dtype=np.float32
            ),
            'num_edges': tfds.features.Tensor(shape=(None,), dtype=np.int64),
            'edge_feat': tfds.features.Tensor(
                shape=(None, 3), dtype=np.float32
            ),
            'edge_index': tfds.features.Tensor(shape=(None, 2), dtype=np.int64),
            'labels': tfds.features.Tensor(shape=(128,), dtype=np.float32),
        }),
        supervised_keys=None,
        homepage=_OGB_URL,
        metadata=tfds.core.MetadataDict({
            'tasks': tasks,
            'graph_visualizer': tfds.visualization.GraphVisualizerMetadataDict(
                edgelist_feature_name='edge_index'
            ),
        }),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Download the original data.
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    # Read the extracted data.
    data_path = path / 'pcba/raw'
    split_path = path / 'pcba/split/scaffold'
    all_data, split_indices = _read_extracted_data(data_path, split_path)

    # Return a list of the train/validation/test split generators.
    return {
        tfds.Split.TRAIN: self._generate_examples(
            all_data, split_indices['train']
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            all_data, split_indices['valid']
        ),
        tfds.Split.TEST: self._generate_examples(
            all_data, split_indices['test']
        ),
    }

  def _generate_examples(self, all_data: ArrayDict, split_indices: np.ndarray):
    """Yields examples."""
    # Precompute for later.
    num_total_graphs = len(all_data['labels'])
    split_indices = set(split_indices)
    accumulated_num_nodes = np.concatenate(
        [np.array([0]), np.cumsum(all_data['num_nodes'])]
    )
    accumulated_num_edges = np.concatenate(
        [np.array([0]), np.cumsum(all_data['num_edges'])]
    )

    # Loop over the training set.
    for idx in range(num_total_graphs):
      # Check if this example is part of the split.
      if idx not in split_indices:
        continue

      # Read all of the graph information.
      labels = all_data['labels'][idx]
      num_nodes = all_data['num_nodes'][idx]
      node_slice = slice(
          accumulated_num_nodes[idx], accumulated_num_nodes[idx + 1]
      )
      node_feat = all_data['node_feat'][node_slice]
      num_edges = all_data['num_edges'][idx]
      edge_slice = slice(
          accumulated_num_edges[idx], accumulated_num_edges[idx + 1]
      )
      edge_feat = all_data['edge_feat'][edge_slice]
      edge_index = all_data['edge_index'][edge_slice]

      # Combine into a single dictionary.
      record = {
          'labels': labels,
          'num_nodes': num_nodes,
          'node_feat': node_feat,
          'num_edges': num_edges,
          'edge_feat': edge_feat,
          'edge_index': edge_index,
      }
      yield idx, record


def _read_extracted_data(
    data_path: Path, split_path: Path
) -> Tuple[ArrayDict, ArrayDict]:
  """Reads and processes the extracted graph data and splits."""
  pd = tfds.core.lazy_imports.pandas

  # Load columns describing the graph features and structure.
  column_names = [
      'edge_index',
      'num_nodes',
      'num_edges',
      'node_feat',
      'edge_feat',
      'labels',
  ]
  file_names = [
      'edge.csv.gz',
      'num-node-list.csv.gz',
      'num-edge-list.csv.gz',
      'node-feat.csv.gz',
      'edge-feat.csv.gz',
      'graph-label.csv.gz',
  ]
  dtypes = [
      np.int64,
      np.int64,
      np.int64,
      np.float32,
      np.float32,
      np.float32,
  ]
  all_data = {}
  for column_name, file_name, dtype in zip(column_names, file_names, dtypes):
    with (data_path / file_name).open('rb') as fp:
      values = pd.read_csv(fp, compression='gzip', header=None).values
      values = values.astype(dtype)
      all_data[column_name] = values

  # Load data splits.
  split_indices = {}
  for split_name in ['train', 'valid', 'test']:
    with (split_path / ('%s.csv.gz' % split_name)).open('rb') as fp:
      indices = pd.read_csv(fp, compression='gzip', header=None).values.T[0]
      split_indices[split_name] = indices

  return all_data, split_indices
