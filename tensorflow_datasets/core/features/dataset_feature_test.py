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

"""Tests for tensorflow_datasets.core.features.dataset_feature."""

import numpy as np
import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as feature_lib

tf.enable_v2_behavior()


class DatasetDictFeatureTest(testing.FeatureExpectationsTestCase):

  def test_int(self):

    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset({'int': tf.int32}),
        shape={'int': ()},  # shape of each element of the dataset
        dtype={'int': tf.int32},
        serialized_info={
            'int': feature_lib.TensorInfo(shape=(None,), dtype=tf.int32),
        },
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value=[{
                    'int': 1
                }, {
                    'int': 2
                }, {
                    'int': 3
                }],
                expected=tf.data.Dataset.from_tensor_slices({'int': [1, 2, 3]}),
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'int': np.ones(shape=(3,), dtype=np.int32)})),
                expected=tf.data.Dataset.from_tensor_slices({'int': [1, 1, 1]}),
            ),
            # Dataset length doesn't matter
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'int': np.ones(shape=(4,), dtype=np.int32)})),
                expected=tf.data.Dataset.from_tensor_slices(
                    {'int': [1, 1, 1, 1]}),
            ),
        ],
        test_attributes=dict(_length=None))

  def test_label(self):

    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            {
                'label': feature_lib.ClassLabel(names=['left', 'right']),
            },
            length=None),
        shape={'label': ()},
        dtype={'label': tf.int64},
        serialized_info={
            'label': feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
        },
        tests=[
            testing.FeatureExpectationItem(
                value=[{
                    'label': 'right'
                }, {
                    'label': 'left'
                }, {
                    'label': 'left'
                }],
                expected=tf.data.Dataset.from_tensor_slices(
                    {'label': [1, 0, 0]}),
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'label': ['right', 'left', 'right', 'left']})),
                expected=tf.data.Dataset.from_tensor_slices(
                    {'label': [1, 0, 1, 0]}),
            ),
        ],
        test_attributes=dict(_length=None))

  def test_nested(self):

    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset({
            'a': tf.string,
            'b': {
                'c': feature_lib.Tensor(shape=(4, 2), dtype=tf.int32),
                'd': tf.uint8,
            }
        }, length=None),
        shape={
            'a': (),
            'b': {
                'c': (4, 2),
                'd': (),
            }
        },
        dtype={
            'a': tf.string,
            'b': {
                'c': tf.int32,
                'd': tf.uint8,
            }
        },
        tests=[
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(tf.data.Dataset.from_tensor_slices({
                    'a': ['aa', 'b', 'ccc'],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    }
                })),
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [
                        tf.compat.as_bytes(t) for t in ('aa', 'b', 'ccc')
                    ],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    }
                }),
            ),
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(tf.data.Dataset.from_tensor_slices({
                    'a': [str(i) for i in range(100)],
                    'b': {   # pylint: disable=g-complex-comprehension
                        'c': [np.ones(shape=(4, 2), dtype=np.int32) for _ in range(100)],
                        'd': [5 for _ in range(100)],
                    }
                })),
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(str(i)) for i in range(100)],
                    'b': {
                        'c': np.ones(shape=(100, 4, 2), dtype=np.int32),
                        'd': [5] * 100,
                    }
                }),
            ),
        ],
    )


class DatasetFeatureTest(testing.FeatureExpectationsTestCase):

  def test_int(self):

    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(tf.int32, length=3),
        shape=(),
        dtype=tf.int32,
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value=[1, 2, 3],
                expected=tf.data.Dataset.from_tensor_slices([1, 2, 3]),
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value=np.ones(shape=(3,), dtype=np.int32),
                expected=tf.data.Dataset.from_tensor_slices([1, 1, 1]),
            ),
            # Datasets with a different lenght will fail on encoding.
            testing.FeatureExpectationItem(
                value=np.ones(shape=(4,), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='Error while serializing feature',
            ),
        ],
    )

  def test_label(self):

    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            feature_lib.ClassLabel(names=['left', 'right']),),
        shape=(),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=['right', 'left', 'left'],
                expected=tf.data.Dataset.from_tensor_slices([1, 0, 0]),
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value=['right', 'left', 'right', 'left'],
                expected=tf.data.Dataset.from_tensor_slices([1, 0, 1, 0]),
            ),
            # Empty sequence length
            testing.FeatureExpectationItem(
                value=[],
                expected=[],
            ),
        ],
    )

  def test_getattr(self):
    feature = feature_lib.Dataset(
        feature_lib.ClassLabel(names=['left', 'right']),)
    self.assertEqual(feature.names, ['left', 'right'])

    feature = feature_lib.Dataset({
        'label': feature_lib.ClassLabel(names=['left', 'right']),
    })
    self.assertEqual(feature['label'].names, ['left', 'right'])

  def test_metadata(self):
    feature = feature_lib.Dataset(feature_lib.ClassLabel(num_classes=2))
    feature.feature.names = ['left', 'right']
    with testing.tmp_dir() as tmp_dir:
      feature.save_metadata(data_dir=tmp_dir, feature_name='test')

      feature2 = feature_lib.Dataset(feature_lib.ClassLabel(num_classes=2))
      feature2.load_metadata(data_dir=tmp_dir, feature_name='test')
    self.assertEqual(feature2.feature.names, ['left', 'right'])


if __name__ == '__main__':
  testing.test_main()
