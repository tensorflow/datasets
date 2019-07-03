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

"""Eurosat remote sensing benchmarking dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{helber2017eurosat,
    title={EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification},
    author={Patrick Helber and Benjamin Bischke and Andreas Dengel and Damian Borth},
    year={2017},
    eprint={1709.00029},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
"""

_DESCRIPTION = """\
EuroSAT dataset is based on Sentinel-2 satellite images covering 13 spectral
bands and consisting of 10 classes with 27000 labeled and
geo-referenced samples.

Two datasets are offered:
- rgb: Contains only the optical R, G, B frequency bands encoded as JPEG image.
- all: Contains all 13 bands in the original value range (float32).

URL: https://github.com/phelber/eurosat
"""

_LABELS = [
    'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
    'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'
]

_URL = 'https://github.com/phelber/eurosat'

_DATA_OPTIONS = ['rgb', 'all']


class EurosatConfig(tfds.core.BuilderConfig):
  """BuilderConfig for eurosat."""

  def __init__(self, selection=None, download_url=None, subdir=None, **kwargs):
    """Constructs a EurosatConfig.

    Args:
      selection: `str`, one of `_DATA_OPTIONS`.
      download_url: `str`, download URL to the zip file.
      subdir: `str`, subdir within the zip file.
      **kwargs: keyword arguments forwarded to super.
    """
    if selection not in _DATA_OPTIONS:
      raise ValueError('selection must be one of %s' % _DATA_OPTIONS)

    kwargs['supported_versions'] = [
        tfds.core.Version('1.0.0', experiments={tfds.core.Experiment.S3: True}),
    ]
    super(EurosatConfig, self).__init__(**kwargs)
    self.selection = selection
    self.download_url = download_url
    self.subdir = subdir


class Eurosat(tfds.core.GeneratorBasedBuilder):
  """Eurosat remote sensing benchmarking dataset."""

  BUILDER_CONFIGS = [
      EurosatConfig(
          selection='rgb',
          name='rgb',
          download_url='http://madm.dfki.de/files/sentinel/EuroSAT.zip',
          subdir='2750',
          version='0.0.1',
          description='Sentinel-2 RGB channels'),
      EurosatConfig(
          selection='all',
          name='all',
          download_url='http://madm.dfki.de/files/sentinel/EuroSATallBands.zip',
          subdir='ds/images/remote_sensing/otherDatasets/sentinel_2/tif',
          version='0.0.1',
          description='13 Sentinel-2 channels'),
  ]

  def _info(self):
    if self.builder_config.selection == 'rgb':
      features = tfds.features.FeaturesDict({
          'image': tfds.features.Image(shape=[64, 64, 3]),
          'label': tfds.features.ClassLabel(names=_LABELS),
          'filename': tfds.features.Text(),
      })
      supervised_keys = ('image', 'label')
    elif self.builder_config.selection == 'all':
      features = tfds.features.FeaturesDict({
          'sentinel2':
              tfds.features.Tensor(shape=[64, 64, 13], dtype=tf.float32),
          'label':
              tfds.features.ClassLabel(names=_LABELS),
          'filename':
              tfds.features.Text(),
      })
      supervised_keys = ('sentinel2', 'label')

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        supervised_keys=supervised_keys,
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(self.builder_config.download_url)
    path = os.path.join(path, self.builder_config.subdir)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
                'path': path,
                'selection': self.builder_config.selection
            },
        ),
    ]

  def _generate_examples(self, path, selection):
    """Yields examples."""
    for filename in tf.io.gfile.glob(os.path.join(path, '*', '*')):
      label = filename.split('/')[-1].split('_')[0]
      if selection == 'rgb':
        record = {
            'image': filename,
            'label': label,
            'filename': os.path.basename(filename)
        }
      else:
        record = {
            'sentinel2': _extract_channels(filename),
            'label': label,
            'filename': os.path.basename(filename)
        }
      if self.version.implements(tfds.core.Experiment.S3):
        yield filename, record
      else:
        yield record


def _extract_channels(filename):
  arr = tfds.core.lazy_imports.skimage.external.tifffile.imread(filename)
  arr = arr.astype('float32')
  return arr
