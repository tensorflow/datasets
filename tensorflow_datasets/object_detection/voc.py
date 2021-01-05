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

"""PASCAL VOC datasets."""

import os
import xml.etree.ElementTree

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


_VOC_CITATION = """\
@misc{{pascal-voc-{year},
	author = "Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.",
	title = "The {{PASCAL}} {{V}}isual {{O}}bject {{C}}lasses {{C}}hallenge {year} {{(VOC{year})}} {{R}}esults",
	howpublished = "http://www.pascal-network.org/challenges/VOC/voc{year}/workshop/index.html"}}
"""

_VOC_DESCRIPTION = """
This dataset contains the data from the PASCAL Visual Object Classes Challenge,
corresponding to the Classification and Detection competitions.

In the Classification competition, the goal is to predict the set of labels
contained in the image, while in the Detection competition the goal is to
predict the bounding box and label of each individual object.
WARNING: As per the official dataset, the test set of VOC2012 does not contain
annotations.
"""

_VOC_CONFIG_DESCRIPTION = """\
This dataset contains the data from the PASCAL Visual Object Classes Challenge
{year}, a.k.a. VOC{year}.

A total of {num_images} images are included in this dataset, where each image
contains a set of objects, out of 20 different classes, making a total of
{num_objects} annotated objects.
"""
_VOC_URL = "http://host.robots.ox.ac.uk/pascal/VOC/voc{year}/"
# Original site, it is down very often.
# _VOC_DATA_URL = "http://host.robots.ox.ac.uk/pascal/VOC/voc{year}/"
# Data mirror:
_VOC_DATA_URL = "http://pjreddie.com/media/files/"
_VOC_LABELS = (
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
_VOC_POSES = (
    "frontal",
    "rear",
    "left",
    "right",
    "unspecified",
)


def _get_example_objects(annon_filepath):
  """Function to get all the objects from the annotation XML file."""
  with tf.io.gfile.GFile(annon_filepath, "r") as f:
    root = xml.etree.ElementTree.parse(f).getroot()

    # Disable pytype to avoid attribute-error due to find returning
    # Optional[Element]
    # pytype: disable=attribute-error
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
    # pytype: enable=attribute-error


class VocConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Voc."""

  def __init__(
      self, year=None, filenames=None, has_test_annotations=True, **kwargs):
    self.year = year
    self.filenames = filenames
    self.has_test_annotations = has_test_annotations
    super(VocConfig, self).__init__(
        name=year,
        # Version history:
        # 4.0.0: Added BuildConfig and 2012 version support, deprecate Voc2007.
        # 3.0.0: S3 with new hashing function (different shuffle).
        # 2.0.0: S3 (new shuffling, sharding and slicing mechanism).
        version=tfds.core.Version("4.0.0"),
        **kwargs)


class Voc(tfds.core.GeneratorBasedBuilder):
  """Pascal VOC 2007 or 2012."""

  BUILDER_CONFIGS = [
      VocConfig(
          year="2007",
          description=_VOC_CONFIG_DESCRIPTION.format(
              year=2007, num_images=9963, num_objects=24640),
          filenames={
              "trainval": "VOCtrainval_06-Nov-2007.tar",
              "test": "VOCtest_06-Nov-2007.tar",
          },
          has_test_annotations=True,
      ),
      VocConfig(
          year="2012",
          description=_VOC_CONFIG_DESCRIPTION.format(
              year=2012, num_images=11540, num_objects=27450),
          filenames={
              "trainval": "VOCtrainval_11-May-2012.tar",
              "test": "VOC2012test.tar",
          },
          has_test_annotations=False,
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_VOC_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "objects": tfds.features.Sequence({
                "label": tfds.features.ClassLabel(names=_VOC_LABELS),
                "bbox": tfds.features.BBoxFeature(),
                "pose": tfds.features.ClassLabel(names=_VOC_POSES),
                "is_truncated": tf.bool,
                "is_difficult": tf.bool,
            }),
            "labels": tfds.features.Sequence(
                tfds.features.ClassLabel(names=_VOC_LABELS)),
            "labels_no_difficult": tfds.features.Sequence(
                tfds.features.ClassLabel(names=_VOC_LABELS)),
        }),
        homepage=_VOC_URL.format(year=self.builder_config.year),
        citation=_VOC_CITATION.format(year=self.builder_config.year),
    )

  def _split_generators(self, dl_manager):
    paths = dl_manager.download_and_extract({
        k: os.path.join(_VOC_DATA_URL, v)
        for k, v in self.builder_config.filenames.items()
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(data_path=paths["test"], set_name="test")),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(data_path=paths["trainval"], set_name="train")),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(data_path=paths["trainval"], set_name="val")),
    ]

  def _generate_examples(self, data_path, set_name):
    """Yields examples."""
    set_filepath = os.path.join(
        data_path,
        os.path.normpath("VOCdevkit/VOC{}/ImageSets/Main/{}.txt".format(
            self.builder_config.year, set_name)))
    load_annotations = (
        self.builder_config.has_test_annotations or set_name != "test")
    with tf.io.gfile.GFile(set_filepath, "r") as f:
      for line in f:
        image_id = line.strip()
        example = self._generate_example(data_path, image_id, load_annotations)
        yield image_id, example

  def _generate_example(self, data_path, image_id, load_annotations):
    image_filepath = os.path.join(
        data_path,
        os.path.normpath("VOCdevkit/VOC{}/JPEGImages/{}.jpg".format(
            self.builder_config.year, image_id)))
    annon_filepath = os.path.join(
        data_path,
        os.path.normpath("VOCdevkit/VOC{}/Annotations/{}.xml".format(
            self.builder_config.year, image_id)))
    if load_annotations:
      objects = list(_get_example_objects(annon_filepath))
      # Use set() to remove duplicates
      labels = sorted(set(obj["label"] for obj in objects))
      labels_no_difficult = sorted(set(
          obj["label"] for obj in objects if obj["is_difficult"] == 0
      ))
    else:  # The test set of VOC2012 does not contain annotations
      objects = []
      labels = []
      labels_no_difficult = []
    return {
        "image": image_filepath,
        "image/filename": image_id + ".jpg",
        "objects": objects,
        "labels": labels,
        "labels_no_difficult": labels_no_difficult,
    }
