# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Utilities for dealing with tf.data.Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import itertools

import numpy as np
import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import tf_compat
from tensorflow_datasets.core import utils


def build_dataset(instruction_dicts,
                  dataset_from_file_fn,
                  shuffle_files=False,
                  parallel_reads=64):
  """Constructs a `tf.data.Dataset` from TFRecord files.

  Args:
    instruction_dicts: `list` of {'filepath':, 'mask':, 'offset_mask':}
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

  # First case: All examples are taken (No value skipped)
  if _no_examples_skipped(instruction_dicts):
    # Only use the filenames as instruction
    instruction_ds = tf.data.Dataset.from_tensor_slices([
        d["filepath"] for d in instruction_dicts
    ])
    build_ds_from_instruction = dataset_from_file_fn
  # Second case: Use the instructions to read the examples
  else:
    instruction_ds = _build_instruction_ds(instruction_dicts)
    build_ds_from_instruction = functools.partial(
        _build_ds_from_instruction,
        ds_from_file_fn=dataset_from_file_fn,
    )

  # If shuffle is True, we shuffle the instructions/shards
  if shuffle_files:
    instruction_ds = instruction_ds.shuffle(len(instruction_dicts))

  # Use interleave to parallel read files and decode records
  ds = instruction_ds.interleave(
      build_ds_from_instruction,
      cycle_length=parallel_reads,
      num_parallel_calls=tf.data.experimental.AUTOTUNE)
  return ds


def _no_examples_skipped(list_of_dict):
  """Return True if no examples are skipped (mask are only True)."""
  return all(itertools.chain.from_iterable([d["mask"] for d in list_of_dict]))


def _build_instruction_ds(instructions):
  """Create a dataset containing individual instruction for each shard.

  Each instruction is a dict:
  ```
  {
      "filepath": tf.Tensor(shape=(), dtype=tf.string),
      "mask_offset": tf.Tensor(shape=(), dtype=tf.int64),
      "mask": tf.Tensor(shape=(100,), dtype=tf.bool),
  }
  ```

  Args:
    instructions: `list[dict]`, the list of instruction dict

  Returns:
    instruction_ds: The dataset containing the instruction. The dataset size is
      the number of shard.
  """
  # Transpose the list[dict] into dict[list]
  tensor_inputs = {
      # offset_mask need to be converted to int64 explicitly
      k: np.array(vals, dtype=np.int64) if k == "mask_offset" else list(vals)
      for k, vals in utils.zip_dict(*instructions)
  }
  return tf.data.Dataset.from_tensor_slices(tensor_inputs)


def _build_mask_ds(mask, mask_offset):
  """Build the mask dataset to indicate which element to skip.

  Args:
    mask: `tf.Tensor`, binary mask to apply to all following elements. This
      mask should have a length 100.
    mask_offset: `tf.Tensor`, Integer specifying from how much the mask
      should be shifted for the first element.

  Returns:
    mask_ds: `tf.data.Dataset`, a dataset returning False for examples to skip
      and True for examples to keep.
  """
  mask_ds = tf.data.Dataset.from_tensor_slices(mask)
  mask_ds = mask_ds.repeat()
  mask_ds = mask_ds.skip(mask_offset)
  return mask_ds


def _build_ds_from_instruction(instruction, ds_from_file_fn):
  """Map an instruction to a real datasets for one particular shard.

  Args:
    instruction: A `dict` of `tf.Tensor` containing the instruction to load
      the particular shard (filename, mask,...)
    ds_from_file_fn: `fct`, function which returns the dataset associated to
      the filename

  Returns:
    dataset: `tf.data.Dataset`, The shard loaded from the instruction
  """
  # Create the example and mask ds for this particular shard
  examples_ds = ds_from_file_fn(instruction["filepath"])
  mask_ds = _build_mask_ds(
      mask_offset=instruction["mask_offset"],
      mask=instruction["mask"],
  )

  # Zip the mask and real examples
  ds = tf.data.Dataset.zip((examples_ds, mask_ds))
  # Filter according to the mask (only keep True)
  ds = ds.filter(lambda example, mask: mask)
  # Only keep the examples
  ds = ds.map(lambda example, mask: example)
  return ds


def _eager_dataset_iterator(dataset):
  for item in dataset:
    flat = tf.nest.flatten(item)
    flat = [t if isinstance(t, tf.RaggedTensor) else t.numpy() for t in flat]
    yield tf.nest.pack_sequence_as(item, flat)


def _graph_dataset_iterator(ds_iter, graph=None):
  """Constructs a Python generator from a tf.data.Iterator."""
  with utils.maybe_with_graph(graph, create_if_none=False):
    init = ds_iter.initializer
    ds_item = ds_iter.get_next()
  with utils.nogpu_session(graph) as sess:
    sess.run(init)
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

  Note that because TensorFlow has support for ragged tensors and NumPy has
  no equivalent representation,
  [`tf.RaggedTensor`s](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
  are left as-is for the user to deal with them (e.g. using `to_list()`).
  In TF 1 (i.e. graph mode), `tf.RaggedTensor`s are returned as
  `tf.ragged.RaggedTensorValue`s.

  Example:

  ```
  ds = tfds.load(name="mnist", split="train")
  ds_numpy = tfds.as_numpy(ds)  # Convert `tf.data.Dataset` to Python generator
  for ex in ds_numpy:
    # `{'image': np.array(shape=(28, 28, 1)), 'labels': np.array(shape=())}`
    print(ex)
  ```

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
    if not (
        isinstance(ds_el, (tf.Tensor, tf.RaggedTensor)) or
        tf_compat.is_dataset(ds_el)):
      raise ValueError("Arguments to as_numpy must be tf.Tensors or "
                       "tf.data.Datasets. Got: %s" % types)

  if tf.executing_eagerly():
    # Eager mode
    for ds_el in flat_ds:
      if isinstance(ds_el, tf.Tensor):
        np_el = ds_el.numpy()
      elif isinstance(ds_el, tf.RaggedTensor):
        np_el = ds_el
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
          tf.compat.v1.data.make_initializable_iterator(ds_el)
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


def dataset_shape_is_fully_defined(ds):
  output_shapes = tf.compat.v1.data.get_output_shapes(ds)
  return all([ts.is_fully_defined() for ts in tf.nest.flatten(output_shapes)])


def features_shape_is_fully_defined(features):
  return all([tf.TensorShape(info.shape).is_fully_defined() for info in
              tf.nest.flatten(features.get_tensor_info())])
