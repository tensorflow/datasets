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

"""Imagenet datasets."""

import io
import os
import tarfile

from absl import logging

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = '''\
ILSVRC 2012, commonly known as 'ImageNet' is an image dataset organized
according to the WordNet hierarchy. Each meaningful concept in WordNet,
possibly described by multiple words or word phrases, is called a "synonym set"
or "synset". There are more than 100,000 synsets in WordNet, majority of them
are nouns (80,000+). In ImageNet, we aim to provide on average 1000 images to
illustrate each synset. Images of each concept are quality-controlled and
human-annotated. In its completion, we hope ImageNet will offer tens of
millions of cleanly sorted images for most of the concepts in the WordNet
hierarchy.

The test split contains 100K images but no labels because no labels have been
publicly released. We provide support for the test split from 2012 with the
minor patch released on October 10, 2019. In order to manually download this
data, a user must perform the following operations:

1. Download the 2012 test split available [here](http://www.image-net.org/challenges/LSVRC/2012/downloads.php#images).
2. Download the October 10, 2019 patch. There is a Google Drive link to the
patch provided on the same page.
3. Combine the two tar-balls, manually overwriting any images in the original
archive with images from the patch. According to the instructions on
image-net.org, this procedure overwrites just a few images.

The resulting tar-ball may then be processed by TFDS.

To assess the accuracy of a model on the ImageNet test split, one must run
inference on all images in the split, export those results to a text file that
must be uploaded to the ImageNet evaluation server. The maintainers of the
ImageNet evaluation server permits a single user to submit up to 2 submissions
per week in order to prevent overfitting.

To evaluate the accuracy on the test split, one must first create an account at
image-net.org. This account must be approved by the site administrator. After
the account is created, one can submit the results to the test server at
http://www.image-net.org/challenges/LSVRC/2013/test_server
The submission consists of several ASCII text files corresponding to multiple
tasks. The task of interest is "Classification submission (top-5 cls error)".
A sample of an exported text file looks like the following:

```
771 778 794 387 650
363 691 764 923 427
737 369 430 531 124
755 930 755 59 168
```

The export format is described in full in "readme.txt" within the 2013
development kit available here:
http://imagenet.stanford.edu/image/ilsvrc2013/ILSVRC2013_devkit.tgz
Please see the section entitled "3.3 CLS-LOC submission format". Briefly, the
format of the text file is 100,000 lines corresponding to each image in the test
split. Each line of integers correspond to the rank-ordered, top 5 predictions
for each test image. The integers are 1-indexed corresponding to the line number
in the corresponding labels file. See imagenet2012_labels.txt.
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

_LABELS_FNAME = 'image_classification/imagenet2012_labels.txt'

# This file contains the validation labels, in the alphabetic order of
# corresponding image names (and not in the order they have been added to the
# tar file).
_VALIDATION_LABELS_FNAME = 'image_classification/imagenet2012_validation_labels.txt'


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


class Imagenet2012(tfds.core.GeneratorBasedBuilder):
  """Imagenet 2012, aka ILSVRC 2012."""

  VERSION = tfds.core.Version('5.1.0', 'Added test split.')
  SUPPORTED_VERSIONS = [
      tfds.core.Version('5.0.0'),
  ]

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain two files: ILSVRC2012_img_train.tar and
  ILSVRC2012_img_val.tar.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self):
    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='http://image-net.org/',
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
      # `splitlines` to remove trailing `\r` in Windows
      labels = labels_f.read().strip().splitlines()
    with tf.io.gfile.GFile(val_path, 'rb') as tar_f_obj:
      tar = tarfile.open(mode='r:', fileobj=tar_f_obj)
      images = sorted(tar.getnames())
    return dict(zip(images, labels))

  def _split_generators(self, dl_manager):
    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    test_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_test.tar')
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, val_path))
    splits = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': dl_manager.iter_archive(train_path),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'archive': dl_manager.iter_archive(val_path),
                'validation_labels': self._get_validation_labels(val_path),
            },
        ),
    ]

    if not tf.io.gfile.exists(test_path):
      logging.warning('ImageNet 2012 Challenge TEST split not found at %s. '
                      'Please download this split. Proceeding with data '
                      'generation anyways to retain backward compatibility.',
                      test_path)
    else:
      splits.append(
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  'archive': dl_manager.iter_archive(test_path),
                  'labels_exist': False,
              }))
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

  def _generate_examples(self, archive, validation_labels=None,
                         labels_exist=True):
    """Yields examples."""
    if not labels_exist:  # Test split
      for key, example in self._generate_examples_test(archive):
        yield key, example
    if validation_labels:  # Validation split
      for key, example in self._generate_examples_validation(archive,
                                                             validation_labels):
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
          fobj_mem, tfds.download.ExtractMethod.TAR_STREAM):
        image = self._fix_image(image_fname, image)
        record = {
            'file_name': image_fname,
            'image': image,
            'label': label,
        }
        yield image_fname, record

  def _generate_examples_validation(self, archive, labels):
    for fname, fobj in archive:
      record = {
          'file_name': fname,
          'image': fobj,
          'label': labels[fname],
      }
      yield fname, record

  def _generate_examples_test(self, archive):
    for fname, fobj in archive:
      record = {
          'file_name': fname,
          'image': fobj,
          'label': -1,
      }
      yield fname, record
