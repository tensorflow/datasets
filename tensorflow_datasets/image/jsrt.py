"""jsrt dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import numpy as np
import os

_CITATION = """
@MISC{Shiraishi2000-kf,
    title   = "Development of a Digital Image Database for Chest Radiographs With
                         and Without a Lung Nodule",
    author  = "Shiraishi, Junji and Katsuragawa, Shigehiko and Ikezoe, Junpei and
                         Matsumoto, Tsuneo and Kobayashi, Takeshi and Komatsu, Ken-Ichi and
                         Matsui, Mitate and Fujita, Hiroshi and Kodera, Yoshie and Doi,
                         Kunio",
    journal = "American Journal of Roentgenology",
    volume  =  174,
    number  =  1,
    pages   = "71--74",
    year    =  2000
}
"""

_DESCRIPTION = """JSRT is a high resoultion (2048x2048, 0.175mm pixel) chest 
x-ray imaging dataset with 4096 gray scale (12bit). It contains 154 images with
a nodule, and 93 non-nodule images."""

_DIFFICULTY = ['Extremely Subtle', 'Very Subtle', 'Subtle', 'Relatively Obvious', 'Obvious']

class Jsrt(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version('0.1.0')
    MANUAL_DOWNLOAD_INSTRUCTIONS = """\
        manual_dir should contain unzipped All247Images.zip and Clinical_Information.zip from the JSRT Database
    """

    @staticmethod
    def hist_match(source, template):
        oldshape = source.shape
        source = source.ravel()
        template = template.ravel()
        s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                                                                        return_counts=True)
        t_values, t_counts = np.unique(template, return_counts=True)
        s_quantiles = np.cumsum(s_counts).astype(np.float64)
        s_quantiles /= s_quantiles[-1]
        t_quantiles = np.cumsum(t_counts).astype(np.float64)
        t_quantiles /= t_quantiles[-1]
        interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)
        return interp_t_values[bin_idx].reshape(oldshape)

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                'image': tfds.features.Image(shape=(2048, 2048, 1), encoding_format='png', dtype=tf.uint16),
                'bse': tfds.features.Image(shape=(2048, 2048, 1), encoding_format='png', dtype=tf.uint16),
                'age': tfds.features.Tensor(shape=(), dtype=tf.int8),
                'sex': tfds.features.ClassLabel(names=['male', 'female', 'other']),
                'nodule': tfds.features.ClassLabel(names=['non-nodule', 'nodule']),
                'nodule_details': {
                    'difficulty': tfds.features.ClassLabel(names=_DIFFICULTY),
                    'size_mm': tfds.features.Tensor(shape=(), dtype=tf.uint8),
                    'x_coord': tfds.features.Tensor(shape=(), dtype=tf.uint16),
                    'y_coord': tfds.features.Tensor(shape=(), dtype=tf.uint16),
                    'type': tfds.features.ClassLabel(names=['benign', 'malignant']),
                    'diagnosis': tfds.features.Tensor(shape=(), dtype=tf.string)
                }
            }),
            homepage='https://www.jsrt.or.jp/data/',
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        lung_nodule_list = os.path.join(dl_manager.manual_dir, 'CLNDAT_EN.txt')
        no_nodule_list = os.path.join(dl_manager.manual_dir, 'CNNDAT_EN.txt')
        jsrt_directory = os.path.join(dl_manager.manual_dir, 'JSRT')
        bse_directory = os.path.join(dl_manager.manual_dir, 'BSE')
        if not (tf.io.gfile.exists(lung_nodule_list) or 
                        tf.io.gfile.exists(no_nodule_list) or
                        tf.io.gfile.exists(jsrt_directory) or
                        tf.io.gfile.exists(bse_directory)):
            msg = "You must download the dataset files manually and unzip them in: {}, {}, {}, and {}".format(lung_nodule_list, no_nodule_list, jsrt_directory, bse_directory)
            raise AssertionError(msg)

        with tf.io.gfile.GFile(no_nodule_list, "r") as f:
            lines = f.read().split('\r')
        nn = []
        for line in lines:
            line = line.split(' ')
            line = list(filter(lambda x: x is not '', line))
            nn.append(line)
        nn = nn[:-1]

        with tf.io.gfile.GFile(lung_nodule_list, "r") as f:
            lines = f.read().split('\r')
        ln = [line.split('\t') for line in lines]
        ln = ln[:-2]
        return [
            tfds.core.SplitGenerator(
                    name=tfds.Split.TRAIN,
                    gen_kwargs={
                        "lung_nodule_list": ln,
                        "no_nodule_list": nn,
                        "jsrt_directory": jsrt_directory,
                        "bse_directory": bse_directory
                    }
            )
        ]

    def _generate_examples(self, lung_nodule_list=None, no_nodule_list=None, jsrt_directory=None, bse_directory=None):
        """Yields examples."""
        def get_images(filename):
            image = tf.io.decode_raw(tf.io.read_file('{}/{}.IMG'.format(jsrt_directory, filename)), tf.uint16, little_endian=False)
            image = tf.reshape(image, (2048, 2048, 1))
            bse = tf.io.decode_png(tf.io.read_file('{}/{}.png'.format(bse_directory, filename)), channels=1, dtype=tf.uint16)
            bse = self.hist_match(bse.numpy(), image.numpy()).astype(np.uint16)
            return image.numpy(), bse

        for line in no_nodule_list:
            filename = line[0][:-4]
            image, bse = get_images(filename)
            yield filename, {
                'image': image,
                'bse': bse,
                'age': int(line[1]),
                'sex': line[2],
                'nodule': 'non-nodule',
                'nodule_details': {
                    'difficulty': _DIFFICULTY[0],
                    'size_mm': 0,
                    'x_coord': 0,
                    'y_coord': 0,
                    'type': 'benign',
                    'diagnosis': ""
                }
            }

        for line in lung_nodule_list:
            filename = line[0][:-4]
            image, bse = get_images(filename)
            try:
                age = int(line[3])
            except Exception:
                age = -1

            yield filename, {
                'image': image,
                'bse': bse,
                'age': age,
                'sex': line[4],
                'nodule': 'nodule',
                'nodule_details': {
                    'difficulty': _DIFFICULTY[int(line[1])-1],
                    'size_mm': int(line[2]),
                    'x_coord': int(line[5]),
                    'y_coord': int(line[6]),
                    'type': line[7],
                    'diagnosis': " ".join(line[8:]),
                }
            }
