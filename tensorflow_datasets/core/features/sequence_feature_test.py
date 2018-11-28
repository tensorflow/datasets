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

"""Tests for tensorflow_datasets.core.features.sequence_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.public_api as tfds


class SequenceFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):

    all_tests = [
        test_utils.FeatureExpectation(
            name='int',
            feature=tfds.features.SequenceDict({
                'int': tf.int32,
            }, length=3),
            shape={'int': (3,)},
            dtype={'int': tf.int32},
            tests=[
                # Python array
                test_utils.FeatureExpectationItem(
                    value={'int': [1, 2, 3]},
                    expected={'int': [1, 2, 3]},
                ),
                # Numpy array
                test_utils.FeatureExpectationItem(
                    value={'int': np.ones(shape=(3,), dtype=np.int32)},
                    expected={'int': [1, 1, 1]},
                ),
                # Array of dict
                test_utils.FeatureExpectationItem(
                    value=[
                        {'int': 1},
                        {'int': 10},
                        {'int': 100},
                    ],
                    expected={'int': [1, 10, 100]},
                ),
                # Wrong sequence length
                test_utils.FeatureExpectationItem(
                    value={'int': np.ones(shape=(4,), dtype=np.int32)},
                    raise_cls=ValueError,
                    raise_msg='Input sequence length do not match',
                ),
            ],
        ),
        test_utils.FeatureExpectation(
            name='label',
            feature=tfds.features.SequenceDict({
                'label': tfds.features.ClassLabel(names=['left', 'right']),
            }, length=None),
            shape={'label': (None,)},
            dtype={'label': tf.int64},
            tests=[
                test_utils.FeatureExpectationItem(
                    value={'label': ['right', 'left', 'left']},
                    expected={'label': [1, 0, 0]},
                ),
                # Variable sequence length
                test_utils.FeatureExpectationItem(
                    value={'label': ['right', 'left', 'right', 'left']},
                    expected={'label': [1, 0, 1, 0]},
                ),
                # Empty sequence length
                test_utils.FeatureExpectationItem(
                    value={'label': []},
                    raise_cls=ValueError,
                    raise_msg='do not support empty sequences',
                ),
            ],
        ),
        test_utils.FeatureExpectation(
            name='nested',
            feature=tfds.features.SequenceDict({
                'a': tf.string,
                'b': {
                    'c': tfds.features.Tensor(shape=(4, 2), dtype=tf.int32),
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
                test_utils.FeatureExpectationItem(
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
                test_utils.FeatureExpectationItem(
                    value={
                        'a': [str(i) for i in range(100)],
                        'b': [{
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
                test_utils.FeatureExpectationItem(
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
        ),
    ]

    imgs = [
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
        np.random.randint(256, size=(128, 100, 3), dtype=np.uint8),
    ]
    imgs_stacked = np.stack(imgs)

    all_tests += [
        test_utils.FeatureExpectation(
            name='image',
            feature=tfds.features.SequenceDict({
                'image': tfds.features.Image(shape=(128, 100, 3)),
            }, length=None),
            shape={'image': (None, 128, 100, 3)},
            dtype={'image': tf.uint8},
            tests=[
                test_utils.FeatureExpectationItem(
                    value=[{'image': img} for img in imgs],
                    expected={'image': imgs_stacked},
                ),
                test_utils.FeatureExpectationItem(
                    value={'image': imgs_stacked},
                    expected={'image': imgs_stacked},
                ),
                test_utils.FeatureExpectationItem(
                    value={'image': imgs},
                    expected={'image': imgs_stacked},
                ),
            ],
        ),
    ]

    return all_tests

  # Should add unittest for _transpose_dict_list


if __name__ == '__main__':
  tf.test.main()
