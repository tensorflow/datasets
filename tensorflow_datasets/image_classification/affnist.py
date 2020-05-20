from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
from six.moves import urllib
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {tijmentieleman,
    author = "Tijmen Tieleman",
    title  = "affNIST",
    url    = "http://www.cs.toronto.edu/~tijmen/affNIST"
}
"""

_DESCRIPTION = """
The affNIST dataset for machine learning is based on the well-known MNIST dataset.
MNIST, however, has become quite a small set, given the power of today's computers, with their multiple CPU's and sometimes GPU's.
affNIST is made by taking images from MNIST and applying various reasonable affine transformations to them.\
In the process, the images become 40x40 pixels large, with significant translations involved,\
so much of the challenge for the models is to learn that a digit means the same thing in the upper right corner as it does in the lower left corner.
"""

_AFFNIST_URL = "http://www.cs.toronto.edu/~tijmen/affNIST/32x/transformed/"
_AFFNIST_TRAIN_DATA_FILENAME = "training_batches.zip"
_AFFNIST_VALIDATION_DATA_FILENAME = "validation_batches.zip"
_AFFNIST_TEST_DATA_FILENAME = "test_batches.zip"
_AFFNIST_IMAGE_SIZE = 40
AFFNIST_IMAGE_SHAPE = (_AFFNIST_IMAGE_SIZE, _AFFNIST_IMAGE_SIZE, 1)
AFFNIST_NUM_CLASSES = 10


class Affnist(tfds.core.GeneratorBasedBuilder):
  """\
  The affNIST dataset for machine learning is based on the well-known MNIST dataset.
  It is made by taking images from MNIST and applying various reasonable affine transformations to them.
  """
  URL = _AFFNIST_URL

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=AFFNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=AFFNIST_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage='http://www.cs.toronto.edu/~tijmen/affNIST/',
        citation=_CITATION,
   )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    filenames = {
        "train_data": _AFFNIST_TRAIN_DATA_FILENAME,
        "validation_data": _AFFNIST_VALIDATION_DATA_FILENAME,
        "test_data": _AFFNIST_TEST_DATA_FILENAME,
    }

    files = dl_manager.download_and_extract(
      {k: urllib.parse.urljoin(self.URL, v) for k, v in filenames.items()})

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": os.path.join(files["train_data"], "training_batches")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "images_dir_path": os.path.join(files["validation_data"], "validation_batches")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": os.path.join(files["test_data"], "test_batches")},
        ),
    ]

  def _generate_examples(self, images_dir_path):
    """Generate affNIST examples as dicts.

    Args:
      images_dir_path (str): Path to the folder containing all the images and labels

    Yields:
      Generator yielding the next examples
    """
    path = sorted(tf.io.gfile.listdir(images_dir_path))
    loadmat = tfds.core.lazy_imports.scipy.io.loadmat
    images = [loadmat(tf.io.gfile.GFile(os.path.join(images_dir_path,i), "rb"))["affNISTdata"][0][0]["image"] for i in path]
    labels = [loadmat(tf.io.gfile.GFile(os.path.join(images_dir_path,i), "rb"))["affNISTdata"][0][0]["label_int"] for i in path]

    images = np.concatenate(images, axis = 1).T.reshape(-1, 40, 40, 1)
    labels = np.concatenate(labels, axis = 1).T.reshape(-1)

    for index, image in enumerate(images):
      record = {"image": image, "label": labels[index]}
      yield index, record
