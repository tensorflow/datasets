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

"""Datasets of the Open Images Challange 2019.

https://storage.googleapis.com/openimages/web/challenge2019.html
"""

import abc

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Open Images is a collaborative release of ~9 million images annotated with
image-level labels, object bounding boxes, object segmentation masks, and
visual relationships. This uniquely large and diverse dataset is designed to
spur state of the art advances in analyzing and understanding images.
"""
_DESCRIPTION_DETECTION = """\
This contains the data from thee Object Detection track of the competition.
The goal in this track is to predict a tight bounding box around all object
instances of 500 classes.

The images are annotated with positive image-level labels, indicating certain
object classes are present, and with negative image-level labels, indicating
certain classes are absent. In the competition, all other unannotated classes
are excluded from evaluation in that image. For each positive image-level label
in an image, every instance of that object class in the image was annotated.
"""
_URL = "https://storage.googleapis.com/openimages/web/challenge2019.html"

_GOOGLE_URL_PREFIX = (
    "https://storage.googleapis.com/openimages/challenge_2019/challenge-2019-")
_FIGURE_EIGHT_BASE_URL = (
    "https://datasets.figure-eight.com/figure_eight_datasets/open-images/")
_TRAIN_IMAGES_URLS = [
    "{}zip_files_copy/train_{:02d}.zip".format(_FIGURE_EIGHT_BASE_URL, n)
    for n in range(9)
]
_VALIDATION_IMAGES_URL = (
    _FIGURE_EIGHT_BASE_URL + "zip_files_copy/validation.zip")
_TEST_IMAGES_URL = _FIGURE_EIGHT_BASE_URL + "test_challenge.zip"
_NUM_CLASSES = 500


class OpenImagesChallenge2019Config(tfds.core.BuilderConfig):
  """BuilderConfig for OpenImages Challenge 2019 datasets."""

  def __init__(self, target_pixels=None, **kwargs):
    kwargs.setdefault("version", tfds.core.Version("1.0.0"))
    super(OpenImagesChallenge2019Config, self).__init__(**kwargs)
    self._target_pixels = target_pixels

  @property
  def target_pixels(self):
    return self._target_pixels


class _OpenImagesChallenge2019(tfds.core.BeamBasedBuilder):
  """Base abstract class for Open Images Challenge 2019 datasets."""

  BUILDER_CONFIGS = [
      OpenImagesChallenge2019Config(
          name="200k",
          description="Images have at most 200,000 pixels, at 72 JPEG quality.",
          target_pixels=200000),
      OpenImagesChallenge2019Config(
          name="300k",
          description="Images have at most 300,000 pixels, at 72 JPEG quality.",
          target_pixels=300000),
  ]

  @property
  @abc.abstractmethod
  def annotation_urls(self):
    """Dictionary passed to the DownloadManager to download annotations.

    An example:
      {"test_annotations": "https://somewebpage.com/data/openimages/test.txt"}

    Returns:
      A dictionary whose values are the URLs to download the annotations of the
      dataset, and the keys are some short string identifying the URL.
      This dictionary is passed to the DownloadManager.
    """

  def _split_generators(self, dl_manager):
    urls = {
        "train_images": _TRAIN_IMAGES_URLS,
        "test_images": [_TEST_IMAGES_URL],
        "validation_images": [_VALIDATION_IMAGES_URL]
    }
    urls.update(self.annotation_urls)
    paths = dl_manager.download(urls)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(paths=paths, split="train"),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(paths=paths, split="test"),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(paths=paths, split="validation"),
        ),
    ]


class OpenImagesChallenge2019Detection(_OpenImagesChallenge2019):
  """Dataset for the Detection Track."""

  @property
  def annotation_urls(self):
    return {
        "train_image_label":
            _GOOGLE_URL_PREFIX + "train-detection-human-imagelabels.csv",
        "train_boxes":
            _GOOGLE_URL_PREFIX + "train-detection-bbox.csv",
        "validation_image_label":
            _GOOGLE_URL_PREFIX + "validation-detection-human-imagelabels.csv",
        "validation_boxes":
            _GOOGLE_URL_PREFIX + "validation-detection-bbox.csv",
        "classes":
            _GOOGLE_URL_PREFIX + "classes-description-500.csv",
        "hierarchy":
            _GOOGLE_URL_PREFIX + "label500-hierarchy.json",
    }

  def _info(self):
    label = tfds.features.ClassLabel(num_classes=_NUM_CLASSES)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION + "\n\n" + _DESCRIPTION_DETECTION,
        features=tfds.features.FeaturesDict({
            "id":
                tfds.features.Text(),
            "image":
                tfds.features.Image(),
            # A sequence of image-level labels.
            "objects":
                tfds.features.Sequence({
                    "label": label,
                    # All labels have been verified by humans.
                    #  - If confidence is 1.0, the object IS in the image.
                    #  - If confidence is 0.0, the object is NOT in the image.
                    "confidence": tf.float32,
                    "source": tfds.features.Text(),
                }),
            # A sequence of bounding boxes.
            "bobjects":
                tfds.features.Sequence({
                    "label": label,
                    "bbox": tfds.features.BBoxFeature(),
                    "is_group_of": tf.bool,
                }),
        }),
        homepage=_URL,
    )

  def _build_pcollection(self, pipeline, paths, split):
    beam = tfds.core.lazy_imports.apache_beam
    # We need to lazily import the oi_beam module (and thus, violate the
    # "imports only at the top" rule), so that beam is only required during the
    # generation of the dataset, and not to use the dataset itself (once built).
    # See: https://www.tensorflow.org/datasets/beam_datasets.
    import tensorflow_datasets.object_detection.open_images_challenge2019_beam as oi_beam  # pylint: disable=g-import-not-at-top,import-outside-toplevel

    if split == "test":
      # Note: annotations are not available for the test split.
      generate_examples_kwargs = dict(
          image_labels_filepath=None,
          box_labels_filepath=None,
          hierarchy_filepath=None,
          classes_filepath=None,
      )
    else:
      generate_examples_kwargs = dict(
          image_labels_filepath=paths["{}_image_label".format(split)],
          box_labels_filepath=paths["{}_boxes".format(split)],
          hierarchy_filepath=paths["hierarchy"],
          classes_filepath=paths["classes"],
      )
    # Fill class names after the data has been downloaded.
    oi_beam.fill_class_names_in_tfds_info(paths["classes"], self.info.features)
    return (pipeline | beam.Create(paths["{}_images".format(split)])
            | "ReadImages" >> beam.ParDo(oi_beam.ReadZipFn())
            | "ProcessImages" >> beam.ParDo(
                oi_beam.ProcessImageFn(
                    target_pixels=self.builder_config.target_pixels,
                    jpeg_quality=72))
            | "GenerateExamples" >> beam.ParDo(
                oi_beam.CreateDetectionExampleFn(**generate_examples_kwargs)))
