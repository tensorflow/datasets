"""caltech256 dataset."""

import os
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Caltech-256 is an object recognition dataset spanning 257 classes (256 object classes and an additional clutter class).
This dataset contains 30,607 real-world images, of different sizes, with each class having at least 80 images.
Object categories are extremely diverse, ranging from grasshopper to tuning fork.
This dataset is an improvement to its predecessor, the Caltech 101 dataset.
"""

_CITATION = """\
@article{article,
title = {Caltech-256 Object Category Dataset},
author = {Griffin, Gregory and Holub, Alex and Perona, Pietro},
journal = {CalTech Report}
year = {2007},
}
"""

_LABELS_FNAME = 'image_classification/caltech256/caltech256_labels.txt'

_BASE_URL = 'https://drive.google.com/u/1/uc?id=1r6o0pSROcV1_VwT4oSjA2FBUSCWGuxLK&export=download'

_TRAIN_POINTS_PER_CLASS = 75


class Caltech256(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for caltech256 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
    '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""

    class_labels_file = tfds.core.tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
        'image': tfds.features.Image(),
        'label': tfds.features.ClassLabel(names_file=class_labels_file),
        'image/file_name': tfds.features.Text(),
      }),
      supervised_keys=('image', 'label'),
      # Homepage of the dataset
      homepage='http://www.vision.caltech.edu/Image_Datasets/Caltech256/',
      citation=_CITATION
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_BASE_URL)
    return {
      'train': self._generate_examples(path, True),
      'test': self._generate_examples(path, False),
    }

  def _generate_examples(self, images_dir_path, is_train_split):
    """Yields examples of data images and labels."""

    # Sets random seed so the random partitioning of files is the same when
    # called for the train and test splits.
    numpy_original_state = np.random.get_state()
    np.random.seed(1234)

    parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
    walk_dir = os.path.join(images_dir_path, parent_dir)
    dirs = tf.io.gfile.listdir(walk_dir)

    for d in dirs:
      # Each directory contains all images from a single class.
      if tf.io.gfile.isdir(os.path.join(walk_dir, d)):
        for full_path, _, filenames in tf.io.gfile.walk(os.path.join(walk_dir, d)):
          if _TRAIN_POINTS_PER_CLASS > len(filenames):
            raise ValueError('Fewer than {} ({}) points in class {}'.format(
              _TRAIN_POINTS_PER_CLASS, len(filenames), d))
          train_fnames = np.random.choice(
            filenames, _TRAIN_POINTS_PER_CLASS, replace=False)
          test_fnames = set(filenames).difference(train_fnames)
          filenames_to_emit = train_fnames if is_train_split else test_fnames

          for image_file in filenames_to_emit:
            if image_file.endswith('.jpg'):
              image_path = os.path.join(full_path, image_file)
              image_label = d.split('.')[1]  # ex: 008.bathtub -> bathtub
              record = {
                'image': image_path,
                'label': image_label,
                'image/file_name': image_file,
              }
              yield '%s/%s' % (d, image_file), record

    # Resets the seeds to their previous states.
    np.random.set_state(numpy_original_state)
