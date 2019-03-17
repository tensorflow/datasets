"""TensorFlow dataset for Binary Alphadigits"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://cs.nyu.edu/~roweis/data/binaryalphadigs.mat"

_DESCRIPTION = ("Binary 20x16 digits of '0' through '9' and capital 'A' " 
                "through 'Z'. 39 examples of each class.")

_IMAGE_SHAPE = (20, 16, 1)

_NAMES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
          'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

_CITATION = """\

"""

class BinaryAlphaDigits(tfds.core.GeneratorBasedBuilder):
    """Binary alphadigits dataset"""

    VERSION = tfds.core.Version('1.0.0')


    def _info(self):
        """Define the Dataset info"""

        return tfds.core.DatasetInfo(
            builder=self,
    
            description=(_DESCRIPTION),
            
            features=tfds.features.FeaturesDict({
                "image":tfds.features.Image(shape=_IMAGE_SHAPE),
                "label": tfds.features.ClassLabel(names=_NAMES),
            }),

            supervised_keys=("image", "label"),
            
            urls=[_URL],
            
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        """Define Splits for training data"""

        path = dl_manager.download(_URL)
        return [
            tfds.core.SplitGenerator(
                name="train",
                num_shards=10,
                gen_kwargs={
                    "data_dir_path": path,
                },
            )
    
    ]

    def _generate_examples(self, data_dir_path):
        """Generate Splits for training data"""

        with tf.io.gfile.GFile(data_dir_path, "rb") as f:
            mat = tfds.core.lazy_imports.scipy_io.loadmat(tf.compat.as_str(f))
        #mat = tfds.core.lazy_imports.scipy_io.loadmat(data_dir_path)
        for i in range(len(mat['dat'])):
            label = mat['classlabels'][0][i].item()
            for j in range(len(mat['dat'][i])):
                image = mat['dat'][i][j].reshape(20, 16, 1)
                yield {
                    "label": label,
                    "image": image
                    }
