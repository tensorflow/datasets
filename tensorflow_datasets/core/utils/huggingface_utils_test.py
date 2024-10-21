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

import datasets as hf_datasets
import huggingface_hub
import numpy as np
import pytest
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def test_convert_to_np_dtype_raises():
  with pytest.raises(TypeError, match='Unrecognized type.+'):
    huggingface_utils._convert_to_np_dtype('I am no dtype')


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
        ('binary', np.bytes_),
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
  assert huggingface_utils._convert_to_np_dtype(hf_dtype) is np_dtype


def test_convert_hf_features_raises_type_error():
  with pytest.raises(TypeError, match='Type <.+> is not supported.'):
    huggingface_utils.convert_hf_features('I am no features')


def test_convert_hf_features_raises_value_error():
  with pytest.raises(
      ValueError, match=r'List \[.+\] should have a length of 1.'
  ):
    huggingface_utils.convert_hf_features(
        [hf_datasets.Value('int32'), hf_datasets.Value('int32')]
    )


@pytest.mark.parametrize(
    'hf_features,tfds_features',
    [
        (
            hf_datasets.Features(
                id=hf_datasets.Value('string'),
                meta={
                    'left_context': hf_datasets.Value('string'),
                    'partial_evidence': [{
                        'start_id': hf_datasets.Value('int32'),
                        'meta': {
                            'evidence_span': [hf_datasets.Value('string')]
                        },
                    }],
                },
            ),
            feature_lib.FeaturesDict({
                'id': feature_lib.Scalar(dtype=np.str_),
                'meta': feature_lib.FeaturesDict({
                    'left_context': feature_lib.Scalar(dtype=np.str_),
                    'partial_evidence': feature_lib.Sequence({
                        'meta': feature_lib.FeaturesDict({
                            'evidence_span': feature_lib.Sequence(
                                feature_lib.Scalar(dtype=np.str_)
                            ),
                        }),
                        'start_id': feature_lib.Scalar(dtype=np.int32),
                    }),
                }),
            }),
        ),
        (
            hf_datasets.Audio(sampling_rate=48000),
            feature_lib.Audio(sample_rate=48000, dtype=np.int32),
        ),
    ],
)
def test_convert_hf_features(hf_features, tfds_features):
  assert repr(huggingface_utils.convert_hf_features(hf_features)) == repr(
      tfds_features
  )


@pytest.fixture(name='mock_list_datasets')
def _list_datasets(monkeypatch):
  def mock_list_datasets():
    return ['mnist', 'bigscience/P3', 'x', 'x/Y-z', 'fashion_mnist']

  monkeypatch.setattr(huggingface_hub, 'list_datasets', mock_list_datasets)


def test_to_huggingface_name_raises(mock_list_datasets):
  del mock_list_datasets
  with pytest.raises(
      registered.DatasetNotFoundError,
      match='"z" is not listed in Huggingface datasets.',
  ):
    assert huggingface_utils.to_huggingface_name('z')


@pytest.mark.parametrize(
    'tfds_dataset_name,hf_dataset_name',
    [
        ('x', 'x'),
        ('X', 'x'),
        ('bigscience__p3', 'bigscience/P3'),
        ('fashion_mnist', 'fashion_mnist'),
        ('x__y_z', 'x/Y-z'),
    ],
)
def test_to_huggingface_name(
    mock_list_datasets, tfds_dataset_name, hf_dataset_name
):
  del mock_list_datasets
  assert (
      huggingface_utils.to_huggingface_name(tfds_dataset_name)
      == hf_dataset_name
  )
