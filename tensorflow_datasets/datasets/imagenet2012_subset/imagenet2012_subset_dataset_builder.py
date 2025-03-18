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

"""Imagenet subset datasets."""

import io
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet2012_dataset_builder
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

# pylint: disable=line-too-long
SUBSET2FILES = {
    '1pct': 'https://raw.githubusercontent.com/google-research/simclr/master/imagenet_subsets/1percent.txt',
    '10pct': 'https://raw.githubusercontent.com/google-research/simclr/master/imagenet_subsets/10percent.txt',
}


class Builder(imagenet2012_dataset_builder.Builder):
  """Class balanced subset of Imagenet 2012 dataset."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(  # pylint: disable=g-complex-comprehension
          name=subset_size,
          description='{} of total ImageNet training set.'.format(subset_size),
          version=tfds.core.Version('5.0.0'),
      )
      for subset_size in SUBSET2FILES
  ]

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='http://image-net.org/',
    )

  def _split_generators(self, dl_manager):
    # Import ImageNet here to avoid circular dependencies

    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    # We don't import the original test split, as it doesn't include labels.
    # These were never publicly released.
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, val_path
          )
      )

    # Download and load subset file.
    subset_file = dl_manager.download(SUBSET2FILES[self.builder_config.name])
    if isinstance(subset_file, list):  # it will only be a list during testing,
      subset_file = subset_file[0]  # where the first entry is 1percent.txt.
    with epath.Path(subset_file).open() as fp:
      subset = set(fp.read().splitlines())  # remove trailing `\r` in Windows

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
                'validation_labels': imagenet_common.get_validation_labels(
                    val_path
                ),
            },
        ),
    ]

  def _generate_examples(self, archive, subset=None, validation_labels=None):
    """Yields examples."""
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
      ):  # pytype: disable=wrong-arg-types  # gen-stub-imports
        image = self._fix_image(image_fname, image)
        if subset is None or image_fname in subset:  # filtering using subset.
          record = {
              'file_name': image_fname,
              'image': image,
              'label': label,
          }
          yield image_fname, record
