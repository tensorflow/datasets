
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

import io
import os
import numpy as np
import pickle as pkl
from tqdm import tqdm
import cv2


class TieredImagenet(tfds.core.GeneratorBasedBuilder):
    """tiered_imagenet is comparatively larger subset of Imagenet that uses splits defined for benchmarking few-shot learning approaches"""
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
            The tieredImageNet is a dataset proposed specifically for few-shot classification. 
            Like miniImagenet, it is subset of ILSVRC-12, but larger subset with total 608 classes. 
            The dataset is proposed to make use of class hierarchy while few-shots classficicatio.
            It is analogous to Omniglot dataset where the characters are grouped into alphabets.
            tieredImageNet groups classes into broader categories that corresponds to higher-level nodes 
            in the ImageNet hierarchy.
            tieredImageNet has total 34 general categories. Each category containing between 10 and 30 
            classes. The categories are split into 20 training, 6 validation and 8 testing categories.
            Each category has corresponding more specific classes.
        """

    _BASE_URL = "https://github.com/renmengye/few-shot-ssl-public.git"
    _DL_URL = "https://drive.google.com/uc?export=download&id=1hqVbS2nhHXa51R9_aB6QDXeC0P2LQG_u"

    VERSION = tfds.core.Version("1.0.2")

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
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=5,
                gen_kwargs={
                    "images": os.path.join(extracted_path,
                                           "val_images_png.pkl"),
                    "labels": os.path.join(extracted_path,
                                           "val_labels.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=5,
                gen_kwargs={
                    "images": os.path.join(extracted_path,
                                           "train_images_png.pkl"),
                    "labels": os.path.join(extracted_path,
                                           "train_labels.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=5,
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
                keys:
                    "image" (np.ndarray, shape=[84, 84, 3],
                                  dtype=np.uint8)
                    "label" (string): class name.
        """
        # read data
        logging.info("Images path %s", images)
        logging.info("Labels path %s", labels)
        with open(labels, "rb") as f:
            data = pkl.load(f, encoding='latin1')
            list_label_specific = data["label_specific"]
        with tf.gfile.GFile(images, "rb") as f:
            array = pkl.load(f, encoding="latin1")
            img_data = np.zeros(
                [list_label_specific.shape[0], 84, 84, 3], dtype=np.uint8)
            for ii, item in tqdm(enumerate(array[:10])):
                im = cv2.imdecode(item, 1)
                img_data[ii] = im
        for i in range(0, list_label_specific.shape[0]):
            dict_data = {
                "image": img_data[i],
                "label": list_label_specific[i]
            }
        yield dict_data
