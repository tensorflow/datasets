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
"""The Waymo Open Dataset. See waymo.com/open."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os
from absl import logging
import tensorflow.compat.v2 as tf
from tensorflow_datasets.proto import waymo_dataset_pb2 as open_dataset
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{waymo_open_dataset,
  title = {Waymo Open Dataset: An autonomous driving dataset},
  website = {url{https://www.waymo.com/open}},
  year = {2020}
}
"""

_DESCRIPTION = """\
The Waymo Open Dataset is comprised of high resolution sensor data
collected by Waymo self-driving cars in a wide variety of conditions.
This data is licensed for non-commercial use.

WARNING: this dataset requires additional authorization and registration.
Please look at tfds documentation for accessing GCS, and
afterwards, please register via https://waymo.com/open/licensing/

This dataset is also available in pre-processed format, making it faster
to load, if you select the correct data_dir:
tfds.load('waymo_open_dataset', \
data_dir='gs://waymo_open_dataset_v_1_0_0_individual_files/tensorflow_datasets')
"""

_HOMEPAGE_URL = "http://www.waymo.com/open/"
_OBJECT_LABELS = [
    "TYPE_UNKNOWN", "TYPE_VEHICLE", "TYPE_PEDESTRIAN", "TYPE_SIGN",
    "TYPE_CYCLIST"
]


class WaymoOpenDataset(tfds.core.BeamBasedBuilder):
  """Waymo Open Dataset."""

  VERSION = tfds.core.Version("0.1.0")
  _CLOUD_BUCKET = "gs://waymo_open_dataset_v_1_0_0_individual_files/"

  def _info(self):

    # Annotation descriptions are in the object development kit.
    annotations = {
        "type": tfds.features.ClassLabel(names=_OBJECT_LABELS),
        "bbox": tfds.features.BBoxFeature(),
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "context": {
                "name": tfds.features.Text()
            },
            "timestamp_micros": tf.int64,
            "camera_FRONT": {
                "image":
                    tfds.features.Image(
                        shape=(1280, 1920, 3), encoding_format="jpeg"),
                "labels":
                    tfds.features.Sequence(annotations)
            },
            "camera_FRONT_LEFT": {
                "image":
                    tfds.features.Image(
                        shape=(1280, 1920, 3), encoding_format="jpeg"),
                "labels":
                    tfds.features.Sequence(annotations)
            },
            "camera_SIDE_LEFT": {
                "image":
                    tfds.features.Image(
                        shape=(886, 1920, 3), encoding_format="jpeg"),
                "labels":
                    tfds.features.Sequence(annotations)
            },
            "camera_FRONT_RIGHT": {
                "image":
                    tfds.features.Image(
                        shape=(1280, 1920, 3), encoding_format="jpeg"),
                "labels":
                    tfds.features.Sequence(annotations)
            },
            "camera_SIDE_RIGHT": {
                "image":
                    tfds.features.Image(
                        shape=(886, 1920, 3), encoding_format="jpeg"),
                "labels":
                    tfds.features.Sequence(annotations)
            },
        }),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    # Training set
    train_files = tf.io.gfile.glob(
        os.path.join(self._CLOUD_BUCKET, "training/segment*camera*"))
    logging.info("Train files: %s", train_files)

    # Validation set
    validation_files = tf.io.gfile.glob(
        os.path.join(self._CLOUD_BUCKET, "validation/segment*camera*"))
    logging.info("Validation files: %s", validation_files)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "tf_record_files": train_files,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "tf_record_files": validation_files,
            }),
    ]

  def _build_pcollection(self, pipeline, tf_record_files):
    """Generate examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_example(tf_record_file):
      for image_and_annotation in _generate_images_and_annotations(
          tf_record_file):
        key = "%s:%s" % (image_and_annotation["context"]["name"],
                         image_and_annotation["timestamp_micros"])
        yield key, image_and_annotation

    return (pipeline
            | beam.Create(tf_record_files)
            | beam.FlatMap(_process_example))


def _generate_images_and_annotations(tf_record_file):
  """Yields the images and annotations from a given file."""
  # Go through all frames
  dataset = tf.data.TFRecordDataset(tf_record_file, compression_type="")
  for data in dataset:
    frame = open_dataset.Frame()
    frame.ParseFromString(bytearray(data.numpy()))  # pytype: disable=wrong-arg-types

    image_and_annotation = {
        "context": {
            "name": frame.context.name
        },
        "timestamp_micros": frame.timestamp_micros
    }

    camera_calibration = {
        calibration.name: calibration
        for calibration in frame.context.camera_calibrations
    }
    camera_labels = {label.name: label for label in frame.camera_labels}

    # Go through all 5 camera images in the frame
    for frame_image in frame.images:
      labels = None
      if frame_image.name in camera_labels:
        image_height = camera_calibration[frame_image.name].height
        image_width = camera_calibration[frame_image.name].width
        labels = _convert_labels(camera_labels[frame_image.name], image_width,
                                 image_height)

      camera_name = open_dataset.CameraName.Name.Name(frame_image.name)
      image_and_annotation["camera_" + camera_name] = {
          "image": io.BytesIO(frame_image.image),
          "labels": labels
      }

    yield image_and_annotation


def _convert_labels(raw_labels, image_width, image_height):
  return [{  # pylint: disable=g-complex-comprehension
      "type": raw_label.type,
      "bbox": _build_bounding_box(raw_label.box, image_width, image_height)
  } for raw_label in raw_labels.labels]


def _build_bounding_box(open_dataset_box, image_width, image_height):
  """Builds and returns TFDS bounding box."""

  center_x = open_dataset_box.center_x
  center_y = open_dataset_box.center_y
  length = open_dataset_box.length
  width = open_dataset_box.width

  return tfds.features.BBox(
      ymin=max((center_y - (width / 2)) / image_height, 0.0),
      ymax=min((center_y + (width / 2)) / image_height, 1.0),
      xmin=max((center_x - (length / 2)) / image_width, 0.0),
      xmax=min((center_x + (length / 2)) / image_width, 1.0),
  )
