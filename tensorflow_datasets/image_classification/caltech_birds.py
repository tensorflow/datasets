# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Caltech birds dataset."""

import collections
import os
import re

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos 
of 200 bird species (mostly North American). The total number of 
categories of birds is 200 and there are 6033 images in the 2010 
dataset and 11,788 images in the 2011 dataset.
Annotations include bounding boxes, segmentation labels.
"""

_URL = ("http://www.vision.caltech.edu/visipedia/CUB-200.html")
_CITATION = """\
@techreport{WelinderEtal2010,
Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},
Institution = {California Institute of Technology},
Number = {CNS-TR-2010-001},
Title = {{Caltech-UCSD Birds 200}},
Year = {2010}
}
"""
_NAME_RE = re.compile(r"((\w*)/)*(\d*).(\w*)/(\w*.jpg)$")


class CaltechBirds2010(tfds.core.GeneratorBasedBuilder):
  """Caltech Birds 2010 dataset."""

  VERSION = tfds.core.Version("0.1.1")

  @property
  def _caltech_birds_info(self):
    return CaltechBirdsInfo(
        name=self.name,
        images_url="https://drive.google.com/uc?export=download&id=1GDr1OkoXdhaXWGA8S3MAq3a522Tak-nx",
        split_url="https://drive.google.com/uc?export=download&id=1vZuZPqha0JjmwkdaS_XtYryE3Jf5Q1AC",
        annotations_url="https://drive.google.com/uc?export=download&id=16NsbTpMs5L6hT4hUJAmpW2u7wH326WTR",
    )

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
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
        citation=_CITATION)

  def _split_generators(self, dl_manager):

    download_path = dl_manager.download([
        self._caltech_birds_info.split_url,
        self._caltech_birds_info.annotations_url,
        self._caltech_birds_info.images_url,
    ])
    extracted_path = dl_manager.download_and_extract([
        self._caltech_birds_info.split_url,
        self._caltech_birds_info.annotations_url
    ])

    train_path = os.path.join(extracted_path[0], "lists/train.txt")
    test_path = os.path.join(extracted_path[0], "lists/test.txt")

    with tf.io.gfile.GFile(train_path) as f:
      train_list = f.read().splitlines()

    with tf.io.gfile.GFile(test_path) as f:
      test_list = f.read().splitlines()

    attributes = collections.defaultdict(list)

    for root, _, files in tf.io.gfile.walk(extracted_path[1]):
      # Parsing the .mat files which have the image annotations
      for fname in files:
        if fname.endswith(".mat"):
          path = os.path.join(root, fname)
          with tf.io.gfile.GFile(path, "rb") as f:
            mat = tfds.core.lazy_imports.scipy.io.loadmat(
                f, squeeze_me=True, variable_names=["bbox", "seg"])
          attributes[fname.split(".")[0]].append(mat["bbox"])
          attributes[fname.split(".")[0]].append(mat["seg"])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(download_path[2]),
                "file_names": train_list,
                "annotations": attributes,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(download_path[2]),
                "file_names": test_list,
                "annotations": attributes,
            }),
    ]

  def _get_bounding_box_values(self, bbox_annotations, img_width, img_height):
    """Function to get normalized bounding box values.

    Args:
      bbox_annotations: list of bbox values in kitti format
      img_width: image width
      img_height: image height

    Returns:
      Normalized bounding box xmin, ymin, xmax, ymax values
    """

    ymin = bbox_annotations["top"] / img_height
    xmin = bbox_annotations["left"] / img_width
    ymax = bbox_annotations["bottom"] / img_height
    xmax = bbox_annotations["right"] / img_width

    return ymin, xmin, ymax, xmax

  def _generate_examples(self, archive, file_names, annotations):
    """Generate birds images, labels and bounding box given the directory path.

    Args:
        archive: object that iterates over the zip
        file_names : list of train/test image file names obtained from mat file
        annotations : dict of image file names and bbox attributes, segmentation
          labels

    Yields:
        Image path, Image file name, its corresponding label and
        bounding box values
    """

    for fname, fobj in archive:
      fname = fname.replace("\\", "/")  # For windows compatibility
      res = _NAME_RE.match(fname)

      # Checking if filename is present in respective train/test list

      if not res or "/".join(fname.split("/")[-2:]) not in file_names:
        continue
      matches = res.groups()
      label_name = matches[-2].lower()  # pytype: disable=attribute-error
      label_key = int(matches[-3]) - 1
      file_name = matches[-1].split(".")[0]  # pytype: disable=attribute-error
      segmentation_mask = annotations[file_name][1]

      height, width = segmentation_mask.shape

      bbox = self._get_bounding_box_values(annotations[file_name][0], width,
                                           height)

      yield fname, {
          "image":
              fobj,
          "image/filename":
              fname,
          "label":
              label_key,
          "label_name":
              label_name,
          "bbox":
              tfds.features.BBox(
                  ymin=min(bbox[0], 1.0),
                  xmin=min(bbox[1], 1.0),
                  ymax=min(bbox[2], 1.0),
                  xmax=min(bbox[3], 1.0)),
          "segmentation_mask":
              segmentation_mask[:, :, np.newaxis],
      }


class CaltechBirds2011(CaltechBirds2010):
  """Caltech Birds 2011 dataset."""

  VERSION = tfds.core.Version("0.1.1")

  @property
  def _caltech_birds_info(self):
    return CaltechBirdsInfo(
        name=self.name,
        images_url="https://drive.google.com/uc?export=download&id=1hbzc_P1FuxMkcabkgn9ZKinBwW683j45",
        split_url=None,
        annotations_url="https://drive.google.com/uc?export=download&id=1EamOKGLoTuZdtcVYbHMWNpkn3iAVj8TP"
    )

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
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
        citation=_CITATION)

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

    for root, _, files in tf.io.gfile.walk(extracted_path[1]):
      for fname in files:
        if fname.endswith(".png"):
          with tf.io.gfile.GFile(os.path.join(root, fname), "rb") as png_f:
            mask = tfds.core.lazy_imports.cv2.imdecode(
                np.frombuffer(png_f.read(), dtype=np.uint8), flags=0)
          attributes[fname.split(".")[0]].append(mask)

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


class CaltechBirdsInfo(
    collections.namedtuple(
        "_CaltechBirdsInfo",
        ["name", "images_url", "split_url", "annotations_url"])):
  """Contains the information necessary to generate a Caltech Birds dataset.

    Args:
        name (str): name of dataset.
        images_url (str): images URL.
        split_url (str): train/test split file URL.
        annotations_url (str): annotation folder URL.
  """
