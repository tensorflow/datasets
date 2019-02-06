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

"""Imagenet datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os
import tarfile

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = '''\
ILSVRC 2012, aka ImageNet is an image dataset organized according to the
WordNet hierarchy. Each meaningful concept in WordNet, possibly described by
multiple words or word phrases, is called a "synonym set" or "synset". There are
more than 100,000 synsets in WordNet, majority of them are nouns (80,000+). In
ImageNet, we aim to provide on average 1000 images to illustrate each synset.
Images of each concept are quality-controlled and human-annotated. In its
completion, we hope ImageNet will offer tens of millions of cleanly sorted
images for most of the concepts in the WordNet hierarchy.
'''

# Web-site is asking to cite paper from 2015.
# http://www.image-net.org/challenges/LSVRC/2012/index#cite
_CITATION = '''\
@article{ILSVRC15,
Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
Title = {{ImageNet Large Scale Visual Recognition Challenge}},
Year = {2015},
journal   = {International Journal of Computer Vision (IJCV)},
doi = {10.1007/s11263-015-0816-y},
volume={115},
number={3},
pages={211-252}
}
'''

_LABELS_FNAME = 'image/imagenet2012_labels.txt'

# This file contains the validation labels, in the alphabetic order of
# corresponding image names (and not in the order they have been added to the
# tar file).
_VALIDATION_LABELS_FNAME = 'image/imagenet2012_validation_labels.txt'


class Imagenet2012(tfds.core.GeneratorBasedBuilder):
  """Imagenet 2012, aka ILSVRC 2012."""

  VERSION = tfds.core.Version('2.0.0')
  # 1.0.0 to 2.0.0: fix validation labels.

  def _info(self):
    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        urls=['http://image-net.org/'],
        citation=_CITATION,
    )

  @staticmethod
  def _get_validation_labels(val_path):
    """Returns labels for validation.

    Args:
      val_path: path to TAR file containing validation images. It is used to
      retrieve the name of pictures and associate them to labels.

    Returns:
      dict, mapping from image name (str) to label (str).
    """
    labels_path = tfds.core.get_tfds_path(_VALIDATION_LABELS_FNAME)
    with tf.io.gfile.GFile(labels_path) as labels_f:
      labels = labels_f.read().strip().split('\n')
    with tf.io.gfile.GFile(val_path, 'rb') as tar_f_obj:
      tar = tarfile.open(mode='r:', fileobj=tar_f_obj)
      images = sorted(tar.getnames())
    return dict(zip(images, labels))

  def _split_generators(self, dl_manager):
    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join([train_path, val_path])
      raise AssertionError(msg)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1000,
            gen_kwargs={
                'archive': dl_manager.iter_archive(train_path),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=5,
            gen_kwargs={
                'archive': dl_manager.iter_archive(val_path),
                'validation_labels': self._get_validation_labels(val_path),
            },
        ),
    ]

  def _generate_examples(self, archive, validation_labels=None):
    if validation_labels:  # Validation split
      for example in self._generate_examples_validation(archive,
                                                        validation_labels):
        yield example
    # Training split. Main archive contains archives names after a synset noun.
    # Each sub-archive contains pictures associated to that synset.
    for fname, fobj in archive:
      label = fname[:-4]  # fname is something like 'n01632458.tar'
      # TODO(b/117643231): in py3, the following lines trigger tarfile module
      # to call `fobj.seekable()`, which Gfile doesn't have. We should find an
      # alternative, as this loads ~150MB in RAM.
      fobj_mem = io.BytesIO(fobj.read())
      for image_fname, image_fobj in tfds.download.iter_archive(
          fobj_mem, tfds.download.ExtractMethod.TAR):
        yield {
            'file_name': image_fname,
            'image': image_fobj,
            'label': label,
        }

  def _generate_examples_validation(self, archive, labels):
    for fname, fobj in archive:
      yield {
          'file_name': fname,
          'image': fobj,
          'label': labels[fname],
      }
