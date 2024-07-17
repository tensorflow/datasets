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

import datetime

import numpy as np
import pytest
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


@pytest.mark.parametrize(
    'name,tfds_name',
    [
        # Dataset names
        ('x', 'x'),
        ('X', 'x'),
        ('x-y', 'x_y'),
        ('x/y', 'x__y'),
        ('x/Y-z', 'x__y_z'),
        # Config and split names
        ('x.y', 'x_y'),
        ('x_v1.0', 'x_v1_0'),
    ],
)
def test_to_tfds_name(name, tfds_name):
  assert conversion_utils.to_tfds_name(name) == tfds_name


@pytest.mark.parametrize(
    'feature,default_value',
    [
        (feature_lib.Scalar(dtype=np.int32), -2147483648),
        (feature_lib.Scalar(dtype=np.float32), -3.4028234663852886e38),
        (
            feature_lib.Sequence({'name': feature_lib.Scalar(dtype=np.int32)}),
            {'name': []},
        ),
        (feature_lib.Sequence(np.int32), []),
        (
            feature_lib.FeaturesDict({
                'foo': feature_lib.Scalar(dtype=np.str_),
            }),
            {'foo': b''},
        ),
        (feature_lib.Image(), conversion_utils._DEFAULT_IMG),
    ],
)
def test_get_default_value(feature, default_value):
  assert conversion_utils._get_default_value(feature) == default_value


@pytest.mark.parametrize(
    'value,feature',
    [
        ({'array': None}, feature_lib.Audio()),
        ({'path': None}, feature_lib.Audio()),
    ],
)
def test_convert_value_raises(value, feature):
  with pytest.raises(
      TypeError, match='Conversion of value.+ is not supported.'
  ):
    conversion_utils.to_tfds_value(value, feature)


@pytest.mark.parametrize(
    'value,feature,expected_value',
    [
        # datetime
        (
            datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc),
            feature_lib.Scalar(dtype=np.int64),
            0,
        ),
        (
            datetime.datetime(1970, 1, 2, tzinfo=datetime.timezone.utc),
            feature_lib.Scalar(dtype=np.int64),
            86400,
        ),
        # scalar
        (42, feature_lib.Scalar(dtype=np.int64), 42),
        (42, feature_lib.Scalar(dtype=np.int32), 42),
        ('abc', feature_lib.Scalar(dtype=np.object_), 'abc'),
        (True, feature_lib.Scalar(dtype=np.bool_), True),
        (False, feature_lib.Scalar(dtype=np.bool_), False),
        (42.0, feature_lib.Scalar(dtype=np.float32), 42.0),
        # sequence
        ([42], feature_lib.Sequence(feature=tf.int64), [42]),
        (42, feature_lib.Sequence(feature=tf.int64), [42]),
        (None, feature_lib.Sequence(feature=tf.int64), []),
        ([None, 'abc'], feature_lib.Sequence(feature=np.str_), [b'', 'abc']),
        (
            {'someint': [None, 'string', None]},
            feature_lib.Sequence(
                {'someint': feature_lib.Scalar(dtype=np.str_)}
            ),
            {'someint': [b'', 'string', b'']},
        ),
        # image
        (
            lazy_imports_lib.lazy_imports.PIL_Image.new(mode='L', size=(4, 4)),
            feature_lib.Image(),
            lazy_imports_lib.lazy_imports.PIL_Image.new(
                mode='RGB', size=(4, 4)
            ),
        ),
        # dict
        (
            {
                'de': b'Hallo Welt',
                'en': b'Hello world',
                'fr': None,  # Hugging Face supports `None` values
            },
            feature_lib.Translation(languages=['en', 'fr', 'de']),
            {
                'de': b'Hallo Welt',
                'en': b'Hello world',
                'fr': b'',
            },
        ),
        (
            {},
            feature_lib.FeaturesDict(
                {'foo': feature_lib.Scalar(dtype=np.str_)}
            ),
            {'foo': b''},
        ),
        # nan, but the feature type is not float
        (
            np.nan,
            feature_lib.Text(),
            b'',
        ),
    ],
)
def test_to_tfds_value(value, feature, expected_value):
  assert conversion_utils.to_tfds_value(value, feature) == expected_value
