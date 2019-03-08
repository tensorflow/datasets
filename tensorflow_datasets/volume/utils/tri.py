"""numpy utility functions for manipulating/converting triangular meshes."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def normalize(x, axis=-1):
  """Divide by the 2-norm in-place. Returns `None`."""
  x /= np.linalg.norm(x, ord=2, axis=axis, keepdims=True)


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


def compute_face_normals(vertices, faces):
  """Compute the outwards facing normal of the triangular mesh.

  Noe the result is not normalized - the magnitude of each row in the returned
  array correspond to twice the area of the corresponding triangular face.

  Args:
    vertices: (num_vertices, 3) float array of vertex coordinates.
    faces: (num_faces, 3) int array of vertex indices making up the triangular
      mesh

  Returns:
    (num_faces, 3) float array of (unnormalized) face normals.
  """
  tris = vertices[faces]
  a, b, c = np.split(tris, (1, 2), axis=-2)  # pylint: disable=unbalanced-tuple-unpacking
  face_normals = np.cross(b - a, c - a)
  return np.squeeze(face_normals, axis=-2)


def compute_vertex_normals(faces, face_normals, num_vertices=None):
  """Compute vertex normals by averaging face normals according to area.

  Note the returned normals are not normalized.

  Args:
    faces: (num_faces, 3) int indices of triangular faces
    face_normals: (num_faces, 3) float array of face normals with magnitudes
      giving the weighting (see `compute_face_normals`).
    num_vertices: number of vertices. If not given, the largest value in
      `faces` is used.

  Returns:
    (num_vertices, 3) float array of (unnormalized) vertex normals.
  """
  if num_vertices is None:
    num_vertices = np.max(faces)
  vertex_normals = np.zeros((num_vertices, 3), dtype=face_normals.dtype)
  for face, normal in zip(faces, face_normals):
    vertex_normals[face] += normal
  return vertex_normals


def sample_barycentric_coordinates(num_samples, dtype=np.float32):
  """Uniformly sample random barycentric coordinates.

  These can be used to interpolate triangular regions uniformly.

  Args:
    num_samples: number of samples to draw.
    dtype: numpy data type of the returned array.

  Returns:
    (num_samples, 3) dtype array of uniformly-sampled barycentric coordinates.
  """
  r0, r1 = np.reshape(
    np.random.uniform(size=2*num_samples), (2, num_samples)).astype(dtype)
  root_r0 = np.sqrt(r0)
  return np.stack([(1 - root_r0), root_r0 * (1 - r1), root_r0 * r1], axis=-1)


def _barycentric_interpolate(values, barycentric_coords):
  """1 value per set of coords."""
  assert(len(values.shape) == len(barycentric_coords.shape) + 1)
  assert(values.shape[-2] == barycentric_coords.shape[-1])
  return np.sum(values * np.expand_dims(barycentric_coords, axis=-1), axis=-2)


def categorical_barycentric_interpolate(
      vertex_values, faces, face_lengths, barycentric_coords):
  """Interpolate values at the vertices.

  Args:
    vertex_values: values to interpolate
    faces: indices of vertices making up triangular faces
    face_lengths: 1D int array of number of points at each face,
      np.sum(face_lengths) == num_interpolated_points
    barycentric_coords: (num_interpolated_points, 3) float
      barycentric coordinates for each interpolated point.

  Returns:
    (num_interpolated_points,) + vertex_values.shape[1:] float values
    corresponding to the interpolation of `vertex_values`.
  """
  faces = np.repeat(faces, face_lengths, axis=0)
  vertex_values = vertex_values[faces]
  return _barycentric_interpolate(vertex_values, barycentric_coords)


def sample_faces(vertices, faces, num_samples, include_normals=True):
  """Sample faces uniformly on a triangular mesh.

  Optionally returns interpolated normals for each point.

  Args:
    vertices: (num_vertices, 3) float array of vertex coordinates
    faces: (num_faces, 3) int array of vertex indices of triangular mesh
    num_samples: number of samples to take
    include_normals: if True, the normals at each point are also calculated
      by interpolating the vertex normals.

  Returns:
    (num_samples, 3) float positions
    (num_samples, 3) float normals (if `include_normals`)
  """
  vertices = np.asarray(vertices)
  if num_samples == 0:
    return np.empty(shape=(0, 3), dtype=vertices.dtype)
  if len(faces) == 0:
    raise ValueError('Cannot sample points from zero faces.')
  face_normals = compute_face_normals(vertices, faces)
  areas = np.linalg.norm(face_normals, ord=2, axis=-1)
  area_total = np.sum(areas)
  if not np.isfinite(area_total):
    raise ValueError('Total area not finite')
  # np.random.multinomial has issues if areas sum greater than 1, even by a bit
  areas /= (area_total * (1 + 1e-5))
  face_lengths = np.random.multinomial(num_samples, areas)
  barycentric_coords = sample_barycentric_coordinates(num_samples)
  points = categorical_barycentric_interpolate(
      vertices, faces, face_lengths, barycentric_coords)
  if include_normals:
    vertex_normals = compute_vertex_normals(
        faces, face_normals, num_vertices=vertices.shape[0])
    normalize(vertex_normals)
    point_normals = categorical_barycentric_interpolate(
        vertex_normals, faces, face_lengths, barycentric_coords)
    normalize(point_normals)
    return face_lengths, barycentric_coords, points, point_normals
  else:
    return face_lengths, barycentric_coords, points
