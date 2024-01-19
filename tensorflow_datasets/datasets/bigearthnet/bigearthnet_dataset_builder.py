# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""BigEarthNet remote sensing dataset of Sentinel-2 image patches."""

from __future__ import annotations

import io
import json
import os

import numpy as np
import tensorflow_datasets.public_api as tfds

_LABELS = [
    'Agro-forestry areas',
    'Airports',
    'Annual crops associated with permanent crops',
    'Bare rock',
    'Beaches, dunes, sands',
    'Broad-leaved forest',
    'Burnt areas',
    'Coastal lagoons',
    'Complex cultivation patterns',
    'Coniferous forest',
    'Construction sites',
    'Continuous urban fabric',
    'Discontinuous urban fabric',
    'Dump sites',
    'Estuaries',
    'Fruit trees and berry plantations',
    'Green urban areas',
    'Industrial or commercial units',
    'Inland marshes',
    'Intertidal flats',
    'Land principally occupied by agriculture, with significant areas of '  # pylint: disable=implicit-str-concat
    'natural vegetation',
    'Mineral extraction sites',
    'Mixed forest',
    'Moors and heathland',
    'Natural grassland',
    'Non-irrigated arable land',
    'Olive groves',
    'Pastures',
    'Peatbogs',
    'Permanently irrigated land',
    'Port areas',
    'Rice fields',
    'Road and rail networks and associated land',
    'Salines',
    'Salt marshes',
    'Sclerophyllous vegetation',
    'Sea and ocean',
    'Sparsely vegetated areas',
    'Sport and leisure facilities',
    'Transitional woodland/shrub',
    'Vineyards',
    'Water bodies',
    'Water courses',
]

_DATA_OPTIONS = ['rgb', 'all']

_ZIP_FILE = 'http://bigearth.net/downloads/BigEarthNet-S2-v1.0.tar.gz'
_ZIP_SUBIDR = 'BigEarthNet-v1.0'

# To clip and rescale the RGB channels for the JPEG images visualizatoin.
# This is not the maximal value.
# Sample observed max value was about 17800, while the sample observed mean
# was about 400 with a standard deviation of about 200.
# Adhoc selection of the upper max value to be mean + 7*std.
_OPTICAL_MAX_VALUE = 2000.0


class BigearthnetConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Bigearthnet."""

  def __init__(self, selection=None, **kwargs):
    """Constructs a BigearthnetConfig.

    Args:
      selection: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if selection not in _DATA_OPTIONS:
      raise ValueError('selection must be one of %s' % _DATA_OPTIONS)

    super(BigearthnetConfig, self).__init__(
        version=tfds.core.Version('1.0.0'),
        release_notes={
            '1.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
        },
        **kwargs,
    )
    self.selection = selection


class Builder(tfds.core.BeamBasedBuilder):
  """Bigearthnet remote sensing dataset of Sentinel-2 image patches."""

  BUILDER_CONFIGS = [
      BigearthnetConfig(
          selection='rgb', name='rgb', description='Sentinel-2 RGB channels'
      ),
      BigearthnetConfig(
          selection='all', name='all', description='13 Sentinel-2 channels'
      ),
  ]

  def _info(self):
    metadata_dict = tfds.features.FeaturesDict({
        'acquisition_date': tfds.features.Text(),
        'coordinates': {
            'lrx': np.int64,
            'lry': np.int64,
            'ulx': np.int64,
            'uly': np.int64,
        },
        'projection': tfds.features.Text(),
        'tile_source': tfds.features.Text(),
    })
    if self.builder_config.selection == 'rgb':
      features = tfds.features.FeaturesDict({
          'image': tfds.features.Image(shape=[120, 120, 3]),
          'labels': tfds.features.Sequence(
              tfds.features.ClassLabel(names=_LABELS)
          ),
          'filename': tfds.features.Text(),
          'metadata': metadata_dict,
      })
      supervised_keys = ('image', 'labels')
    elif self.builder_config.selection == 'all':
      features = tfds.features.FeaturesDict({
          'B01': tfds.features.Tensor(shape=[20, 20], dtype=np.float32),
          'B02': tfds.features.Tensor(shape=[120, 120], dtype=np.float32),
          'B03': tfds.features.Tensor(shape=[120, 120], dtype=np.float32),
          'B04': tfds.features.Tensor(shape=[120, 120], dtype=np.float32),
          'B05': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'B06': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'B07': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'B08': tfds.features.Tensor(shape=[120, 120], dtype=np.float32),
          'B09': tfds.features.Tensor(shape=[20, 20], dtype=np.float32),
          'B11': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'B12': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'B8A': tfds.features.Tensor(shape=[60, 60], dtype=np.float32),
          'labels': tfds.features.Sequence(
              tfds.features.ClassLabel(names=_LABELS)
          ),
          'filename': tfds.features.Text(),
          'metadata': metadata_dict,
      })
      supervised_keys = None

    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=supervised_keys,
        homepage='http://bigearth.net',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download(_ZIP_FILE)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive_path': dl_path,
            },
        ),
    ]

  def _build_pcollection(self, pipeline, archive_path):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    selection = self.builder_config.selection

    return (
        pipeline
        | 'ArchivePath' >> beam.Create([archive_path])
        | 'ReadArchive' >> beam.FlatMap(_read_archive, selection)
        | 'Reshuffle' >> beam.transforms.Reshuffle()
        | 'ProcessExamples' >> beam.Map(_process_example, selection)
    )


def _read_archive(archive_path, selection):
  """Yields non-processed examples out of archive."""
  example = {}
  read_band_files = 0
  for fpath, fobj in tfds.core.download.extractor.iter_tar_stream(archive_path):
    read_band_files += 1
    _, patch_name, fname = fpath.split(os.path.sep)
    if fname.endswith('_labels_metadata.json'):
      example['metadata'] = fobj.read()
    elif fname.endswith('.tif'):
      band = fname[-7:-4]
      if selection != 'rgb' or (
          selection == 'rgb' and band in {'B02', 'B03', 'B04'}
      ):
        example[band] = fobj.read()
        example.setdefault('bands', []).append(band)
    else:
      raise AssertionError('Unexpected file: %s' % fpath)
    if read_band_files == 13:
      example['filename'] = patch_name
      yield example
      example = {}
      read_band_files = 0


def _process_example(example, selection):
  example = example.copy()
  example['metadata'] = json.loads(example['metadata'])
  example['labels'] = example['metadata'].pop('labels')
  for band in example.pop('bands') or []:
    example[band] = _load_tif(example[band])
  if selection == 'rgb':
    _create_rgb_image(example)
  return example['filename'], example


def _create_rgb_image(d):
  """Creates and rescales RGB image."""
  img = np.stack([d.pop('B04'), d.pop('B03'), d.pop('B02')], axis=2)
  img = img / _OPTICAL_MAX_VALUE * 255.0
  d['image'] = np.clip(img, 0, 255).astype(np.uint8)


def _load_tif(data):
  """Loads TIF file and returns as float32 numpy array."""
  img = tfds.core.lazy_imports.PIL_Image.open(io.BytesIO(data))
  img = np.array(img.getdata()).reshape(img.size).astype(np.float32)
  return img
