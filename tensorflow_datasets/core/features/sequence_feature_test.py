# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.features.sequence_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as feature_lib

tf.compat.v1.enable_eager_execution()


class SequenceDictFeatureTest(testing.FeatureExpectationsTestCase):

  def test_int(self):

    self.assertFeature(
        feature=feature_lib.Sequence({'int': tf.int32}, length=3),
        shape={'int': (3,)},
        dtype={'int': tf.int32},
        serialized_info={
            'int': feature_lib.TensorInfo(shape=(3,), dtype=tf.int32),
        },
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value={'int': [1, 2, 3]},
                expected={'int': [1, 2, 3]},
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value={'int': np.ones(shape=(3,), dtype=np.int32)},
                expected={'int': [1, 1, 1]},
            ),
            # Array of dict
            testing.FeatureExpectationItem(
                value=[
                    {'int': 1},
                    {'int': 10},
                    {'int': 100},
                ],
                expected={'int': [1, 10, 100]},
            ),
            # Wrong sequence length
            testing.FeatureExpectationItem(
                value={'int': np.ones(shape=(4,), dtype=np.int32)},
                raise_cls=ValueError,
                raise_msg='Input sequence length do not match',
            ),
        ],
    )

  def test_label(self):

    self.assertFeature(
        feature=feature_lib.Sequence({
            'label': feature_lib.ClassLabel(names=['left', 'right']),
        }, length=None),
        shape={'label': (None,)},
        dtype={'label': tf.int64},
        serialized_info={
            'label': feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
        },
        tests=[
            testing.FeatureExpectationItem(
                value={'label': ['right', 'left', 'left']},
                expected={'label': [1, 0, 0]},
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value={'label': ['right', 'left', 'right', 'left']},
                expected={'label': [1, 0, 1, 0]},
            ),
            # Empty sequence length
            testing.FeatureExpectationItem(
                value={'label': []},
                expected={'label': []},
            ),
        ],
    )

  def test_nested(self):

    self.assertFeature(
        feature=feature_lib.Sequence({
            'a': tf.string,
            'b': {
                'c': feature_lib.Tensor(shape=(4, 2), dtype=tf.int32),
                'd': tf.uint8,
            }
        }, length=None),
        shape={
            'a': (None,),
            'b': {
                'c': (None, 4, 2),
                'd': (None,),
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
                value={
                    'a': ['aa', 'b', 'ccc'],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    }
                },
                expected={
                    'a': [
                        tf.compat.as_bytes(t) for t in ('aa', 'b', 'ccc')
                    ],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    }
                },
            ),
            testing.FeatureExpectationItem(
                value={
                    'a': [str(i) for i in range(100)],
                    'b': [{   # pylint: disable=g-complex-comprehension
                        'c': np.ones(shape=(4, 2), dtype=np.int32),
                        'd': 5,
                    } for _ in range(100)]
                },
                expected={
                    'a': [tf.compat.as_bytes(str(i)) for i in range(100)],
                    'b': {
                        'c': np.ones(shape=(100, 4, 2), dtype=np.int32),
                        'd': [5] * 100,
                    }
                },
            ),
            # Test inputs not same sequence length
            testing.FeatureExpectationItem(
                value={
                    'a': ['aa', 'b', 'ccc'],
                    'b': {
                        'c': np.ones(shape=(4, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    }
                },
                raise_cls=ValueError,
                raise_msg='length of all elements of one sequence should',
            ),
        ],
    )

  def test_image(self):

    imgs = [
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
    ]
    imgs_stacked = np.stack(imgs)

    self.assertFeature(
        feature=feature_lib.Sequence({
            'image': feature_lib.Image(shape=(128, 100, 3)),
        }, length=None),
        shape={'image': (None, 128, 100, 3)},
        dtype={'image': tf.uint8},
        tests=[
            testing.FeatureExpectationItem(
                value=[{'image': img} for img in imgs],
                expected={'image': imgs_stacked},
            ),
            testing.FeatureExpectationItem(
                value={'image': imgs_stacked},
                expected={'image': imgs_stacked},
            ),
            testing.FeatureExpectationItem(
                value={'image': imgs},
                expected={'image': imgs_stacked},
            ),
            # Empty value
            testing.FeatureExpectationItem(
                value={'image': []},
                # The empty value still has the right shape
                expected={'image': np.empty(
                    shape=(0, 128, 100, 3),
                    dtype=np.uint8
                )},
            ),
        ],
    )

  # Should add unittest for _transpose_dict_list


class SequenceFeatureTest(testing.FeatureExpectationsTestCase):

  def test_int(self):

    self.assertFeature(
        feature=feature_lib.Sequence(tf.int32, length=3),
        shape=(3,),
        dtype=tf.int32,
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value=[1, 2, 3],
                expected=[1, 2, 3],
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value=np.ones(shape=(3,), dtype=np.int32),
                expected=[1, 1, 1],
            ),
            # Wrong sequence length
            testing.FeatureExpectationItem(
                value=np.ones(shape=(4,), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='Input sequence length do not match',
            ),
        ],
    )

  def test_label(self):

    self.assertFeature(
        feature=feature_lib.Sequence(
            feature_lib.ClassLabel(names=['left', 'right']),
        ),
        shape=(None,),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=['right', 'left', 'left'],
                expected=[1, 0, 0],
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value=['right', 'left', 'right', 'left'],
                expected=[1, 0, 1, 0],
            ),
            # Empty sequence length
            testing.FeatureExpectationItem(
                value=[],
                expected=[],
            ),
        ],
    )

  def test_getattr(self):
    feature = feature_lib.Sequence(
        feature_lib.ClassLabel(names=['left', 'right']),
    )
    self.assertEqual(feature.names, ['left', 'right'])

    feature = feature_lib.Sequence({
        'label': feature_lib.ClassLabel(names=['left', 'right']),
    })
    self.assertEqual(feature['label'].names, ['left', 'right'])

  def test_metadata(self):
    feature = feature_lib.Sequence(feature_lib.ClassLabel(num_classes=2))
    feature.feature.names = ['left', 'right']
    with testing.tmp_dir() as tmp_dir:
      feature.save_metadata(data_dir=tmp_dir, feature_name='test')

      feature2 = feature_lib.Sequence(feature_lib.ClassLabel(num_classes=2))
      feature2.load_metadata(data_dir=tmp_dir, feature_name='test')
    self.assertEqual(feature2.feature.names, ['left', 'right'])


if __name__ == '__main__':
  testing.test_main()
