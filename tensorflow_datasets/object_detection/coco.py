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
"""MS Coco Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import json
import os

from absl import logging
import tensorflow.compat.v2 as tf

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

DESCRIPTION = """COCO is a large-scale object detection, segmentation, and
captioning dataset. This version contains images, bounding boxes "
and labels for the {year} version.
Note:
 * Some images from the train and validation sets don't have annotations.
 * Coco 2014 and 2017 uses the same images, but different train/val/test splits
 * The test split don't have any annotations (only images).
 * Coco defines 91 classes but the data only uses 80 classes.
 * Panotptic annotations defines defines 200 classes but only uses 133.
"""


Split = collections.namedtuple(
    'Split', ['name', 'images', 'annotations', 'annotation_type'])


class AnnotationType(object):
  """Enum of the annotation format types.

  Splits are annotated with different formats.
  """
  BBOXES = 'bboxes'
  PANOPTIC = 'panoptic'
  NONE = 'none'


class CocoConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CocoConfig."""

  def __init__(
      self,
      splits=None,
      has_panoptic=False,
      **kwargs):
    super(CocoConfig, self).__init__(
        version=tfds.core.Version('1.1.0'),
        **kwargs)
    self.splits = splits
    self.has_panoptic = has_panoptic


class Coco(tfds.core.GeneratorBasedBuilder):
  """Base MS Coco dataset."""

  BUILDER_CONFIGS = [
      CocoConfig(
          name='2014',
          description=DESCRIPTION.format(year=2014),
          splits=[
              Split(
                  name=tfds.Split.TRAIN,
                  images='train2014',
                  annotations='annotations_trainval2014',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images='val2014',
                  annotations='annotations_trainval2014',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.TEST,
                  images='test2014',
                  annotations='image_info_test2014',
                  annotation_type=AnnotationType.NONE,
              ),
              # Coco2014 contains an extra test split
              Split(
                  name='test2015',
                  images='test2015',
                  annotations='image_info_test2015',
                  annotation_type=AnnotationType.NONE,
              ),
          ],
      ),
      CocoConfig(
          name='2017',
          description=DESCRIPTION.format(year=2017),
          splits=[
              Split(
                  name=tfds.Split.TRAIN,
                  images='train2017',
                  annotations='annotations_trainval2017',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images='val2017',
                  annotations='annotations_trainval2017',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.TEST,
                  images='test2017',
                  annotations='image_info_test2017',
                  annotation_type=AnnotationType.NONE,
              ),
          ],
      ),
      CocoConfig(
          name='2017_panoptic',
          description=DESCRIPTION.format(year=2017),
          has_panoptic=True,
          splits=[
              Split(
                  name=tfds.Split.TRAIN,
                  images='train2017',
                  annotations='panoptic_annotations_trainval2017',
                  annotation_type=AnnotationType.PANOPTIC,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images='val2017',
                  annotations='panoptic_annotations_trainval2017',
                  annotation_type=AnnotationType.PANOPTIC,
              ),
          ],
      ),
  ]

  def _info(self):

    features = {
        # Images can have variable shape
        'image': tfds.features.Image(encoding_format='jpeg'),
        'image/filename': tfds.features.Text(),
        'image/id': tf.int64,
    }
    # Either uses panotptic or original annotations
    if self.builder_config.has_panoptic:
      features.update({
          'panoptic_image': tfds.features.Image(encoding_format='png'),
          'panoptic_image/filename': tfds.features.Text(),
          'panoptic_objects': tfds.features.Sequence({
              'id': tf.int64,
              # Coco has unique id for each annotation. The id can be used for
              # mapping panoptic image to semantic segmentation label.
              'area': tf.int64,
              'bbox': tfds.features.BBoxFeature(),
              # Coco2017 has 200 categories but only 133 are present in the
              # dataset
              'label': tfds.features.ClassLabel(num_classes=133),
              'is_crowd': tf.bool,
          }),
      })
    else:
      features.update({
          'objects': tfds.features.Sequence({
              'id': tf.int64,
              # Coco has unique id for each annotation. The id can be used for
              # mapping panoptic image to semantic segmentation label.
              'area': tf.int64,
              'bbox': tfds.features.BBoxFeature(),
              # Coco has 91 categories but only 80 are present in the dataset
              'label': tfds.features.ClassLabel(num_classes=80),
              'is_crowd': tf.bool,
          }),
      })
    # More info could be added, like segmentation (as png mask), captions,
    # person key-points, more metadata (original flickr url,...).

    return tfds.core.DatasetInfo(
        builder=self,
        description=self.builder_config.description,
        # More info could be added, like the segmentation (as png mask),
        # captions, person key-points. For caption encoding, it would probably
        # be better to have a separate class CocoCaption2014 to avoid poluting
        # the main class with builder config for each encoder.
        features=tfds.features.FeaturesDict(features),
        homepage='http://cocodataset.org/#home',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    # Merge urls from all splits together
    urls = {}
    for split in self.builder_config.splits:
      urls['{}_images'.format(split.name)] = 'zips/{}.zip'.format(split.images)
      urls['{}_annotations'.format(split.name)] = 'annotations/{}.zip'.format(
          split.annotations)

    # DownloadManager memoize the url, so duplicate urls will only be downloaded
    # once.
    root_url = 'http://images.cocodataset.org/'
    extracted_paths = dl_manager.download_and_extract({
        key: root_url + url for key, url in urls.items()
    })

    splits = []
    for split in self.builder_config.splits:
      image_dir = extracted_paths['{}_images'.format(split.name)]
      annotations_dir = extracted_paths['{}_annotations'.format(split.name)]
      if self.builder_config.has_panoptic:
        panoptic_image_zip_path = os.path.join(
            annotations_dir,
            'annotations',
            'panoptic_{}.zip'.format(split.images)
        )
        panoptic_dir = dl_manager.extract(panoptic_image_zip_path)
        panoptic_dir = os.path.join(
            panoptic_dir, 'panoptic_{}'.format(split.images))
      else:
        panoptic_dir = None
      splits.append(tfds.core.SplitGenerator(
          name=split.name,
          gen_kwargs=dict(
              image_dir=image_dir,
              annotation_dir=annotations_dir,
              split_name=split.images,
              annotation_type=split.annotation_type,
              panoptic_dir=panoptic_dir,
          ),
      ))
    return splits

  def _generate_examples(
      self,
      image_dir,
      annotation_dir,
      split_name,
      annotation_type,
      panoptic_dir):
    """Generate examples as dicts.

    Args:
      image_dir: `str`, directory containing the images
      annotation_dir: `str`, directory containing annotations
      split_name: `str`, <split_name><year> (ex: train2014, val2017)
      annotation_type: `AnnotationType`, the annotation format (NONE, BBOXES,
        PANOPTIC)
      panoptic_dir: If annotation_type is PANOPTIC, contains the panoptic
        image directory

    Yields:
      example key and data
    """

    if annotation_type == AnnotationType.BBOXES:
      instance_filename = 'instances_{}.json'
    elif annotation_type == AnnotationType.PANOPTIC:
      instance_filename = 'panoptic_{}.json'
    elif annotation_type == AnnotationType.NONE:  # No annotation for test sets
      instance_filename = 'image_info_{}.json'

    # Load the annotations (label names, images metadata,...)
    instance_path = os.path.join(
        annotation_dir,
        'annotations',
        instance_filename.format(split_name),
    )
    coco_annotation = ANNOTATION_CLS[annotation_type](instance_path)
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
    #     'file_name': 'COCO_train2017_000000262145.jpg'
    #     'flickr_url': 'http://farm8.staticflickr.com/7187/xyz.jpg',
    #     'coco_url': 'http://images.cocodataset.org/train2017/xyz.jpg',
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
    if self.builder_config.has_panoptic:
      objects_key = 'panoptic_objects'
    else:
      objects_key = 'objects'
    self.info.features[objects_key]['label'].names = [
        c['name'] for c in categories
    ]
    # TODO(b/121375022): Conversion should be done by ClassLabel
    categories_id2name = {c['id']: c['name'] for c in categories}

    # Iterate over all images
    annotation_skipped = 0
    for image_info in sorted(images, key=lambda x: x['id']):
      if annotation_type == AnnotationType.BBOXES:
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
        instances = coco_annotation.get_annotations(img_id=image_info['id'])
      elif annotation_type == AnnotationType.PANOPTIC:
        # Each panoptic annotation is a dict:
        # {
        #     'file_name': '000000037777.png',
        #     'image_id': 37777,
        #     'segments_info': [
        #         {
        #             'area': 353,
        #             'category_id': 52,
        #             'iscrowd': 0,
        #             'id': 6202563,
        #             'bbox': [221, 179, 37, 27],
        #         },
        #         ...
        #     ]
        # }
        panoptic_annotation = coco_annotation.get_annotations(
            img_id=image_info['id'])
        instances = panoptic_annotation['segments_info']
      else:
        instances = []  # No annotations

      if not instances:
        annotation_skipped += 1

      def build_bbox(x, y, width, height):
        # pylint: disable=cell-var-from-loop
        # build_bbox is only used within the loop so it is ok to use image_info
        return tfds.features.BBox(
            ymin=y / image_info['height'],
            xmin=x / image_info['width'],
            ymax=(y + height) / image_info['height'],
            xmax=(x + width) / image_info['width'],
        )
        # pylint: enable=cell-var-from-loop

      example = {
          'image': os.path.join(image_dir, split_name, image_info['file_name']),
          'image/filename': image_info['file_name'],
          'image/id': image_info['id'],
          objects_key: [{   # pylint: disable=g-complex-comprehension
              'id': instance['id'],
              'area': instance['area'],
              'bbox': build_bbox(*instance['bbox']),
              'label': categories_id2name[instance['category_id']],
              'is_crowd': bool(instance['iscrowd']),
          } for instance in instances]
      }
      if self.builder_config.has_panoptic:
        panoptic_filename = panoptic_annotation['file_name']
        panoptic_image_path = os.path.join(panoptic_dir, panoptic_filename)
        example['panoptic_image'] = panoptic_image_path
        example['panoptic_image/filename'] = panoptic_filename

      yield image_info['file_name'], example

    logging.info(
        '%d/%d images do not contains any annotations',
        annotation_skipped,
        len(images),
    )


class CocoAnnotation(object):
  """Coco annotation helper class."""

  def __init__(self, annotation_path):
    with tf.io.gfile.GFile(annotation_path) as f:
      data = json.load(f)
    self._data = data

  @property
  def categories(self):
    """Return the category dicts, as sorted in the file."""
    return self._data['categories']

  @property
  def images(self):
    """Return the image dicts, as sorted in the file."""
    return self._data['images']

  def get_annotations(self, img_id):
    """Return all annotations associated with the image id string."""
    raise NotImplementedError  # AnotationType.NONE don't have annotations


class CocoAnnotationBBoxes(CocoAnnotation):
  """Coco annotation helper class."""

  def __init__(self, annotation_path):
    super(CocoAnnotationBBoxes, self).__init__(annotation_path)

    img_id2annotations = collections.defaultdict(list)
    for a in self._data['annotations']:
      img_id2annotations[a['image_id']].append(a)
    self._img_id2annotations = {
        k: list(sorted(v, key=lambda a: a['id']))
        for k, v in img_id2annotations.items()
    }

  def get_annotations(self, img_id):
    """Return all annotations associated with the image id string."""
    # Some images don't have any annotations. Return empty list instead.
    return self._img_id2annotations.get(img_id, [])


class CocoAnnotationPanoptic(CocoAnnotation):
  """Coco annotation helper class."""

  def __init__(self, annotation_path):
    super(CocoAnnotationPanoptic, self).__init__(annotation_path)
    self._img_id2annotations = {
        a['image_id']: a for a in self._data['annotations']
    }

  def get_annotations(self, img_id):
    """Return all annotations associated with the image id string."""
    return self._img_id2annotations[img_id]


ANNOTATION_CLS = {
    AnnotationType.NONE: CocoAnnotation,
    AnnotationType.BBOXES: CocoAnnotationBBoxes,
    AnnotationType.PANOPTIC: CocoAnnotationPanoptic,
}
