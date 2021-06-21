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

"""Tests for tensorflow_datasets.core.features.feature."""

import pathlib
import sys
import textwrap

import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib

tf.enable_v2_behavior()


class AnInputConnector(features_lib.FeatureConnector):
  """Simple FeatureConnector implementing the based methods used for test."""

  def get_tensor_info(self):
    # With this connector, the way the data is on disk ({'a', 'b'}) do not match
    # the way it is exposed to the user (int64), so we overwrite
    # FeaturesDict.get_tensor_info
    return features_lib.TensorInfo(shape=(), dtype=tf.int64)

  def get_serialized_info(self):
    return {
        'a': features_lib.TensorInfo(shape=(), dtype=tf.int64),
        'b': features_lib.TensorInfo(shape=(), dtype=tf.int64),
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
    return features_lib.TensorInfo(shape=(), dtype=tf.float32)

  def encode_example(self, example_data):
    return example_data * 10.0

  def decode_example(self, tfexample_data):
    return tfexample_data / 10.0


class FeatureDictTest(testing.FeatureExpectationsTestCase):

  def test_tensor_info(self):

    self.assertEqual(
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
    )

    self.assertNotEqual(
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(None, 3), dtype=tf.int32),
    )

    self.assertNotEqual(
        features_lib.TensorInfo(shape=(2, 3), dtype=tf.string),
        features_lib.TensorInfo(shape=(5, 3), dtype=tf.string),
    )

    t = features_lib.TensorInfo(shape=(None, 3), dtype=tf.string)
    self.assertEqual(t, features_lib.TensorInfo.copy_from(t))

  def test_fdict(self):

    self.assertFeature(
        feature=features_lib.FeaturesDict({
            'input': AnInputConnector(),
            'output': AnOutputConnector(),
            'img': {
                'size': {
                    'height': tf.int64,
                    'width': tf.int64,
                },
                'metadata/path': tf.string,
            }
        }),
        serialized_info={
            'input': {
                'a': features_lib.TensorInfo(shape=(), dtype=tf.int64),
                'b': features_lib.TensorInfo(shape=(), dtype=tf.int64),
            },
            'output': features_lib.TensorInfo(shape=(), dtype=tf.float32),
            'img': {
                'size': {
                    'height': features_lib.TensorInfo(shape=(), dtype=tf.int64),
                    'width': features_lib.TensorInfo(shape=(), dtype=tf.int64),
                },
                'metadata/path':
                    features_lib.TensorInfo(shape=(), dtype=tf.string),
            }
        },
        dtype={
            'input': tf.int64,
            'output': tf.float32,
            'img': {
                'size': {
                    'height': tf.int64,
                    'width': tf.int64,
                },
                'metadata/path': tf.string,
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

  def test_feature_getitem(self):
    fdict = features_lib.FeaturesDict({
        'integer': tf.int32,
        'string': tf.string,
    })
    self.assertEqual(fdict['integer'].dtype, tf.int32)
    self.assertEqual(fdict['string'].dtype, tf.string)

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
            'label': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=2)),
            'metadata': Sequence({
                'frame': Image(shape=(32, 32, 3), dtype=tf.uint8),
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

  def test_repr_tensor(self):

    # Top level Tensor is printed expanded
    self.assertEqual(
        repr(features_lib.Tensor(shape=(), dtype=tf.int32)),
        'Tensor(shape=(), dtype=tf.int32)',
    )

    # Sequences colapse tensor repr
    self.assertEqual(
        repr(features_lib.Sequence(tf.int32)),
        'Sequence(tf.int32)',
    )

    class ChildTensor(features_lib.Tensor):
      pass

    self.assertEqual(
        repr(
            features_lib.FeaturesDict({
                'colapsed': features_lib.Tensor(shape=(), dtype=tf.int32),
                # Tensor with defined shape are printed expanded
                'noncolapsed': features_lib.Tensor(shape=(1,), dtype=tf.int32),
                # Tensor inherited are expanded
                'child': ChildTensor(shape=(), dtype=tf.int32),
            })),
        textwrap.dedent("""\
        FeaturesDict({
            'child': ChildTensor(shape=(), dtype=tf.int32),
            'colapsed': tf.int32,
            'noncolapsed': Tensor(shape=(1,), dtype=tf.int32),
        })"""),
    )


def test_custom_feature_connector(tmp_path: pathlib.Path):
  module_name = 'tensorflow_datasets.core.features.test_feature'
  feature_qualname = f'{module_name}.CustomFeatureConnector'
  assert module_name not in sys.modules
  assert feature_qualname not in features_lib.FeatureConnector._registered_features

  # Save tfds.feature.Tensor to avoid importing the custom feature connector
  feature = features_lib.Tensor(shape=(), dtype=tf.int32)
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


if __name__ == '__main__':
  testing.test_main()
