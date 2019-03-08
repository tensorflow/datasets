from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import numpy as np
from tensorflow_datasets.volume.utils import tri


class TriTest(unittest.TestCase):
  def test_triangulated_faces(self):
    face_values = np.arange(9, dtype=np.int64)
    face_lengths = np.array([5, 4], dtype=np.int64)
    tri_faces = tri.triangulated_faces(face_values, face_lengths)
    expected = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 4],
        [5, 6, 7],
        [5, 7, 8],
    ])

    np.testing.assert_equal(tri_faces, expected)

  def test_compute_face_normals(self):
    faces = np.array([[0, 1, 2], [0, 2, 1]])
    vertices = np.array([[0, 0, 0], [0, 1, 0], [0, 1, 1]], dtype=np.float32)
    normals = tri.compute_face_normals(vertices, faces)
    np.testing.assert_allclose(normals, [[1, 0, 0], [-1, 0, 0]])
    vertices = 2*vertices
    normals = tri.compute_face_normals(vertices, faces)
    np.testing.assert_allclose(normals, [[4, 0, 0], [-4, 0, 0]])

  def test_compute_vertex_normals(self):
    faces = np.array([[0, 1, 2], [0, 3, 1]])
    vertices = np.array([
      [0, 0, 0],
      [0, 1, 0],
      [0, 1, 1],
      [1, 1, 0]], dtype=np.float32)
    num_vertices = np.shape(vertices)[0]
    face_normals = tri.compute_face_normals(vertices, faces)
    vertex_normals = tri.compute_vertex_normals(
      faces, face_normals, num_vertices)
    np.testing.assert_equal(vertex_normals.shape, vertices.shape)
    np.testing.assert_equal(
      vertex_normals,
      np.array([
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [0, 0, 1],
      ], dtype=np.float32))

  def test_sample_faces(self):
    x_offset = 10
    vertices = np.array([
        [x_offset, 0, 0],
        [x_offset, 0, 2],
        [x_offset, 1, 2],
    ], dtype=np.float32)
    faces = np.array([
        [0, 1, 2]
    ], dtype=np.int64)
    n_points = 1000
    face_lengths, barycentric_coords, points, point_normals = tri.sample_faces(
        vertices, faces, n_points)
    self.assertTrue(np.all(barycentric_coords >= 0))
    self.assertTrue(np.all(barycentric_coords <= 1))
    np.testing.assert_allclose(np.linalg.norm(point_normals, axis=-1), 1)
    np.testing.assert_equal(points.shape, (n_points, 3))
    np.testing.assert_equal(face_lengths, (n_points,))
    x, y, z = points.T
    np.testing.assert_allclose(x, x_offset)
    self.assertTrue(np.all(z >= 2*y))
    self.assertTrue(np.all(y >= 0))
    self.assertTrue(np.all(z <= 2))


if __name__ == '__main__':
  unittest.main()
