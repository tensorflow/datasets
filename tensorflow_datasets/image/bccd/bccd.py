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

"""Blood Cell Count and Detection Dataset."""

import collections
import os
import xml.etree.ElementTree as ET

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
BCCD Dataset is a small-scale dataset for blood cells detection.

Thanks the original data and annotations from cosmicad and akshaylamba.
The original dataset is re-organized into VOC format.
BCCD Dataset is under MIT licence.

Data preparation is important to use machine learning.
In this project, the Faster R-CNN algorithm from keras-frcnn for Object Detection is used.
From this dataset, nicolaschen1 developed two Python scripts to make
preparation data (CSV file and images) for recognition of abnormalities
in blood cells on medical images.

export.py: it creates the file "test.csv" with all data needed: filename, class_name, x1,y1,x2,y2.
plot.py: it plots the boxes for each image and save it in a new directory.

Image Type : jpeg(JPEG)
Width x Height : 640 x 480
"""

_HOMEPAGE_URL = "https://github.com/Shenggan/BCCD_Dataset"
_DOWNLOAD_URL = "https://github.com/Shenggan/BCCD_Dataset/archive/v1.0.zip"

_CITATION = """\
@ONLINE {BCCD_Dataset,
    author = "Shenggan",
    title  = "BCCD Dataset",
    year   = "2017",
    url    = "https://github.com/Shenggan/BCCD_Dataset"
}
"""
_CLASS_LABELS = [
    "RBC",
    "WBC",
    "Platelets",
]


class BCCD(tfds.core.GeneratorBasedBuilder):
  """Blood Cell Count and Detection Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(480, 640, 3), encoding_format="jpeg"),
            "image/filename":
                tfds.features.Text(),
            # Multiple bounding box per image
            "objects":
                tfds.features.Sequence({
                    "label": tfds.features.ClassLabel(names=_CLASS_LABELS),
                    "bbox": tfds.features.BBoxFeature(),
                }),
        }),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    train_list = []
    test_list = []
    val_list = []

    dl_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    # Name of the extracted folder is 'BCCD_Dataset-1.0'
    extracted_dir_path = os.path.join(dl_path, "BCCD_Dataset-1.0")
    splits_dir_path = os.path.join(extracted_dir_path, "BCCD", "ImageSets",
                                   "Main")

    for root, _, filename in tf.io.gfile.walk(splits_dir_path):
      for fname in filename:
        full_file_name = os.path.join(root, fname)
        with tf.io.gfile.GFile(full_file_name) as f:
          for line in f:
            if fname == "train.txt":
              train_list.append(line)
            elif fname == "test.txt":
              test_list.append(line)
            elif fname == "val.txt":
              val_list.append(line)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "file_names": train_list,
                "extracted_dir_path": extracted_dir_path
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "file_names": val_list,
                "extracted_dir_path": extracted_dir_path
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "file_names": test_list,
                "extracted_dir_path": extracted_dir_path
            }),
    ]

  def _generate_examples(self, file_names, extracted_dir_path):
    """Yeilds Examples.

    Args:
      file_names: The path of the file that contains the splits
      extracted_dir_path: The path of the extracted folder

    Yields:
      Generator yielding the next examples
    """

    bbox_attrib = ["xmin", "xmax", "ymin", "ymax", "width", "height"]
    xml_list = collections.defaultdict(str)

    images_dir_path = os.path.join(extracted_dir_path, "BCCD", "JPEGImages")

    annotations_dir_path = os.path.join(extracted_dir_path, "BCCD",
                                        "Annotations")

    def get_image_file_path(filename):
      """Returns image path."""
      return os.path.join(images_dir_path, "{}.jpg".format(filename.strip()))

    def get_annotations_file_path(filename):
      """Returns annotations file path."""
      return os.path.join(annotations_dir_path,
                          "{}.xml".format(filename.strip()))

    for fname in file_names:
      annotation_file_path = get_annotations_file_path(fname)
      xml_list[fname] = ET.parse(annotation_file_path)
      attributes = collections.defaultdict(list)
      for element in xml_list[fname].iter():
        # Extract necessary Bbox attributes from XML file
        # "Name" tag contains the label
        if element.tag.strip() == "name":
          attributes[element.tag.strip()].append(element.text.strip())
        elif element.tag.strip() in bbox_attrib:
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

      def get_label(attributes, n):
        return attributes["name"][n]

      key = fname
      example = {
          "image":
              get_image_file_path(fname),
          "image/filename":
              fname,
          "objects": [
              {  # pylint: disable=g-complex-comprehension
                  "label": get_label(attributes, n),
                  "bbox": build_box(attributes, n)
              } for n in range(len(attributes["name"]))
          ]
      }
      yield key, example
