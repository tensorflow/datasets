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

r"""Generate bccd data.

"""

import os
import random

from absl import app
from absl import flags
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.bccd import bccd_dataset_builder
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

MIN_OBJECT_HEIGHT_WIDTH = 100
MAX_OBJECT_HEIGHT_WIDTH = 400
MIN_NUM_OBJECTS = 1
MAX_NUM_OBJECTS = 3


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, "image", "bccd", "dummy_data")


def _write_text_file(filepath, content):
  """Write a text file given its content."""
  dirname = os.path.dirname(filepath)
  if not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  with tf.io.gfile.GFile(filepath, "w") as f:
    f.write(content)


def _generate_jpeg(example_id, height, width):
  """Generate a fake jpeg image for the given example id."""
  jpeg = fake_data_utils.get_random_jpeg(height=height, width=width)
  filepath = os.path.join(
      _output_dir(),
      "BCCD_Dataset-1.0/BCCD/JPEGImages/BloodImage_{:05d}.jpg".format(
          example_id))
  dirname = os.path.dirname(filepath)
  if not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  tf.io.gfile.copy(jpeg, filepath, overwrite=True)


def _generate_annotation(example_id, height, width):
  """Generate a fake annotation XML for the given example id."""
  # pylint: disable=protected-access
  label_names = tfds.features.ClassLabel(
      names=bccd_dataset_builder._CLASS_LABELS).names  # pytype: disable=module-attr
  # pylint: enable=protected-access
  annotation = "<annotation>\n"
  annotation += "<folder>JPEGImages</folder>\n"
  annotation += "<filename>%d.jpg</filename>\n" % example_id
  annotation += "<path>/home/pi/detection_dataset/JPEGImages/%d.jpg</path>" % example_id
  annotation += "<source>\n"
  annotation += "<database>Unknown</database>\n"
  annotation += "</source>"
  annotation += "<size>\n"
  annotation += "<width>%d</width>\n" % width
  annotation += "<height>%d</height>\n" % height
  annotation += "</size>\n"
  for i in range(random.randint(MIN_NUM_OBJECTS, MAX_NUM_OBJECTS)):
    annotation += "<object>\n"
    annotation += "  <name>%s</name>\n" % random.choice(label_names)
    annotation += "  <pose>Unspecified</pose>\n"
    annotation += "  <truncated>0</truncated>\n"
    if i > 0:
      annotation += "  <difficult>%s</difficult>\n" % random.randint(0, 1)
    else:
      annotation += "  <difficult>0</difficult>\n"
    obj_w = random.randint(MIN_OBJECT_HEIGHT_WIDTH, MAX_OBJECT_HEIGHT_WIDTH)
    obj_h = random.randint(MIN_OBJECT_HEIGHT_WIDTH, MAX_OBJECT_HEIGHT_WIDTH)
    obj_x = random.randint(0, width - obj_w)
    obj_y = random.randint(0, height - obj_h)
    annotation += "  <bndbox>\n"
    annotation += "    <xmin>%d</xmin>\n" % obj_x
    annotation += "    <ymin>%d</ymin>\n" % obj_y
    annotation += "    <xmax>%d</xmax>\n" % (obj_x + obj_w - 1)
    annotation += "    <ymax>%d</ymax>\n" % (obj_y + obj_h - 1)
    annotation += "  </bndbox>\n"
    annotation += "</object>\n"
  annotation += "</annotation>\n"
  # Add annotation XML to the tar file.
  filepath = os.path.join(
      _output_dir(),
      "BCCD_Dataset-1.0/BCCD/Annotations/BloodImage_{:05d}.xml".format(
          example_id))
  _write_text_file(filepath, annotation)


def _generate_data_for_set(set_name, example_start, num_examples):
  """Generate different data examples for the train, validation or test sets."""
  # Generate JPEG and XML files of each example.
  for example_id in range(example_start, example_start + num_examples):
    _generate_jpeg(example_id, 480, 640)
    _generate_annotation(example_id, 480, 640)
  # Add all example ids to the TXT file with all examples in the set.
  filepath = os.path.join(
      _output_dir(), "BCCD_Dataset-1.0/BCCD/ImageSets/Main/%s.txt" % set_name)
  _write_text_file(
      filepath, "".join([
          "BloodImage_{:05d}\n".format(example_id)
          for example_id in range(example_start, example_start + num_examples)
      ]))


def _generate_trainval_archive():
  """Generate train/val archive."""
  _generate_data_for_set("train", example_start=0, num_examples=2)
  _generate_data_for_set("val", example_start=2, num_examples=1)


def _generate_test_archive():
  """Generate test archive."""
  _generate_data_for_set("test", example_start=3, num_examples=2)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_trainval_archive()
  _generate_test_archive()


if __name__ == "__main__":
  app.run(main)
