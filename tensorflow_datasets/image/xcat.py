"""xcat dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import csv
import os

# TODO(xcat): BibTeX citation
_CITATION = """
"""

# TODO(xcat):
_DESCRIPTION = """
"""


class Xcat(tfds.core.GeneratorBasedBuilder):
  """TODO(xcat): Short description of my dataset."""

  VERSION = tfds.core.Version('0.1.0')
  MANUAL_DOWNLOAD_INSTRUCTIONS = "Internal Gradient Dataset"
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'xray': tfds.features.Image(shape=(2048,2048,1), dtype=tf.uint16, encoding_format='png'),
            'bse': tfds.features.Image(shape=(2048,2048,1), dtype=tf.uint16, encoding_format='png')
        }),
        supervised_keys=('xray', 'bse'),
        homepage='https://dataset-homepage/',
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'manual_dir': dl_manager.manual_dir,
                'file': 'train_body_c7.csv',
                'data_dir': 'projections_body_c7'
            }
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'manual_dir': dl_manager.manual_dir,
                'file': 'test_body_c7.csv',
                'data_dir': 'projections_body_c7'
            }
        )
    ]

  def _generate_examples(self, manual_dir=None, file=None, data_dir=None):
    with tf.io.gfile.GFile(os.path.join(manual_dir, file)) as f:
        reader = csv.DictReader(f)
        for row in reader:           
            bse_file = row['filename']
            xray_file = row['filename'].split('.')
            xray_file[2] = 'bone'
            xray_file = ".".join(xray_file)
            
            key = row['filename'].split('.')[0]
            
            bse_data = tf.io.read_file(os.path.join(manual_dir, data_dir, bse_file))
            xray_data = tf.io.read_file(os.path.join(manual_dir, data_dir, xray_file))
            bse = tf.reshape((tf.io.decode_raw(bse_data, tf.float32)), (2048,2048,1))
            xray = tf.reshape((tf.io.decode_raw(xray_data, tf.float32)), (2048,2048,1))
            
            bse = (bse - tf.reduce_min(bse))/(tf.reduce_max(bse)-tf.reduce_min(bse))
            xray = (xray - tf.reduce_min(xray))/(tf.reduce_max(xray)-tf.reduce_min(xray))
            
            bse = tf.cast(tf.round(bse*65534), tf.uint16)
            xray = tf.cast(tf.round(xray*65534), tf.uint16)
            
            yield key, {
                'xray': xray.numpy(),
                'bse': bse.numpy()
            }
