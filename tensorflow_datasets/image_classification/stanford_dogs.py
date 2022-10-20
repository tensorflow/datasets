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

"""Stanford dogs dataset."""

import collections
import os
import re
import xml.etree.ElementTree as ET

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The Stanford Dogs dataset contains images of 120 breeds of dogs from around
the world. This dataset has been built using images and annotation from
ImageNet for the task of fine-grained image categorization. There are
20,580 images, out of which 12,000 are used for training and 8580 for
testing. Class labels and bounding box annotations are provided
for all the 12,000 images.
"""

_URL = ("http://vision.stanford.edu/aditya86/ImageNetDogs/main.html")

_CITATION = """\
@inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,
author = "Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and
          Li Fei-Fei",
title = "Novel Dataset for Fine-Grained Image Categorization",
booktitle = "First Workshop on Fine-Grained Visual Categorization,
             IEEE Conference on Computer Vision and Pattern Recognition",
year = "2011",
month = "June",
address = "Colorado Springs, CO",
}
@inproceedings{imagenet_cvpr09,
        AUTHOR = {Deng, J. and Dong, W. and Socher, R. and Li, L.-J. and
                  Li, K. and Fei-Fei, L.},
        TITLE = {{ImageNet: A Large-Scale Hierarchical Image Database}},
        BOOKTITLE = {CVPR09},
        YEAR = {2009},
        BIBSOURCE = "http://www.image-net.org/papers/imagenet_cvpr09.bib"}
"""

_IMAGES_URL = "http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar"
_SPLIT_URL = "http://vision.stanford.edu/aditya86/ImageNetDogs/lists.tar"
_ANNOTATIONS_URL = "http://vision.stanford.edu/aditya86/ImageNetDogs/annotation.tar"
_NAME_RE = re.compile(r"([\w-]*[/\\])*([\w]*.jpg)$")


class StanfordDogs(tfds.core.GeneratorBasedBuilder):
  """Stanford Dogs dataset."""

  # Version 0.2.0: Fix non-deterministic label names
  VERSION = tfds.core.Version("0.2.0")

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # Images are of varying size
            "image":
                tfds.features.Image(),
            "image/filename":
                tfds.features.Text(),
            "label":
                tfds.features.ClassLabel(num_classes=120),
            # Multiple bounding box per image
            "objects":
                tfds.features.Sequence({
                    "bbox": tfds.features.BBoxFeature(),
                }),
        }),
        supervised_keys=("image", "label"),
        homepage=_URL,
        citation=_CITATION)

  def _split_generators(self, dl_manager):

    images_path = dl_manager.download(_IMAGES_URL)
    split_path, annotation_path = dl_manager.download_and_extract(
        [_SPLIT_URL, _ANNOTATIONS_URL])
    xml_file_list = collections.defaultdict(str)

    # Parsing the mat file which contains the list of train/test images
    scipy = tfds.core.lazy_imports.scipy

    def parse_mat_file(file_name):
      with tf.io.gfile.GFile(file_name, "rb") as f:
        parsed_mat_arr = scipy.io.loadmat(f, squeeze_me=True)
      file_list = [
          os.path.split(element)[-1] for element in parsed_mat_arr["file_list"]
      ]

      return file_list, parsed_mat_arr

    for fname in tf.io.gfile.listdir(split_path):
      # Train-test split using train_list.mat and test_list.mat
      full_file_name = os.path.join(split_path, fname)

      if "train" in fname:
        train_list, train_mat_arr = parse_mat_file(full_file_name)
        label_names = set([  # Set to remove duplicates
            os.path.split(element)[-2].lower()  # Extract path/label/img.jpg
            for element in train_mat_arr["file_list"]
        ])
      elif "test" in fname:
        test_list, _ = parse_mat_file(full_file_name)

    self.info.features["label"].names = sorted(label_names)

    for root, _, files in tf.io.gfile.walk(annotation_path):
      # Parsing the XML file which have the image annotations
      for fname in files:
        annotation_file_name = os.path.join(root, fname)
        with tf.io.gfile.GFile(annotation_file_name, "rb") as f:
          xml_file_list[fname] = ET.parse(f)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(images_path),
                "file_names": train_list,
                "annotation_files": xml_file_list,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(images_path),
                "file_names": test_list,
                "annotation_files": xml_file_list,
            })
    ]

  def _generate_examples(self, archive, file_names, annotation_files):
    """Generate dog images, labels, bbox attributes given the directory path.

    Args:
      archive: object that iterates over the zip
      file_names : list of train/test image file names obtained from mat file
      annotation_files : dict of image file names and their xml object

    Yields:
      Image path, Image file name, its corresponding label and
      bounding box values
    """
    bbox_attrib = ["xmin", "xmax", "ymin", "ymax", "width", "height"]

    for fname, fobj in archive:
      res = _NAME_RE.match(fname)
      if not res or (os.path.split(fname)[-1] not in file_names):
        continue

      label = res.group(1)[:-1].lower()
      file_name = res.group(2)
      attributes = collections.defaultdict(list)
      for element in annotation_files[file_name.split(".")[0]].iter():
        # Extract necessary Bbox attributes from XML file
        if element.tag.strip() in bbox_attrib:
          attributes[element.tag.strip()].append(float(element.text.strip()))

      # BBox attributes in range of 0.0 to 1.0
      def normalize_bbox(bbox_side, image_side):
        return min(bbox_side / image_side, 1.0)

      def build_box(attributes, n):
        return tfds.features.BBox(
            ymin=normalize_bbox(attributes["ymin"][n], attributes["height"][0]),
            xmin=normalize_bbox(attributes["xmin"][n], attributes["width"][0]),
            ymax=normalize_bbox(attributes["ymax"][n], attributes["height"][0]),
            xmax=normalize_bbox(attributes["xmax"][n], attributes["width"][0]),
        )

      yield fname, {
          "image":
              fobj,
          "image/filename":
              fname,
          "label":
              label,
          "objects": [{
              "bbox": build_box(attributes, n)
          } for n in range(len(attributes["xmin"]))]
      }
