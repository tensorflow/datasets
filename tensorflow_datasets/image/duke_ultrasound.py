# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""DAS beamformed phantom images and paired clinical post-processed images."""

import csv
import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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
anatomical structures. These data were collected with support from the
National Institute of Biomedical Imaging and Bioengineering under Grant
R01-EB026574 and National Institutes of Health under Grant 5T32GM007171-44.
A usage example is available
[here](https://colab.research.google.com/drive/1R_ARqpWoiHcUQWg1Fxwyx-ZkLi0IZ5qs)."""

_DATA_URL = {
    'phantom_data': 'https://research.repository.duke.edu/downloads/vt150j912',
    'mark_data': 'https://research.repository.duke.edu/downloads/4x51hj56d'
}

_DEFAULT_SPLITS = {
    'train': 'https://research.repository.duke.edu/downloads/tt44pn391',
    'test': 'https://research.repository.duke.edu/downloads/zg64tm441',
    'validation': 'https://research.repository.duke.edu/downloads/dj52w535x',
    'MARK': 'https://research.repository.duke.edu/downloads/wd375w77v',
    'A': 'https://research.repository.duke.edu/downloads/nc580n18d',
    'B': 'https://research.repository.duke.edu/downloads/7h149q56p'
}


class DukeUltrasound(tfds.core.GeneratorBasedBuilder):
  """DAS beamformed phantom images and paired post-processed images."""

  VERSION = tfds.core.Version('1.0.0')

  def __init__(self, custom_csv_splits=None, **kwargs):
    """custom_csv_splits is a dictionary of { 'name': 'csvpaths'}."""
    super(DukeUltrasound, self).__init__(**kwargs)
    self.custom_csv_splits = custom_csv_splits if custom_csv_splits else {}

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
            'harmonic': tfds.features.Tensor(shape=(), dtype=tf.bool)
        }),
        supervised_keys=('das/dB', 'dtce'),
        homepage='https://github.com/ouwen/mimicknet',
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    downloads = _DEFAULT_SPLITS.copy()
    downloads.update(_DATA_URL)
    dl_paths = dl_manager.download_and_extract(downloads)
    splits = [
        tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
            name=name,
            gen_kwargs={
                'datapath': {
                    'mark_data': dl_paths['mark_data'],
                    'phantom_data': dl_paths['phantom_data']
                },
                'csvpath': dl_paths[name]
            }) for name, _ in _DEFAULT_SPLITS.items()
    ]

    for name, csv_path in self.custom_csv_splits.items():
      splits.append(
          tfds.core.SplitGenerator(
              name=name,
              gen_kwargs={
                  'datapath': dl_paths['data'],
                  'csvpath': csv_path
              }))

    return splits

  def _generate_examples(self, datapath, csvpath):
    with tf.io.gfile.GFile(csvpath) as f:
      reader = csv.DictReader(f)
      for row in reader:
        data_key = 'mark_data' if row['target'] == 'mark' else 'phantom_data'

        filepath = os.path.join(datapath[data_key], row['filename'])
        matfile = tfds.core.lazy_imports.scipy.io.loadmat(
            tf.io.gfile.GFile(filepath, 'rb'))

        iq = np.abs(np.reshape(matfile['iq'], -1))
        iq = iq / iq.max()
        iq = 20 * np.log10(iq)

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
