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

"""VGGFace2 Dataset."""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{Cao18,
author = "Cao, Q. and Shen, L. and Xie, W. and Parkhi, O. M. and Zisserman, A.",
title  = "VGGFace2: A dataset for recognising faces across pose and age",
booktitle = "International Conference on Automatic Face and Gesture \
Recognition",
year  = "2018"}"""

_DESCRIPTION = """\
VGGFace2 is a large-scale face recognition dataset. \
Images are downloaded from Google Image Search and have large variations \
in pose, age, illumination, ethnicity and profession. VGGFace2 contains images \
from identities spanning a wide range of different ethnicities, accents, \
professions and ages. All face images are captured "in the wild", with pose \
and emotion variations and different lighting and occlusion conditions. Face \
distribution for different identities is varied, from 87 to 843, with an \
average of 362 images for each subject.
"""


_LABELS_FNAME = 'image_classification/vgg_face2_labels.txt'


class VggFace2(tfds.core.GeneratorBasedBuilder):
  """VGGFace2 - A large scale image dataset for face recognition."""

  VERSION = tfds.core.Version('1.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain two files: vggface2_test.tar.gz and
  vggface2_train.tar.gz.
  You need to register on http://zeus.robots.ox.ac.uk/vgg_face2/signup/ in
  order to get the link to download the dataset.
  """

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),
        }),
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='http://zeus.robots.ox.ac.uk/vgg_face2/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    train_path = os.path.join(dl_manager.manual_dir, 'vggface2_train.tar.gz')
    test_path = os.path.join(dl_manager.manual_dir, 'vggface2_test.tar.gz')
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(test_path):
      raise AssertionError(
          'VGGFace2 requires manual download of the data. Please download '
          'the train and test set and place them into: {}, {}'.format(
              train_path, test_path))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': dl_manager.iter_archive(train_path),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'archive': dl_manager.iter_archive(test_path),
            },
        ),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    for fname, fobj in archive:
      fname = fname.replace('\\', '/')  # For windows compatibility
      if fname.startswith('train/'):
        file_name = fname[len('train/'):]
      else:
        file_name = fname[len('test/'):]
      record = {'file_name': file_name, 'image': fobj, 'label': file_name[:7]}
      yield fname, record
