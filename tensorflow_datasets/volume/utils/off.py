"""Provides `OffObject` for interfacing with `.off` files."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import struct


def _num_edges(face_lengths):
  return sum(face_lengths)


def _parse_off_vertex(line):
  return tuple(float(s) for s in line.split(' '))


def _parse_off_face(line):
  return tuple(int(s) for s in line.split(' ')[1:])


class OffObject(object):
  """Class for loading/saving `.off` files.

  See e.g.
  http://shape.cs.princeton.edu/benchmark/documentation/off_format.html

  General polygonal meshes (a generalization of triangular meshes, where each
  face can have any number of sides) can be expressed using a (num_vertices, 3)
  float array of vertex coordinates and a jagged array of indices. i.e.

  ```python
  jagged_faces = [
      [0, 1, 2, 3],
      [2, 3, 4]
    ]

  ```
  could represent a square with vertices indexed by [0, 1, 2, 3] and another
  triangle with vertices indexed by [2, 3, 4]. Given some 3D vertex coordinate,
  we could get the vertices of the square and triangle as follows.
  ```
  all_vertices = np.random.normal((5, 3))
  square_vertices = all_vertices[jagged_faces[0]]
  tri_vertices = all_vertices[jagged_faces[1]]
  ```

  While nice to think about, manipulating `jagged_arrays` using numpy slicing
  is difficult. Instead, we store the values in `jagged_faces` and the number
  of vertices in each face separately. The above `jagged_faces` would thus be
  ```python
  face_values = [0, 1, 2, 3, 2, 3, 4]
  face_lengths = [4, 3]
  ```

  These are what is parsed/stored in `OffObject` instances.

  ```python
  with open('my_off_file.off', 'rb') as fp:
    off_obj = OffObject.from_file(fp)
  print(off_obj.face_values)  # [0, 1, 2, 3, 2, 3, 4]
  print(off_obj.face_lengths) # [4, 3]
  print(off_obj.vertices)     # (5, 3) float array
  ```

  This is consistent with tensorflows `tf.RaggedTensor.from_row_lengths`

  See also `tensorflow_datasets.volume.utils.tri.trinagulated_faces` to convert
  to a triangular mesh.
  """

  def __init__(self, vertices, face_values, face_lengths, num_edges=None):
    self._num_edges = num_edges
    self._vertices = np.asarray(vertices)
    self._face_values = np.asarray(face_values)
    self._face_lengths = np.asarray(face_lengths)

  @property
  def vertices(self):
    return self._vertices

  @property
  def face_values(self):
    return self._face_values

  @property
  def face_lengths(self):
    return self._face_lengths

  @property
  def num_edges(self):
    if self._num_edges is None:
      self._num_edges = _num_edges(self._face_lengths)
    return self._num_edges

  @property
  def num_vertices(self):
    return len(self.vertices)

  @property
  def num_faces(self):
    return len(self._face_values)

  @staticmethod
  def from_file(fp):
    lines = fp.readlines()
    lines = (l.decode("utf-8") for l in lines)
    lines = (l.rstrip() for l in lines if not l.startswith('#'))
    lines = (l for l in lines if l != '')
    line_iter = iter(lines)
    try:
      line = next(line_iter)
      if line[:3] != 'OFF':
        raise IOError('Invalid .off file: must start with OFF')
      line = line[3:]
      if line == '':
        line = next(line_iter)
    except StopIteration:
      raise IOError('Invalid off file - no header found.')

    # not all num_edges are calculated - often just zero
    # can be calculated from faces lazily
    n_verts, num_faces, _ = (int(i) for i in line.split(' '))
    try:
      vertices = tuple(
          _parse_off_vertex(next(line_iter)) for _ in range(n_verts))
      faces = tuple(
          _parse_off_face(next(line_iter)) for _ in range(num_faces))
    except StopIteration:
      raise IOError('Invalid off file - insufficient number of lines.')
    try:
      next(line_iter)
      raise IOError('Invalid off file - too many lines')
    except StopIteration:
      face_values = np.concatenate(faces, axis=0)
      face_lengths = [len(f) for f in faces]
      return OffObject(vertices, face_values, face_lengths)

  def to_file(self, fp):
    fp.write('OFF\n')
    fp.write('%d %d %d\n' % (self.num_vertices, self.num_faces, self.num_edges))
    for v in self.vertices:
      fp.write('%s\n' % ' '.join(str(vi) for vi in v))
    values = self.face_values

    for face_size in self.face_lengths:
      face, values = np.split(values, (face_size,))  # pylint: disable=unbalanced-tuple-unpacking
      fp.write('%d %s\n' % (len(face), ' '.join(str(fi) for fi in face)))



def triangulated_faces(face_values, face_lengths):
  """Triangulate the polygon mesh defined by face values/lengths.

  face_values and face_lengths encode the jagged array defining the polygon
  faces. For example, the mesh made up of a square with vertices [0, 1, 2, 3]
  and a triangle with vertices indexed by [1, 2, 4] would be given by
  ```python
  face_values = [0, 1, 2, 3, 1, 2, 4]
  face_lengths = [4, 3]
  ```
  i.e. the first 4 entries of `face_values` correspond to the square, and
  `face_values[4:4+3]` correspond to the triangle. We triangulate this by
  splitting the square into 2 triangles, [0, 1, 2] and [0, 2, 3] (note the
  direction is preserved which is important if outwards direction is defined
  by the ordering.
  ```python
  >>> triangulated_faces(face_values, face_lengths)
  # [
  #   [0, 1, 2],  # first half of square
  #   [0, 2, 3],  # second half of square
  #   [1, 2, 4],  # original triangle
  # ]
  ```

  Args:
    face_values: 1D int array of indices of vertices in a single lists
    face_lengths: (num_poly_faces,) int array of number of indices in
      `face_values` corresponding to each face.

  Returns:
    (num_tri_faces, 3) int array of vertex indices for each triangular face.
  """
  n = np.sum(face_lengths) - 2 * len(face_lengths)
  out = np.empty((n, 3), dtype=face_values.dtype)
  faces = np.split(face_values, np.cumsum(face_lengths[:-1]))
  assert(len(faces[-1]) == face_lengths[-1])

  start = 0
  for face in faces:
    end = start + len(face) - 2
    out[start:end, 0] = face[0]
    out[start:end, 1] = face[1:-1]
    out[start:end, 2] = face[2:]
    start = end
  return out
