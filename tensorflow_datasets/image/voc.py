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

"""PASCAL VOC datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import xml.etree.ElementTree

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_VOC2007_CITATION = """\
@misc{pascal-voc-2007,
  author = "Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.",
  title = "The {PASCAL} {V}isual {O}bject {C}lasses {C}hallenge 2007 {(VOC2007)} {R}esults",
  howpublished = "http://www.pascal-network.org/challenges/VOC/voc2007/workshop/index.html"}
"""
_VOC2007_DESCRIPTION = """\
This dataset contains the data from the PASCAL Visual Object Classes Challenge
2007, a.k.a. VOC2007, corresponding to the Classification and Detection
competitions.
A total of 9,963 images are included in this dataset, where each image contains
a set of objects, out of 20 different classes, making a total of 24,640
annotated objects.
In the Classification competition, the goal is to predict the set of labels
contained in the image, while in the Detection competition the goal is to
predict the bounding box and label of each individual object.
"""
_VOC2007_URL = "http://host.robots.ox.ac.uk/pascal/VOC/voc2007/"
# Original site, it is down very often.
# _VOC2007_DATA_URL = "http://host.robots.ox.ac.uk/pascal/VOC/voc2007/"
# Data mirror:
_VOC2007_DATA_URL = "http://pjreddie.com/media/files/"
_VOC2007_LABELS = (
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tvmonitor",
)
_VOC2007_POSES = (
    "frontal",
    "rear",
    "left",
    "right",
    "unspecified",
)


class Voc2007(tfds.core.GeneratorBasedBuilder):
  """Pascal VOC 2007."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_VOC2007_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "objects": tfds.features.Sequence({
                "label": tfds.features.ClassLabel(names=_VOC2007_LABELS),
                "bbox": tfds.features.BBoxFeature(),
                "pose": tfds.features.ClassLabel(names=_VOC2007_POSES),
                "is_truncated": tf.bool,
                "is_difficult": tf.bool,
            }),
            "labels": tfds.features.Sequence(
                tfds.features.ClassLabel(names=_VOC2007_LABELS)),
            "labels_no_difficult": tfds.features.Sequence(
                tfds.features.ClassLabel(names=_VOC2007_LABELS)),
        }),
        urls=[_VOC2007_URL],
        citation=_VOC2007_CITATION)

  def _split_generators(self, dl_manager):
    trainval_path = dl_manager.download_and_extract(
        os.path.join(_VOC2007_DATA_URL, "VOCtrainval_06-Nov-2007.tar"))
    test_path = dl_manager.download_and_extract(
        os.path.join(_VOC2007_DATA_URL, "VOCtest_06-Nov-2007.tar"))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(data_path=test_path, set_name="test")),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs=dict(data_path=trainval_path, set_name="train")),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs=dict(data_path=trainval_path, set_name="val")),
    ]

  def _generate_examples(self, data_path, set_name):
    set_filepath = os.path.join(
        data_path, "VOCdevkit/VOC2007/ImageSets/Main/{}.txt".format(set_name))
    with tf.io.gfile.GFile(set_filepath, "r") as f:
      for line in f:
        image_id = line.strip()
        yield self._generate_example(data_path, image_id)

  def _generate_example(self, data_path, image_id):
    """Yields examples."""
    image_filepath = os.path.join(
        data_path, "VOCdevkit/VOC2007/JPEGImages", "{}.jpg".format(image_id))
    annon_filepath = os.path.join(
        data_path, "VOCdevkit/VOC2007/Annotations", "{}.xml".format(image_id))

    def _get_example_objects():
      """Function to get all the objects from the annotation XML file."""
      with tf.io.gfile.GFile(annon_filepath, "r") as f:
        root = xml.etree.ElementTree.parse(f).getroot()

        size = root.find("size")
        width = float(size.find("width").text)
        height = float(size.find("height").text)

        for obj in root.findall("object"):
          # Get object's label name.
          label = obj.find("name").text.lower()
          # Get objects' pose name.
          pose = obj.find("pose").text.lower()
          is_truncated = (obj.find("truncated").text == "1")
          is_difficult = (obj.find("difficult").text == "1")
          bndbox = obj.find("bndbox")
          xmax = float(bndbox.find("xmax").text)
          xmin = float(bndbox.find("xmin").text)
          ymax = float(bndbox.find("ymax").text)
          ymin = float(bndbox.find("ymin").text)
          yield {
              "label": label,
              "pose": pose,
              "bbox": tfds.features.BBox(
                  ymin / height, xmin / width, ymax / height, xmax / width),
              "is_truncated": is_truncated,
              "is_difficult": is_difficult,
          }

    objects = list(_get_example_objects())
    # Use set() to remove duplicates
    labels = sorted(set(obj["label"] for obj in objects))
    labels_no_difficult = sorted(set(
        obj["label"] for obj in objects if obj["is_difficult"] == 0
    ))
    return {
        "image": image_filepath,
        "image/filename": image_id + ".jpg",
        "objects": objects,
        "labels": labels,
        "labels_no_difficult": labels_no_difficult,
    }
