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
  with tf.io.gfile.GFile(path, "rb") as fp:
    class_names, class_ids = zip(*(
        l.split("\t") for l in fp.read().split("\n") if l != ""))
  return class_names, class_ids


class ShapenetPart2017(tfds.core.GeneratorBasedBuilder):
  URLS = [SHAPENET_URL, _ICCV2017_URL]
  _DL_URL = "https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip"
  VERSION = core_utils.Version("0.0.1")

  def _info(self):
    _, class_ids = load_class_names()
    cloud = tfds.features.SequenceDict({
        "labels": tfds.features.ClassLabel(num_classes=NUM_PART_CLASSES),
        "positions": tfds.features.Tensor(shape=(3,), dtype=tf.float32),
        "normals": tfds.features.Tensor(shape=(3,), dtype=tf.float32)
    })
    label = tfds.features.ClassLabel(names=class_ids)
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
    with tf.io.gfile.GFile(split_path, "rb") as fp:
      subpaths = json.load(fp)
    for subpath in subpaths:
      class_id, example_id = subpath.split("/")[1:]
      path = os.path.join(data_dir, class_id, "%s.txt" % example_id)
      with tf.io.gfile.GFile(path, "rb") as fp:
        data = np.loadtxt(fp, dtype=np.float32)
      positions, normals, labels = np.split(data, (3, 6), axis=1)  # pylint: disable=unbalanced-tuple-unpacking
      yield dict(
        cloud=dict(
            positions=positions,
            normals=normals,
            labels=labels.astype(np.int64)
        ),
        label=class_id,
        example_id=example_id
      )
