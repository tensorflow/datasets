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

"""https://www.kaggle.com/c/diabetic-retinopathy-detection/data.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import io
import os

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """\
@ONLINE {kaggle-diabetic-retinopathy,
    author = "Kaggle and EyePacs",
    title  = "Kaggle Diabetic Retinopathy Detection",
    month  = "jul",
    year   = "2015",
    url    = "https://www.kaggle.com/c/diabetic-retinopathy-detection/data"
}
"""
_URL_TEST_LABELS = "https://storage.googleapis.com/kaggle-forum-message-attachments/90528/2877/retinopathy_solution.csv"


class DiabeticRetinopathyDetectionConfig(tfds.core.BuilderConfig):
  """BuilderConfig for DiabeticRetinopathyDetection."""

  def __init__(self, target_pixels=None, **kwargs):
    """BuilderConfig for DiabeticRetinopathyDetection.

    Args:
      target_pixels: If given, rescale the images so that the total number of
        pixels is roughly this value.
      **kwargs: keyword arguments forward to super.
    """
    super(DiabeticRetinopathyDetectionConfig, self).__init__(**kwargs)
    self._target_pixels = target_pixels

  @property
  def target_pixels(self):
    return self._target_pixels


class DiabeticRetinopathyDetection(tfds.core.GeneratorBasedBuilder):
  """Diabetic retinopathy detection."""

  BUILDER_CONFIGS = [
      DiabeticRetinopathyDetectionConfig(
          name="original",
          version="2.0.0",
          description="Images at their original resolution and quality."),
      DiabeticRetinopathyDetectionConfig(
          name="1M",
          version="2.1.0",
          description="Images have roughly 1,000,000 pixels, at 72 quality.",
          target_pixels=1000000),
      DiabeticRetinopathyDetectionConfig(
          name="250K",
          version="2.1.0",
          description="Images have roughly 250,000 pixels, at 72 quality.",
          target_pixels=250000),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A large set of high-resolution retina images taken under "
        "a variety of imaging conditions.",
        features=tfds.features.FeaturesDict({
            "name": tfds.features.Text(),  # patient ID + eye. eg: "4_left".
            "image": tfds.features.Image(),
            # From 0 (no DR - saine) to 4 (Proliferative DR). -1 means no label.
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        urls=["https://www.kaggle.com/c/diabetic-retinopathy-detection/data"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    # TODO(pierrot): implement download using kaggle API.
    # TODO(pierrot): implement extraction of multiple files archives.
    path = dl_manager.manual_dir
    test_labels_path = dl_manager.download(_URL_TEST_LABELS)
    if os.path.isdir(test_labels_path):
       # While testing: download() returns the dir containing the tests files.
      test_labels_path = os.path.join(test_labels_path,
                                      "retinopathy_solution.csv")
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
            num_shards=100,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "train"),
                "csv_path": os.path.join(path, "trainLabels.csv"),
                # CSV of the train split does not have the "Usage" column.
                # 35,126 examples.
                "csv_usage": None,
            },
        ),
        tfds.core.SplitGenerator(
            name="validation",
            num_shards=100,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "test"),
                "csv_path": test_labels_path,
                # Validation split corresponds to the public leaderboard data.
                # 10,906 examples.
                "csv_usage": "Public",
            },
        ),
        tfds.core.SplitGenerator(
            name="test",
            num_shards=100,
            gen_kwargs={
                "images_dir_path": os.path.join(path, "test"),
                "csv_path": test_labels_path,
                # Test split corresponds to the public leaderboard data.
                # 42,670 examples.
                "csv_usage": "Private",
            },
        ),
    ]

  def _generate_examples(self, images_dir_path, csv_path=None, csv_usage=None):
    """Yields Example instances from given CSV.

    Args:
      images_dir_path: path to dir in which images are stored.
      csv_path: optional, path to csv file with two columns: name of image and
        label. If not provided, just scan image directory, don't set labels.
      csv_usage: optional, subset of examples from the csv file to use based on
        the "Usage" column from the csv.
    """
    if csv_path:
      with tf.io.gfile.GFile(csv_path) as csv_f:
        reader = csv.DictReader(csv_f)
        data = [(row["image"], int(row["level"]))
                for row in reader
                if csv_usage is None or row["Usage"] == csv_usage]
    else:
      data = [(fname[:-5], -1)
              for fname in tf.io.gfile.listdir(images_dir_path)
              if fname.endswith(".jpeg")]
    for name, label in data:
      yield {
          "name": name,
          "image": _resize_image_if_necessary(
              tf.io.gfile.GFile("%s/%s.jpeg" % (images_dir_path, name),
                                mode="rb"),
              target_pixels=self.builder_config.target_pixels),
          "label": label,
      }


def _resize_image_if_necessary(image_fobj, target_pixels=None):
  """Resize an image to have (roughly) the given number of target pixels.

  Args:
    image_fobj: File object containing the original image.
    target_pixels: If given, number of pixels that the image must have.

  Returns:
    A file object.
  """
  if target_pixels is None:
    return image_fobj

  cv2 = tfds.core.lazy_imports.cv2
  # Decode image using OpenCV2.
  image = cv2.imdecode(
      np.fromstring(image_fobj.read(), dtype=np.uint8), flags=3)
  # Get image height and width.
  height, width, _ = image.shape
  actual_pixels = height * width
  if actual_pixels > target_pixels:
    factor = np.sqrt(target_pixels / actual_pixels)
    image = cv2.resize(image, dsize=None, fx=factor, fy=factor)
  # Encode the image with quality=72 and store it in a BytesIO object.
  _, buff = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 72])
  return io.BytesIO(buff.tostring())
