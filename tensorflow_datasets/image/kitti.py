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

"""Kitti dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{Geiger2012CVPR,
  author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},
  title = {Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2012}
}
"""
_DESCRIPTION = """\
Kitti contains a suite of vision tasks built using an autonomous driving
platform. The full benchmark contains many tasks such as stereo, optical flow,
visual odometry, etc. This dataset contains the object detection dataset,
including the monocular images and bounding boxes. The dataset contains 7481
training images annotated with 3D bounding boxes. A full description of the
annotations can be found in the readme of the object development kit readme on
the Kitti homepage.
"""
_HOMEPAGE_URL = "http://www.cvlibs.net/datasets/kitti/"
_DATA_URL = "https://s3.eu-central-1.amazonaws.com/avg-kitti"
_IMAGES_FNAME = "data_object_image_2.zip"
_LABELS_FNAME = "data_object_label_2.zip"
_OBJECT_LABELS = [
    "Car",
    "Van",
    "Truck",
    "Pedestrian",
    "Person_sitting",
    "Cyclist",
    "Tram",
    "Misc",
]

# Raw Kitti representation of a bounding box. Coordinates are in pixels,
# measured from the top-left hand corner.
RawBoundingBox = collections.namedtuple("RawBoundingBox",
                                        ["top", "bottom", "left", "right"])


class Kitti(tfds.core.GeneratorBasedBuilder):
  """Kitti dataset."""

  VERSION = tfds.core.Version(
      "1.0.0", experiments={tfds.core.Experiment.S3: True})

  def _info(self):
    # Annotation descriptions are in the object development kit.
    annotations = {
        "type": tfds.features.ClassLabel(names=_OBJECT_LABELS),
        "truncated": tfds.features.Tensor(shape=(), dtype=tf.float32),
        "occluded": tfds.features.ClassLabel(num_classes=4),
        "alpha": tfds.features.Tensor(shape=(), dtype=tf.float32),
        "bbox": tfds.features.BBoxFeature(),
        "dimensions": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
        "location": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
        "rotation_y": tfds.features.Tensor(shape=(), dtype=tf.float32),
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/file_name": tfds.features.Text(),  # E.g. "000001.png".
            "objects": tfds.features.Sequence(annotations),
        }),
        urls=[_HOMEPAGE_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    filenames = {
        "images": os.path.join(_DATA_URL, _IMAGES_FNAME),
        "annotations": os.path.join(_DATA_URL, _LABELS_FNAME),
    }
    files = dl_manager.download(filenames)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images": dl_manager.iter_archive(files["images"]),
                "annotations": dl_manager.iter_archive(files["annotations"]),
                "subdir": "training",
            }),
    ]

  def _generate_examples(self, images, annotations, subdir):
    """Yields images and annotations.

    Args:
      images: object that iterates over the archive of images.
      annotations: object that iterates over the archive of annotations.
      subdir: subdirectory from which to extract images and annotations, e.g.
        training or testing.

    Yields:
      A tuple containing the example's key, and the example.
    """
    cv2 = tfds.core.lazy_imports.cv2

    all_annotations = dict()
    for fpath, fobj in annotations:
      prefix, ext = os.path.splitext(fpath)
      if ext != ".txt":
        continue
      if prefix.split("/")[0] != subdir:
        continue

      # Key is the datapoint id. E.g. training/label_2/label_000016 -> 16.
      all_annotations[int(prefix[-6:])] = _parse_kitti_annotations(fobj)

    for fpath, fobj in images:
      prefix, ext = os.path.splitext(fpath)
      if ext != ".png":
        continue
      if prefix.split("/")[0] != subdir:
        continue

      annotations = all_annotations[int(prefix[-6:])]
      img = cv2.imdecode(np.fromstring(fobj.read(), dtype=np.uint8),
                         cv2.IMREAD_COLOR)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      height, width, _ = img.shape
      for obj in annotations:
        obj["bbox"] = _build_bounding_box(obj["bbox_raw"], height, width)
        del obj["bbox_raw"]
      _, fname = os.path.split(fpath)
      record = {"image": img, "image/file_name": fname, "objects": annotations}
      yield fname, record


def _build_bounding_box(bbox, height, width):
  """Builds and returns TFDS bounding box.

  Args:
    bbox: RawBoundingBox, bounding box in Kitti coordinates (origin top left).
    height: Image height in pixels.
    width: Image width in pixels.

  Returns:
    A TFDS BBox (origin bottom left).
  """
  return tfds.features.BBox(
      ymin=(height - bbox.bottom) / height,
      ymax=(height - bbox.top) / height,
      xmin=bbox.left / width,
      xmax=bbox.right / width,
  )


def _parse_kitti_annotations(annotations_csv):
  """Loads and parses the Kitti object annotations.

  Args:
    annotations_csv: csv file containing annotations for a single image.

  Returns:
    A list of labelled bounding boxes. Each bounding box is stored as a
    dictionary of features.
  """
  annotations = []
  for line in annotations_csv:
    (obj_type, truncated, occluded, alpha, left, top, right, bottom, height,
     width, length, x, y, z,
     rotation_y) = list(csv.reader([line.decode()], delimiter=" "))[0]
    # DontCare objects lack annotations, so skip them.
    if obj_type == "DontCare":
      continue
    annotations.append({
        "type": obj_type,
        "truncated": float(truncated),
        "occluded": int(occluded),
        "alpha": float(alpha),
        "bbox_raw": RawBoundingBox(
            top=float(top),
            bottom=float(bottom),
            left=float(left),
            right=float(right)),
        "dimensions": [float(v) for v in [height, width, length]],
        "location": [float(v) for v in [x, y, z]],
        "rotation_y": float(rotation_y),
    })
  return annotations
