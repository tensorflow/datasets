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

"""MS Coco Dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import json
import os

from absl import logging
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{DBLP:journals/corr/LinMBHPRDZ14,
  author    = {Tsung{-}Yi Lin and
               Michael Maire and
               Serge J. Belongie and
               Lubomir D. Bourdev and
               Ross B. Girshick and
               James Hays and
               Pietro Perona and
               Deva Ramanan and
               Piotr Doll{\'{a}}r and
               C. Lawrence Zitnick},
  title     = {Microsoft {COCO:} Common Objects in Context},
  journal   = {CoRR},
  volume    = {abs/1405.0312},
  year      = {2014},
  url       = {http://arxiv.org/abs/1405.0312},
  archivePrefix = {arXiv},
  eprint    = {1405.0312},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/LinMBHPRDZ14},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


class Coco2014(tfds.core.GeneratorBasedBuilder):
  """MS Coco dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "COCO is a large-scale object detection, segmentation, and "
            "captioning dataset. This version contains images, bounding boxes "
            "and labels for the 2014 version.\n"
            "Note:\n"
            " * Some images from the train and validation sets don't have "
            "annotations.\n"
            " * The test split don't have any annotations (only images).\n"
            " * Coco defines 91 classes but the data only had 80 classes.\n"),
        # More info could be added, like the segmentation (as png mask),
        # captions, person key-points. For caption encoding, it would probably
        # be better to have a separate class CocoCaption2014 to avoid poluting
        # the main class with builder config for each encoder.
        features=tfds.features.FeaturesDict({
            # Images can have variable shape
            "image": tfds.features.Image(encoding_format="jpeg"),
            "image/filename": tfds.features.Text(),
            "objects": tfds.features.Sequence({
                "bbox": tfds.features.BBoxFeature(),
                # Coco has 91 categories but only 80 are present in the dataset
                "label": tfds.features.ClassLabel(num_classes=80),
                "is_crowd": tf.bool,
            }),
        }),
        urls=["http://cocodataset.org/#home"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    root_url = "http://images.cocodataset.org/"
    urls = {
        # Train/validation set
        "train_images": "zips/train2014.zip",
        "val_images": "zips/val2014.zip",
        "trainval_annotations": "annotations/annotations_trainval2014.zip",
        # Testing set (no annotations) (2014)
        "test_images": "zips/test2014.zip",
        "test_annotations": "annotations/image_info_test2014.zip",
        # Testing set (no annotations) (2015)
        "test2015_images": "zips/test2015.zip",
        "test2015_annotations": "annotations/image_info_test2015.zip",
    }
    extracted_paths = dl_manager.download_and_extract({
        key: root_url + url for key, url in urls.items()
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["train_images"],
                annotation_dir=extracted_paths["trainval_annotations"],
                split_type="train2014",
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["val_images"],
                annotation_dir=extracted_paths["trainval_annotations"],
                split_type="val2014",
            )),
        # Warning: Testing split only contains the images without any annotation
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["test_images"],
                annotation_dir=extracted_paths["test_annotations"],
                split_type="test2014",
                has_annotation=False,
            )),
        tfds.core.SplitGenerator(
            name="test2015",
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["test2015_images"],
                annotation_dir=extracted_paths["test2015_annotations"],
                split_type="test2015",
                has_annotation=False,
            )),
    ]

  def _generate_examples(
      self, image_dir, annotation_dir, split_type, has_annotation=True):
    """Generate examples as dicts.

    Args:
      image_dir: `str`, directory containing the images
      annotation_dir: `str`, directory containing
      split_type: `str`, <split_name><year> (ex: train2014)
      has_annotation: `bool`, when False (for the testing set), the annotations
        are not recorded

    Yields:
      Generator yielding the next samples
    """
    if has_annotation:
      instance_filename = "instances_{}.json"
    else:
      instance_filename = "image_info_{}.json"

    # Load the label names and images
    instance_path = os.path.join(
        annotation_dir,
        "annotations",
        instance_filename.format(split_type),
    )
    coco_annotation = CocoAnnotation(instance_path)
    # Each category is a dict:
    # {
    #    'id': 51,  # From 1-91, some entry missing
    #    'name': 'bowl',
    #    'supercategory': 'kitchen',
    # }
    categories = coco_annotation.categories
    # Each image is a dict:
    # {
    #     'id': 262145,
    #     'file_name': 'COCO_train2014_000000262145.jpg'
    #     'flickr_url': 'http://farm8.staticflickr.com/7187/xyz.jpg',
    #     'coco_url': 'http://images.cocodataset.org/train2014/xyz.jpg',
    #     'license': 2,
    #     'date_captured': '2013-11-20 02:07:55',
    #     'height': 427,
    #     'width': 640,
    # }
    images = coco_annotation.images

    # TODO(b/121375022): ClassLabel names should also contains 'id' and
    # and 'supercategory' (in addition to 'name')
    # Warning: As Coco only use 80 out of the 91 labels, the c['id'] and
    # dataset names ids won't match.
    self.info.features["objects"]["label"].names = [
        c["name"] for c in categories
    ]
    # TODO(b/121375022): Conversion should be done by ClassLabel
    categories_id2name = {c["id"]: c["name"] for c in categories}

    # Iterate over all images
    annotation_skipped = 0
    for image_info in sorted(images, key=lambda x: x["id"]):
      if has_annotation:
        # Each instance annotation is a dict:
        # {
        #     'iscrowd': 0,
        #     'bbox': [116.95, 305.86, 285.3, 266.03],
        #     'image_id': 480023,
        #     'segmentation': [[312.29, 562.89, 402.25, ...]],
        #     'category_id': 58,
        #     'area': 54652.9556,
        #     'id': 86,
        # }
        instances = coco_annotation.get_annotations(img_id=image_info["id"])
      else:
        instances = []  # No annotations

      if not instances:
        annotation_skipped += 1

      def build_bbox(x, y, width, height):
        # pylint: disable=cell-var-from-loop
        # build_bbox is only used within the loop so it is ok to use image_info
        return tfds.features.BBox(
            ymin=y / image_info["height"],
            xmin=x / image_info["width"],
            ymax=(y + height) / image_info["height"],
            xmax=(x + width) / image_info["width"],
        )
        # pylint: enable=cell-var-from-loop

      yield {
          "image": os.path.join(image_dir, split_type, image_info["file_name"]),
          "image/filename": image_info["file_name"],
          "objects": [{   # pylint: disable=g-complex-comprehension
              "bbox": build_bbox(*instance_info["bbox"]),
              "label": categories_id2name[instance_info["category_id"]],
              "is_crowd": bool(instance_info["iscrowd"]),
          } for instance_info in instances],
      }
    logging.info(
        "%d/%d images do not contains any annotations",
        annotation_skipped,
        len(images),
    )


class CocoAnnotation(object):
  """Coco annotation helper class."""

  def __init__(self, annotation_path):

    with tf.io.gfile.GFile(annotation_path) as f:
      data = json.load(f)
    self._data = data

    self._img_id2annotations = {}

    # Get the annotations associated with an image
    if "annotations" in data:  # Testing set don't has any annotations
      img_id2annotations = collections.defaultdict(list)
      for a in data["annotations"]:
        img_id2annotations[a["image_id"]].append(a)
      self._img_id2annotations = {
          k: list(sorted(v, key=lambda a: a["id"]))
          for k, v in img_id2annotations.items()
      }

  @property
  def categories(self):
    """Return the category dicts, as sorted in the file."""
    return self._data["categories"]

  @property
  def images(self):
    """Return the category dicts, as sorted in the file."""
    return self._data["images"]

  def get_annotations(self, img_id):
    """Return all annotations associated with the image id string."""
    # Some images don't have any annotations. Return empty list instead.
    return self._img_id2annotations.get(img_id, [])
