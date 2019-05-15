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

"""ModelNet datasets.

The provided `DatasetBuilder`s correspond to the
[base modelnet dataset](http://modelnet.cs.princeton.edu/). The 10-class and
40-class variants are implemented as separate `DatasetBuilder`s to ensure only
the relevant data is downloaded.

These builders provide the greatest versatility in terms of configurations. We
provide 4 base configurations:

* `poly_mesh`: the raw polygon mesh provided in each `.off` file. Because each
face can have any number of vertices, we store `face_values` as a single list
of vertex indices and `face_lengths`. The original face lists can be recovered
using `tf.RaggedTensor.from_row_lengths(face_values, face_lengths)`.
* `tri_mesh`: the original polygon mesh where each face is split into triangular
faces.
* `cloud{N}`, `N in (100, 500)`: sampled surface points with normals.

In the mesh cases (`poly_mesh` and `tri_mesh`), we provide the vertices exactly
as given in the original dataset. These come at different offsets and scales,
so we additionally provide the center and radius of the minimum sphere
containing all points.

For the point clouds, we preprocess the vertices before sampling such that all
points lie within a unit sphere centered at the origin. This is to be consistent
with `ModelnetSampled`. In this case, we also provide the original center
and radius.

For clouds of a different size, you can use
```python
import tensorflow_datasets.volume.modelnet.modelnet as mn

my_num_points = 12345
my_config = mn.PointCloudModelnetConfig(my_num_points)
mn.Modelnet40.BUILDER_CONFIGS.append(my_config)

dataset = tfds.load('modelnet40/cloud%d' % my_num_points)
```

You can implement your own config by extending
`tensorflow_datasets.volume.modelnet.modelnet.ModelnetConfig`, implementing the
`input_features` and `load` methods and constructing via a builder.

```python
import tensorflow_datasets as tfds
import tensorflow_datasets.volume.modelnet.modelnet as mn


class MyModelnetConfig(mn.ModelnetConfig):
  def input_features(self):
    # TODO
    ...

  def load(self, fp, path=None)
    # fp is a file-like object with `.off` encoding.
    # TODO
    ...

my_config = MyModelnetConfig(
    name="my_modelnet_config",
    description="my custom modelnet config",
    input_key="custom_input")


builder = mn.Modelnet40(config=my_config)
builder.download_and_prepare()
datasets = builder.as_dataset()
```

## ModelnetAligned40

Similar to `Modelnet40` but using the aligned version of the dataset. Custom
configs can also be applied here

## ModelnetSampled

The dataset provided by [Pointnet++](http://stanford.edu/~rqi/pointnet2/)
authors consisting of pre-sampled point clouds with normals. Since the download
is the same, we provide the number of classes in separate configs.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import itertools
import os
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core import utils as core_utils
import tensorflow_datasets.public_api as tfds

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import lazy_imports
from tensorflow_datasets.volume.utils import off

_URL_BASE = "http://modelnet.cs.princeton.edu/"
DEFAULT_SEED =  143


def naive_bounding_sphere(points):
  center = (np.min(points, axis=0) + np.max(points, axis=0)) / 2
  radius = np.max(np.linalg.norm(points - center, axis=-1))
  return radius, center


def load_off_data(fp):
  # trimesh doesn't give direct access to the polygon mesh
  data = off.OffObject.from_file(fp)
  vertices = data.vertices.astype(np.float32)
  face_values = data.face_values.astype(np.int64)
  face_lengths = data.face_lengths.astype(np.int64)

  return vertices, face_values, face_lengths


def load_off_mesh(fp):
  vertices, face_values, face_lengths = load_off_data(fp)
  faces = off.triangulated_faces(face_values, face_lengths)
  return vertices, faces


def cloud_features(num_points, with_originals=False):
  features = {
      "positions": tfds.features.Tensor(
        shape=(num_points, 3), dtype=tf.float32),
      "normals": tfds.features.Tensor(
        shape=(num_points, 3), dtype=tf.float32)
    }
  if with_originals:
    features.update({
      "original_center": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
      "original_radius": tfds.features.Tensor(shape=(), dtype=tf.float32),
    })
  return tfds.features.FeaturesDict(features)


class ModelnetConfig(tfds.core.BuilderConfig):
  def __init__(
      self, name, description, input_key, version=core_utils.Version(0, 0, 2),
      **kwargs):
    self.input_key = input_key
    super(ModelnetConfig, self).__init__(
      name=name, description=description, version=version, **kwargs)

  @abc.abstractmethod
  def input_features(self):
    raise NotImplementedError

  @abc.abstractmethod
  def load(self, fp, path=None):
    raise NotImplementedError

  def __enter__(self):
    return self

  def __exit__(self, *args, **kwargs):
    pass


class PolyMeshModelnetConfig(ModelnetConfig):
  def __init__(self, **kwargs):
    super(PolyMeshModelnetConfig, self).__init__(
      name="poly_mesh",
      input_key="mesh",
      description="Polygon mesh",
      **kwargs)

  def input_features(self):
    return tfds.features.FeaturesDict({
        "vertices": tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
        "face_values": tfds.features.Tensor(shape=(None,), dtype=tf.int64),
        "face_lengths": tfds.features.Tensor(shape=(None,), dtype=tf.int64),
    })

  def load(self, fp, path=None):
    vertices, face_values, face_lengths = load_off_data(fp)
    return dict(
      vertices=vertices.astype(np.float32),
      face_values=face_values,
      face_lengths=face_lengths,
    )


class TriMeshModelnetConfig(ModelnetConfig):
  def __init__(self, **kwargs):
    super(TriMeshModelnetConfig, self).__init__(
      name="tri_mesh", input_key="mesh", description="Triangular mesh",
      **kwargs)

  def input_features(self):
    return tfds.features.FeaturesDict({
        "vertices": tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
        "faces": tfds.features.Tensor(shape=(None, 3), dtype=tf.int64),
      })

  def load(self, fp, path=None):
    vertices, faces = load_off_mesh(fp)
    return dict(vertices=vertices, faces=faces)


class PointCloudModelnetConfig(ModelnetConfig):
  def __init__(self, num_points, seed=DEFAULT_SEED, name=None, **kwargs):
    if name is None:
      name = "cloud%d" % num_points
      if seed != DEFAULT_SEED:
        name = '%s-%d' % (name, seed)
    self._seed = seed
    super(PointCloudModelnetConfig, self).__init__(
      name=name,
      description="%d element point cloud" % num_points,
      input_key="cloud", **kwargs)
    self.num_points = num_points
    self._original_state = None

  def input_features(self):
    return cloud_features(self.num_points, with_originals=True)

  def load(self, fp, path=None):
    trimesh = lazy_imports.trimesh
    vertices, faces = load_off_mesh(fp)
    # quick recentering to avoid numerical instabilities in sampling
    center = (np.max(vertices, axis=0) + np.min(vertices, axis=0)) / 2
    vertices -= center
    scale = np.max(vertices)
    vertices /= scale
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)  # pylint: disable=no-member
    positions, face_indices = trimesh.sample.sample_surface( # pylint: disable=no-member
      mesh, self.num_points)
    normals = mesh.face_normals[face_indices]

    r, c = naive_bounding_sphere(positions)
    positions -= c
    positions /= r
    center += c * scale
    scale *= r
    return dict(
      positions=positions.astype(np.float32),
      normals=normals.astype(np.float32),
      original_center=center,
      original_radius=scale,
    )

  def __enter__(self):
    # we rely on trimesh for sampling, but it doesn't allow for user-supplied
    # `RandomContext`s, so we cache the random state, set seed and restore
    # on exit.
    if self._original_state is not None:
      raise RuntimeError("Cannot nest PointCloudModelnetConfig contexts.")
    self._original_state = np.random.get_state()
    np.random.seed(self._seed)
    return self

  def __exit__(self, *args, **kwargs):
    # restore original numpy random state
    assert(self._original_state is not None)
    np.random.set_state(self._original_state)
    self._original_state = None


class ModelnetSampledConfig(tfds.core.BuilderConfig):
  num_points = 10000

  def __init__(self, num_classes, name_prefix="c"):
    """num_classes must be 10 or 40."""
    assert(num_classes in (10, 40))
    self.input_key = "cloud"
    self.num_classes = num_classes
    super(ModelnetSampledConfig, self).__init__(
        name="%s%d" % (name_prefix, num_classes),
        description=(
          "%d-class sampled 1000-point cloud used by PointNet++" % num_classes),
        version=core_utils.Version(0, 0, 1)
    )

  def input_features(self):
    return cloud_features(self.num_points)

  def map_cloud(self, cloud):
    return cloud


def _class_names_path(num_classes):
  return tfds.core.get_tfds_path(os.path.join(
      "volume", "modelnet", "class_names%d.txt" % num_classes))


def _modelnet_info(builder):
  """Shared by Modelnet and ModelnetSampled classes (only method in common)."""
  config = builder.builder_config
  inputs = config.input_features()
  input_key = config.input_key
  example_index = tfds.features.Tensor(shape=(), dtype=tf.int64)
  class_names_path = _class_names_path(builder.num_classes)
  label = tfds.features.ClassLabel(names_file=class_names_path)
  features = tfds.features.FeaturesDict({
    input_key: inputs,
    "label": label,
    "example_index": example_index,
  })
  supervised_keys = (input_key, "label")

  return tfds.core.DatasetInfo(
      builder=builder,
      features=features,
      citation=builder._CITATION,
      supervised_keys=supervised_keys,
      urls=builder.URLS,
  )


class Modelnet10(tfds.core.GeneratorBasedBuilder):
  """Multi-class shape classification."""
  BUILDER_CONFIGS = [
    PolyMeshModelnetConfig(),
    TriMeshModelnetConfig(),
    PointCloudModelnetConfig(num_points=1024),
  ]
  URLS = [_URL_BASE]
  _CITATION = """\
