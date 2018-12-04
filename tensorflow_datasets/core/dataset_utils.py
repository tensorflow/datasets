# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.core import utils

__all__ = [
    "build_dataset",
    "iterate_over_dataset",
]


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
    # TODO(rsepassi): Replace masking with window and flat_map
    # num, den = sum(mask), len(mask)
    # Something like (adjusting for nested structure):
    # examples_ds.window(den).flat_map(lambda ds: ds.take(num))

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


def iterate_over_dataset(dataset):
  """Yields numpy elements of `tf.data.Dataset`."""
  if tf.executing_eagerly():
    for item in dataset:
      flat = tf.contrib.framework.nest.flatten(item)
      flat = [el.numpy() for el in flat]
      yield tf.contrib.framework.nest.pack_sequence_as(item, flat)
  else:
    item = dataset.make_one_shot_iterator().get_next()
    with utils.nogpu_session() as sess:
      while True:
        try:
          yield sess.run(item)
        except tf.errors.OutOfRangeError:
          break
