"""Breast cancer whole slide image dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import csv
import numpy as np

import tensorflow as tf
import tensorflow_datasets as tfds

_URL = "http://spiechallenges.cloudapp.net/competitions/14#participate"

# BibTeX citation
_CITATION = """\
@article{peikari2017automatic,
  title={Automatic cellularity assessment from post-treated breast surgical specimens},
  author={Peikari, Mohammad and Salama, Sherine and Nofech-Mozes, Sharon and Martel, Anne L},
  journal={Cytometry Part A},
  volume={91},
  number={11},
  pages={1078--1087},
  year={2017},
  publisher={Wiley Online Library}
}
"""


_DESCRIPTION = """\
The dataset's training/validation set consists of 2578 patches extracted from 96 breast cancer \
whole slide images (WSI). Each patch is labelled by a tumor cellularity score. The testing set \
contains 1121 patches from 25 WSIs. Labels for testing data are not provided by far. \
The dataset can be used to develop an automated method for evaluating cancer cellularity from \
histology patches extracted from WSIs. The method is aimed to increase reproducibility of cancer \
cellularity scores and enhance tumor burden assessment.
"""

_IMAGE_SHAPE = (512, 512, 3)

def _load_tif(path):
  with tf.io.gfile.GFile(path, "rb") as fp:
    image = tfds.core.lazy_imports.PIL_Image.open(fp)
  return np.array(image)


class Breastpathq(tfds.core.GeneratorBasedBuilder):
  """Breast cancer whole slide image dataset."""

  # Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tf.float32
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    # manual download is required for this dataset
    extracted_path = dl_manager.manual_dir
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
              "images_dir_path": os.path.join(extracted_path, "breastpathq/datasets/train"),
              "labels": os.path.join(extracted_path, "breastpathq/datasets/train_labels.csv"),
            },
        ),
        tfds.core.SplitGenerator(
          name=tfds.Split.VALIDATION,
          gen_kwargs={
            "images_dir_path": os.path.join(extracted_path, "breastpathq/datasets/validation"),
            "labels": os.path.join(extracted_path, "breastpathq-test/val_labels.csv"),
          }
        ), 
    ]

  def _generate_examples(self, image_dir_path, labels):
    """Yields examples."""
    # Yields (key, example) tuples from the dataset
    with tf.io.gfile.GFile(labels, "r") as f:
      dataset = csv.DictReader(f)
      for row in dataset:
        image_id = row['slide']+'_'+row['rid']
        yield image_id, {
            "image": _load_tif(os.path.join(image_dir_path, image_id+'.tif')),
            'label': row['y'],
        }

