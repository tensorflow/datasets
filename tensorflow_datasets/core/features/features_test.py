# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.features.feature."""

import pathlib
import sys
import textwrap
from unittest import mock

from absl import logging
from absl.testing import parameterized
import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib


class AnInputConnector(features_lib.FeatureConnector):
  """Simple FeatureConnector implementing the based methods used for test."""

  def get_tensor_info(self):
    # With this connector, the way the data is on disk ({'a', 'b'}) do not match
    # the way it is exposed to the user (int64), so we overwrite
    # FeaturesDict.get_tensor_info
    return features_lib.TensorInfo(shape=(), dtype=np.int64)

  def get_serialized_info(self):
    return {
        'a': features_lib.TensorInfo(shape=(), dtype=np.int64),
        'b': features_lib.TensorInfo(shape=(), dtype=np.int64),
    }

  def encode_example(self, example_data):
    # Encode take the input data and wrap in in a dict
    return {'a': example_data + 1, 'b': example_data * 10}

  def decode_example(self, tfexample_dict):
    # Merge the two values
    return tfexample_dict['a'] + tfexample_dict['b']


class AnOutputConnector(features_lib.FeatureConnector):
  """Simple FeatureConnector implementing the based methods used for test."""

  def get_tensor_info(self):
    return features_lib.TensorInfo(shape=(), dtype=np.float32)

  def encode_example(self, example_data):
    return example_data * 10.0

  def decode_example(self, tfexample_data):
    return tfexample_data / 10.0


