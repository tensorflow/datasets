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

"""Spoken Digit Dataset."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = "https://github.com/Jakobovski/free-spoken-digit-dataset/archive/v1.0.9.tar.gz"
_HOMEPAGE_URL = "https://github.com/Jakobovski/free-spoken-digit-dataset"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Spoken Digit Dataset."""

  VERSION = tfds.core.Version("1.0.9")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "audio": tfds.features.Audio(file_format="wav", sample_rate=8000),
            "label": tfds.features.ClassLabel(num_classes=10),
            "audio/filename": tfds.features.Text(),
        }),
        supervised_keys=("audio", "label"),
        homepage=_HOMEPAGE_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns Split Generators."""
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    extracted_dir_path = os.path.join(
        dl_path, "free-spoken-digit-dataset-1.0.9"
    )
    path = os.path.join(extracted_dir_path, "recordings")
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"path": path}
        )
    ]

  def _generate_examples(self, path):
    """Yields examples.

    Args:
       path: Path of the directory that contains audio files

    Yields:
       Next examples
    """
    for root, _, file_name in tf.io.gfile.walk(path):
      for fname in file_name:
        if fname.endswith(".wav"):  # Select only .wav files
          # Example of audio file name: 7_jackson_32.wav
          label = fname.split(".")[0].split("_")[0]
          key = fname.split(".")[0]
          example = {
              "audio": os.path.join(root, fname),
              "label": label,
              "audio/filename": fname,
          }
          yield key, example
