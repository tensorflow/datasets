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

"""MS Coco Dataset."""

import collections
import json
import os
import numpy as np

# TODO external dependency
from pycocotools import mask as maskUtils

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
    'Split',
    ['name', 'images', 'annotation_file', 'annotation_download',
     'annotation_type'])


class AnnotationType(object):
  """Enum of the annotation format types.

  Splits are annotated with different formats.
  """
  BBOXES = 'bboxes'
  PANOPTIC = 'panoptic'
  POSE = 'pose'
  NONE = 'none'


class CocoConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CocoConfig."""

  def __init__(
      self,
      splits=None,
      has_panoptic=False,
      has_pose=False,
      **kwargs):
    super(CocoConfig, self).__init__(
        version=tfds.core.Version('1.1.0'),
        **kwargs)
    self.splits = splits
    self.has_panoptic = has_panoptic
    self.has_pose = has_pose


class Coco(tfds.core.GeneratorBasedBuilder):
  """Base MS Coco dataset."""

  BUILDER_CONFIGS = [
      CocoConfig(
          name='2014',
          description=DESCRIPTION.format(year=2014),
          splits=[
              Split(
                  name=tfds.Split.TRAIN,
                  images=['train2014'],
                  annotation_file='instances_train2014.json',
                  annotation_download='annotations_trainval2014',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images=['val2014'],
                  annotation_file='instances_val2014.json',
                  annotation_download='annotations_trainval2014',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.TEST,
                  images=['test2014'],
                  annotation_file='image_info_test2014.json',
                  annotation_download='image_info_test2014',
                  annotation_type=AnnotationType.NONE,
              ),
              # Coco2014 contains an extra test split
              Split(
                  name='test2015',
                  images=['test2015'],
                  annotation_file='image_info_test2015.json',
                  annotation_download='image_info_test2015',
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
                  images=['train2017'],
                  annotation_file='instances_train2017.json',
                  annotation_download='annotations_trainval2017',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images=['val2017'],
                  annotation_file='instances_train2017.json',
                  annotation_download='annotations_trainval2017',
                  annotation_type=AnnotationType.BBOXES,
              ),
              Split(
                  name=tfds.Split.TEST,
                  images=['test2017'],
                  annotation_file='image_info_test2017.json',
                  annotation_download='image_info_test2017',
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
                  images=['train2017'],
                  annotation_file='panoptic_train2017.json',
                  annotation_download='panoptic_annotations_trainval2017',
                  annotation_type=AnnotationType.PANOPTIC,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images=['val2017'],
                  annotation_file='panoptic_val2017.json',
                  annotation_download='panoptic_annotations_trainval2017',
                  annotation_type=AnnotationType.PANOPTIC,
              ),
          ],
      ),
      CocoConfig(
          name='2014_pose',
          description=DESCRIPTION.format(year=2014),
          has_pose=True,
          splits=[
              Split(
                  name=tfds.Split.TRAIN,
                  images=['train2014'],
                  annotation_file='densepose_coco_2014_train.json',
                  annotation_download='densepose_coco_2014_train',
                  annotation_type=AnnotationType.POSE,
              ),
              Split(
                  name='valminusminival2014',
                  images=['val2014'],
                  annotation_file='densepose_coco_2014_valminusminival.json',
                  annotation_download='densepose_coco_2014_valminusminival',
                  annotation_type=AnnotationType.POSE,
              ),
              Split(
                  name=tfds.Split.VALIDATION,
                  images=['val2014'],
                  annotation_file='densepose_coco_2014_minival.json',
                  annotation_download='densepose_coco_2014_minival',
                  annotation_type=AnnotationType.POSE,
              ),
              Split(
                  name=tfds.Split.TEST,
                  images=['test2014', 'test2015'],
                  annotation_file='densepose_coco_2014_test.json',
                  annotation_download='densepose_coco_2014_test',
                  annotation_type=AnnotationType.NONE,
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
    elif self.builder_config.has_pose:
      features.update({
          'people': tfds.features.Sequence({
              'id': tf.int64,
              'num_keypoints': tf.int64,
              'joints': tfds.features.Tensor(shape=(17, 2), dtype=tf.int64),
              'joints_visible': tfds.features.Tensor(shape=(17,), dtype=tf.bool),
              'area': tf.int64,
              'body_segmentation': tfds.features.Image(shape=(256, 256, 1), encoding_format='png'),
              'bbox': tfds.features.BBoxFeature(),
              # This is only for consistency with other annotation formats, the only available class
              # are people.
              'label': tfds.features.ClassLabel(num_classes=1),
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
    splits = []
    root_url = 'http://images.cocodataset.org/'
    for split in self.builder_config.splits:
      urls = {}
      for images in split.images:
        urls['{}_images'.format(images)] = '{}zips/{}.zip'.format(root_url, images)
      if self.builder_config.has_pose:
        urls['annotations'] = \
            'https://dl.fbaipublicfiles.com/densepose/{}.json'.format(split.annotation_download)
      else:
        urls['annotations'] = '{}annotations/{}.zip'.format(
            root_url, split.annotation_download)

      # DownloadManager memoize the url, so duplicate urls will only be downloaded
      # once.
      extracted = dl_manager.download_and_extract(urls)

      image_paths = [os.path.join(extracted['{}_images'.format(images)], images)
                     for images in split.images]

      if self.builder_config.has_panoptic:
        # Built on assumption that there is only one image download for panoptic
        panoptic_image_zip_path = os.path.join(
            extracted['annotations'],
            'annotations',
            'panoptic_{}.zip'.format(split.images[0])
        )
        panoptic_dir = dl_manager.extract(panoptic_image_zip_path)
        panoptic_dir = os.path.join(
            panoptic_dir, 'panoptic_{}'.format(split.images[0]))
      else:
        panoptic_dir = None
      if self.builder_config.has_pose:
        annotation_path = extracted['annotations']
      else:
        annotation_path = os.path.join(
            extracted['annotations'], 'annotations', split.annotation_file)
      splits.append(tfds.core.SplitGenerator(
          name=split.name,
          gen_kwargs=dict(
              image_paths=image_paths,
              annotation_path=annotation_path,
              annotation_type=split.annotation_type,
              panoptic_dir=panoptic_dir,
          ),
      ))
    return splits

  def _generate_examples(
      self,
      image_paths,
      annotation_path,
      annotation_type,
      panoptic_dir):
    """Generate examples as dicts.

    Args:
      image_paths: List[`str`], directories containing the images
      annotation_path: `str`, path containing annotations
      annotation_type: `AnnotationType`, the annotation format (NONE, BBOXES,
        PANOPTIC)
      panoptic_dir: If annotation_type is PANOPTIC, contains the panoptic
        image directory

    Yields:
      example key and data
    """
    # Load the annotations (label names, images metadata,...)
    coco_annotation = ANNOTATION_CLS[annotation_type](annotation_path)
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
    elif self.builder_config.has_pose:
      objects_key = 'people'
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
      elif annotation_type == AnnotationType.POSE:
        # Each pose annotation is a dict:
        # {
        #     'segmentation': [[345.28, 220.68, 348.17, 269.8, ...]],
        #     'num_keypoints': 13,
        #     'keypoints': [0, 0, 0, 0, 0, 0, 381, 69, 2, 377, 67, 2, ...], (x y visibility)
        #     'dp_masks': [
        #        {
        #             'counts': 'hb71o70000001O0jL2ZNOd18VNHh1=UNDh1...',
        #             'size': [256, 256]
        #        },
        #        ...
        #      ],
        #      'area': 86145.2971,
        #      'dp_I': [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, ...],
        #      'dp_x': [133.66580200195312, 61.39377212524414, 93.56140899658203, ...],
        #      'dp_U': [0.07984049618244171, 0.11004531383514404, 0.19391614198684692, ...],
        #      'image_id': 36,
        #      'dp_V': [0.34230515360832214, 0.6589370965957642, 0.5380166172981262, ...],
        #      'bbox': [167.58, 162.89, 310.61, 465.19],
        #      'category_id': 1,
        #      'dp_y': [96.58982849121094, 97.64864349365234, 116.95169067382812, ...],
        #      'id': 453991
        # }
        #
        # Documentation from
        # https://github.com/facebookresearch/DensePose/blob/master/challenge/2019_COCO_DensePose/data_format.md
        # DensePose annotations are stored in dp_* fields:
        #
        # Annotated masks:
        # dp_masks: RLE encoded dense masks. All part masks are of size 256x256. They correspond to
        #           14 semantically meaningful parts of the body: Torso, Right Hand, Left Hand,
        #           Left Foot, Right Foot, Upper Leg Right, Upper Leg Left, Lower Leg Right, Lower
        #           Leg Left, Upper Arm Left, Upper Arm Right, Lower Arm Left, Lower Arm Right, Head;
        #
        # Annotated points:
        # dp_x, dp_y: spatial coordinates of collected points on the image. The coordinates are
        #             scaled such that the bounding box size is 256x256;
        # dp_I:       The patch index that indicates which of the 24 surface patches the point is
        #             on. Patches correspond to the body parts described above. Some body parts are
        #             split into 2 patches: 1, 2 = Torso, 3 = Right Hand, 4 = Left Hand, 5 = Left
        #             Foot, 6 = Right Foot, 7, 9 = Upper Leg Right, 8, 10 = Upper Leg Left, 11,
        #             13 = Lower Leg Right, 12, 14 = Lower Leg Left, 15, 17 = Upper Arm Left,
        #             16, 18 = Upper Arm Right, 19, 21 = Lower Arm Left, 20, 22 = Lower Arm Right,
        #             23, 24 = Head;
        # dp_U, dp_V: Coordinates in the UV space. Each surface patch has a separate 2D parameterization.
        pose_annotations = coco_annotation.get_annotations(img_id=image_info['id'])
        additional_instance_infos = []
        for annotation in pose_annotations:
          keypoints = np.array(annotation['keypoints']).reshape(17, 3)
          additional_info = {
            'num_keypoints': annotation['num_keypoints'],
            'joints': keypoints[:, :2],
            'joints_visible': keypoints[:, 2] > 0,
          }
          if 'dp_masks' in annotation:
            body_parts = np.zeros([256, 256, 1], dtype='uint8')
            assert len(annotation['dp_masks']) == 14
            for i, mask in enumerate(annotation['dp_masks']):
              if mask:  # sometimes masks are just empty
                decoded_mask = maskUtils.decode(mask)
                body_parts[decoded_mask > 0] = i + 1
          else:
            body_parts = 255 * np.ones([256, 256, 1], dtype='uint8')
          additional_info['body_segmentation'] = body_parts
          additional_instance_infos.append(additional_info)
        instances = pose_annotations
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

      # search for the image in all provided directories
      possible_images = (os.path.join(directory, image_info['file_name'])
                         for directory in image_paths)
      image = next(i for i in possible_images if tf.io.gfile.exists(i))

      example = {
          'image': image,
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
      if annotation_type == AnnotationType.POSE:
        for i, additional_info in enumerate(additional_instance_infos):
          example[objects_key][i].update(additional_info)

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


class CocoAnnotationPose(CocoAnnotation):
  """Coco human pose annotation helper class."""

  def __init__(self, annotation_path):
    super(CocoAnnotationPose, self).__init__(annotation_path)
    img_id2annotations = collections.defaultdict(list)
    for a in self._data['annotations']:
      img_id2annotations[a['image_id']].append(a)
    self._img_id2annotations = {
        k: list(sorted(v, key=lambda a: a['id']))
        for k, v in img_id2annotations.items()
    }

  def get_annotations(self, img_id):
    """Return all annotations associated with the image id string."""
    return self._img_id2annotations[img_id]


ANNOTATION_CLS = {
    AnnotationType.NONE: CocoAnnotation,
    AnnotationType.BBOXES: CocoAnnotationBBoxes,
    AnnotationType.PANOPTIC: CocoAnnotationPanoptic,
    AnnotationType.POSE: CocoAnnotationPose,
}
