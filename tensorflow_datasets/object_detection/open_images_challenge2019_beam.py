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
"""Classes and functions to generate the OI Challenge 2019 dataset using Apache Beam."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import io
import json
import os

from absl import logging
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

beam = tfds.core.lazy_imports.apache_beam
cv2 = tfds.core.lazy_imports.cv2

Metrics = beam.metrics.Metrics


class ReadZipFn(beam.DoFn):
  """Iterates a zip file, yielding filenames and file contents."""

  def process(self, zip_filepath):
    for filename, file in tfds.download.iter_archive(
        zip_filepath, tfds.download.ExtractMethod.ZIP):
      if filename.endswith(".jpg"):
        yield filename, file.read()


class ProcessImageFn(beam.DoFn):
  """Resizes images, re-compresses them in JPEG and yields the result."""

  def __init__(self, target_pixels, jpeg_quality=72):
    self._target_pixels = target_pixels
    self._jpeg_quality = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
    self._images_failed = Metrics.counter(self.__class__, "images_failed")

  def process(self, element):
    filename, content = element
    try:
      image = cv2.imdecode(np.fromstring(content, dtype=np.uint8), flags=3)
    except:
      logging.info("Exception raised while decoding image %s", filename)
      raise
    if image is None:
      self._images_failed.inc()
      logging.info("Image %s could not be decoded", filename)
    else:
      # GIF images contain a single frame.
      if len(image.shape) == 4:  # rank=4 -> rank=3
        image = image.reshape(image.shape[1:])
      # Get image height and width.
      height, width, _ = image.shape
      actual_pixels = height * width
      # If necessary, resize the image to have at most self._target_pixels,
      # keeping the aspect ratio.
      if self._target_pixels and actual_pixels > self._target_pixels:
        factor = np.sqrt(self._target_pixels / actual_pixels)
        image = cv2.resize(image, dsize=None, fx=factor, fy=factor)
      # Encode the image with quality=72 and store it in a BytesIO object.
      _, buff = cv2.imencode(".jpg", image, self._jpeg_quality)
      yield filename, io.BytesIO(buff.tostring())


class CreateDetectionExampleFn(beam.DoFn):
  """Creates TFDS examples for the Detection track."""

  def __init__(self, image_labels_filepath, box_labels_filepath,
               hierarchy_filepath, classes_filepath):
    self._image_labels_filepath = image_labels_filepath
    self._box_labels_filepath = box_labels_filepath
    self._hierarchy_filepath = hierarchy_filepath
    self._classes_filepath = classes_filepath
    self._image2labels = None
    self._image2boxes = None
    self._hierarchy = None
    self._mid2int = None

  def start(self):
    if self._image_labels_filepath:
      self._image2labels = load_image_level_labels(self._image_labels_filepath)
    if self._box_labels_filepath:
      self._image2boxes = load_box_level_labels(self._box_labels_filepath)
    if self._hierarchy_filepath:
      self._hierarchy = load_class_hierarchy(self._hierarchy_filepath)
    if self._classes_filepath:
      class_descriptions = load_class_descriptions(self._classes_filepath)
      self._mid2int = {mid: i for i, (mid, _) in enumerate(class_descriptions)}

  def process(self, element):
    filename, image_bytes = element
    image_id = os.path.basename(filename).split(".")[0]
    # Image-level annotations.
    objects = []
    if self._image2labels:
      for label, source, confidence in self._image2labels[image_id]:
        objects.append({
            "label": self._mid2int[label],
            "source": source,
            "confidence": confidence,
        })
    # Bounding box-level annotations.
    bobjects = []
    if self._image2boxes:
      for annotation in self._image2boxes[image_id]:
        label, xmin, xmax, ymin, ymax, is_group_of = annotation
        bbox = tfds.features.BBox(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
        bobjects.append({
            "label": self._mid2int[label],
            "bbox": bbox,
            "is_group_of": is_group_of,
        })

    yield image_id, {
        "id": image_id,
        "image": image_bytes,
        "objects": objects,
        "bobjects": bobjects,
    }


def load_image_level_labels(filepath):
  """Returns a dictionary mapping image IDs to a list of image-level labels."""
  image2labels = collections.defaultdict(list)
  with tf.io.gfile.GFile(filepath, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header.
    for row in reader:
      if len(row) == 3:
        image_id, label, confidence = row
        source = "verification"
      elif len(row) == 4:
        image_id, source, label, confidence = row
      image2labels[image_id].append((label, source, float(confidence)))
  return image2labels


def load_box_level_labels(filepath):
  """Returns a dictionary mapping image IDs to a list of bounding box annotations."""
  image2boxes = collections.defaultdict(list)
  with tf.io.gfile.GFile(filepath, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header.
    for row in reader:
      if len(row) == 7:
        image_id, label, xmin_s, xmax_s, ymin_s, ymax_s, is_group_of_s = row
      elif len(row) == 13:
        image_id, label = row[0], row[2]
        xmin_s, xmax_s, ymin_s, ymax_s = row[4:8]
        is_group_of_s = row[10]
      xmin, xmax, ymin, ymax = map(float, (xmin_s, xmax_s, ymin_s, ymax_s))
      is_group_of = bool(int(is_group_of_s))
      image2boxes[image_id].append((label, xmin, xmax, ymin, ymax, is_group_of))
  return image2boxes


def load_class_hierarchy(filepath):
  with tf.io.gfile.GFile(filepath, "r") as jsonfile:
    return json.load(jsonfile)


def load_class_descriptions(filepath):
  with tf.io.gfile.GFile(filepath, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Note: this file doesn't have any header.
    return [row for row in reader]


def fill_class_names_in_tfds_info(classes_filepath, tfds_info_features):
  """Fills the class names in ClassLabel features."""
  class_descriptions = load_class_descriptions(classes_filepath)
  mids = [mid for mid, _ in class_descriptions]
  tfds_info_features["objects"]["label"].names = mids
  tfds_info_features["bobjects"]["label"].names = mids
