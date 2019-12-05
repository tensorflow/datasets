# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""ARC dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging
import json
import numpy as np
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{chollet_françois_2019,
  title     = {The Measure of Intelligence},
  url       = {https://arxiv.org/abs/1911.01547},
  journal   = {arXiv.org},
  author    = {François Chollet},
  year      = {2019},
  month     = {Nov}
}
"""

_DESCRIPTION = """
ARC can be seen as a general artificial intelligence benchmark, as a program
synthesis benchmark, or as a psychometric intelligence test. It is targeted at
both humans and artificially intelligent systems that aim at emulating a
human-like form of general fluid intelligence.
"""


_BASE_URL = "https://github.com/fchollet/ARC/"
_COMMIT = "bd9e2c934c83d00251b7b4781ffc38cd167c885f"
_DL_URL = "{}zipball/{}/".format(_BASE_URL, _COMMIT)
_DL_RESOURCE = tfds.download.Resource(
    url=_DL_URL,
    extract_method=tfds.download.ExtractMethod.ZIP)
_EXTRACT_SUBDIR = "fchollet-ARC-{}".format(_COMMIT[:7])


def pad_grid(grid):
    """Convert a list of list of ints to a 30x30 NumPy grid + a size array.

    Each ARC task is composed of pairs of grids (usually 3 demo pairs, and 1
    test pair). Each grid is represented as a list of list of integers from 0
    to 9. Each grid's size is between 1x1 and 30x30. To create batches of
    grids in TFDS, we need them all to have the same size. And we also need
    each grid to be represented as a NumPy array. So this function converts a
    grid represented as a list of list of ints to a 30x30 NumPy uint8 array
    containing the same data plus 0 padding to reach the 30x30 size. It also
    returns another NumPy uint8 array, of shape (2,), representing the original
    size of the grid: np.array([height, width], dtype=np.uint8).

    For example:
    >>> padded_grid, grid_size = ARC.pad_grid([[1, 2, 3], [4, 5, 6]])
    >>> padded_grid
    array([[1, 2, 3, 0, 0, ..., 0],
          [4, 5, 6, 0, 0, ..., 0],
          [0, 0, 0, 0, 0, ..., 0]],
          ...
          [0, 0, 0, 0, 0, ..., 0]], dtype=uint8)
    >>> padded_grid.shape
    (30, 30)
    >>> grid_size
    array([2, 3], dtype=uint8))

    Args:
        grid (list of list of ints): the input grid.

    Returns:
        (padded_grid, grid_size): padded_grid is a 30x30 NumPy uint8 array
        containing the input data padded with 0s. grid_size is a NumPy uint8
        array containing the original height and width of the grid.

    Raises:
        ValueError: if the input grid's size is not between 1x1 and 30x30. Or
        if the input grid contains rows of different lengths. Or if the input
        grid contains values which NumPy cannot convert to uint8 (e.g., None or
        strings).
        Note: this function assumes that the input is indeed a list of list
        of integers from 0 to 9. If not, then it may produce unexpected
        results or raise other exceptions such as TypeErrors.
    """
    height = len(grid)
    if not 0 < height <= 30:
      raise ValueError("Invalid grid height: {}".format(height))
    width = len(grid[0])
    if not 0 < height <= 30:
      raise ValueError("Invalid grid width: {}".format(width))
    padded_grid = np.zeros(shape=[30, 30], dtype=np.uint8)
    padded_grid[:height, :width] = grid
    grid_size = np.array([height, width], dtype=np.uint8)
    return padded_grid, grid_size


def crop_padded_grid(padded_grid, grid_size):
    """Crops a padded grid down to its original size."""
    return tf.slice(padded_grid, [0, 0], tf.cast(grid_size, tf.int32))


def pad_grid_pairs(pairs):
    """Pads every grid in a list of grid pairs.

    Args:
        pairs (list of dicts): the list of grid pairs. Each grid pair is
        represented as a dict with two keys: "input" and "output". Each value
        is a grid represented as a list of list of ints.

    Returns:
        padded_pairs (list of dicts): a list of pairs of padded grids with
        their size. Each pair is represented as a dict with four keys: "input",
        "input_size", "output" and "output_size". The "input" and "output"
        values are padded grids (30x30 NumPy uint8 arrays), and the
        "input_size" and "output_size" values are NumPy uint8 arrays of shape
        (2,) containing the original size of each grid (height, width).

    Raises:
        ValueError: see `pad_grid()`.
    """
    prepared_pairs = []
    for pair in pairs:
      input_grid, input_size = pad_grid(pair["input"])
      output_grid, output_size = pad_grid(pair["output"])
      prepared_pairs.append({
              "input": input_grid,
              "input_size": input_size,
              "output": output_grid,
              "output_size": output_size
          })
    return prepared_pairs


class ARC(tfds.core.GeneratorBasedBuilder):
  """The Abstraction and Reasoning Corpus (ARC)."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # Grids are of varying size
            "task_id": tfds.features.Text(),
            "train": tfds.features.Sequence({
                "input": tfds.features.Tensor(shape=(30, 30), dtype=tf.uint8),
                "input_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
                "output": tfds.features.Tensor(shape=(30, 30), dtype=tf.uint8),
                "output_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
            }),
            "test": tfds.features.Sequence({
                "input": tfds.features.Tensor(shape=(30, 30), dtype=tf.uint8),
                "input_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
                "output": tfds.features.Tensor(shape=(30, 30), dtype=tf.uint8),
                "output_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
            })
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_BASE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Downloads the data, defines the splits and returns SplitGenerators."""

    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    extracted_dir = dl_manager.download_and_extract(_DL_RESOURCE)
    data_dir = os.path.join(extracted_dir, _EXTRACT_SUBDIR, "data")
    train_dir = os.path.join(data_dir, "training")
    test_dir = os.path.join(data_dir, "evaluation")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "directory": train_dir,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "directory": test_dir,
            }),
    ]

  def _generate_examples(self, directory):
    """Yields (key, example) tuples from the dataset"""
    json_filepaths = tf.io.gfile.glob(os.path.join(directory, "*.json"))
    for json_path in sorted(json_filepaths):
        with tf.io.gfile.GFile(json_path) as f:
            task = json.load(f)
        task_id = os.path.basename(json_path)[:-len(".json")]
        try:
            yield task_id, {
                "task_id": task_id,
                "train": pad_grid_pairs(task["train"]),
                "test": pad_grid_pairs(task["test"]),
            }
        except (ValueError, TypeError) as ex:
            logging.exception("Could not load task {}.".format(task_id))
