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
"""Imagenet subset datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os

import tensorflow.compat.v2 as tf
from tensorflow_datasets.image_classification.imagenet import Imagenet2012
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = '''\
Imagenet2012Subset is a subset of original ImageNet ILSVRC 2012 dataset.
The dataset share the *same* validation set as the original ImageNet ILSVRC 2012
dataset. However, the training set is subsampled in a label balanced fashion.
In `1pct` configuration, 1%, or 12811, images are sampled, most classes have
the same number of images (average 12.8), some classes randomly have 1 more
example than others; and in `10pct` configuration, ~10%, or 128116, most classes
have the same number of images (average 128), and some classes randomly have 1
more example than others.

This is supposed to be used as a benchmark for semi-supervised learning, and
has been originally used in SimCLR paper (https://arxiv.org/abs/2002.05709).
'''

_CITATION = '''\
@article{chen2020simple,
  title={A Simple Framework for Contrastive Learning of Visual Representations},
  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
  journal={arXiv preprint arXiv:2002.05709},
  year={2020}
}
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

# pylint: disable=line-too-long
_LABELS_FNAME = 'image_classification/imagenet2012_labels.txt'
SUBSET2FILES = {
    '1pct': 'https://raw.githubusercontent.com/google-research/simclr/master/imagenet_subsets/1percent.txt',
    '10pct': 'https://raw.githubusercontent.com/google-research/simclr/master/imagenet_subsets/10percent.txt'
}


class Imagenet2012Subset(Imagenet2012):
  """Class balanced subset of Imagenet 2012 dataset."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(  # pylint: disable=g-complex-comprehension
          name=subset_size,
          description='{} of total ImageNet training set.'.format(subset_size),
          version=tfds.core.Version(
              '5.0.0', ''),
      ) for subset_size in SUBSET2FILES
  ]

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
        homepage='http://image-net.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    # We don't import the original test split, as it doesn't include labels.
    # These were never publicly released.
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, val_path))

    # Download and load subset file.
    subset_file = dl_manager.download(SUBSET2FILES[self.builder_config.name])
    if isinstance(subset_file, list):  # it will only be a list during testing,
      subset_file = subset_file[0]     # where the first entry is 1percent.txt.
    with tf.io.gfile.GFile(subset_file) as fp:
      subset = set(fp.read().split('\n'))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': dl_manager.iter_archive(train_path),
                'subset': subset,
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

  def _generate_examples(self, archive, subset=None, validation_labels=None):
    """Yields examples."""
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
        if subset is None or image_fname in subset:  # filtering using subset.
          record = {
              'file_name': image_fname,
              'image': image,
              'label': label,
          }
          yield image_fname, record

