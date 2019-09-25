"""DAS beamformed phantom images and paired clinical post-processed images."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import numpy as np
import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import scipy.io as sio


_CITATION = """\
@article{DBLP:journals/corr/abs-1908-05782,
  author    = {Ouwen Huang and
               Will Long and
               Nick Bottenus and
               Gregg E. Trahey and
               Sina Farsiu and
               Mark L. Palmeri},
  title     = {MimickNet, Matching Clinical Post-Processing Under Realistic Black-Box
               Constraints},
  journal   = {CoRR},
  volume    = {abs/1908.05782},
  year      = {2019},
  url       = {http://arxiv.org/abs/1908.05782},
  archivePrefix = {arXiv},
  eprint    = {1908.05782},
  timestamp = {Mon, 19 Aug 2019 13:21:03 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1908-05782},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}"""

_DESCRIPTION = """\
DukeUltrasound is an ultrasound dataset collected at Duke University with a 
Verasonics c52v probe. It contains delay-and-sum (DAS) beamformed data 
as well as data post-processed with Siemens Dynamic TCE for speckle 
reduction, contrast enhancement and improvement in conspicuity of 
anatomical structures."""

_URLS = ['https://arxiv.org/abs/1908.05782', 'https://github.com/ouwen/mimicknet']


class DukeUltrasound(tfds.core.GeneratorBasedBuilder):
  """DAS beamformed phantom images and paired post-processed images."""

  VERSION = tfds.core.Version("1.0.0",
                              experiments={tfds.core.Experiment.S3: False})
  SUPPORTED_VERSIONS = [
      tfds.core.Version("3.0.0", "S3: www.tensorflow.org/datasets/splits"),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'das': {
                'dB': tfds.features.Tensor(shape=(None,), dtype=tf.float32),
                'real': tfds.features.Tensor(shape=(None,), dtype=tf.float32),
                'imag': tfds.features.Tensor(shape=(None,), dtype=tf.float32)
            },
            'dtce': tfds.features.Tensor(shape=(None,), dtype=tf.float32),
            'f0_hz': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'voltage': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'focus_cm': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'height': tfds.features.Tensor(shape=(), dtype=tf.uint32),
            'width': tfds.features.Tensor(shape=(), dtype=tf.uint32),
            'initial_radius': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'final_radius': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'initial_angle': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'final_angle': tfds.features.Tensor(shape=(), dtype=tf.float32),
            'probe': tfds.features.Tensor(shape=(), dtype=tf.string),
            'scanner': tfds.features.Tensor(shape=(), dtype=tf.string),
            'target': tfds.features.Tensor(shape=(), dtype=tf.string),
            'timestamp_id': tfds.features.Tensor(shape=(), dtype=tf.uint32),
            'harmonic': tfds.features.Tensor(shape=(), dtype=tf.bool),
        }),
        supervised_keys=('das/dB', 'dtce'),
        urls=_URLS,
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    dl_paths = dl_manager.download_and_extract({
        'data': 'https://storage.googleapis.com/duke-tfds/ultraduke/ultraphantom.tar.gz',
        'train': 'https://storage.googleapis.com/duke-tfds/ultraduke/training-v2-verasonics-phantom.csv',
        'test': 'https://storage.googleapis.com/duke-tfds/ultraduke/testing-phantom-v2.csv',
        'validation': 'https://storage.googleapis.com/duke-tfds/ultraduke/validation-phantom-v2.csv',
        'invivo': 'https://storage.googleapis.com/duke-tfds/ultraduke/mark.csv'
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'datapath': dl_paths['data'],
                'csvpath': dl_paths['train']
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'datapath': dl_paths['data'],
                'csvpath': dl_paths['validation']
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'datapath': dl_paths['data'],
                'csvpath': dl_paths['test']
            },
        ),
        tfds.core.SplitGenerator(
            name='invivo',
            gen_kwargs={
                'datapath': dl_paths['data'],
                'csvpath': dl_paths['invivo']
            },
        )
    ]

  def _generate_examples(self, datapath, csvpath):
    reader = csv.DictReader(tf.io.gfile.GFile(csvpath))
    for row in reader:
      filepath = os.path.join(datapath, 'ultraphantom', row['filename'])
      matfile = sio.loadmat(tf.io.gfile.GFile(filepath, 'rb'))

      iq = np.abs(np.reshape(matfile['iq'], -1))
      iq = iq/iq.max()
      iq = 20*np.log10(iq)

      yield row['filename'], {
          'das': {
              'dB': iq.astype(np.float32),
              'real': np.reshape(matfile['iq'], -1).real.astype(np.float32),
              'imag': np.reshape(matfile['iq'], -1).imag.astype(np.float32)
          },
          'dtce': np.reshape(matfile['dtce'], -1).astype(np.float32),
          'f0_hz': row['f0'],
          'voltage': row['v'],
          'focus_cm': row['focus_cm'],
          'height': row['axial_samples'],
          'width': row['lateral_samples'],
          'initial_radius': row['initial_radius'],
          'final_radius': row['final_radius'],
          'initial_angle': row['initial_angle'],
          'final_angle': row['final_angle'],
          'probe': row['probe'],
          'scanner': row['scanner'],
          'target': row['target'],
          'timestamp_id': row['timestamp_id'],
          'harmonic': row['harm']
      }
