# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for `tensorflow_datasets.core.visualization.show_examples`."""

from unittest import mock

import numpy as np
from tensorflow_datasets import testing
from tensorflow_datasets.core import load
from tensorflow_datasets.core import visualization

# Import for registration
from tensorflow_datasets.image_classification import imagenet  # pylint: disable=unused-import,g-bad-import-order


class ShowExamplesTest(testing.TestCase):

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples(self, mock_fig):
    with testing.mock_data(num_examples=20):
      ds, ds_info = load.load('imagenet2012', split='train', with_info=True)
    visualization.show_examples(ds, ds_info)

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples_supervised(self, _):
    with testing.mock_data(num_examples=20):
      ds, ds_info = load.load(
          'imagenet2012', split='train', with_info=True, as_supervised=True
      )
    visualization.show_examples(ds, ds_info)

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples_with_batch(self, _):
    with testing.mock_data(num_examples=20):
      ds, ds_info = load.load(
          'imagenet2012', split='train', with_info=True, batch_size=32
      )
    visualization.show_examples(ds, ds_info, is_batched=True)

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples_graph(self, _):
    with testing.mock_data(num_examples=20):
      ds, ds_info = load.load('ogbg_molpcba', split='train', with_info=True)
    visualization.show_examples(ds, ds_info)

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples_graph_with_colors_and_labels(self, _):
    with testing.mock_data(num_examples=20):
      ds, ds_info = load.load('ogbg_molpcba', split='train', with_info=True)

    # Dictionaries used to map nodes and edges to colors.
    atomic_numbers_to_elements = {
        6: 'C',
        7: 'N',
        8: 'O',
        9: 'F',
        14: 'Si',
        15: 'P',
        16: 'S',
        17: 'Cl',
        35: 'Br,',
    }
    elements_to_colors = {
        element: f'C{index}'
        for index, element in enumerate(atomic_numbers_to_elements.values())
    }
    bond_types_to_colors = {num: f'C{num}' for num in range(4)}

    # Node colors are atomic numbers.
    def node_color_fn(graph):
      atomic_numbers = 1 + graph['node_feat'][:, 0].numpy()
      return {
          index: elements_to_colors[atomic_numbers_to_elements[atomic_number]]
          for index, atomic_number in enumerate(atomic_numbers)
      }

    # Node labels are element names.
    def node_label_fn(graph):
      atomic_numbers = 1 + graph['node_feat'][:, 0].numpy()
      return {
          index: atomic_numbers_to_elements[atomic_number]
          for index, atomic_number in enumerate(atomic_numbers)
      }

    # Edge colors are bond types.
    def edge_color_fn(graph):
      bonds = graph['edge_index'].numpy()
      bond_types = graph['edge_feat'][:, 0].numpy()
      return {
          tuple(bond): bond_types_to_colors[bond_type]
          for bond, bond_type in zip(bonds, bond_types)
      }

    visualization.show_examples(
        ds,
        ds_info,
        node_color_fn=node_color_fn,
        node_label_fn=node_label_fn,
        edge_color_fn=edge_color_fn,
    )

  @mock.patch('matplotlib.pyplot.figure')
  def test_show_examples_missing_sample(self, _):
    with testing.mock_data(num_examples=3):
      ds, ds_info = load.load('imagenet2012', split='train', with_info=True)
    visualization.show_examples(ds.take(3), ds_info)


if __name__ == '__main__':
  testing.test_main()
