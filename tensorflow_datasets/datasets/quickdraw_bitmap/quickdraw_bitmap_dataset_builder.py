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

"""QuickDraw dataset."""

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_QUICKDRAW_IMAGE_SIZE = 28
_QUICKDRAW_IMAGE_SHAPE = (_QUICKDRAW_IMAGE_SIZE, _QUICKDRAW_IMAGE_SIZE, 1)
_QUICKDRAW_BASE_URL = (
    "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap"  # pylint: disable=line-too-long
)
_QUICKDRAW_LABELS_FNAME = "datasets/quickdraw_bitmap/labels.txt"

_URL = "https://github.com/googlecreativelab/quickdraw-dataset"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Quickdraw bitmap dataset.

  This is the version of the QuickDraw data in which 28x28 grayscale images
  are generated from the raw vector information (i.e. the 'bitmap' dataset, not
  the 'raw' or 'simplified drawings' datasets).
  """

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    labels_path = tfds.core.tfds_path(_QUICKDRAW_LABELS_FNAME)
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_QUICKDRAW_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names_file=labels_path),
        }),
        supervised_keys=("image", "label"),
        homepage=_URL,
    )

  def _split_generators(self, dl_manager):
    # The QuickDraw bitmap repository is structured as one .npy file per label.
    labels = self.info.features["label"].names
    urls = {
        label: "{}/{}.npy".format(_QUICKDRAW_BASE_URL, label)
        for label in labels
    }

    file_paths = dl_manager.download(urls)

    # There is no predefined train/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "file_paths": file_paths,
            },
        )
    ]

  def _generate_examples(self, file_paths):
    """Generate QuickDraw bitmap examples.

    Given a list of file paths with data for each class label, generate examples
    in a random order.

    Args:
      file_paths: (dict of {str: str}) the paths to files containing the data,
        indexed by label.

    Yields:
      The QuickDraw examples, as defined in the dataset info features.
    """
    for label, path in sorted(file_paths.items(), key=lambda x: x[0]):
      with tf.io.gfile.GFile(path, "rb") as f:
        class_images = np.load(f)
        for i, np_image in enumerate(class_images):
          record = {
              "image": np_image.reshape(_QUICKDRAW_IMAGE_SHAPE),
              "label": label,
          }
          yield "%s_%i" % (label, i), record
