"""The STL-10 dataset is an image recognition dataset for developing \
unsupervised feature learning, deep learning, self-taught learning algorithms. \
It is inspired by the CIFAR-10 dataset but with some modifications.\
 In particular, each class has fewer labeled training examples than in CIFAR-10,\
 but a very large set of unlabeled examples is provided to learn \
image models prior to supervised training. The primary challenge is to make use \
of the unlabeled data (which comes from a similar but different distribution from the labeled data) to build a useful prior.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import numpy as np
import tensorflow_datasets.public_api as tfds


_CITATION = """
Adam Coates, Honglak Lee, Andrew Y. Ng An Analysis of Single Layer Networks in Unsupervised Feature Learning AISTATS, 2011.
"""


_DESCRIPTION = """
The STL-10 dataset is an image recognition dataset for developing unsupervised
feature learning, deep learning, self-taught learning algorithms. It is inspired
by the CIFAR-10 dataset but with some modifications. In particular, each class
has fewer labeled training examples than in CIFAR-10, but a very large set of
unlabeled examples is provided to learn image models prior to supervised
training.The primary challenge is to make use of the unlabeled data
(which comes from a similar but different distribution from the labeled data) to build a useful prior.
"""


def read_all_images(images_path):
    """
    :param path_to_data: the file containing the binary images from the STL-10 dataset
    :return: an array containing all the images
    """
    with tf.io.gfile.GFile(images_path, 'rb') as f:
        everything = np.frombuffer(f.read(),dtype=np.uint8)
        images = np.reshape(everything, (-1, 3, 96, 96))
        images = np.transpose(images, (0, 3, 2, 1))
        return images


def read_labels(path_to_labels):
    """
     :param path_to_labels: path to the binary file containing labels from the STL-10 dataset
     :return: an array containing the labels
    """
    with tf.io.gfile.GFile(path_to_labels, 'rb') as f:
        labels = np.frombuffer(f.read(),dtype=np.uint8)
        return labels


class Stl10(tfds.core.GeneratorBasedBuilder):
    """
    The STL-10 dataset is an image recognition dataset for developing unsupervised feature learning, deep learning, self-taught learning algorithms.
    """

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(shape=(96,96,3)),
                "label": tfds.features.ClassLabel(num_classes=11)
            }),
            supervised_keys=("image", "label"),
            # Homepage of the dataset for documentation
            urls=["https://cs.stanford.edu/~acoates/stl10/"],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        dl_paths = dl_manager.download_and_extract({
            'stl10': 'http://ai.stanford.edu/~acoates/stl10/stl10_binary.tar.gz',
        })
        extracted_path = dl_paths['stl10']
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "images_dir_path": os.path.join(
                        extracted_path,
                        "stl10_binary/train_X.bin"),
                    "labels_path": os.path.join(
                        extracted_path,
                        "stl10_binary/train_y.bin")},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "images_dir_path": os.path.join(
                        extracted_path,
                        "stl10_binary/test_X.bin"),
                    "labels_path": os.path.join(
                        extracted_path,
                        "stl10_binary/test_y.bin")},
            ),
        ]

    def _generate_examples(self, images_dir_path, labels_path):
        """Yields examples."""
        images = read_all_images(images_dir_path)
        labels = read_labels(labels_path)
        for i, (image, label) in enumerate(zip(images, labels)):
            yield i, {"image": image, "label": label}
