    """TODO(my_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf
import tensorflow_datasets as tfds

# TODO(my_dataset): BibTeX citation
_CITATION = """\
@inproceedings{inproceedings,
    author = {Wu, Hongbo and Bailey, Chris and Rasoulinejad, Parham and Li, Shuo},
    year = {2017},
    month = {09},
    pages = {127--135},
    title = {Automatic Landmark Estimation for Adolescent Idiopathic Scoliosis Assessment Using BoostNet},
    doi = {10.1007/978-3-319-66182-7_15}
}
"""

# TODO(my_dataset):
_DESCRIPTION = """\
The dataset consists of 609 spinal anterior-posterior x-ray images; it is dataset 16 on SpineWeb.
The Cobb angles for each image were calculated using landmarks, where four landmarks denoted one vertebrae.
"""
#_IMAGE_SHAPE = ?

class SpineWeb(tfds.core.GeneratorBasedBuilder):
  """SpineWeb"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(encoding_format='jpeg'), # image size?
            "label": tfds.features.Tensor(shape=(3,), dtype=tf.float32) # main thoracic, proximal thoracic, thoracolumbar/lumbar
            })
        }),
        supervised_keys=('image','cobb_angles'),
        urls=['http://spineweb.digitalimaginggroup.ca'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(isic): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs

    dl_paths = dl_manager.download_and_extract({
      'train': 'https://spineweb.s3.amazonaws.com/training_images.zip',
      'train_csv': 'https://spineweb.s3.amazonaws.com/training_angles.csv',
      'test': 'https://spineweb.s3.amazonaws.com/test_images.zip',
      'test_csv': 'https://spineweb.s3.amazonaws.com/test_angles.csv'
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'images_dir_path': dl_paths['train'],
                'labels': dl_paths['train_csv']
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'images_dir_path': dl_paths['test'],
                'labels': dl_paths['test_csv']
            },
        ),
    ]

  def _generate_examples(self, images_dir_path, labels):
    """Yields examples."""
    # TODO(my_dataset): Yields (key, example) tuples from the dataset
    image_names_list = tf.io.gfile.listdir(images_dir_path)
    with open(labels, 'rb') as f:
        labels_list = [tf.convert_to_tensor(line) for line in csv.reader(f)]
    for image_name, label in zip(image_names_list, labels_list):
        record = {
            "image": os.path.join(images_dir_path, image_name),
            "label": label
        }

        yield image_name, record
