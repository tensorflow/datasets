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

"""Kitti dataset."""

import collections
import csv
import os
import numpy as np
import tensorflow.compat.v2 as tf
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
_DEVKIT_FNAME = "devkit_object.zip"
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
# The percentage of trainset videos to put into validation and test sets.
# The released test images do not have labels.
_VALIDATION_SPLIT_PERCENT_VIDEOS = 10
_TEST_SPLIT_PERCENT_VIDEOS = 10

# Raw Kitti representation of a bounding box. Coordinates are in pixels,
# measured from the top-left hand corner.
RawBoundingBox = collections.namedtuple("RawBoundingBox",
                                        ["top", "bottom", "left", "right"])


class Kitti(tfds.core.GeneratorBasedBuilder):
  """Kitti dataset."""

  VERSION = tfds.core.Version("3.2.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("3.1.0"),
  ]
  RELEASE_NOTES = {
      "3.2.0": "Devkit updated."
  }

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
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    filenames = {
        "images": _DATA_URL + "/" + _IMAGES_FNAME,
        "annotations": _DATA_URL + "/" + _LABELS_FNAME,
        "devkit": _DATA_URL + "/" + _DEVKIT_FNAME,
    }
    files = dl_manager.download(filenames)
    train_images, validation_images, test_images = _build_splits(
        dl_manager.iter_archive(files["devkit"]))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images": dl_manager.iter_archive(files["images"]),
                "annotations": dl_manager.iter_archive(files["annotations"]),
                "subdir": "training",
                "image_ids": train_images,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "images": dl_manager.iter_archive(files["images"]),
                "annotations": dl_manager.iter_archive(files["annotations"]),
                "subdir": "training",
                "image_ids": validation_images,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images": dl_manager.iter_archive(files["images"]),
                "annotations": dl_manager.iter_archive(files["annotations"]),
                "subdir": "training",
                "image_ids": test_images,
            }),
    ]

  def _generate_examples(self, images, annotations, subdir, image_ids):
    """Yields images and annotations.

    Args:
      images: object that iterates over the archive of images.
      annotations: object that iterates over the archive of annotations.
      subdir: subdirectory from which to extract images and annotations, e.g.
        training or testing.
      image_ids: file ids for images in this split.

    Yields:
      A tuple containing the example's key, and the example.
    """
    cv2 = tfds.core.lazy_imports.cv2

    all_annotations = dict()
    for fpath, fobj in annotations:
      prefix, ext = os.path.splitext(fpath)
      if ext != ".txt":
        continue
      if prefix.split(os.path.sep)[0] != subdir:
        continue

      # Key is the datapoint id. E.g. training/label_2/label_000016 -> 16.
      all_annotations[int(prefix[-6:])] = _parse_kitti_annotations(fobj)

    for fpath, fobj in images:
      prefix, ext = os.path.splitext(fpath)
      if ext != ".png":
        continue
      if prefix.split(os.path.sep)[0] != subdir:
        continue
      image_id = int(prefix[-6:])
      if image_id not in image_ids:
        continue
      annotations = all_annotations[image_id]
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


def _build_splits(devkit):
  """Splits the train data into train/val/test by video.

  Ensures that images from the same video do not traverse the splits.

  Args:
    devkit: object that iterates over the devkit archive.

  Returns:
    train_images: File ids for the training set images.
    validation_images: File ids for the validation set images.
    test_images: File ids for the test set images.
  """
  mapping_line_ids = None
  mapping_lines = None
  for fpath, fobj in devkit:
    if fpath == os.path.join("mapping", "train_rand.txt"):
      # Converts 1-based line index to 0-based line index.
      mapping_line_ids = [
          int(x.strip()) - 1 for x in fobj.read().decode("utf-8").split(",")
      ]
    elif fpath == os.path.join("mapping", "train_mapping.txt"):
      mapping_lines = fobj.read().splitlines()
      mapping_lines = [x.decode("utf-8") for x in mapping_lines]

  assert mapping_line_ids
  assert mapping_lines

  video_to_image = collections.defaultdict(list)
  for image_id, mapping_lineid in enumerate(mapping_line_ids):
    line = mapping_lines[mapping_lineid]
    video_id = line.split(" ")[1]
    video_to_image[video_id].append(image_id)

  # Sets numpy random state.
  numpy_original_state = np.random.get_state()
  np.random.seed(seed=123)

  # Max 1 for testing.
  num_test_videos = max(1,
                        _TEST_SPLIT_PERCENT_VIDEOS * len(video_to_image) // 100)
  num_validation_videos = max(
      1,
      _VALIDATION_SPLIT_PERCENT_VIDEOS * len(video_to_image) // 100)
  test_videos = set(
      np.random.choice(
          sorted(list(video_to_image.keys())), num_test_videos, replace=False))
  validation_videos = set(
      np.random.choice(
          sorted(list(set(video_to_image.keys()) - set(test_videos))),
          num_validation_videos,
          replace=False))
  test_images = []
  validation_images = []
  train_images = []
  for k, v in video_to_image.items():
    if k in test_videos:
      test_images.extend(v)
    elif k in validation_videos:
      validation_images.extend(v)
    else:
      train_images.extend(v)

  # Resets numpy random state.
  np.random.set_state(numpy_original_state)
  return train_images, validation_images, test_images
