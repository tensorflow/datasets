# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils import bool_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DATA_URL = {
    'phantom_data': 'https://research.repository.duke.edu/downloads/vt150j912',
    'mark_data': 'https://research.repository.duke.edu/downloads/4x51hj56d',
}

_DEFAULT_SPLITS = {
    'train': 'https://research.repository.duke.edu/downloads/tt44pn391',
    'test': 'https://research.repository.duke.edu/downloads/zg64tm441',
    'validation': 'https://research.repository.duke.edu/downloads/dj52w535x',
    'MARK': 'https://research.repository.duke.edu/downloads/wd375w77v',
    'A': 'https://research.repository.duke.edu/downloads/nc580n18d',
    'B': 'https://research.repository.duke.edu/downloads/7h149q56p',
}


class Builder(tfds.core.GeneratorBasedBuilder):
  """DAS beamformed phantom images and paired post-processed images."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.1': 'Fixes parsing of boolean field `harmonic`.',
      '1.0.0': 'Initial release.',
  }

  def __init__(self, custom_csv_splits=None, **kwargs):
    """custom_csv_splits is a dictionary of { 'name': 'csvpaths'}."""
    super(Builder, self).__init__(**kwargs)
    self.custom_csv_splits = custom_csv_splits if custom_csv_splits else {}

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'das': {
                'dB': tfds.features.Tensor(shape=(None,), dtype=np.float32),
                'real': tfds.features.Tensor(shape=(None,), dtype=np.float32),
                'imag': tfds.features.Tensor(shape=(None,), dtype=np.float32),
            },
            'dtce': tfds.features.Tensor(shape=(None,), dtype=np.float32),
            'f0_hz': tfds.features.Tensor(shape=(), dtype=np.float32),
            'voltage': tfds.features.Tensor(shape=(), dtype=np.float32),
            'focus_cm': tfds.features.Tensor(shape=(), dtype=np.float32),
            'height': tfds.features.Tensor(shape=(), dtype=np.uint32),
            'width': tfds.features.Tensor(shape=(), dtype=np.uint32),
            'initial_radius': tfds.features.Tensor(shape=(), dtype=np.float32),
            'final_radius': tfds.features.Tensor(shape=(), dtype=np.float32),
            'initial_angle': tfds.features.Tensor(shape=(), dtype=np.float32),
            'final_angle': tfds.features.Tensor(shape=(), dtype=np.float32),
            'probe': tfds.features.Tensor(shape=(), dtype=np.str_),
            'scanner': tfds.features.Tensor(shape=(), dtype=np.str_),
            'target': tfds.features.Tensor(shape=(), dtype=np.str_),
            'timestamp_id': tfds.features.Tensor(shape=(), dtype=np.uint32),
            'harmonic': tfds.features.Tensor(shape=(), dtype=np.bool_),
        }),
        supervised_keys=('das/dB', 'dtce'),
        homepage='https://github.com/ouwen/mimicknet',
    )

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
                    'phantom_data': dl_paths['phantom_data'],
                },
                'csvpath': dl_paths[name],
            },
        )
        for name, _ in _DEFAULT_SPLITS.items()
    ]

    for name, csv_path in self.custom_csv_splits.items():
      splits.append(
          tfds.core.SplitGenerator(
              name=name,
              gen_kwargs={'datapath': dl_paths['data'], 'csvpath': csv_path},
          )
      )

    return splits

  def _generate_examples(self, datapath, csvpath):
    with epath.Path(csvpath).open() as f:
      reader = csv.DictReader(f)
      for row in reader:
        data_key = 'mark_data' if row['target'] == 'mark' else 'phantom_data'

        filepath = os.path.join(datapath[data_key], row['filename'])
        matfile = tfds.core.lazy_imports.scipy.io.loadmat(
            tf.io.gfile.GFile(filepath, 'rb')
        )

        iq = np.abs(np.reshape(matfile['iq'], -1))
        iq = iq / iq.max()
        iq = 20 * np.log10(iq)

        yield row['filename'], {
            'das': {
                'dB': iq.astype(np.float32),
                'real': np.reshape(matfile['iq'], -1).real.astype(np.float32),
                'imag': np.reshape(matfile['iq'], -1).imag.astype(np.float32),
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
            'harmonic': bool_utils.parse_bool(row['harm']),
        }
