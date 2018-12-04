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

"""https://www.kaggle.com/c/diabetic-retinopathy-detection/data.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class DiabeticRetinopathyDetection(
    tfds.core.GeneratorBasedDatasetBuilder):
  """Diabetic retinopathy detection."""

  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description="A large set of high-resolution retina images taken under "
        "a variety of imaging conditions.",
        version="1.0.0",
        features=tfds.features.FeaturesDict({
            "name": tfds.features.Text(),  # patient ID + eye. eg: "4_left".
            "image": tfds.features.Image(),
            # From 0 (no DR - saine) to 4 (Proliferative DR). -1 means no label.
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        urls=["https://www.kaggle.com/c/diabetic-retinopathy-detection/data"],
        size_in_bytes=97.0 * tfds.units.GiB,
    )

  def _split_generators(self, dl_manager):
    # TODO(pierrot): implement download using kaggle API.
    # TODO(pierrot): implement extraction of multiple files archives.
    path = dl_manager.manual_dir
    return [
        tfds.core.SplitGenerator(
            name="sample",  # 10 images, to do quicktests using dataset.
            num_shards=1,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "sample"),
            },
        ),
        tfds.core.SplitGenerator(
            name="train",
            num_shards=10,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "train"),
                "csv_path": os.path.join(path, "trainLabels.csv"),
            },
        ),
        tfds.core.SplitGenerator(
            name="test",
            num_shards=10,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "test"),
            },
        ),
    ]

  def _generate_examples(self, images_dir_path, csv_path=None):
    """Yields Example instances from given CSV.

    Args:
      images_dir_path: path to dir in which images are stored.
      csv_path: optional, path to csv file with two columns: name of image and
        label. If not provided, just scan image directory, don't set labels.
    """
    if csv_path:
      with tf.gfile.Open(csv_path) as csv_f:
        reader = csv.DictReader(csv_f)
        data = [(row["image"], int(row["level"])) for row in reader]
    else:
      data = [(fname[:-5], -1)
              for fname in tf.gfile.ListDirectory(images_dir_path)
              if fname.endswith(".jpeg")]
    for name, label in data:
      yield self.info.features.encode_example({
          "name": name,
          "image": "%s/%s.jpeg" % (images_dir_path, name),
          "label": label,
      })
