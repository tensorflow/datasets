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

class Coco2017(tfds.core.GeneratorBasedBuilder):
  """MS Coco2017 dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "COCO is a large-scale object detection, segmentation, and "
            "captioning dataset. This version contains images, panoptic segmentation "
            "and labels for the 2017 version.\n"
            "Note:\n"
            " * Some images from the train and validation sets don't have "
            "annotations.\n"
            " * The test split don't have any annotations (only images).\n"
            " * Coco2017 defines 133 classes.\n"),
        features=tfds.features.FeaturesDict({
            # Images can have variable shape
            "image": tfds.features.Image(encoding_format="jpeg"),
            "image/filename": tfds.features.Text(),
            "panoptic_image": tfds.features.Image(encoding_format="png"),
            "panoptic_image/filename": tfds.features.Text(),
            "segments_info": tfds.features.SequenceDict({
                "area": tf.int64,
                "id": tf.int64,
                "bbox": tfds.features.BBoxFeature(),
                # Coco2017 has 133 categories
                "label": tfds.features.ClassLabel(num_classes=133),
                "is_crowd": tf.bool,
            }),
        }),
        urls=["http://cocodataset.org/#home"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    root_url = "http://images.cocodataset.org/"
    urls = {
        # Train/validation set
        "train_images": "zips/train2017.zip",
        "val_images": "zips/val2017.zip",
        "panoptic_annotations_trainval2017": "annotations/panoptic_annotations_trainval2017.zip",
        # Testing set (no annotations) (2017)
        "test_images": "zips/test2017.zip",
        "test_annotations": "annotations/image_info_test2017.zip",
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
                annotation_dir=extracted_paths["panoptic_annotations_trainval2017"],
                split_type="train2017",
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["val_images"],
                annotation_dir=extracted_paths["panoptic_annotations_trainval2017"],
                split_type="val2017",
            )),
        # Warning: Testing split only contains the images without any annotation
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs=dict(
                image_dir=extracted_paths["test_images"],
                annotation_dir=extracted_paths["test_annotations"],
                split_type="test2017",
                has_annotation=False,
            )),
    ]




  def _generate_examples(
      self, image_dir, annotation_dir, split_type, has_annotation=True):
    """Generate examples as dicts.

    Args:
      image_dir: `str`, directory containing the images
      annotation_dir: `str`, directory containing annotations
      split_type: `str`, <split_name><year> (ex: train2017)
      has_annotation: `bool`, when False (for the testing set), the annotations
        are not recorded

    Yields:
      Generator yielding the next samples
    """
    if has_annotation:
      instance_filename = "panoptic_{}.json"
    else:
      instance_filename = "image_info_{}.json"

    # Load the label names and images
    instance_path = os.path.join(
        annotation_dir,
        "annotations",
        instance_filename.format(split_type),
    )
    coco_annotation = Coco2017Annotation(instance_path)
    # Each category is a dict:
    # {
    #    'id': 51,  
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


    self.info.features["segments_info"]["label"].names = [
        c["name"] for c in categories
    ]
    
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
          "panoptic_image": os.path.join(annotation_dir, "annotations","panoptic_{}".format(split_type),image_info["file_name"].replace(".jpg",".png")),
          "panoptic_image/filename": image_info["file_name"].replace(".jpg",".png"), 
          "segments_info": [{
              "area": instance_info["segments_info"][j]["area"],
              "id": instance_info["segments_info"][j]["id"],
              "bbox": build_bbox(*instance_info["segments_info"][j]["bbox"]),
              "label": categories_id2name[instance_info["segments_info"][j]["category_id"]],
              "is_crowd": bool(instance_info["segments_info"][j]["iscrowd"]),
          }  for instance_info in instances for j in range(len(instance_info['segments_info']))],
      }
    logging.info(
        "%d/%d images do not contains any annotations",
        annotation_skipped,
        len(images),
    )


class Coco2017Annotation(object):
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
          k: list(sorted(v, key=lambda a: a["image_id"]))
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


