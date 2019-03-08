from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import tempfile
import numpy as np
from tensorflow_datasets.volume.utils import off


def random_off(num_vertices=10, num_faces=4, min_verts=3, max_verts=5):
  vertices = np.random.normal(size=(num_vertices*3)).reshape((num_vertices, 3))
  face_lengths = np.random.randint(min_verts, max_verts, size=num_faces)
  face_values = np.random.randint(num_vertices, size=np.sum(face_lengths))
  return off.OffObject(vertices, face_values, face_lengths)


class OffObjectTest(unittest.TestCase):
  def test_save_load(self):
    obj = random_off()
    with tempfile.TemporaryFile() as fp:
      obj.to_file(fp)
      fp.seek(0)
      replica = off.OffObject.from_file(fp)
    np.testing.assert_equal(obj.vertices, replica.vertices)
    np.testing.assert_equal(obj.face_values, replica.face_values)
    np.testing.assert_equal(obj.face_lengths, replica.face_lengths)


if __name__ == '__main__':
  unittest.main()