class FeatureDictTest(parameterized.TestCase,
                      testing.FeatureExpectationsTestCase):

  def test_tensor_info(self):

    self.assertEqual(
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
    )

    self.assertEqual(
        features_lib.TensorInfo(shape=(None, 3), dtype=np.object_),
        features_lib.TensorInfo(shape=(None, 3), dtype=np.object_),
    )

    self.assertNotEqual(
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.int32),
    )

    self.assertNotEqual(
        features_lib.TensorInfo(shape=(2, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(5, 3), dtype=tf.string),
    )

    self.assertNotEqual(
        features_lib.TensorInfo(shape=(2, 3), dtype=np.object_),
        features_lib.TensorInfo(shape=(5, 3), dtype=np.object_),
    )

    t = features_lib.TensorInfo(shape=(None, 3), dtype=tf.string)
    self.assertEqual(t, features_lib.TensorInfo.copy_from(t))

  @parameterized.parameters(
      (np.int64, np.str_,
       mock.Mock(
           side_effect=Exception(
               'no warning should be raised when using NumPy types'))),
      (tf.int64, tf.string, mock.Mock()))
  def test_tensor_spec(self, image_dtype, metadata_dtype, warning_mock):
    logging.warning = warning_mock
    feature = features_lib.FeaturesDict({
        'input': AnInputConnector(),
        'output': AnOutputConnector(),
        'img': {
            'size': {
                'height':
                    features_lib.Tensor(shape=(2, 3), dtype=image_dtype),
                'width':
                    features_lib.Tensor(shape=[None, 3], dtype=image_dtype),
            },
            'image': features_lib.Image(shape=(28, 28, 1)),
            'metadata/path': metadata_dtype,
        }
    })
    self.assertAllEqualNested(
        feature.get_tensor_spec(), {
            'input': tf.TensorSpec(shape=[], dtype=np.int64),
            'output': tf.TensorSpec(shape=[], dtype=np.float32),
            'img': {
                'size': {
                    'height': tf.TensorSpec(shape=[2, 3], dtype=np.int64),
                    'width': tf.TensorSpec(shape=[None, 3], dtype=np.int64),
                },
                'image': tf.TensorSpec(shape=[28, 28, 1], dtype=np.uint8),
                'metadata/path': tf.TensorSpec(shape=[], dtype=np.object_),
            }
        })

  @parameterized.parameters((np.int64, np.str_, np.str_),
                            (tf.int64, tf.string, np.object_))
  def test_fdict(self, image_dtype, metadata_dtype, output_metadata_dtype):

    self.assertFeature(
        feature=features_lib.FeaturesDict({
            'input': AnInputConnector(),
            'output': AnOutputConnector(),
            'img': {
                'size': {
                    'height': image_dtype,
                    'width': image_dtype,
                },
                'metadata/path': metadata_dtype,
            }
        }),
        serialized_info={
            'input': {
                'a': features_lib.TensorInfo(shape=(), dtype=np.int64),
                'b': features_lib.TensorInfo(shape=(), dtype=np.int64),
            },
            'output': features_lib.TensorInfo(shape=(), dtype=np.float32),
            'img': {
                'size': {
                    'height': features_lib.TensorInfo(shape=(), dtype=np.int64),
                    'width': features_lib.TensorInfo(shape=(), dtype=np.int64),
                },
                'metadata/path':
                    features_lib.TensorInfo(
                        shape=(), dtype=output_metadata_dtype),
            }
        },
        dtype={
            'input': np.int64,
            'output': np.float32,
            'img': {
                'size': {
                    'height': np.int64,
                    'width': np.int64,
                },
                'metadata/path': output_metadata_dtype,
            }
        },
        shape={
            'input': (),
            'output': (),
            'img': {
                'size': {
                    'height': (),
                    'width': (),
                },
                'metadata/path': (),
            },
        },
        tests=[
            # Np array
            testing.FeatureExpectationItem(
                value={
                    'input': 1,
                    'output': -1,
                    'img': {
                        'size': {
                            'height': 256,
                            'width': 128,
                        },
                        'metadata/path': 'path/to/xyz.jpg',
                    }
                },
                expected_serialized={
                    'input': {
                        'a': 2,  # 1 + 1
                        'b': 10,  # 1 * 10
                    },
                    'output': -10.0,  # -1 * 10.0
                    'img': {
                        'size': {
                            'height': 256,
                            'width': 128,
                        },
                        'metadata/path': 'path/to/xyz.jpg',
                    }
                },
                expected={
                    # a = 1 + 1, b = 1 * 10 => output = a + b = 2 + 10 = 12
                    'input': 12,  # 2 + 10
                    'output': -1.0,
                    'img': {
                        'size': {
                            'height': 256,
                            'width': 128,
                        },
                        'metadata/path': tf.compat.as_bytes('path/to/xyz.jpg'),
                    },
                },
            ),
        ],
    )

  @parameterized.parameters(
      ({
          'integer': np.int32,
          'string': np.object_,
      },),
      ({
          'integer': tf.int32,
          'string': tf.string,
      },),
  )
  def test_feature_getitem(self, features_dict):
    fdict = features_lib.FeaturesDict(features_dict)
    self.assertEqual(fdict['integer'].dtype, np.int32)
    self.assertEqual(fdict['string'].dtype, np.object_)

  def test_feature__repr__(self):

    label = features_lib.ClassLabel(names=['m', 'f'])
    feature_dict = features_lib.FeaturesDict({
        'metadata':
            features_lib.Sequence({
                'frame': features_lib.Image(shape=(32, 32, 3)),
            }),
        'label':
            features_lib.Sequence(label),
    })

    self.assertEqual(
        repr(feature_dict),
        textwrap.dedent("""\
        FeaturesDict({
            'label': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=2)),
            'metadata': Sequence({
                'frame': Image(shape=(32, 32, 3), dtype=uint8),
            }),
        })"""),
    )

  def test_feature_save_load_metadata_slashes(self):
    with testing.tmp_dir() as data_dir:
      fd = features_lib.FeaturesDict({
          'image/frame': features_lib.Image(shape=(32, 32, 3)),
          'image/label': features_lib.ClassLabel(num_classes=2),
      })
      fd.save_metadata(data_dir)
      fd.load_metadata(data_dir)

  @parameterized.parameters((np.int32), (tf.int32))
  def test_repr_tensor(self, dtype):

    # Top level Tensor is printed expanded
    self.assertEqual(
        repr(features_lib.Tensor(shape=(), dtype=tf.int32)),
        'Tensor(shape=(), dtype=int32)',
    )

    # Sequences colapse tensor repr
    self.assertEqual(
        repr(features_lib.Sequence(tf.int32)),
        'Sequence(int32)',
    )

    class ChildTensor(features_lib.Tensor):
      pass

    self.assertEqual(
        repr(
            features_lib.FeaturesDict({
                'colapsed': features_lib.Tensor(shape=(), dtype=dtype),
                # Tensor with defined shape are printed expanded
                'noncolapsed': features_lib.Tensor(shape=(1,), dtype=dtype),
                # Tensor inherited are expanded
                'child': ChildTensor(shape=(), dtype=dtype),
            })),
        textwrap.dedent("""\
        FeaturesDict({
            'child': ChildTensor(shape=(), dtype=int32),
            'colapsed': int32,
            'noncolapsed': Tensor(shape=(1,), dtype=int32),
        })"""),
    )


def test_custom_feature_connector(tmp_path: pathlib.Path):
  module_name = 'tensorflow_datasets.core.features.test_feature'
  feature_qualname = f'{module_name}.CustomFeatureConnector'
  assert module_name not in sys.modules
  assert feature_qualname not in features_lib.FeatureConnector._registered_features

  # Save tfds.feature.Tensor to avoid importing the custom feature connector
  feature = features_lib.Tensor(shape=(), dtype=np.int32)
  feature.save_config(tmp_path)

  # Update the features.json file to simulate as if the original
  # FeatureConnector had been save
  feature_path = tmp_path / 'features.json'
  content = feature_path.read_text()
  content = content.replace(
      'tensorflow_datasets.core.features.tensor_feature.Tensor',
      feature_qualname,
  )
  feature_path.write_text(content)

  # Loading will load the custom feature connector, even if it is not
  # registered yet.
  feature = features_lib.FeatureConnector.from_config(tmp_path)

  # After loading, the custom feature connector is registered
  assert module_name in sys.modules
  assert feature_qualname in features_lib.FeatureConnector._registered_features

  # Check that the loaded feature is the custom feature
  from tensorflow_datasets.core.features import test_feature  # pylint: disable=g-import-not-at-top
  assert isinstance(feature, test_feature.CustomFeatureConnector)


def test_tensor_feature_backward_compatibility():
  registered = features_lib.FeatureConnector._registered_features
  cls = features_lib.Tensor
  module_base = 'tensorflow_datasets.core.features.'
  # Both aliases are registered
  assert registered[module_base + 'tensor_feature.Tensor'] is cls
  assert registered[module_base + 'feature.Tensor'] is cls


def test_from_json_content_backward_compatibility():
  legacy_json = {
      'type': 'tensorflow_datasets.core.features.features_dict.FeaturesDict',
      'content': {
          'input': {
              'type': 'tensorflow_datasets.core.features.image_feature.Image',
              'content': {
                  'shape': [28, 28, 3],
                  'dtype': 'uint8',
                  'encoding_format': 'png'
              }
          },
          'target': {
              'type':
                  'tensorflow_datasets.core.features.class_label_feature.ClassLabel',
              'content': {
                  'num_classes': 10
              }
          }
      }
  }
  parsed_features_dict = features_lib.FeatureConnector.from_json(legacy_json)
  assert parsed_features_dict.keys() == set(['input', 'target'])


if __name__ == '__main__':
  testing.test_main()
