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

"""ogbg_molpcba dataset."""

from typing import Dict, Text, Tuple

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core.utils import type_utils
import tensorflow_datasets.public_api as tfds

# Type hints.
ArrayDict = Dict[Text, np.ndarray]
ReadOnlyPath = type_utils.ReadOnlyPath

_DESCRIPTION = """
'ogbg-molpcba' is a molecular dataset sampled from PubChem BioAssay.
It is a graph prediction dataset from the Open Graph Benchmark (OGB).

This dataset is experimental, and the API is subject to change in
future releases.

The below description of the dataset is adapted from the OGB paper:

### Input Format
All the molecules are pre-processed using RDKit ([1]).

*  Each graph represents a molecule, where nodes are atoms, and edges are
   chemical bonds.
*  Input node features are 9-dimensional, containing atomic number and chirality,
   as well as other additional atom features such as formal charge and
   whether the atom is in the ring.
*  Input edge features are 3-dimensional, containing bond type,
   bond stereochemistry, as well as an additional bond feature indicating
   whether the bond is conjugated.

The exact description of all features is available at
https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py.

### Prediction
The task is to predict 128 different biological activities (inactive/active).
See [2] and [3] for more description about these targets.
Not all targets apply to each molecule: missing targets are indicated by NaNs.

### References

[1]: Greg Landrum, et al. 'RDKit: Open-source cheminformatics'.
     URL: https://github.com/rdkit/rdkit

[2]: Bharath Ramsundar, Steven Kearnes, Patrick Riley, Dale Webster,
     David Konerding and Vijay Pande. 'Massively Multitask Networks for
     Drug Discovery'.
     URL: https://arxiv.org/pdf/1502.02072.pdf

[3]: Zhenqin Wu, Bharath Ramsundar, Evan N Feinberg, Joseph Gomes,
     Caleb Geniesse, Aneesh S. Pappu, Karl Leswing, and Vijay Pande.
     MoleculeNet: a benchmark for molecular machine learning.
     Chemical Science, 9(2):513-530, 2018.
"""

_CITATION = """
@inproceedings{DBLP:conf/nips/HuFZDRLCL20,
  author    = {Weihua Hu and
               Matthias Fey and
               Marinka Zitnik and
               Yuxiao Dong and
               Hongyu Ren and
               Bowen Liu and
               Michele Catasta and
               Jure Leskovec},
  editor    = {Hugo Larochelle and
               Marc Aurelio Ranzato and
               Raia Hadsell and
               Maria{-}Florina Balcan and
               Hsuan{-}Tien Lin},
  title     = {Open Graph Benchmark: Datasets for Machine Learning on Graphs},
  booktitle = {Advances in Neural Information Processing Systems 33: Annual Conference
               on Neural Information Processing Systems 2020, NeurIPS 2020, December
               6-12, 2020, virtual},
  year      = {2020},
  url       = {https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html},
  timestamp = {Tue, 19 Jan 2021 15:57:06 +0100},
  biburl    = {https://dblp.org/rec/conf/nips/HuFZDRLCL20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

# URL.
_OGB_URL = 'https://ogb.stanford.edu/docs/graphprop'
_DOWNLOAD_URL = 'https://snap.stanford.edu/ogb/data/graphproppred/csv_mol_download/pcba.zip'

# File containing the names of individual tasks.
_TASKS_FNAME = 'graphs/ogbg_molpcba/ogbg_molpcba_tasks.txt'


class OgbgMolpcba(tfds.core.GeneratorBasedBuilder):
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
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        # We mimic the features of the OGB platform-agnostic DataLoader.
        features=tfds.features.FeaturesDict({
            'num_nodes':
                tfds.features.Tensor(shape=(None,), dtype=tf.int64),
            'node_feat':
                tfds.features.Tensor(shape=(None, 9), dtype=tf.float32),
            'num_edges':
                tfds.features.Tensor(shape=(None,), dtype=tf.int64),
            'edge_feat':
                tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
            'edge_index':
                tfds.features.Tensor(shape=(None, 2), dtype=tf.int64),
            'labels':
                tfds.features.Tensor(shape=(128,), dtype=tf.float32),
        }),
        supervised_keys=None,
        homepage=_OGB_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict({
            'tasks':
                tasks,
            'graph_visualizer':
                tfds.visualization.GraphVisualizerMetadataDict(
                    edgelist_feature_name='edge_index')
        }),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Download the original data.
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    # Read the extracted data.
    data_path = (path / 'pcba/raw')
    split_path = (path / 'pcba/split/scaffold')
    all_data, split_indices = _read_extracted_data(data_path, split_path)

    # Return a list of the train/validation/test split generators.
    return {
        tfds.Split.TRAIN:
            self._generate_examples(all_data, split_indices['train']),
        tfds.Split.VALIDATION:
            self._generate_examples(all_data, split_indices['valid']),
        tfds.Split.TEST:
            self._generate_examples(all_data, split_indices['test']),
    }

  def _generate_examples(self, all_data: ArrayDict, split_indices: np.ndarray):
    """Yields examples."""
    # Precompute for later.
    num_total_graphs = len(all_data['labels'])
    split_indices = set(split_indices)
    accumulated_num_nodes = np.concatenate([np.array([0]),
                                            np.cumsum(all_data['num_nodes'])])
    accumulated_num_edges = np.concatenate([np.array([0]),
                                            np.cumsum(all_data['num_edges'])])

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
    data_path: ReadOnlyPath,
    split_path: ReadOnlyPath
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
