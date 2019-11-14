# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Carvana Image Masking Challenge"""

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """Automatically identify the boundaries of the car in an image."""

_URL = "https://www.kaggle.com/c/carvana-image-masking-challenge"

_CITATION = r"this dataset does not provide a citation."


class Carvana(tfds.core.GeneratorBasedBuilder):
    """Carvana Image Masking Challenge."""

    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                'image': tfds.features.Image(shape=(1280, 1920, 3), dtype=tf.uint8),
                'mask/rle': tfds.features.Sequence(tf.int32),
                'mask': tfds.features.Image(shape=(1, 1280, 1920, 3), dtype=tf.uint8),
                'rotation': tf.uint8,
                'metadata': {
                    'model': tf.string,
                    'make': tf.string,
                    'year': tf.string,
                    'trim1': tf.string,
                    'trim2': tf.string,
                }
            }),
            supervised_keys=("image", "mask"),
            homepage=_URL,
            citation=None
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        dl_paths = dl_manager.download_kaggle_data(
            "carvana-image-masking-challenge")

        data_dir = dl_manager.extract({
            'metadata': dl_paths['metadata.csv.zip'],
            'images_train': dl_paths['train_hq.zip'],
            'images_test': dl_paths['test.zip'],
            'masks_train': dl_paths['train_masks.zip'],
            'masks_lre_train': dl_paths['train_masks.csv.zip'],
        })

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    'images_dir': os.path.join(data_dir['images_train'], 'train_hq'),
                    'masks_dir': os.path.join(data_dir['masks_train'], 'train_masks'),
                    'metadata_file': os.path.join(data_dir['metadata'], 'metadata.csv'),
                    'masks_lre_file': os.path.join(data_dir['masks_lre_train'], 'train_masks.csv')
                }
            )
        ]

    def _read_metadata(self, metadata_file):
        metadata = tf.io.gfile.GFile(metadata_file)
        metadata = metadata.readlines()[1:]
        metadata = (m.strip().split(',') for m in metadata)
        # the [1:-1] is to crop the " at each label
        metadata = {
            id[1:-1]: {'year': year[1:-1],
                       'make': make[1:-1],
                       'model': model[1:-1],
                       'trim1': trim1[1:-1],
                       'trim2': trim2[1:-1]
                       }
            for id, year, make, model, trim1, trim2 in metadata}
        return metadata

    def _read_masks_rle(self, masks_file):
        masks = tf.io.gfile.GFile(masks_file)
        masks = masks.readlines()[1:]
        masks = [line.split(',') for line in masks]
        masks = {id: [int(p) for p in points.split(' ')]
                 for id, points in masks}
        return masks

    def _generate_examples(self, metadata_file, images_dir, masks_dir, masks_lre_file):
        metadata = self._read_metadata(metadata_file)
        masks_rle = self._read_masks_rle(masks_lre_file)

        images = tf.io.gfile.listdir(images_dir)

        for img in sorted(images):
            name, _ext = os.path.splitext(img)
            id, rotation = name.split('_')
            rotation = int(rotation) - 1
            meta = metadata[id]

            yield name, {
                'image': os.path.join(images_dir, img),
                'mask': os.path.join(masks_dir, f'{name}_mask.gif'),
                'mask/rle': masks_rle[img],
                'rotation': rotation,
                'metadata': meta,
            }
