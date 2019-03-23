
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

LANDMARK_HEADINGS = ("lefteye_x lefteye_y righteye_x righteye_y "
                     "nose_x nose_y mouth_x mouth_y").split()

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

            })
        )