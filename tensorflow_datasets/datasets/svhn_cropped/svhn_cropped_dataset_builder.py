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

"""Street View House Numbers (SVHN) Dataset, cropped version."""
import urllib

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

URL = "http://ufldl.stanford.edu/housenumbers/"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Street View House Numbers (SVHN) Dataset, cropped version."""

  VERSION = tfds.core.Version("3.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("3.1.0"),
  ]
  RELEASE_NOTES = {
      "3.1.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    features_dict = {
        "image": tfds.features.Image(shape=(32, 32, 3)),
        "label": tfds.features.ClassLabel(num_classes=10),
    }
    if self.version > "3.0.0":
      features_dict["id"] = tfds.features.Text()
    return self.dataset_info_from_configs(
        description=(
            "The Street View House Numbers (SVHN) Dataset is an image digit "
            "recognition dataset of over 600,000 digit images coming from "
            "real world data. Images are cropped to 32x32."
        ),
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=("image", "label"),
        homepage=URL,
    )

  def _split_generators(self, dl_manager):
    output_files = dl_manager.download({
        "train": urllib.parse.urljoin(URL, "train_32x32.mat"),
        "test": urllib.parse.urljoin(URL, "test_32x32.mat"),
        "extra": urllib.parse.urljoin(URL, "extra_32x32.mat"),
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                split_prefix="train_",
                filepath=output_files["train"],
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                split_prefix="test_",
                filepath=output_files["test"],
            ),
        ),
        tfds.core.SplitGenerator(
            name="extra",
            gen_kwargs=dict(
                split_prefix="extra_",
                filepath=output_files["extra"],
            ),
        ),
    ]

  def _generate_examples(self, split_prefix, filepath):
    """Generate examples as dicts.

    Args:
      split_prefix: `str` prefix that identifies the split.
      filepath: `str` path of the file to process.

    Yields:
      Generator yielding the next samples
    """
    with tf.io.gfile.GFile(filepath, "rb") as f:
      data = tfds.core.lazy_imports.scipy.io.loadmat(f)

    # Maybe should shuffle ?

    assert np.max(data["y"]) <= 10  # Sanity check
    assert np.min(data["y"]) > 0

    for i, (image, label) in enumerate(
        zip(np.rollaxis(data["X"], -1), data["y"])
    ):
      label = label.reshape(())
      record = {
          "image": image,
          "label": label % 10,  # digit 0 is saved as 0 (instead of 10)
      }
      if self.version > "3.0.0":
        record["id"] = "{}{:06d}".format(split_prefix, i)
      yield i, record


# TODO(tfds): Add the SvhnFull dataset
