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

"""Caltech Birds 2011 dataset."""
import collections
import concurrent.futures
import os
import re

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.caltech_birds2010 import caltech_birds2010_dataset_builder
import tensorflow_datasets.public_api as tfds

_URL = ("http://www.vision.caltech.edu/datasets/cub_200_2011/")
_NAME_RE = re.compile(r"((\w*)/)*(\d*).(\w*)/(\w*.jpg)$")

# Number of workers to use for concurrent parts of the code.
_WORKERS = 8


class Builder(caltech_birds2010_dataset_builder.Builder):
  """Caltech Birds 2011 dataset."""

  VERSION = tfds.core.Version("0.1.1")

  @property
  def _caltech_birds_info(self):
    return caltech_birds2010_dataset_builder.CaltechBirdsInfo(
        name=self.name,
        images_url="https://drive.google.com/uc?export=download&id=1hbzc_P1FuxMkcabkgn9ZKinBwW683j45",
        split_url=None,
        annotations_url="https://drive.google.com/uc?export=download&id=1EamOKGLoTuZdtcVYbHMWNpkn3iAVj8TP"
    )

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            # Images are of varying size
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=200),
            "label_name": tfds.features.Text(),
            "bbox": tfds.features.BBoxFeature(),
            "segmentation_mask": tfds.features.Image(shape=(None, None, 1)),
        }),
        supervised_keys=("image", "label"),
        homepage=_URL,
    )

  def _split_generators(self, dl_manager):
    download_path = dl_manager.download([
        self._caltech_birds_info.images_url,
    ])

    extracted_path = dl_manager.download_and_extract([
        self._caltech_birds_info.images_url,
        self._caltech_birds_info.annotations_url
    ])

    image_names_path = os.path.join(extracted_path[0],
                                    "CUB_200_2011/images.txt")
    split_path = os.path.join(extracted_path[0],
                              "CUB_200_2011/train_test_split.txt")
    bbox_path = os.path.join(extracted_path[0],
                             "CUB_200_2011/bounding_boxes.txt")

    train_list, test_list = [], []
    attributes = collections.defaultdict(list)

    with tf.io.gfile.GFile(split_path) as f, tf.io.gfile.GFile(
        image_names_path) as f1, tf.io.gfile.GFile(bbox_path) as f2:
      for line, line1, line2 in zip(f, f1, f2):
        img_idx, val = line.split()
        idx, img_name = line1.split()
        res = _NAME_RE.match(img_name)
        matches = res.groups()
        attributes[matches[-1].split(".")[0]].append(line2.split()[1:])  # pytype: disable=attribute-error
        if img_idx == idx:
          if int(val) == 1:
            train_list.append(img_name)
          else:
            test_list.append(img_name)

    def process_file(root, fname):
      with tf.io.gfile.GFile(os.path.join(root, fname), "rb") as png_f:
        mask = tfds.core.lazy_imports.cv2.imdecode(
            np.frombuffer(png_f.read(), dtype=np.uint8), flags=0)
      attributes[fname.split(".")[0]].append(mask)

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=_WORKERS) as executor:
      futures = []
      for root, _, files in tf.io.gfile.walk(extracted_path[1]):
        for fname in files:
          if fname.endswith(".png"):
            future = executor.submit(process_file, root, fname)
            futures.append(future)
      for future in concurrent.futures.as_completed(futures):
        future.result()

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(download_path[0]),
                "file_names": train_list,
                "annotations": attributes,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(download_path[0]),
                "file_names": test_list,
                "annotations": attributes,
            }),
    ]

  def _get_bounding_box_values(self, bbox_annotations, img_width, img_height):
    """Gets normalized bounding box values (Conversion to KITTI format).

    Args:
      bbox_annotations: list of bbox values in kitti format
      img_width: image width
      img_height: image height

    Returns:
      Normalized bounding box xmin, ymin, xmax, ymax values
    """
    xmin = float(bbox_annotations[0]) / img_width
    ymin = float(bbox_annotations[1]) / img_height
    xmax = (float(bbox_annotations[0]) + float(bbox_annotations[2])) / img_width
    ymax = (float(bbox_annotations[1]) +
            float(bbox_annotations[3])) / img_height

    return ymin, xmin, ymax, xmax
