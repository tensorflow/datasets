"""A dataset of spine x-ray images and cobb angles"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets as tfds
import imageio
import numpy as np
import csv
import os

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

_DESCRIPTION = """\
The dataset consists of 609 spinal anterior-posterior x-ray images; it is dataset 16 on SpineWeb.
The Cobb angles for each image were calculated using landmarks, where four landmarks denoted one vertebrae.
Here, the training labels are a tensor of 3 cobb angles, corresponding to thoracic, proximal thoracic, and thoracolumbar/lumbar
"""


class SpineWeb(tfds.core.GeneratorBasedBuilder):
  """SpineWeb"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(None, None, 1)),  # b&w jpeg
            # main thoracic, proximal thoracic, thoracolumbar/lumbar cobb angles
            "label": tfds.features.Tensor(shape=(3,), dtype=tf.float32)
        }),
        supervised_keys=('image', 'label'),
        urls=['http://spineweb.digitalimaginggroup.ca'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
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
    unordered_list = tf.io.gfile.listdir(images_dir_path)
    image_names_list = sorted(unordered_list)
    with tf.io.gfile.GFile(labels, 'r') as f:
        labels_list = [tf.convert_to_tensor(
            np.array(line).astype(np.float32)) for line in csv.reader(f)]
    for image_name, label in zip(image_names_list, labels_list):
        # file_path = "%s/%s" % (images_dir_path, image_name)
        file_path = os.path.join(images_dir_path, image_name)
        print(file_path)
        # if file_path.endswith('.jpg'):
        #     img = imageio.imread(file_path, as_gray=True, pilmode='L')
        #     img = img.astype(np.uint8)
        #     img = img[..., None]
        # else:
        #     img = file_path
        img = imageio.imread(img_file, as_gray=True, pilmode='L')
        img = img.astype(np.uint8)
        img = img[..., None]
        # img = tf.io.read_file(file_path)
        # img = tf.image.decode_jpeg(img, channels=1).numpy()
        record = {
          "image": img,
          "label": label
        }

    yield image_name, record
