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

"""LVIS dataset."""

from __future__ import annotations

import collections
import json
import pathlib

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
LVIS: A dataset for large vocabulary instance segmentation.
"""

_CITATION = """
@inproceedings{gupta2019lvis,
  title={{LVIS}: A Dataset for Large Vocabulary Instance Segmentation},
  author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},
  booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},
  year={2019}
}
"""

_URLS = {
    'train_annotation':
        'https://s3-us-west-2.amazonaws.com/dl.fbaipublicfiles.com/LVIS/lvis_v1_train.json.zip',
    'train_images':
        'http://images.cocodataset.org/zips/train2017.zip',
    'validation_annotation':
        'https://s3-us-west-2.amazonaws.com/dl.fbaipublicfiles.com/LVIS/lvis_v1_val.json.zip',
    'validation_images':
        'http://images.cocodataset.org/zips/val2017.zip',
    'test_annotation':
        'https://s3-us-west-2.amazonaws.com/dl.fbaipublicfiles.com/LVIS/lvis_v1_image_info_test_dev.json.zip',
    'test_images':
        'http://images.cocodataset.org/zips/test2017.zip'
}

# Annotations with invalid bounding boxes. Will not be used.
_INVALID_ANNOTATIONS = [
    # Train split.
    662101,
    81217,
    462924,
    227817,
    29381,
    601484,
    412185,
    504667,
    572573,
    91937,
    239022,
    181534,
    101685,
    # Validation split.
    36668,
    57541,
    33126,
    10932
]

_NUM_CLASSES = 1203


class Lvis(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for lvis dataset."""

  VERSION = tfds.core.Version('1.2.0')
  RELEASE_NOTES = {
      '1.1.0':
          'Added fields `neg_category_ids` and `not_exhaustive_category_ids`.',
      '1.2.0':
          'Added class names.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    class_label = tfds.features.ClassLabel(
        names_file=tfds.core.tfds_path(
            'object_detection/lvis/lvis_classes.txt'))
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image':
                tfds.features.Image(encoding_format='jpeg'),
            'image/id':
                tf.int64,
            'neg_category_ids':
                tfds.features.Sequence(class_label),
            'not_exhaustive_category_ids':
                tfds.features.Sequence(class_label),
            'objects':
                tfds.features.Sequence({
                    # LVIS has unique id for each annotation.
                    'id': tf.int64,
                    'area': tf.int64,
                    'bbox': tfds.features.BBoxFeature(),
                    'label': class_label,
                    'segmentation': tfds.features.Image(shape=(None, None, 1)),
                }),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,
        homepage='https://www.lvisdataset.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = dl_manager.download_and_extract(_URLS)
    image_dirs = [
        paths['train_images'] / 'train2017',
        paths['validation_images'] / 'val2017',
        paths['test_images'] / 'test2017',
    ]
    return {
        tfds.Split.TRAIN:
            self._generate_examples(
                image_dirs, paths['train_annotation'] / 'lvis_v1_train.json'),
        tfds.Split.VALIDATION:
            self._generate_examples(
                image_dirs,
                paths['validation_annotation'] / 'lvis_v1_val.json'),
        tfds.Split.TEST:
            self._generate_examples(
                image_dirs,
                paths['test_annotation'] / 'lvis_v1_image_info_test_dev.json'),
    }

  def _generate_examples(self, image_dirs, annotation_file):
    """Yields examples."""
    lvis_annotation = LvisAnnotation(annotation_file)

    def _process_example(image_info):
      # Search image dirs.
      filename = pathlib.Path(image_info['coco_url']).name
      image = _find_image_in_dirs(image_dirs, filename)
      instances = lvis_annotation.get_annotations(img_id=image_info['id'])
      instances = [x for x in instances if x['id'] not in _INVALID_ANNOTATIONS]
      neg_category_ids = image_info.get('neg_category_ids', [])
      not_exhaustive_category_ids = image_info.get(
          'not_exhaustive_category_ids', [])
      example = {
          'image': image,
          'image/id': image_info['id'],
          'neg_category_ids': [i - 1 for i in neg_category_ids],
          'not_exhaustive_category_ids': [
              i - 1 for i in not_exhaustive_category_ids
          ],
          'objects': [],
      }
      for inst in instances:
        example['objects'].append({
            'id':
                inst['id'],
            'area':
                inst['area'],
            'bbox':
                _build_bbox(image_info, *inst['bbox']),
            'label':
                inst['category_id'] - 1,
            'segmentation':
                _build_segmentation_mask(image_info, inst['segmentation'])
        })
      return image_info['id'], example

    beam = tfds.core.lazy_imports.apache_beam
    return beam.Create(lvis_annotation.images) | beam.Map(_process_example)


def _find_image_in_dirs(image_dirs, filename):
  """Finds `filename` in one of the `image_dir` folders."""
  images = [d / filename for d in image_dirs if (d / filename).exists()]
  assert len(images) == 1, (images, image_dirs, filename)
  return images[0]


def _build_bbox(image_info, x, y, width, height):
  # build_bbox is only used within the loop so it is ok to use image_info
  return tfds.features.BBox(
      ymin=y / image_info['height'],
      xmin=x / image_info['width'],
      ymax=(y + height) / image_info['height'],
      xmax=(x + width) / image_info['width'],
  )


def _build_segmentation_mask(image_info, seg):
  cv2 = tfds.core.lazy_imports.cv2
  mask = np.zeros((image_info['height'], image_info['width']), np.uint8)
  error_msg = f'Annotation contains an invalid polygon with < 3 points: {seg}'
  assert all(len(poly) % 2 == 0 and len(poly) >= 6 for poly in seg), error_msg

  for poly in seg:
    poly = np.asarray(poly, np.int32).reshape((1, -1, 2))
    cv2.fillPoly(mask, poly, 255)
  return mask[:, :, np.newaxis]


class LvisAnnotation:
  """LVIS annotation helper class.

  The format of the annations is explained on
  https://www.lvisdataset.org/dataset.
  """

  def __init__(self, annotation_path):
    with epath.Path(annotation_path).open() as f:
      data = json.load(f)
    self._data = data

    img_id2annotations = collections.defaultdict(list)
    for a in self._data.get('annotations', []):
      img_id2annotations[a['image_id']].append(a)
    self._img_id2annotations = {
        k: list(sorted(v, key=lambda a: a['id']))
        for k, v in img_id2annotations.items()
    }

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
    # Some images don't have any annotations. Return empty list instead.
    return self._img_id2annotations.get(img_id, [])
