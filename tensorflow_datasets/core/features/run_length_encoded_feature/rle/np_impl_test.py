from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import numpy as np

from tensorflow_datasets.core.features.run_length_encoded_feature.rle import np_impl


class BlreNpTest(unittest.TestCase):

  def test_merge_rle_lengths(self):
    v0, l0 = [5, 5, 2], [10, 10, 1]
    v1, l1 = [5, 2], [20, 1]
    v0, l0 = np_impl.merge_rle_lengths(v0, l0)
    np.testing.assert_equal(v0, v1)
    np.testing.assert_equal(l0, l1)

  def test_split_long_rle_lengths(self):
    v0, l0 = [5], [300]
    v1, l1 = [5, 5], [255, 45]

    v0, l0 = np_impl.split_long_rle_lengths(v0, l0, dtype=np.uint8)
    np.testing.assert_equal(v0, v1)
    np.testing.assert_equal(l0, l1)

    v0, l0 = [5, 2, 3], [10, 1000, 4]
    v1, l1 = [5, 2, 2, 2, 2, 3], [10, 255, 255, 255, 235, 4]

    v0, l0 = np_impl.split_long_rle_lengths(v0, l0, dtype=np.uint8)
    np.testing.assert_equal(v0, v1)
    np.testing.assert_equal(l0, l1)

  def test_merge_brle_lengths(self):
    np.testing.assert_equal(
      np_impl.merge_brle_lengths([10, 0, 10, 2]), [20, 2])
    np.testing.assert_equal(
        np_impl.merge_brle_lengths([10, 0, 10, 2]), [20, 2])
    np.testing.assert_equal(
        np_impl.merge_brle_lengths([10, 1, 10, 2]), [10, 1, 10, 2])
    np.testing.assert_equal(
        np_impl.merge_brle_lengths([0, 10, 2, 3]), [0, 10, 2, 3])

  def test_split_long_brle_lengths(self):
    np.testing.assert_equal(
      np_impl.split_long_brle_lengths([300, 600, 10], np.uint8),
      [255, 0, 45, 255, 0, 255, 0, 90, 10])

  def test_brle_split_merge(self):
    x = [300, 600, 10]
    split = np_impl.split_long_brle_lengths(x, np.uint8)
    merged = np_impl.merge_brle_lengths(split)
    np.testing.assert_equal(merged, x)

  def test_dense_to_brle(self):
    x = np.array([False]*300 + [True]*200 + [False]*1000)
    np.testing.assert_equal(np_impl.dense_to_brle(x), [300, 200, 1000])
    np.testing.assert_equal(
        np_impl.dense_to_brle(x, np.uint8),
        [255, 0, 45, 200, 255, 0, 255, 0, 255, 0, 235])

  def test_brle_to_rle(self):
    np.testing.assert_equal(
        np_impl.brle_to_rle([0, 5, 2, 0]), [1, 5, 0, 2])

  def test_rle_to_brle(self):
    np.testing.assert_equal(
        np_impl.rle_to_brle([0, 5, 1, 3, 0, 10]),
        [5, 3, 10, 0])
    np.testing.assert_equal(
        np_impl.rle_to_brle([0, 5, 0, 3, 1, 10]),
        [8, 10])
    np.testing.assert_equal(
        np_impl.rle_to_brle([1, 5, 0, 3, 1, 10]),
        [0, 5, 3, 10])
    np.testing.assert_equal(
        np_impl.rle_to_brle([1, 5, 0, 2]),
        [0, 5, 2, 0])


if __name__ == '__main__':
  unittest.main()
