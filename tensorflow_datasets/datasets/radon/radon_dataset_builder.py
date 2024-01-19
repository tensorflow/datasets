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

"""Radon dataset."""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function

import collections
import urllib

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

BASE_URL = 'http://www.stat.columbia.edu/~gelman/arm/examples/radon/'


def convert_to_int(d):
  return np.int32(d)


def convert_to_float(d):
  return np.float32(d)


def return_same(d):
  return d


def features():
  return collections.OrderedDict([
      ('idnum', (tf.int32, convert_to_int)),
      ('state', (tf.string, return_same)),
      ('state2', (tf.string, return_same)),
      ('stfips', (tf.int32, convert_to_int)),
      ('zip', (tf.int32, convert_to_int)),
      ('region', (tf.int32, convert_to_int)),
      ('typebldg', (tf.int32, convert_to_int)),
      ('floor', (tf.int32, convert_to_int)),
      ('room', (tf.int32, convert_to_int)),
      ('basement', (tf.string, return_same)),
      ('windoor', (tf.string, return_same)),
      ('rep', (tf.int32, convert_to_int)),
      ('stratum', (tf.int32, convert_to_int)),
      ('wave', (tf.int32, convert_to_int)),
      ('starttm', (tf.int32, convert_to_int)),
      ('stoptm', (tf.int32, convert_to_int)),
      ('startdt', (tf.int32, convert_to_int)),
      ('stopdt', (tf.int32, convert_to_int)),
      ('pcterr', (tf.float32, convert_to_float)),
      ('adjwt', (tf.float32, convert_to_float)),
      ('dupflag', (tf.int32, convert_to_int)),
      ('zipflag', (tf.int32, convert_to_int)),
      ('cntyfips', (tf.int32, convert_to_int)),
      ('county', (tf.string, return_same)),
      ('Uppm', (tf.float32, convert_to_float)),
      ('lon', (tf.float32, convert_to_float)),
      ('lat', (tf.float32, convert_to_float)),
  ])


class Builder(tfds.core.GeneratorBasedBuilder):
  """Radon dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'activity': np.float32,
            'features': {
                name: dtype for name, (dtype, _) in features().items()
            },
        }),
        supervised_keys=('features', 'activity'),
        homepage='http://www.stat.columbia.edu/~gelman/arm/examples/radon/',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    paths = dl_manager.download({
        'file_path_srrs2': urllib.parse.urljoin(BASE_URL, 'srrs2.dat'),
        'file_path_cty': urllib.parse.urljoin(BASE_URL, 'cty.dat'),
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=paths,
        ),
    ]

  def _generate_examples(self, file_path_srrs2, file_path_cty):
    """Yields examples."""
    pd = tfds.core.lazy_imports.pandas

    with epath.Path(file_path_srrs2).open() as f:
      df_srrs2 = pd.read_csv(f)
    with epath.Path(file_path_cty).open() as f:
      df_cty = pd.read_csv(f)

    df_srrs2.rename(columns=str.strip, inplace=True)
    df_cty.rename(columns=str.strip, inplace=True)

    # We will now join datasets on Federal Information Processing Standards
    # (FIPS) id, ie, codes that link geographic units, counties and county
    # equivalents. http://jeffgill.org/Teaching/rpqm_9.pdf
    df_srrs2['fips'] = 1000 * df_srrs2.stfips + df_srrs2.cntyfips
    df_cty['fips'] = 1000 * df_cty.stfips + df_cty.ctfips

    df = df_srrs2.merge(df_cty[['fips', 'Uppm', 'lon', 'lat']], on='fips')
    df = df.drop_duplicates(subset='idnum')
    df.drop('fips', axis=1, inplace=True)

    df['wave'].replace({'  .': '-1'}, inplace=True)
    df['rep'].replace({' .': '-1'}, inplace=True)
    df['zip'].replace({'     ': '-1'}, inplace=True)

    for i, (_, row) in enumerate(df.iterrows()):
      radon_val = row.pop('activity')
      yield i, {
          'activity': float(radon_val),
          'features': {
              name: features()[name][1](value) for name, value in row.items()
          },
      }
