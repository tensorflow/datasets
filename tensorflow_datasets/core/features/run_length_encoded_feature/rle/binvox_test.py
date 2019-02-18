from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import unittest
import tempfile
import tensorflow as tf
import tensorflow_datasets.core.features.run_length_encoded_feature.rle.binvox as bv
import tensorflow_datasets.core.features.run_length_encoded_feature.rle.np_impl as np_impl
import tensorflow as tf
import tensorflow_datasets as tfds  # for patching


class BinvoxText(unittest.TestCase):
  def test_write_read(self):
    tmp_dir = tempfile.mkdtemp("tfds")
    bv_path = os.path.join(tmp_dir, "test.binvox")
    def clean_up():
      if os.path.isdir(tmp_dir):
        tf.io.gfile.rmtree(tmp_dir)

    shape = (4, 6, 8)
    translate = (2.2, 3.8, 1.2)
    scale = 2.4
    size = np.prod(shape)
    assert(size < 256)

    rle_data = np.array([0, 10, 1, 20, 0, size - 30], np.uint8)

    try:
      with tf.io.gfile.GFile(bv_path, 'wb') as fp:
        bv.write_binvox(fp, rle_data, shape, translate, scale)

      with tf.io.gfile.GFile(bv_path, 'rb') as fp:
        out_rle_data, out_shape, out_translate, out_scale = bv.parse_binvox(fp)
    except Exception:
      clean_up()
      raise

    np.testing.assert_array_equal(rle_data, out_rle_data)
    np.testing.assert_array_equal(shape, out_shape)
    np.testing.assert_array_equal(translate, out_translate)
    np.testing.assert_array_equal(scale, out_scale)


if __name__ == '__main__':
  unittest.main()
