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

"""Tests for tensorflow_datasets.core.features.class_label_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import features
from tensorflow_datasets.core import test_utils


class ClassLabelFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    return [
        test_utils.FeatureExpectation(
            name='label',
            feature=features.ClassLabel(num_classes=10),
            dtype=tf.int64,
            shape=(),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=3,
                    expected=3,
                ),
                test_utils.FeatureExpectationItem(
                    value='3',
                    expected=3,
                ),
                test_utils.FeatureExpectationItem(
                    value=10,
                    raise_cls=ValueError,
                    raise_msg='greater than configured num_classes',
                ),
                test_utils.FeatureExpectationItem(
                    value='10',
                    raise_cls=ValueError,
                    raise_msg='Invalid',
                ),
            ]
        ),
        test_utils.FeatureExpectation(
            name='directions',
            feature=features.ClassLabel(names=['left', 'right']),
            dtype=tf.int64,
            shape=(),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=1,
                    expected=1,
                ),
                test_utils.FeatureExpectationItem(
                    value='left',
                    expected=0,
                ),
                test_utils.FeatureExpectationItem(
                    value='right',
                    expected=1,
                ),
            ]
        ),
    ]

  def test_num_classes(self):
    labels = features.ClassLabel(num_classes=10)
    self.assertEqual(10, labels.num_classes)
    self.assertEqual(10, len(labels.names))

    self.assertEqual(1, labels.str2int('1'))
    self.assertEqual(u'1', labels.int2str(1))

    with self.assertRaisesWithPredicateMatch(ValueError, 'Invalid'):
      labels.str2int('10')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Invalid'):
      labels.int2str(10)

  def test_str_classes(self):
    labels = features.ClassLabel(names=[
        'label3',
        'label1',
        'label2',
    ])
    self.assertEqual(3, labels.num_classes)
    self.assertEqual(labels.names, [
        'label3',
        'label1',
        'label2',
    ])

    self.assertEqual(labels.str2int('label3'), 0)
    self.assertEqual(labels.str2int('label1'), 1)
    self.assertEqual(labels.str2int('label2'), 2)
    self.assertEqual(labels.int2str(0), 'label3')
    self.assertEqual(labels.int2str(1), 'label1')
    self.assertEqual(labels.int2str(2), 'label2')

  def test_save_load(self):
    labels1 = features.ClassLabel(names=['label3', 'label1', 'label2'])
    labels2 = features.ClassLabel(num_classes=None)
    labels3 = features.ClassLabel(num_classes=1)

    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      labels1.save_metadata(tmp_dir, 'test-labels')
      labels2.load_metadata(tmp_dir, 'test-labels')
      with self.assertRaisesWithPredicateMatch(
          ValueError, 'number of names do not match the defined num_classes'):
        labels3.load_metadata(tmp_dir, 'test-labels')

    # labels2 should have been copied from label1
    self.assertEqual(3, labels2.num_classes)
    self.assertEqual(labels2.names, [
        'label3',
        'label1',
        'label2',
    ])

  def test_names(self):

    labels = features.ClassLabel(names=['label3', 'label1', 'label2'])
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'overwrite already defined ClassLabel'):
      labels.names = ['other', 'labels']

    labels = features.ClassLabel()
    labels.names = ['label3', 'label1', 'label2']
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'overwrite already defined ClassLabel'):
      labels.names = ['other', 'labels']

    labels = features.ClassLabel(num_classes=3)
    labels.names = ['label3', 'label1', 'label2']

    labels = features.ClassLabel(num_classes=3)
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'number of names do not match the defined num_classes'):
      labels.names = ['label3', 'label1']


if __name__ == '__main__':
  tf.test.main()