@inproceedings{wu20153d,
  title={3d shapenets: A deep representation for volumetric shapes},
  author={Wu, Zhirong and Song, Shuran and Khosla, Aditya and Yu, Fisher and Zhang, Linguang and Tang, Xiaoou and Xiao, Jianxiong},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={1912--1920},
  year={2015}
}
"""
  _DL_URL = "http://vision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip"

  num_classes = 10

  def _get_archive_resource(self, dl_manager):
    return dl_manager.download(self._DL_URL)

  def _info(self):
    return _modelnet_info(self)

  def _split_generators(self, dl_manager):
    archive_res = self._get_archive_resource(dl_manager)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(
                dl_manager=dl_manager, archive_res=archive_res,
                split_name="train"),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=2,
            gen_kwargs=dict(
                dl_manager=dl_manager, archive_res=archive_res,
                split_name="test"),
        )
    ]

  def _generate_examples(self, dl_manager, archive_res, split_name):
    config = self.builder_config
    input_key = config.input_key

    with config:
      for path, fp in dl_manager.iter_archive(archive_res):
        if not path.endswith(".off"):
          continue
        class_name, split, fn = path.split("/")[-3:]
        if split != split_name:
          continue

        inputs = config.load(fp, path)
        if inputs is not None:
          yield {
            input_key: inputs,
            "example_index": int(fn.split("_")[-1][:-4]) - 1,
            "label": class_name,
          }


# must be a separate class to separate downloads
class Modelnet40(Modelnet10):
  _DL_URL = "http://modelnet.cs.princeton.edu/ModelNet40.zip"
  num_classes = 40



class ModelnetAligned40(Modelnet40):
  URLS = [_URL_BASE, "https://github.com/lmb-freiburg/orion"]
  _CITATION = """\
