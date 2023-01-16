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

"""Graph visualizer."""

from __future__ import annotations

from typing import Any, Callable, Dict, Optional, Union

from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.core.visualization import visualizer

_GraphFn = Callable[[Any], Any]
_Color = Union[float, str]
_NodeColorFn = Callable[[Any], _Color]
_EdgeColorFn = Callable[[Any], _Color]
_NodeColorDict = Dict[Any, _Color]
_EdgeColorDict = Dict[Any, _Color]


class GraphVisualizerMetadataDict(dataset_info.MetadataDict):
  """A `tfds.core.Metadata` object for metadata for visualizing graph datasets.

  This metadata information is used by tfds.core.visualization.GraphVisualizer.
  """

  def __init__(self, edgelist_feature_name, *args, **kwargs):
    super(GraphVisualizerMetadataDict, self).__init__(*args, **kwargs)
    self['edgelist_feature_name'] = edgelist_feature_name


def _extract_metadata_dict(
    metadata: Optional[dataset_info.Metadata],
) -> Optional[GraphVisualizerMetadataDict]:
  """Extracts out the metadata dict for the GraphVisualizer."""
  if metadata is None:
    return None

  for metadata_entry in metadata.values():
    for key in metadata_entry:
      if key == 'edgelist_feature_name':
        return metadata_entry
  return None


class GraphVisualizer(visualizer.Visualizer):
  """Visualizer for graph prediction datasets."""

  def match(self, ds_info: dataset_info.DatasetInfo) -> bool:
    """Checks whether this dataset can be visualized with this visualizer.

    See base class for more information.
    Args:
      ds_info: Metadata for the dataset.

    Returns:
      boolean value indicating whether the current visualizer can be used.
    """
    graph_viz_metadata = _extract_metadata_dict(ds_info.metadata)
    return graph_viz_metadata is not None

  def show(
      self,
      ds: tf.data.Dataset,
      ds_info: dataset_info.DatasetInfo,
      node_label_fn: Optional[_GraphFn] = None,
      node_color_fn: Optional[_GraphFn] = None,
      edge_color_fn: Optional[_GraphFn] = None,
      rows: int = 3,
      cols: int = 3,
      plot_scale: float = 5,
      **kwargs,
  ):
    """Display the dataset.

    Args:
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until (rows *
        cols) are read or the dataset is consumed.
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      node_label_fn: A callable that maps individual graph examples to a
        dictionary of node labels, rendered within the nodes.
      node_color_fn: A callable that maps individual graph examples to a
        dictionary of node colors.
      edge_color_fn: A callable that maps individual graph examples to a
        dictionary of edge colors.
      rows: `int`, number of rows of the display grid.
      cols: `int`, number of columns of the display grid.
      plot_scale: `float`, controls the plot size of the images. Keep this value
        around 5 to get a good plot. High and low values may cause the labels to
        get overlapped.
      **kwargs: Additional arguments passed to networkx.draw_networkx().

    Returns:
      fig: The pyplot figure.
    """

    plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot
    nx = lazy_imports_lib.lazy_imports.networkx

    # Construct edge-getter function which will extract edges from each graph.
    get_edges_fn = _make_edge_getter_fn(ds_info)

    # Create subplots.
    fig, axs = plt.subplots(
        nrows=rows,
        ncols=cols,
        squeeze=False,
        figsize=(plot_scale * cols, plot_scale * rows),
    )
    plt.subplots_adjust(hspace=1 / plot_scale, wspace=1 / plot_scale)

    for graph, ax in zip(ds, axs.reshape(-1)):
      # Obtain edges.
      edges = get_edges_fn(graph)

      # Create NetworkX graph.
      nx_graph = nx.Graph()
      nx_graph.add_edges_from(edges)

      # Add node labels, node colors and edge colors, if specified.
      if node_label_fn is not None:
        kwargs['labels'] = node_label_fn(graph)

      if node_color_fn is not None:
        node_color_map = node_color_fn(graph)
        node_color_mapper = _make_node_color_mapper(node_color_map)
        kwargs['node_color'] = list(map(node_color_mapper, nx_graph.nodes()))

      if edge_color_fn is not None:
        edge_color_map = edge_color_fn(graph)
        edge_color_mapper = _make_edge_color_mapper(edge_color_map)
        kwargs['edge_color'] = list(map(edge_color_mapper, nx_graph.edges()))

      # Draw with NetworkX.
      nx.draw_networkx(nx_graph, ax=ax, **kwargs)

    return fig


def _make_edge_getter_fn(ds_info: dataset_info.DatasetInfo) -> _GraphFn:
  """Returns a function which will extract edges from each graph."""
  graph_viz_metadata = _extract_metadata_dict(ds_info.metadata)
  edgelist_feature_name = graph_viz_metadata['edgelist_feature_name']

  def get_edges_fn(graph):
    return graph[edgelist_feature_name].numpy()

  return get_edges_fn


def _make_node_color_mapper(
    node_color_map: _NodeColorDict, default_color: str = 'C0'
) -> _NodeColorFn:
  """Helper to map nodes to colors."""

  def node_color_mapper(node):
    return node_color_map.get(node, default_color)

  return node_color_mapper


def _make_edge_color_mapper(
    edge_color_map: _EdgeColorDict, default_color: str = 'C0'
) -> _EdgeColorFn:
  """Helper to map edges to colors."""

  def edge_color_mapper(edge):
    reversed_edge = tuple(reversed(edge))
    if edge in edge_color_map:
      return edge_color_map[edge]
    elif reversed_edge in edge_color_map:
      return edge_color_map[reversed_edge]
    else:
      return default_color

  return edge_color_mapper
