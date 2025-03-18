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

"""Shapes3D dataset."""

import numpy as np
import tensorflow_datasets.public_api as tfds

_URL = "https://storage.googleapis.com/3d-shapes/3dshapes.h5"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Shapes3d data set."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(64, 64, 3)),
            "label_floor_hue": tfds.features.ClassLabel(num_classes=10),
            "label_wall_hue": tfds.features.ClassLabel(num_classes=10),
            "label_object_hue": tfds.features.ClassLabel(num_classes=10),
            "label_scale": tfds.features.ClassLabel(num_classes=8),
            "label_shape": tfds.features.ClassLabel(num_classes=4),
            "label_orientation": tfds.features.ClassLabel(num_classes=15),
            "value_floor_hue": tfds.features.Tensor(shape=[], dtype=np.float32),
            "value_wall_hue": tfds.features.Tensor(shape=[], dtype=np.float32),
            "value_object_hue": tfds.features.Tensor(
                shape=[], dtype=np.float32
            ),
            "value_scale": tfds.features.Tensor(shape=[], dtype=np.float32),
            "value_shape": tfds.features.Tensor(shape=[], dtype=np.float32),
            "value_orientation": tfds.features.Tensor(
                shape=[], dtype=np.float32
            ),
        }),
        homepage="https://github.com/deepmind/3d-shapes",
    )

  def _split_generators(self, dl_manager):
    filepath = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs=dict(filepath=filepath)
        ),
    ]

  def _generate_examples(self, filepath):
    """Generate examples for the Shapes3d dataset.

    Args:
      filepath: path to the Shapes3d hdf5 file.

    Yields:
      Dictionaries with images and the different labels.
    """
    # Simultaneously iterating through the different data sets in the hdf5
    # file will be slow with a single file. Instead, we first load everything
    # into memory before yielding the samples.
    with tfds.core.lazy_imports.h5py.File(filepath, "r") as h5dataset:
      image_array = np.array(h5dataset["images"])
      # The 'label' data set in the hdf5 file actually contains the float values
      # and not the class labels.
      values_array = np.array(h5dataset["labels"])

    # We need to calculate the class labels from the float values in the file.
    labels_array = np.zeros_like(values_array, dtype=np.int64)
    for i in range(values_array.shape[1]):
      labels_array[:, i] = _discretize(values_array[:, i])  # pylint: disable=unsupported-assignment-operation

    for i, (image, labels, values) in enumerate(
        zip(image_array, labels_array, values_array)
    ):
      record = {
          "image": image,
          "label_floor_hue": labels[0],
          "label_wall_hue": labels[1],
          "label_object_hue": labels[2],
          "label_scale": labels[3],
          "label_shape": labels[4],
          "label_orientation": labels[5],
          "value_floor_hue": values[0],
          "value_wall_hue": values[1],
          "value_object_hue": values[2],
          "value_scale": values[3],
          "value_shape": values[4],
          "value_orientation": values[5],
      }
      yield i, record


def _discretize(a):
  """Discretizes array values to class labels."""
  arr = np.asarray(a)
  index = np.argsort(arr)
  inverse_index = np.zeros(arr.size, dtype=np.intp)
  inverse_index[index] = np.arange(arr.size, dtype=np.intp)
  arr = arr[index]
  obs = np.r_[True, arr[1:] != arr[:-1]]
  return obs.cumsum()[inverse_index] - 1
