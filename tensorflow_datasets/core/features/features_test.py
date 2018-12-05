# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.features.feature.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import test_utils


class AnInputConnector(features_lib.FeaturesDict):
  """Simple FeatureConnector implementing the based methods used for test."""

  def __init__(self):
    super(AnInputConnector, self).__init__({
        'a': tf.int64,
        'b': tf.int64,
    })

  def get_tensor_info(self):
    # With this connector, the way the data is on disk ({'a', 'b'}) do not match
    # the way it is exposed to the user (int64), so we overwrite
    # FeaturesDict.get_tensor_info
    return features_lib.TensorInfo(shape=(), dtype=tf.int64)

  def encode_example(self, example_data):
    # Encode take the input data and wrap in in a dict
    return super(AnInputConnector, self).encode_example({
        'a': example_data + 1,
        'b': example_data * 10
    })

  def decode_example(self, tfexample_dict):
    # Decode take the saved dict and merge the two values
    tfexample_dict = super(AnInputConnector,
                           self).decode_example(tfexample_dict)
    return tfexample_dict['a'] + tfexample_dict['b']


class AnOutputConnector(features_lib.FeatureConnector):
  """Simple FeatureConnector implementing the based methods used for test."""

  def get_tensor_info(self):
    return features_lib.TensorInfo(shape=(), dtype=tf.float32)

  def encode_example(self, example_data):
    return example_data * 10.0

  def decode_example(self, tfexample_data):
    return tfexample_data / 10.0


class FeatureDictTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):

    return [
        test_utils.FeatureExpectation(
            name='fdict',
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
                'input/a':
                    tf.FixedLenFeature(shape=(), dtype=tf.int64),
                'input/b':
                    tf.FixedLenFeature(shape=(), dtype=tf.int64),
                'output':
                    tf.FixedLenFeature(shape=(), dtype=tf.float32),
                'img/size/height':
                    tf.FixedLenFeature(shape=(), dtype=tf.int64),
                'img/size/width':
                    tf.FixedLenFeature(shape=(), dtype=tf.int64),
                'img/metadata/path':
                    tf.FixedLenFeature(shape=(), dtype=tf.string),
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
                test_utils.FeatureExpectationItem(
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
                        'input/a': 2,  # 1 + 1
                        'input/b': 10,  # 1 * 10
                        'output': -10.0,  # -1 * 10.0
                        'img/size/height': 256,
                        'img/size/width': 128,
                        'img/metadata/path': 'path/to/xyz.jpg',
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
                            'metadata/path':
                                tf.compat.as_bytes('path/to/xyz.jpg'),
                        },
                    },
                ),
            ],
        ),
    ]

  def feature_getitem_test(self):
    fdict = features_lib.FeaturesDict({
        'integer': tf.int32,
        'string': tf.string,
    })
    self.assertEqual(fdict['integer'].dtype, tf.int32)
    self.assertEqual(fdict['string'].dtype, tf.string)


class OneOfTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):

    return [
        test_utils.FeatureExpectation(
            name='oneof',
            feature=features_lib.OneOf(
                choice='choice2',
                feature_dict={
                    'choice1': tf.float32,
                    'choice2': AnInputConnector(),
                },
            ),
            # All choices are present in the serialized feature
            serialized_info={
                'choice1': tf.FixedLenFeature(shape=(), dtype=tf.float32),
                'choice2/a': tf.FixedLenFeature(shape=(), dtype=tf.int64),
                'choice2/b': tf.FixedLenFeature(shape=(), dtype=tf.int64),
            },
            # choice2 selected so dtype == AnInputConnector().dtype
            dtype=tf.int64,
            # choice2 selected so shape == AnInputConnector().shape
            shape=(),
            tests=[
                # Np array
                test_utils.FeatureExpectationItem(
                    value={
                        'choice1': 0.0,
                        'choice2': 1,
                    },
                    # All choices are serialized
                    expected_serialized={
                        'choice1': 0.0,
                        'choice2/a': 2,  # 1 + 1
                        'choice2/b': 10,  # 1 * 10
                    },
                    # Only choice 2 is decoded.
                    # a = 1 + 1, b = 1 * 10 => output = a + b = 2 + 10 = 12
                    expected=12,
                ),
            ],
        ),
    ]


class FeatureTensorTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):

    np_input = np.random.rand(2, 3).astype(np.float32)
    array_input = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    np_input_dynamic_1 = np.random.randint(256, size=(2, 3, 2), dtype=np.int32)
    np_input_dynamic_2 = np.random.randint(256, size=(5, 3, 2), dtype=np.int32)

    return [
        test_utils.FeatureExpectation(
            name='shape_static',
            feature=features_lib.Tensor(shape=(2, 3), dtype=tf.float32),
            dtype=tf.float32,
            shape=(2, 3),
            tests=[
                # Np array
                test_utils.FeatureExpectationItem(
                    value=np_input,
                    expected=np_input,
                ),
                # Python array
                test_utils.FeatureExpectationItem(
                    value=array_input,
                    expected=array_input,
                ),
                # Invalid dtype
                test_utils.FeatureExpectationItem(
                    value=np.random.randint(256, size=(2, 3)),
                    raise_cls=ValueError,
                    raise_msg='int64 do not match',
                ),
                # Invalid shape
                test_utils.FeatureExpectationItem(
                    value=np.random.rand(2, 4).astype(np.float32),
                    raise_cls=ValueError,
                    raise_msg='are incompatible',
                ),
            ],
        ),
        test_utils.FeatureExpectation(
            name='shape_dynamic',
            feature=features_lib.Tensor(shape=(None, 3, 2), dtype=tf.int32),
            dtype=tf.int32,
            shape=(None, 3, 2),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=np_input_dynamic_1,
                    expected=np_input_dynamic_1,
                ),
                test_utils.FeatureExpectationItem(
                    value=np_input_dynamic_2,
                    expected=np_input_dynamic_2,
                ),
                # Invalid shape
                test_utils.FeatureExpectationItem(
                    value=
                    np.random.randint(256, size=(2, 3, 1), dtype=np.int32),
                    raise_cls=ValueError,
                    raise_msg='are incompatible',
                ),
            ]
        ),
        test_utils.FeatureExpectation(
            name='bool_flat',
            feature=features_lib.Tensor(shape=(), dtype=tf.bool),
            dtype=tf.bool,
            shape=(),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=np.array(True),
                    expected=True,
                ),
                test_utils.FeatureExpectationItem(
                    value=np.array(False),
                    expected=False,
                ),
                test_utils.FeatureExpectationItem(
                    value=True,
                    expected=True,
                ),
                test_utils.FeatureExpectationItem(
                    value=False,
                    expected=False,
                ),
            ]
        ),
        test_utils.FeatureExpectation(
            name='bool_array',
            feature=features_lib.Tensor(shape=(3,), dtype=tf.bool),
            dtype=tf.bool,
            shape=(3,),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=np.array([True, True, False]),
                    expected=[True, True, False],
                ),
                test_utils.FeatureExpectationItem(
                    value=[True, False, True],
                    expected=[True, False, True],
                ),
            ]
        ),
    ]


if __name__ == '__main__':
  tf.test.main()
