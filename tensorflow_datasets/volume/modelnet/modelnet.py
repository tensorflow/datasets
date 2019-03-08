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

"""ModelNet datasets."""

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
from tensorflow_datasets.volume.utils import off
from tensorflow_datasets.volume.utils import tri

_URL_BASE = "http://modelnet.cs.princeton.edu/"


def _load_off_data(fp):
  data = off.OffObject.from_file(fp)
  vertices = data.vertices.astype(np.float32)
  vertices /= np.max(np.linalg.norm(vertices, axis=-1))  # prevents overflow
  face_values = data.face_values.astype(np.int64)
  face_lengths = data.face_lengths.astype(np.int64)
  return vertices, face_values, face_lengths


def _cloud_features(num_points):
  return tfds.features.FeaturesDict({
      "positions": tfds.features.Tensor(
        shape=(num_points, 3), dtype=tf.float32),
      "normals": tfds.features.Tensor(
        shape=(num_points, 3), dtype=tf.float32)
    })


class ModelnetConfig(tfds.core.BuilderConfig):
  def __init__(
      self, name, description_prefix, input_key=None):
    if input_key is None:
      input_key = name
    self.input_key = input_key
    description = (
      "%s data for ModelNet object dataset" % description_prefix)
    super(ModelnetConfig, self).__init__(
      name=name, description=description, version=core_utils.Version("0.0.1"))

  @abc.abstractmethod
  def input_features(self):
    raise NotImplementedError


class PolyMeshModelnetConfig(ModelnetConfig):
  def __init__(self, **kwargs):
    super(PolyMeshModelnetConfig, self).__init__(
      name="poly_mesh",
      description_prefix="Polygon mesh", **kwargs)

  def input_features(self):
    return tfds.features.FeaturesDict({
        "vertices": tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
        "face_values": tfds.features.Tensor(shape=(None,), dtype=tf.int64),
        "face_lengths": tfds.features.Tensor(shape=(None,), dtype=tf.int64),
    })

  def map(self, vertices, face_values, face_lengths):
    return dict(
      vertices=vertices,
      face_values=face_values,
      face_lengths=face_lengths,
    )


class TriMeshModelnetConfig(ModelnetConfig):
  def __init__(self, **kwargs):
    super(TriMeshModelnetConfig, self).__init__(
      name="tri_mesh", description_prefix="Triangular mesh",
      **kwargs)

  def input_features(self):
    return tfds.features.FeaturesDict({
        "vertices": tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
        "faces": tfds.features.Tensor(shape=(None, 3), dtype=tf.int64),
      })

  def map(self, vertices, face_values, face_lengths):
    faces = tri.triangulated_faces(face_values, face_lengths)
    return dict(vertices=vertices, faces=faces)


class PointCloudModelnetConfig(ModelnetConfig):
  def __init__(self, num_points, **kwargs):
    super(PointCloudModelnetConfig, self).__init__(
      name="cloud%d" % num_points,
      description_prefix="%d element point cloud" % num_points,
      input_key="cloud", **kwargs)
    self.num_points = num_points

  def input_features(self):
    return _cloud_features(self.num_points)

  def map(self, vertices, face_values, face_lengths):
    faces = tri.triangulated_faces(face_values, face_lengths)
    _, _, positions, normals = tri.sample_faces(
        vertices, faces, self.num_points, include_normals=True)
    return dict(positions=positions, normals=normals)


class ModelnetSampledConfig(tfds.core.BuilderConfig):
  num_points = 10000

  def __init__(self, num_classes):
    """num_classes must be 10 or 40."""
    assert(num_classes in (10, 40))
    self.input_key = "cloud"
    self.num_classes = num_classes
    super(ModelnetSampledConfig, self).__init__(
        name="c%d" % num_classes,
        description=(
          "%d-class sampled 1000-point cloud used by PointNet++" % num_classes),
        version=core_utils.Version(0, 0, 1)
    )

  def input_features(self):
    return _cloud_features(self.num_points)


def _class_names_path(num_classes):
  return tfds.core.get_tfds_path(os.path.join(
      "volume", "modelnet", "class_names%d.txt" % num_classes))


def load_class_names(num_classes):
  """Load class names corresponding to the given number of classes.

  Args:
    num_classes: int, one of 10, 40

  Returns:
    list of length `num_classes` with string descriptors corresponding to
    the class indices.
  """
  class_names_path = _class_names_path(num_classes)
  assert(tf.io.gfile.exists(class_names_path))
  with tf.io.gfile.GFile(class_names_path, "rb") as fp:
    class_names = fp.read().split("\n")
  class_names = [c for c in class_names if c != ""]
  assert(len(class_names) == num_classes)
  return class_names


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
    PointCloudModelnetConfig(num_points=100),
    PointCloudModelnetConfig(num_points=5000),
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
    for path, fp in dl_manager.iter_archive(archive_res):
      if not path.endswith(".off"):
        continue
      class_name, split, fn = path.split("/")[-3:]
      if split != split_name:
        continue

      inputs = config.map(*_load_off_data(fp))
      yield {
        input_key: inputs,
        "example_index": int(fn.split("_")[-1][:-4]) - 1,
        "label": class_name,
      }


# must be a separate class to separate downloads
class Modelnet40(Modelnet10):
  _DL_URL = "http://modelnet.cs.princeton.edu/ModelNet40.zip",
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
    with tf.io.gfile.GFile(split_path, "rb") as fp:
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
      yield dict(cloud=cloud, label=label, example_index=example_index)
