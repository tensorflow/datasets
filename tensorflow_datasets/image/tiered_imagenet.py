
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

import io
import os
import csv
import numpy as np
import gzip
import pickle


class TieredImagenet(tfds.core.GeneratorBasedBuilder):
    """tiered_imagenet is larger subset  of Imagenet that uses splits defined for benchmarking few-shot learning approaches"""
    VERSION = tfds.core.Version("1.0.2")

    _CITATION = """\
        @inproceedings{ren18fewshotssl,
        author   = {Mengye Ren and 
                    Eleni Triantafillou and 
                    Sachin Ravi and 
                    Jake Snell and 
                    Kevin Swersky and 
                    Joshua B. Tenenbaum and 
                    Hugo Larochelle and 
                    Richard S. Zemel},
        title    = {Meta-Learning for Semi-Supervised Few-Shot Classification},
        booktitle= {Proceedings of 6th International Conference on Learning Representations {ICLR}},
        year     = {2018},
        }
    """
    _DESCRIPTION = """\
        tieredImageNet is dataset proposed  for few-shot classification. Like miniImagenet, it is a
        subset of ILSVRC-12, but larger subset with total 608 classes. It is analogous to Omniglot, in 
        which characters are grouped into alphabets, tieredImageNet groups classes into broader categories
        corresponding to higher-level nodes in the ImageNet (Deng et al., 2009) hierarchy. 
        There are 34 categories in total, with each category containing between 10 and 30 classes.
         These are split into 20 training, 6 validation and 8
        testing categories 
    """

    _BASE_URL = "https://github.com/renmengye/few-shot-ssl-public.git"
    _DL_URL = "https://www.dropbox.com/s/2cezsh9wcwx4o4w/MiniImagenet.zip?dl=1"
    _IMAGE_SIZE_X = 84
    _IMAGE_SIZE_Y = 84
    _NUM_CLASSES = 34
    _NUM_CLASSES_TRAIN = 20
    _NUM_CLASSES_VALIDATION = 6
    _NUM_CLASSES_TEST = 8

    _IMAGE_SHAPE = (
        _IMAGE_SIZE_X, _IMAGE_SIZE_Y, 3)

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=self._DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.ClassLabel(num_classes=self._NUM_CLASSES),
            }),
            supervised_keys=("image", "label"),
            urls=[self._BASE_URL],
            citation=self._CITATION,
        )

    def _split_generators(self, dl_manager):
        """Downloads the data and defines the split."""
        extracted_path = dl_manager.download_and_extract(self._DL_URL)
#        extracted_path = "D:/phd/experiments/all_datasets/tiered-imagenet/"
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs={
                    "images": os.path.join(extracted_path,
                                           "train_images_png.pkl"),
                    "labels": os.path.join(extracted_path,
                                           "train_labels.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=1,
                gen_kwargs={
                    "images": os.path.join(extracted_path,
                                           "val_images_png.pkl"),
                    "labels": os.path.join(extracted_path,
                                           "val_labels.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=1,
                gen_kwargs={
                    "images": os.path.join(extracted_path,
                                           "test_images_png.pkl"),
                    "labels": os.path.join(extracted_path,
                                           "test_labels.pkl"),
                }
            ),
        ]

    def _generate_examples(self, images, labels):
        """yields examples from the dataset.
        Args:
            images: path to extracted images.
            labels: path to extracted labels.
        Yields:
            dict_data (dict): data dictionary of image and label.
                keys:
                    "image_data" (np.ndarray, shape=[num_data, 84, 84, 3],
                                  dtype=np.uint8)
                    "class_dict" (dict): class name to list of image indices.
                        value: (list of int, len=600)
        """

        # read data
        with tf.gfile.GFile(images, "rb") as f:
            img_data = pickle.load(f,encoding="latin1")
        with tf.gfile.GFile(labels, "rb") as f:
            label_data = pickle.load(f)
            
        for (class_name) in enumerate(label_data.items()):
                img = img_data[0]

                dict_data = {
                    "image": img,
                    "label": idx_class_split
                }

                yield dict_data
