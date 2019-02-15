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


import tensorflow as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import tf_compat
from tensorflow_datasets.core import utils


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

  def instruction_ds_to_file_ds(instruction):
    """Map from instruction to real datasets."""
    examples_ds = dataset_from_file_fn(instruction["filepath"])
    mask_ds = tf.data.Dataset.from_tensor_slices(instruction["mask"])
    mask_ds = mask_ds.repeat(),
    # Zip the mask and real examples
    ds = tf.data.Dataset.zip({
        "example": examples_ds,
        "mask_value": mask_ds,
    })
    # Filter according to the mask (only keep True)
    # Use [0] as from_tensor_slices() yields a tuple
    ds = ds.filter(lambda dataset_dict: dataset_dict["mask_value"][0])
    # Only keep the examples
    ds = ds.map(lambda dataset_dict: dataset_dict["example"])
    return ds

  # Transpose the list[dict] into dict[list]
  tensor_inputs = {
      key: list(values) for key, values in utils.zip_dict(*instruction_dicts)
  }
  # Skip slicing if all masks are True (No value skipped)
  if all(all(m) for m in tensor_inputs["mask"]):
    tensor_inputs = tensor_inputs["filepath"]
    instruction_ds_to_file_ds = dataset_from_file_fn

  # Dataset of filenames (or file instructions)
  dataset = tf.data.Dataset.from_tensor_slices(tensor_inputs)
  if shuffle_files:
    dataset = dataset.shuffle(len(instruction_dicts))
  # Use interleave to parallel read files and decode records
  dataset = dataset.interleave(
      instruction_ds_to_file_ds,
      cycle_length=parallel_reads,
      num_parallel_calls=tf.data.experimental.AUTOTUNE)
  return dataset


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
