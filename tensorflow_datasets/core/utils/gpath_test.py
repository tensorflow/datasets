"""Tests for tensorflow_datasets.core.utils.gpath."""

import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import gpath


class GPathTest(testing.TestCase):


  def test_path_exists(self):
    PATH = "gs://tfds-data/datasets/mnist/3.0.0/"
    g_path = gpath.GPath(PATH)
    self.assertTrue(g_path.exists())

  def test_path_not_exists(self):
    PATH = "gs://tfds-data/foo/bar"
    g_path = gpath.GPath(PATH)
    self.assertFalse(g_path.exists())

if __name__ == '__main__':
  testing.test_main()
