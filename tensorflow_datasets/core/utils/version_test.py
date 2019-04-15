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

"""Tests for tensorflow_datasets.core.utils.version."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import version


class VersionTest(testing.TestCase):

  def test_str_to_version(self):
    self.assertEqual(version._str_to_version('1.2.3'), (1, 2, 3))
    self.assertEqual(version._str_to_version('1.2.*', True), (1, 2, '*'))
    self.assertEqual(version._str_to_version('1.*.3', True), (1, '*', 3))
    self.assertEqual(version._str_to_version('*.2.3', True), ('*', 2, 3))
    self.assertEqual(version._str_to_version('1.*.*', True), (1, '*', '*'))
    with self.assertRaisesWithPredicateMatch(ValueError, 'Invalid version '):
      version.Version('1.3')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Invalid version '):
      version.Version('1.3.*')

  def test_version(self):
    """Test the zip nested function."""

    self.assertEqual(version.Version(), version.Version(0, 0, 0))
    self.assertEqual(version.Version('1.3.534'), version.Version(1, 3, 534))
    self.assertEqual(
        version.Version(major=1, minor=3, patch=5), version.Version(1, 3, 5))

    self.assertEqual(version.Version('latest'), version.Version.LATEST)
    self.assertEqual(
        version.Version(version.Version('1.3.5')), version.Version(1, 3, 5))

    self.assertEqual(str(version.Version(10, 2, 3)), '10.2.3')
    self.assertEqual(str(version.Version()), '0.0.0')

    with self.assertRaisesWithPredicateMatch(ValueError, 'Format should be '):
      version.Version('1.3.-534')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Format should be '):
      version.Version('1.3')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Format should be '):
      version.Version('1.3.')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Format should be '):
      version.Version('1..5')
    with self.assertRaisesWithPredicateMatch(ValueError, 'Format should be '):
      version.Version('a.b.c')

  def test_match(self):
    v = version.Version('1.2.3')
    self.assertTrue(v.match('1.2.3'))
    self.assertTrue(v.match('1.2.*'))
    self.assertTrue(v.match('1.*.*'))
    self.assertTrue(v.match('*.*.*'))
    self.assertTrue(v.match('*.2.3'))
    self.assertFalse(v.match('1.2.4'))
    self.assertFalse(v.match('1.3.*'))
    self.assertFalse(v.match('1.3.*'))
    self.assertFalse(v.match('2.*.*'))


if __name__ == '__main__':
  testing.test_main()