@InProceedings{SB15,
  author       = "N. Sedaghat and T. Brox",
  title        = "Unsupervised Generation of a Viewpoint Annotated Car Dataset from Videos",
  booktitle    = "IEEE International Conference on Computer Vision (ICCV)",
  year         = "2015",
  url          = "http://lmb.informatik.uni-freiburg.de/Publications/2015/SB15"
}"""

  def _get_archive_resource(self, dl_manager):
    url = "https://lmb.informatik.uni-freiburg.de/resources/datasets/ORION/modelnet40_manually_aligned.tar"
    path = dl_manager.download(url)
    # a cunning disguise...
    res = resource_lib.Resource(
      path=path, extract_method=resource_lib.ExtractMethod.TAR_GZ)
    return res


class ModelnetSampled(tfds.core.GeneratorBasedBuilder):
  URLS = [_URL_BASE, "http://stanford.edu/~rqi/pointnet2/"]
  BUILDER_CONFIGS = [ModelnetSampledConfig(num_classes=n) for n in [10, 40]]
  _CITATION = """\
@article{qi2017pointnetplusplus,
      title={PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space},
      author={Qi, Charles R and Yi, Li and Su, Hao and Guibas, Leonidas J},
      journal={arXiv preprint arXiv:1706.02413},
      year={2017}
    }
"""
  @property
  def num_classes(self):
    return self.builder_config.num_classes

  def _info(self):
    return _modelnet_info(self)

  def _split_generators(self, dl_manager):
    res = "https://shapenet.cs.stanford.edu/media/modelnet40_normal_resampled.zip"
    data_dir = dl_manager.download_and_extract(res)
    data_dir = os.path.join(data_dir, "modelnet40_normal_resampled")
    out = []
    num_classes = self.num_classes
    for split, key, num_shards in (
            (tfds.Split.TRAIN, "train", 4 * num_classes // 10),
            (tfds.Split.TEST, "test", 1 * num_classes // 10),
        ):
      split_path = os.path.join(
        data_dir, "modelnet%d_%s.txt" % (num_classes, key))
      out.append(tfds.core.SplitGenerator(
            name=split,
            num_shards=num_shards,
            gen_kwargs=dict(split_path=split_path, data_dir=data_dir)))
    return out

  def _generate_examples(self, split_path, data_dir):
    with tf.io.gfile.GFile(split_path, "r") as fp:
      example_ids = [l for l in fp.read().split("\n") if l != ""]
    for example_id in example_ids:
      split_id = example_id.split("_")
      label = "_".join(split_id[:-1])
      example_index = int(split_id[-1]) - 1
      path = os.path.join(data_dir, label, "%s.txt" % example_id)
      with tf.io.gfile.GFile(path, "rb") as fp:
        data = np.loadtxt(fp, delimiter=",", dtype=np.float32)
      positions, normals = np.split(data, 2, axis=1)  # pylint: disable=unbalanced-tuple-unpacking
      cloud = dict(positions=positions, normals=normals)
      cloud = self.builder_config.map_cloud(cloud)
      yield dict(cloud=cloud, label=label, example_index=example_index)
