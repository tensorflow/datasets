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

"""https://www.kaggle.com/c/diabetic-retinopathy-detection/data.
"""

import csv
import io
import os

from absl import logging
import numpy as np
import tensorflow.compat.v2 as tf
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
_BTGRAHAM_DESCRIPTION_PATTERN = (
    "Images have been preprocessed as the winner of the Kaggle competition did "
    "in 2015: first they are resized so that the radius of an eyeball is "
    "{} pixels, then they are cropped to 90% of the radius, and finally they "
    "are encoded with 72 JPEG quality.")


class DiabeticRetinopathyDetectionConfig(tfds.core.BuilderConfig):
  """BuilderConfig for DiabeticRetinopathyDetection."""

  def __init__(self, target_pixels=None, **kwargs):
    """BuilderConfig for DiabeticRetinopathyDetection.

    Args:
      target_pixels: If given, rescale the images so that the total number of
        pixels is roughly this value.
      **kwargs: keyword arguments forward to super.
    """
    super(DiabeticRetinopathyDetectionConfig, self).__init__(
        version=tfds.core.Version("3.0.0"),
        release_notes={
            "3.0.0": "New split API (https://tensorflow.org/datasets/splits)",
        },
        **kwargs)
    self._target_pixels = target_pixels

  @property
  def target_pixels(self):
    return self._target_pixels


class DiabeticRetinopathyDetection(tfds.core.GeneratorBasedBuilder):
  """Diabetic retinopathy detection."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You have to download this dataset from Kaggle.
  https://www.kaggle.com/c/diabetic-retinopathy-detection/data
  After downloading, unpack the test.zip file into test/ directory in manual_dir
  and sample.zip to sample/. Also unpack the sampleSubmissions.csv and
  trainLabels.csv.
  """

  BUILDER_CONFIGS = [
      DiabeticRetinopathyDetectionConfig(
          name="original",
          description="Images at their original resolution and quality."),
      DiabeticRetinopathyDetectionConfig(
          name="1M",
          description="Images have roughly 1,000,000 pixels, at 72 quality.",
          target_pixels=1000000),
      DiabeticRetinopathyDetectionConfig(
          name="250K",
          description="Images have roughly 250,000 pixels, at 72 quality.",
          target_pixels=250000),
      DiabeticRetinopathyDetectionConfig(
          name="btgraham-300",
          description=_BTGRAHAM_DESCRIPTION_PATTERN.format(300),
          target_pixels=300),
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
        homepage="https://www.kaggle.com/c/diabetic-retinopathy-detection/data",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    # TODO(pierrot): implement download using kaggle API.
    # TODO(pierrot): implement extraction of multiple files archives.
    path = dl_manager.manual_dir
    test_labels_path = dl_manager.download(_URL_TEST_LABELS)
    if tf.io.gfile.isdir(test_labels_path):
      # While testing: download() returns the dir containing the tests files.
      test_labels_path = os.path.join(test_labels_path,
                                      "retinopathy_solution.csv")
    return [
        tfds.core.SplitGenerator(
            name="sample",  # 10 images, to do quicktests using dataset.
            gen_kwargs={
                "images_dir_path": os.path.join(path, "sample"),
            },
        ),
        tfds.core.SplitGenerator(
            name="train",
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
      image_filepath = "%s/%s.jpeg" % (images_dir_path, name)
      record = {
          "name": name,
          "image": self._process_image(image_filepath),
          "label": label,
      }
      yield name, record

  def _process_image(self, filepath):
    with tf.io.gfile.GFile(filepath, mode="rb") as image_fobj:
      if self.builder_config.name.startswith("btgraham"):
        return _btgraham_processing(
            image_fobj=image_fobj,
            filepath=filepath,
            target_pixels=self.builder_config.target_pixels,
            crop_to_radius=True)
      else:
        return _resize_image_if_necessary(
            image_fobj=image_fobj,
            target_pixels=self.builder_config.target_pixels)


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


def _btgraham_processing(
    image_fobj, filepath, target_pixels, crop_to_radius=False):
  """Process an image as the winner of the 2015 Kaggle competition.

  Args:
    image_fobj: File object containing the original image.
    filepath: Filepath of the image, for logging purposes only.
    target_pixels: The number of target pixels for the radius of the image.
    crop_to_radius: If True, crop the borders of the image to remove gray areas.

  Returns:
    A file object.
  """
  cv2 = tfds.core.lazy_imports.cv2
  # Decode image using OpenCV2.
  image = cv2.imdecode(
      np.fromstring(image_fobj.read(), dtype=np.uint8), flags=3)
  # Process the image.
  image = _scale_radius_size(image, filepath, target_radius_size=target_pixels)
  image = _subtract_local_average(image, target_radius_size=target_pixels)
  image = _mask_and_crop_to_radius(
      image, target_radius_size=target_pixels, radius_mask_ratio=0.9,
      crop_to_radius=crop_to_radius)
  # Encode the image with quality=72 and store it in a BytesIO object.
  _, buff = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 72])
  return io.BytesIO(buff.tostring())


def _scale_radius_size(image, filepath, target_radius_size):
  """Scale the input image so that the radius of the eyeball is the given."""
  cv2 = tfds.core.lazy_imports.cv2
  x = image[image.shape[0] // 2, :, :].sum(axis=1)
  r = (x > x.mean() / 10.0).sum() / 2.0
  if r < 1.0:
    # Some images in the dataset are corrupted, causing the radius heuristic to
    # fail. In these cases, just assume that the radius is the height of the
    # original image.
    logging.info("Radius of image \"%s\" could not be determined.", filepath)
    r = image.shape[0] / 2.0
  s = target_radius_size / r
  return cv2.resize(image, dsize=None, fx=s, fy=s)


def _subtract_local_average(image, target_radius_size):
  cv2 = tfds.core.lazy_imports.cv2
  image_blurred = cv2.GaussianBlur(image, (0, 0), target_radius_size / 30)
  image = cv2.addWeighted(image, 4, image_blurred, -4, 128)
  return image


def _mask_and_crop_to_radius(
    image, target_radius_size, radius_mask_ratio=0.9, crop_to_radius=False):
  """Mask and crop image to the given radius ratio."""
  cv2 = tfds.core.lazy_imports.cv2
  mask = np.zeros(image.shape)
  center = (image.shape[1]//2, image.shape[0]//2)
  radius = int(target_radius_size * radius_mask_ratio)
  cv2.circle(mask, center=center, radius=radius, color=(1, 1, 1), thickness=-1)
  image = image * mask + (1 - mask) * 128
  if crop_to_radius:
    x_max = min(image.shape[1] // 2 + radius, image.shape[1])
    x_min = max(image.shape[1] // 2 - radius, 0)
    y_max = min(image.shape[0] // 2 + radius, image.shape[0])
    y_min = max(image.shape[0] // 2 - radius, 0)
    image = image[y_min:y_max, x_min:x_max, :]
  return image
