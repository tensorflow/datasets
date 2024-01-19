# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

import io
import os

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

# Web-site is asking to cite paper from 2015.
# https://image-net.org/challenges/LSVRC/2012/index#cite

# From https://github.com/cytsai/ilsvrc-cmyk-image-list
CMYK_IMAGES = [
    'n01739381_1309.JPEG',
    'n02077923_14822.JPEG',
    'n02447366_23489.JPEG',
    'n02492035_15739.JPEG',
    'n02747177_10752.JPEG',
    'n03018349_4028.JPEG',
    'n03062245_4620.JPEG',
    'n03347037_9675.JPEG',
    'n03467068_12171.JPEG',
    'n03529860_11437.JPEG',
    'n03544143_17228.JPEG',
    'n03633091_5218.JPEG',
    'n03710637_5125.JPEG',
    'n03961711_5286.JPEG',
    'n04033995_2932.JPEG',
    'n04258138_17003.JPEG',
    'n04264628_27969.JPEG',
    'n04336792_7448.JPEG',
    'n04371774_5854.JPEG',
    'n04596742_4225.JPEG',
    'n07583066_647.JPEG',
    'n13037406_4650.JPEG',
]

PNG_IMAGES = ['n02105855_2933.JPEG']


class Builder(tfds.core.GeneratorBasedBuilder):
  """Imagenet 2012, aka ILSVRC 2012."""

  VERSION = tfds.core.Version('5.1.0')
  SUPPORTED_VERSIONS = [
      tfds.core.Version('5.0.0'),
  ]
  RELEASE_NOTES = {
      '5.1.0': 'Added test split.',
      '5.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
      '4.0.0': '(unpublished)',
      '3.0.0': """
      Fix colorization on ~12 images (CMYK -> RGB).
      Fix format for consistency (convert the single png image to Jpeg).
      Faster generation reading directly from the archive.
      """,
      '2.0.1': 'Encoding fix. No changes from user point of view.',
      '2.0.0': 'Fix validation labels.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain two files: ILSVRC2012_img_train.tar and
  ILSVRC2012_img_val.tar.
  You need to register on https://image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='https://image-net.org/',
    )

  def _split_generators(self, dl_manager):
    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    test_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_test.tar')
    splits = []
    _add_split_if_exists(
        split_list=splits,
        split=tfds.Split.TRAIN,
        split_path=train_path,
        dl_manager=dl_manager,
    )
    _add_split_if_exists(
        split_list=splits,
        split=tfds.Split.VALIDATION,
        split_path=val_path,
        dl_manager=dl_manager,
        validation_labels=imagenet_common.get_validation_labels(val_path),
    )
    _add_split_if_exists(
        split_list=splits,
        split=tfds.Split.TEST,
        split_path=test_path,
        dl_manager=dl_manager,
        labels_exist=False,
    )
    if not splits:
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the data and place them into:\n'
          f' * train: {train_path}\n'
          f' * test: {test_path}\n'
          f' * validation: {val_path}\n'
          'At least one of the split should be available.'
      )
    return splits

  def _fix_image(self, image_fname, image):
    """Fix image color system and format starting from v 3.0.0."""
    if self.version < '3.0.0':
      return image
    if image_fname in CMYK_IMAGES:
      image = io.BytesIO(tfds.core.utils.jpeg_cmyk_to_rgb(image.read()))
    elif image_fname in PNG_IMAGES:
      image = io.BytesIO(tfds.core.utils.png_to_jpeg(image.read()))
    return image

  def _generate_examples(
      self, archive, validation_labels=None, labels_exist=True
  ):
    """Yields examples."""
    if not labels_exist:  # Test split
      for key, example in imagenet_common.generate_examples_test(archive):
        yield key, example
    if validation_labels:  # Validation split
      for key, example in imagenet_common.generate_examples_validation(
          archive, validation_labels
      ):
        yield key, example
    # Training split. Main archive contains archives names after a synset noun.
    # Each sub-archive contains pictures associated to that synset.
    for fname, fobj in archive:
      label = fname[:-4]  # fname is something like 'n01632458.tar'
      # TODO(b/117643231): in py3, the following lines trigger tarfile module
      # to call `fobj.seekable()`, which Gfile doesn't have. We should find an
      # alternative, as this loads ~150MB in RAM.
      fobj_mem = io.BytesIO(fobj.read())
      for image_fname, image in tfds.download.iter_archive(
          fobj_mem, tfds.download.ExtractMethod.TAR_STREAM
      ):
        image = self._fix_image(image_fname, image)
        record = {
            'file_name': image_fname,
            'image': image,
            'label': label,
        }
        yield image_fname, record


def _add_split_if_exists(split_list, split, split_path, dl_manager, **kwargs):
  """Add split to given list of splits only if the file exists."""
  if not tf.io.gfile.exists(split_path):
    logging.warning(
        (
            'ImageNet 2012 Challenge %s split not found at %s. '
            'Proceeding with data generation anyways but the split will be '
            'missing from the dataset...'
        ),
        str(split),
        split_path,
    )
  else:
    split_list.append(
        tfds.core.SplitGenerator(
            name=split,
            gen_kwargs={
                'archive': dl_manager.iter_archive(split_path),
                **kwargs,
            },
        ),
    )
