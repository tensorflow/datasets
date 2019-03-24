
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

LANDMARK_HEADINGS = ("lefteye_x lefteye_y righteye_x righteye_y "
                     "nose_x nose_y mouth_x mouth_y").split()
IMAGE_DATA = ("http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/Caltech_WebFaces.tar")
LANDMARK_DATA = ("http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/WebFaces_GroundThruth.txt")
class Caltech10K_WebFaces(tfds.core.GeneratorBasedBuilder):

    VERSION = tfds.core.Version("0.1.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description='',
            features=tfds.features.FeaturesDict({
                "image": 
                    tfds.features.Image(encoding_format='jpeg'),
                "landmarks": {name: tf.int64 for name in LANDMARK_HEADINGS}
            }),
            urls=['http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/'],
            citation=""
        )


    def _split_generator(self, dl_manager):
        extracted_dirs = dl_manager.download_and_extract({
            "images": IMAGE_DATA,
            "landmarks" LANDMARK_DATA
        })
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=10,
                gen_kwargs={
                    "file_id": 0,
                    "extracted_dirs": extracted_dirs,
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=4,
                gen_kwargs={
                    "file_id": 1,
                    "extracted_dirs": extracted_dirs,
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=4,
                gen_kwargs={
                    "file_id": 2,
                    "extracted_dirs": extracted_dirs,
                })
        ]


    def _process_caltech10k_config_file(self, file_path):
        with tf.io.gfile.GFile(file_path) as f:
            data_raw = f.read()
        lines = data_raw.split("\n")

        keys = [x.split()[0] for x in lines[:-1]]
        values = {}
        # Go over each line (skip the last one, as it is empty).
        for line in lines[0:-1]:
        row_values = line.strip().split()
        # Each row start with the 'file_name' and then space-separated values.
        values[row_values[0]] = [v for v in row_values[1:]]
        return keys, values

    def _generate_examples(self, extracted_dirs):
        filedir = os.path.join(extracted_dirs['images'],'images')
        landmarks_path = extracted_dirs["landmarks"]

        #with tf.io.gfile.GFile()

