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

"""Open images datasets.

https://storage.googleapis.com/openimages/web/index.html
"""

import collections
import csv
import functools
import io
import os

from absl import logging
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Open Images is a dataset of ~9M images that have been annotated with image-level
 labels and object bounding boxes.

The training set of V4 contains 14.6M bounding boxes for 600 object classes on
1.74M images, making it the largest existing dataset with object location
annotations. The boxes have been largely manually drawn by professional
annotators to ensure accuracy and consistency. The images are very diverse and
often contain complex scenes with several objects (8.4 per image on average).
Moreover, the dataset is annotated with image-level labels spanning thousands of
classes.
"""

_CITATION = """\
@article{OpenImages,
  author = {Alina Kuznetsova and
            Hassan Rom and
            Neil Alldrin and
            Jasper Uijlings and
            Ivan Krasin and
            Jordi Pont-Tuset and
            Shahab Kamali and
            Stefan Popov and
            Matteo Malloci and
            Tom Duerig and
            Vittorio Ferrari},
  title = {The Open Images Dataset V4: Unified image classification,
           object detection, and visual relationship detection at scale},
  year = {2018},
  journal = {arXiv:1811.00982}
}
@article{OpenImages2,
  author = {Krasin, Ivan and
            Duerig, Tom and
            Alldrin, Neil and
            Ferrari, Vittorio
            and Abu-El-Haija, Sami and
            Kuznetsova, Alina and
            Rom, Hassan and
            Uijlings, Jasper and
            Popov, Stefan and
            Kamali, Shahab and
            Malloci, Matteo and
            Pont-Tuset, Jordi and
            Veit, Andreas and
            Belongie, Serge and
            Gomes, Victor and
            Gupta, Abhinav and
            Sun, Chen and
            Chechik, Gal and
            Cai, David and
            Feng, Zheyun and
            Narayanan, Dhyanesh and
            Murphy, Kevin},
  title = {OpenImages: A public dataset for large-scale multi-label and
           multi-class image classification.},
  journal = {Dataset available from
             https://storage.googleapis.com/openimages/web/index.html},
  year={2017}
}
"""

# Reading from .tar.gz is slower than extracting the gz and then reading from
# tar. We still read from the tar because it's faster to read fewer files on
# many network based FS.
# pylint: disable=line-too-long
_URLS = {
    'train_images': [
        tfds.download.Resource(  # pylint:disable=g-complex-comprehension
            url='http://open-images-dataset.s3.amazonaws.com/tar/train_%s.tar.gz'
            % i_,
            extract_method=tfds.download.ExtractMethod.GZIP)
        for i_ in '0123456789abcdef'
    ],
    'test_images':
        tfds.download.Resource(
            url='http://open-images-dataset.s3.amazonaws.com/tar/test.tar.gz',
            extract_method=tfds.download.ExtractMethod.GZIP),
    'validation_images':
        tfds.download.Resource(
            url='http://open-images-dataset.s3.amazonaws.com/tar/validation.tar.gz',
            extract_method=tfds.download.ExtractMethod.GZIP),
    'train_human_labels':
        'https://storage.googleapis.com/openimages/2018_04/train/train-annotations-human-imagelabels.csv',
    'train_machine_labels':
        'https://storage.googleapis.com/openimages/2018_04/train/train-annotations-machine-imagelabels.csv',
    'test_human_labels':
        'https://storage.googleapis.com/openimages/2018_04/test/test-annotations-human-imagelabels.csv',
    'test_machine_labels':
        'https://storage.googleapis.com/openimages/2018_04/test/test-annotations-machine-imagelabels.csv',
    'validation_human_labels':
        'https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-human-imagelabels.csv',
    'validation_machine_labels':
        'https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-machine-imagelabels.csv',
    'train-annotations-bbox':
        'https://storage.googleapis.com/openimages/2018_04/train/train-annotations-bbox.csv',
    'test-annotations-bbox':
        'https://storage.googleapis.com/openimages/2018_04/test/test-annotations-bbox.csv',
    'validation-annotations-bbox':
        'https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-bbox.csv',
}
# pylint: enable=line-too-long

_Object = collections.namedtuple('Object', ['label', 'confidence', 'source'])
_Bbox = collections.namedtuple('Bbox', [
    'label', 'source', 'bbox', 'is_occluded', 'is_truncated', 'is_group_of',
    'is_depiction', 'is_inside'
])

IMAGE_LEVEL_SOURCES = [
    'verification',
    'crowdsource-verification',  # human labels
    'machine',
]

BBOX_SOURCES = [
    'freeform',
    'xclick',  # Manually drawn boxes.
    'activemil',  # Machine generated, human controlled.
]


class OpenImagesV4Config(tfds.core.BuilderConfig):
  """BuilderConfig for OpenImagesV4."""

  def __init__(self, target_pixels=None, **kwargs):
    """BuilderConfig for OpenImagesV4.

    Args:
      target_pixels: If given, rescale the images so that the number of pixels
        is roughly this value.
      **kwargs: keyword arguments forward to super.
    """
    kwargs['version'] = tfds.core.Version('2.0.0')
    kwargs['release_notes'] = {
        '2.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
    }
    super(OpenImagesV4Config, self).__init__(**kwargs)
    self._target_pixels = target_pixels

  @property
  def target_pixels(self):
    return self._target_pixels


class OpenImagesV4(tfds.core.GeneratorBasedBuilder):
  """Open Images v4."""

  BUILDER_CONFIGS = [
      OpenImagesV4Config(
          name='original',
          description='Images at their original resolution and quality.'),
      OpenImagesV4Config(
          name='300k',
          description='Images have roughly 300,000 pixels, at 72 JPEG quality.',
          target_pixels=300000),
      OpenImagesV4Config(
          name='200k',
          description='Images have roughly 200,000 pixels, at 72 JPEG quality.',
          target_pixels=200000)
  ]

  def _info(self):
    source_class_label = tfds.features.ClassLabel(names=IMAGE_LEVEL_SOURCES +
                                                  BBOX_SOURCES)
    all_class_label = tfds.features.ClassLabel(
        names_file=tfds.core.tfds_path(
            os.path.join('object_detection', 'open_images_classes_all.txt')))
    trainable_class_label = tfds.features.ClassLabel(
        names_file=tfds.core.tfds_path(
            os.path.join('object_detection',
                         'open_images_classes_trainable.txt')))
    boxable_class_label = tfds.features.ClassLabel(
        names_file=tfds.core.tfds_path(
            os.path.join('object_detection',
                         'open_images_classes_boxable.txt')))
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image':
                tfds.features.Image(),
            'image/filename':
                tfds.features.Text(),  # eg '226f0a1873b9bf8e.jpg'
            'objects':
                tfds.features.Sequence({
                    'label': all_class_label,
                    # Original data is 0, .1, ..., 1. We use 0, 1, 2, ..., 10.
                    'confidence': tf.int32,
                    'source': source_class_label,
                }),
            'objects_trainable':
                tfds.features.Sequence({
                    'label': trainable_class_label,
                    # Original data is 0, .1, ..., 1. We use 0, 1, 2, ..., 10.
                    'confidence': tf.int32,
                    'source': source_class_label,
                }),
            'bobjects':
                tfds.features.Sequence({
                    'label': boxable_class_label,
                    'source': source_class_label,
                    'bbox': tfds.features.BBoxFeature(),
                    # Following values can be:
                    # 1 (true), 0 (false) and -1 (unknown).
                    'is_occluded': tf.int8,
                    'is_truncated': tf.int8,
                    'is_group_of': tf.int8,
                    'is_depiction': tf.int8,
                    'is_inside': tf.int8,
                }),
        }),
        homepage='https://storage.googleapis.com/openimages/web/index.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    paths = dl_manager.download_and_extract(_URLS)

    # Load labels from CSVs:
    def load(names):
      csv_positions = [0] * len(names)
      return functools.partial(_load_objects, [paths[name] for name in names],
                               csv_positions)

    train_objects = load(['train_human_labels', 'train_machine_labels'])
    test_objects = load(['test_human_labels', 'test_machine_labels'])
    validation_objects = load(
        ['validation_human_labels', 'validation_machine_labels'])

    def load_boxes(name):
      csv_positions = [0]
      return functools.partial(_load_bboxes, paths[name], csv_positions)

    train_bbox = load_boxes('train-annotations-bbox')
    test_bbox = load_boxes('test-annotations-bbox')
    validation_bbox = load_boxes('validation-annotations-bbox')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                archive_paths=paths['train_images'],
                objects_getter=train_objects,
                bboxes_getter=train_bbox,
                prefixes='0123456789abcdef'),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                archive_paths=[paths['test_images']],
                objects_getter=test_objects,
                bboxes_getter=test_bbox),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(
                archive_paths=[paths['validation_images']],
                objects_getter=validation_objects,
                bboxes_getter=validation_bbox),
        ),
    ]

  def _generate_examples(self,
                         archive_paths,
                         objects_getter,
                         bboxes_getter,
                         prefixes=None):
    """Yields examples."""
    trainable_classes = set(
        self.info.features['objects_trainable']['label'].names)
    for i, archive_path in enumerate(archive_paths):
      prefix = prefixes[i] if prefixes else None
      objects = objects_getter(prefix)
      bboxes = bboxes_getter(prefix)
      logging.info('Opening archive %s ...', archive_path)
      archive = tfds.download.iter_archive(
          archive_path, tfds.download.ExtractMethod.TAR_STREAM)
      for fpath, fobj in archive:
        fname = os.path.basename(fpath)
        image_id = int(os.path.splitext(fname)[0], 16)
        image_objects = [obj._asdict() for obj in objects.get(image_id, [])]
        image_bboxes = [bbox._asdict() for bbox in bboxes.get(image_id, [])]
        image_objects_trainable = [
            obj for obj in image_objects if obj['label'] in trainable_classes
        ]
        record = {
            'image':
                _resize_image_if_necessary(
                    fobj, target_pixels=self.builder_config.target_pixels),
            'image/filename':
                fname,
            'objects':
                image_objects,
            'objects_trainable':
                image_objects_trainable,
            'bobjects':
                image_bboxes,
        }
        yield fname, record


def _resize_image_if_necessary(image_fobj, target_pixels=None):
  """Resize an image to have (roughly) the given number of target pixels.

  Args:
    image_fobj: File object containing the original image.
    target_pixels: If given, number of pixels that the image must have.

  Returns:
    A file object.
  """
  if target_pixels is None:
    return image_fobj

  cv2 = tfds.core.lazy_imports.cv2
  # Decode image using OpenCV2.
  image = cv2.imdecode(
      np.frombuffer(image_fobj.read(), dtype=np.uint8), flags=3)
  # Get image height and width.
  height, width, _ = image.shape
  actual_pixels = height * width
  if actual_pixels > target_pixels:
    factor = np.sqrt(target_pixels / actual_pixels)
    image = cv2.resize(image, dsize=None, fx=factor, fy=factor)
  # Encode the image with quality=72 and store it in a BytesIO object.
  _, buff = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 72])
  return io.BytesIO(buff.tobytes())


def _load_objects(csv_paths, csv_positions, prefix):
  """Returns objects listed within given CSV files."""
  logging.info('Loading CSVs %s from positions %s with prefix %s', csv_paths,
               csv_positions, prefix)
  objects = collections.defaultdict(list)
  for i, labels_path in enumerate(csv_paths):
    with tf.io.gfile.GFile(labels_path) as csv_f:
      if csv_positions[i] > 0:
        csv_f.seek(csv_positions[i])
      else:
        csv_f.readline()  # Drop headers
      reader = csv.reader(csv_f)
      for image_id, source, label, confidence in reader:
        if prefix and image_id[0] != prefix:
          break
        csv_positions[i] = csv_f.tell()
        image_id = int(image_id, 16)
        current_obj = _Object(label, int(float(confidence) * 10), source)
        objects[image_id].append(current_obj)
  return dict(objects)


def _load_bboxes(csv_path, csv_positions, prefix):
  """Returns bounded boxes listed within given CSV file."""
  logging.info('Loading CSVs %s from positions %s with prefix %s', csv_path,
               csv_positions, prefix)
  boxes = collections.defaultdict(list)
  with tf.io.gfile.GFile(csv_path) as csv_f:
    if csv_positions[0] > 0:
      csv_f.seek(csv_positions[0])
    else:
      csv_f.readline()  # Drop headers
    reader = csv.reader(csv_f)
    for (
        image_id,
        source,
        label,
        confidence,
        xmin,
        xmax,
        ymin,
        ymax,
        is_occluded,
        is_truncated,
        is_group_of,
        is_depiction,
        is_inside,
    ) in reader:
      if prefix and image_id[0] != prefix:
        break
      csv_positions[0] = csv_f.tell()
      image_id = int(image_id, 16)
      del confidence  # always 1 in bounding boxes.
      current_row = _Bbox(
          label, source,
          tfds.features.BBox(
              float(ymin), float(xmin), float(ymax), float(xmax)),
          int(is_occluded), int(is_truncated), int(is_group_of),
          int(is_depiction), int(is_inside))
      boxes[image_id].append(current_row)
  return dict(boxes)
