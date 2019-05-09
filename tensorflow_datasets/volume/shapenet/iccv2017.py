from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import tensorflow as tf

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import utils as core_utils
from tensorflow_datasets.volume.shapenet.core import SHAPENET_URL
import json

NUM_OBJECT_CLASSES = 16
NUM_PART_CLASSES = 50

# labels for class i are range(LABEL_SPLITS[i], LABEL_SPLITS[i+1])
LABEL_SPLITS = (
  0,
  4,
  6,
  8,
  12,
  16,
  19,
  22,
  24,
  28,
  30,
  36,
  38,
  41,
  44,
  47,
  50,
)

def part_class_indices(object_class_index):
  return range(
    LABEL_SPLITS[object_class_index],
    LABEL_SPLITS[object_class_index+1],
  )

_CITATION = """\
@article{yi2017large,
  title={Large-scale 3d shape reconstruction and segmentation from shapenet core55},
  author={Yi, Li and Shao, Lin and Savva, Manolis and Huang, Haibin and Zhou, Yang and Wang, Qirui and Graham, Benjamin and Engelcke, Martin and Klokov, Roman and Lempitsky, Victor and others},
  journal={arXiv preprint arXiv:1710.06104},
  year={2017}
}"""

_ICCV2017_URL = "https://shapenet.cs.stanford.edu/iccv17/"

def load_class_names():
  """Load class names and ids.

  Note these are different to the part classes.

  Returns:
    class_names: NUM_OBJECT_CLASSES-length list of class names, e.g. "Airplane"
    class_ids: NUM_OBJECT_CLASSES-length list of class ids, e.g. "02691156"
  """
  path = os.path.join(
      os.path.dirname(__file__), "iccv2017_synsetoffset2category.txt")
  with tf.io.gfile.GFile(path, "r") as fp:
    class_names, class_ids = zip(*(
        l.split("\t") for l in fp.read().split("\n") if l != ""))
  return class_names, class_ids


CLASS_NAMES, CLASS_IDS = load_class_names()


class ShapenetPart2017Config(tfds.core.BuilderConfig):
  def __init__(
      self,
      name_prefix="base",
      version=core_utils.Version("0.0.1"),
      description="point cloud segmentation dataset for iccv2017 challenge",
      class_id=None):
    if class_id is None:
      self.class_index = None
      self.class_id = None
      self.class_name = None
      name = name_prefix
    else:
      if isinstance(class_id, int):
        self.class_name = class_names[class_id]
        self.class_id = class_ids[class_id]
        self.class_index = class_id
      else:
        class_id = class_id.lower()
        for i, (name, id_) in enumerate(zip(CLASS_NAMES, CLASS_IDS)):
          if class_id in (name.lower(), id_):
            self.class_id = id_
            self.class_name = name.lower()
            self.class_index = i
            break
        else:
          raise ValueError('Unrecognized class_id %s' % class_id)
        name = '%s-%s' % (name_prefix, self.class_id)
        description = '%s (%s)' % (description, self.class_name)
    super(ShapenetPart2017Config, self).__init__(
      name=name, version=version, description=description)

  @property
  def cloud_features(self):
    if self.class_index is None:
      num_part_classes = NUM_PART_CLASSES
    else:
      num_part_classes = (
        LABEL_SPLITS[self.class_index+1] - LABEL_SPLITS[self.class_index])
    return tfds.features.SequenceDict({
        "labels": tfds.features.ClassLabel(num_classes=num_part_classes),
        "positions": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
        "normals": tfds.features.Tensor(shape=(3,), dtype=tf.float32)
    })

  def map_cloud(self, cloud):
    return cloud


base_config = ShapenetPart2017Config()


class ShapenetPart2017(tfds.core.GeneratorBasedBuilder):
  URLS = [SHAPENET_URL, _ICCV2017_URL]
  _DL_URL = "https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip"

  BUILDER_CONFIGS = [base_config]

  def _info(self):
    cloud = self.builder_config.cloud_features
    label = tfds.features.ClassLabel(names=CLASS_IDS)
    example_id = tfds.features.Text()
    features = tfds.features.FeaturesDict({
      "label": label,
      "example_id": example_id,
      "cloud": cloud,
    })

    description = "ICCV2017 point cloud segmentation challenge"

    return tfds.core.DatasetInfo(
        builder=self,
        description=description,
        features=features,
        citation=_CITATION,
        supervised_keys=("cloud", "label"),
        urls=self.URLS
    )

  def _split_generators(self, dl_manager):
    data_dir = dl_manager.download_and_extract(self._DL_URL)
    data_dir = os.path.join(
      data_dir, "shapenetcore_partanno_segmentation_benchmark_v0_normal")
    split_dir = os.path.join(data_dir, "train_test_split")

    out = []
    for split, key, num_shards in (
            (tfds.Split.TRAIN, "train", 16),
            (tfds.Split.VALIDATION, "val", 2),
            (tfds.Split.TEST, "test", 4),
        ):
      split_path = os.path.join(split_dir, "shuffled_%s_file_list.json" % key)
      out.append(tfds.core.SplitGenerator(
            name=split,
            num_shards=num_shards,
            gen_kwargs=dict(split_path=split_path, data_dir=data_dir)))
    return out

  def _generate_examples(self, split_path, data_dir):
    config_class_id = self.builder_config.class_id
    config_class_index = self.builder_config.class_index
    label_offset = 0 if config_class_index is None else LABEL_SPLITS[
      config_class_index]

    with tf.io.gfile.GFile(split_path, "rb") as fp:
      subpaths = json.load(fp)
    for subpath in subpaths:
      class_id, example_id = subpath.split("/")[1:]
      if config_class_id is not None and class_id != config_class_id:
        continue
      path = os.path.join(data_dir, class_id, "%s.txt" % example_id)
      with tf.io.gfile.GFile(path, "rb") as fp:
        data = np.loadtxt(fp, dtype=np.float32)
      positions, normals, labels = np.split(data, (3, 6), axis=1)  # pylint: disable=unbalanced-tuple-unpacking
      yield dict(
        cloud=self.builder_config.map_cloud(dict(
            positions=positions,
            normals=normals,
            labels=labels.astype(np.int64) - label_offset
        )),
        label=class_id,
        example_id=example_id
      )
