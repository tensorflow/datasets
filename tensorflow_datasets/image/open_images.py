# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = '''\
Open Images is a dataset of ~9M images that have been annotated with image-level
 labels and object bounding boxes.

The training set of V4 contains 14.6M bounding boxes for 600 object classes on
1.74M images, making it the largest existing dataset with object location
annotations. The boxes have been largely manually drawn by professional
annotators to ensure accuracy and consistency. The images are very diverse and
often contain complex scenes with several objects (8.4 per image on average).
Moreover, the dataset is annotated with image-level labels spanning thousands of
classes.
'''

_CITATION = '''\
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
'''

# Reading from .tar.gz is slower than extracting the gz and then reading from
# tar. We still read from the tar because it's faster to read fewer files on
# many network based FS.
# pylint: disable=line-too-long
_URLS = {
    'train_images': [
        tfds.download.Resource(
            url='http://open-images-dataset.s3.amazonaws.com/tar/train_%s.tar.gz' % i,
            extract_method=tfds.download.ExtractMethod.GZIP)
        for i in '0123456789abcdef'],
    'test_images': tfds.download.Resource(
        url='http://open-images-dataset.s3.amazonaws.com/tar/test.tar.gz',
        extract_method=tfds.download.ExtractMethod.GZIP),
    'validation_images': tfds.download.Resource(
        url='http://open-images-dataset.s3.amazonaws.com/tar/validation.tar.gz',
        extract_method=tfds.download.ExtractMethod.GZIP),
    'train_human_labels': 'https://storage.googleapis.com/openimages/2018_04/train/train-annotations-human-imagelabels.csv',
    'train_machine_labels': 'https://storage.googleapis.com/openimages/2018_04/train/train-annotations-machine-imagelabels.csv',
    'test_human_labels': 'https://storage.googleapis.com/openimages/2018_04/test/test-annotations-human-imagelabels.csv',
    'test_machine_labels': 'https://storage.googleapis.com/openimages/2018_04/test/test-annotations-machine-imagelabels.csv',
    'validation_human_labels': 'https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-human-imagelabels.csv',
    'validation_machine_labels': 'https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-machine-imagelabels.csv',
    'class_descriptions': 'https://storage.googleapis.com/openimages/2018_04/class-descriptions.csv',
}
# pylint: enable=line-too-long


class OpenImagesV4(tfds.core.GeneratorBasedBuilder):
  """Open Images v4."""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'image/filename': tfds.features.Text(),  # eg '226f0a1873b9bf8e.jpg'
            'objects': tfds.features.SequenceDict({
                'label': tfds.features.ClassLabel(),
                # Original data is 0, .1, ..., 1. We use 0, 1, 2, ..., 10.
                'confidence': tf.int32,
                'source': tfds.features.ClassLabel(names=[
                    'verification', 'crowdsource-verification',  # human labels
                    'machine',
                ]),
            }),
        }),
        urls=['https://storage.googleapis.com/openimages/web/index.html'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    paths = dl_manager.download_and_extract(_URLS)
    source_str2int = self.info.features['objects']['source'].str2int
    # Set the labels' names:
    with tf.gfile.Open(paths['class_descriptions']) as classes_f:
      classes = [l.split(',')[0]
                 for l in classes_f.read().split('\n') if l]
    logging.info('Number of loaded classes: %s', len(classes))
    self.info.features['objects']['label'].names = classes
    label_str2int = self.info.features['objects']['label'].str2int
    # Load labels from CSVs:
    def load(paths_):
      return _load_objects([paths[p] for p in paths_],
                           source_str2int, label_str2int)
    train_objects = load(['train_human_labels', 'train_machine_labels'])
    test_objects = load(['test_human_labels', 'test_machine_labels'])
    validation_objects = load(['validation_human_labels',
                               'validation_machine_labels'])
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=512,
            gen_kwargs=dict(archive_paths=paths['train_images'],
                            objects=train_objects),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=36,
            gen_kwargs=dict(archive_paths=[paths['test_images']],
                            objects=test_objects),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=12,
            gen_kwargs=dict(archive_paths=[paths['validation_images']],
                            objects=validation_objects),
        ),
    ]

  def _generate_examples(self, archive_paths, objects):
    for archive_path in archive_paths:
      logging.info('Opening archive %s ...', archive_path)
      archive = tfds.download.iter_archive(archive_path,
                                           tfds.download.ExtractMethod.TAR_GZ)
      for fpath, fobj in archive:
        fname = os.path.basename(fpath)
        image_id, _ = os.path.splitext(fname)
        objs = objects[int(image_id, 16)]
        image_objects = [
            dict(label=label, confidence=confidence, source=source)
            for label, confidence, source in objs]
        yield {
            'image': fobj,
            'image/filename': fname,
            'objects': image_objects,
        }


def _load_objects(csv_paths, source_str2int, label_str2int):
  """Returns objects listed within given CSV files."""
  logging.info('Loading CSVs %s', csv_paths)
  objects = []
  current_image_id = None
  current_objects = []
  for labels_path in csv_paths:
    with tf.gfile.Open(labels_path) as csv_f:
      csv_f.readline()  # Drop headers
      reader = csv.reader(csv_f)
      for image_id, source, label, confidence in reader:
        image_id = int(image_id, 16)
        source = source_str2int(source)
        label = label_str2int(label)
        if image_id != current_image_id:
          if current_image_id:
            objects.append((current_image_id, current_objects))
          current_image_id = image_id
          current_objects = []
        current_objects.append((label, int(float(confidence) * 10), source))
      # the last line of file:
      objects.append((current_image_id, current_objects))
  return dict(objects)
