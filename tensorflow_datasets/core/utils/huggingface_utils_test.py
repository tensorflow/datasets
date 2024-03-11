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
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def test_convert_to_np_dtype_raises():
  with pytest.raises(TypeError, match='Unrecognized type.+'):
    huggingface_utils.convert_to_np_dtype('I am no dtype')


@pytest.mark.parametrize(
    'hf_dtype,np_dtype',
    [
        # from mapping
        ('bool', np.bool_),
        ('float', np.float32),
        ('double', np.float64),
        ('large_string', np.object_),
        ('utf8', np.object_),
        ('string', np.object_),
        # from np
        ('bool_', np.bool_),
        ('int32', np.int32),
        ('int64', np.int64),
        # from timestamp
        ('timestamp[s, tz=UTC]', np.int64),
        # from tf
        ('bfloat16', tf.bfloat16),
    ],
)
def test_convert_to_np_dtype(hf_dtype, np_dtype):
  assert huggingface_utils.convert_to_np_dtype(hf_dtype) is np_dtype


@pytest.mark.parametrize(
    'feature,default_value',
    [
        (feature_lib.Scalar(dtype=np.int32), -2147483648),
        (feature_lib.Scalar(dtype=np.float32), -3.4028234663852886e38),
        (feature_lib.Sequence(np.int32), []),
        (
            feature_lib.FeaturesDict({
                'foo': feature_lib.Scalar(dtype=np.str_),
            }),
            {'foo': b''},
        ),
    ],
)
def test_get_default_value(feature, default_value):
  assert huggingface_utils._get_default_value(feature) == default_value


@pytest.mark.parametrize(
    'hf_value,feature',
    [
        ({'array': None}, feature_lib.Audio()),
        ({'path': None}, feature_lib.Audio()),
    ],
)
def test_convert_value_raises(hf_value, feature):
  with pytest.raises(
      TypeError, match='Conversion of value.+ is not supported.'
  ):
    huggingface_utils.convert_hf_value(hf_value, feature)


@pytest.mark.parametrize(
    'hf_value,feature,expected_value',
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
    ],
)
def test_convert_value(hf_value, feature, expected_value):
  assert huggingface_utils.convert_hf_value(hf_value, feature) == expected_value


@pytest.mark.parametrize(
    'hf_dataset_name,tfds_dataset_name',
    [
        ('x', 'x'),
        ('X', 'x'),
        ('x-y', 'x_y'),
        ('x/y', 'x__y'),
        ('x_v1.0', 'x_v1_0'),
    ],
)
def test_from_hf_to_tfds(hf_dataset_name, tfds_dataset_name):
  assert (
      huggingface_utils.convert_hf_dataset_name(hf_dataset_name)
      == tfds_dataset_name
  )


@pytest.mark.parametrize(
    'hf_config_name,tfds_config_name',
    [(None, None), ('x', 'x'), ('X', 'x'), ('X,y', 'x_y')],
)
def test_convert_config_name(hf_config_name, tfds_config_name):
  assert (
      huggingface_utils.convert_hf_config_name(hf_config_name)
      == tfds_config_name
  )
