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

"""Utilities for dealing with tf.data.Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import tf_compat
from tensorflow_datasets.core import utils


WINDOW_SIZE = 100


def mask_to_instruction(mask):
  """Convert mask to dataset read instruction.

  Used for the split API to skip some examples. From a mask
  `[False * 20, True * 20, False * 80]`, the output will be:
  `{'skip': 20, 'take': 20}`

  Args:
    mask: `list[bool]`, a 100 element list of bool which specify which element
      of the dataset to read.

  Returns:
    `dict`: The instruction dict for the dataset reading pipeline
  """
  groups = [(k, len(list(v))) for k, v in itertools.groupby(mask)]
  if groups[0][0]:  # Eventually insert False at the beginning
    groups.insert(0, (False, 0))
  if groups[-1][0]:  # Eventually insert False at the end
    groups.append((False, 0))

  values = [k for k, _ in groups]
  counts = [v for _, v in groups]

  if (len(groups) != 3 or
      values[0] or      # 1st elem should be False
      not values[1] or  # 2nd elem should be True
      values[2] or         # 3rd elem should be False
      sum(counts) != WINDOW_SIZE
     ):
    raise AssertionError("Invalid mask parsing {} => {}".format(mask, groups))

  return {
      "skip": counts[0],
      "take": counts[1],
  }


def _transpose_list_dict(list_dict):
  """Transpose a list of nested dict into a nested dict of list."""
  struct = list_dict[0]
  struct_flat = tf.nest.flatten(struct)
  struct_flat = [[] for _ in struct_flat]

  for elem in list_dict:  # Add each elems to the flatten struct
    for field, x in zip(struct_flat, tf.nest.flatten(elem)):
      field.append(x)
  struct_flat = [
      np.array(s, dtype=np.int64)
      if isinstance(s[0], int) else s
      for s in struct_flat
  ]

  return tf.nest.pack_sequence_as(struct, struct_flat)


def build_dataset(instruction_dicts,
                  dataset_from_file_fn,
                  shuffle_files=False,
                  parallel_reads=64):
  """Constructs a `tf.data.Dataset` from TFRecord files.

  Args:
    instruction_dicts: `list` of {'filepath':, 'mask':}
      containing the information about which files and which examples to use.
      The boolean mask will be repeated and zipped with the examples from
      filepath.
    dataset_from_file_fn: function returning a `tf.data.Dataset` given a
      filename.
    shuffle_files: `bool`, Whether to shuffle the input filenames.
    parallel_reads: `int`, how many files to read in parallel.

  Returns:
    `tf.data.Dataset`
  """

  def instruction_to_dataset(instruction):
    """Map from instruction to real datasets."""
    # Create the dataset
    ds = dataset_from_file_fn(instruction["filepath"])

    # TODO(b/120126758): Here, we could apply an offset for each shards
    # like: ds = ds.skip(instruction['offset'])

    # Filter data according to the mask (only keep True)
    ds = ds.window(WINDOW_SIZE)
    def apply_mask(ds_window):
      ds_window = tf.data.Dataset.zip(ds_window)
      ds_window = ds_window.skip(instruction["mask_window"]["skip"])
      ds_window = ds_window.take(instruction["mask_window"]["take"])
      return ds_window
    ds = ds.flat_map(apply_mask)

    return ds

  # Transpose the list[dict] into dict[list]
  tensor_inputs = _transpose_list_dict(instruction_dicts)

  # Skip slicing if all masks are True (No value skipped)
  if all(v == WINDOW_SIZE for v in tensor_inputs["mask_window"]["take"]):
    tensor_inputs = tensor_inputs["filepath"]
    instruction_to_dataset = dataset_from_file_fn

  # Dataset of filenames (or file instructions)
  ds = tf.data.Dataset.from_tensor_slices(tensor_inputs)
  if shuffle_files:
    ds = ds.shuffle(len(instruction_dicts))
  # Use interleave to parallel read files and decode records
  ds = ds.interleave(
      instruction_to_dataset,
      cycle_length=parallel_reads,
      num_parallel_calls=tf.data.experimental.AUTOTUNE)
  return ds


def _eager_dataset_iterator(dataset):
  for item in dataset:
    flat = tf.nest.flatten(item)
    flat = [el.numpy() for el in flat]
    yield tf.nest.pack_sequence_as(item, flat)


def _graph_dataset_iterator(ds_item, graph=None):
  with utils.nogpu_session(graph) as sess:
    while True:
      try:
        yield sess.run(ds_item)
      except tf.errors.OutOfRangeError:
        break


@api_utils.disallow_positional_args(allowed=["dataset"])
def as_numpy(dataset, graph=None):
  """Converts a `tf.data.Dataset` to an iterable of NumPy arrays.

  `as_numpy` converts a possibly nested structure of `tf.data.Dataset`s
  and `tf.Tensor`s to iterables of NumPy arrays and NumPy arrays, respectively.

  Args:
    dataset: a possibly nested structure of `tf.data.Dataset`s and/or
      `tf.Tensor`s.
    graph: `tf.Graph`, optional, explicitly set the graph to use.

  Returns:
    A structure matching `dataset` where `tf.data.Dataset`s are converted to
    generators of NumPy arrays and `tf.Tensor`s are converted to NumPy arrays.
  """
  nested_ds = dataset
  del dataset

  # Flatten
  flat_ds = tf.nest.flatten(nested_ds)
  flat_np = []

  # Type check for Tensors and Datasets
  for ds_el in flat_ds:
    types = [type(el) for el in flat_ds]
    types = tf.nest.pack_sequence_as(nested_ds, types)
    if not (isinstance(ds_el, tf.Tensor) or tf_compat.is_dataset(ds_el)):
      raise ValueError("Arguments to as_numpy must be tf.Tensors or "
                       "tf.data.Datasets. Got: %s" % types)

  if tf.executing_eagerly():
    # Eager mode
    for ds_el in flat_ds:
      if isinstance(ds_el, tf.Tensor):
        np_el = ds_el.numpy()
      elif tf_compat.is_dataset(ds_el):
        np_el = _eager_dataset_iterator(ds_el)
      else:
        assert False
      flat_np.append(np_el)
  else:
    # Graph mode

    # First create iterators for datasets
    with utils.maybe_with_graph(graph, create_if_none=False):
      ds_iters = [
          tf.compat.v1.data.make_one_shot_iterator(ds_el).get_next()
          for ds_el in flat_ds if tf_compat.is_dataset(ds_el)
      ]
    ds_iters = [_graph_dataset_iterator(ds_iter, graph) for ds_iter in ds_iters]

    # Then create numpy arrays for tensors
    with utils.nogpu_session(graph) as sess:  # Shared session for tf.Tensor
      # Calling sess.run once so that randomness is shared.
      np_arrays = sess.run([tensor for tensor in flat_ds
                            if not tf_compat.is_dataset(tensor)])

    # Merge the dataset iterators and np arrays
    iter_ds = iter(ds_iters)
    iter_array = iter(np_arrays)
    flat_np = [
        next(iter_ds) if tf_compat.is_dataset(ds_el) else next(iter_array)
        for ds_el in flat_ds
    ]

  # Nest
  return tf.nest.pack_sequence_as(nested_ds, flat_np)
