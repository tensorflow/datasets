"""Dataset class for MURA dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://cs.stanford.edu/group/mlgroup/MURA-v1.1.zip"

_DESCRIPTION = ("MURA (musculoskeletal radiographs) is a large dataset of bone"
                "X-rays. Algorithms are tasked with determining whether an "
                "X-ray study is normal or abnormal.")

_TYPES = ["elbow", "finger", "forearm", "hand", "humerus", "shoulder", "wrist"]

_CITATION = """\
@article{rajpurkar2017mura,
  title={MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs},
  author={Rajpurkar, Pranav and Irvin, Jeremy and Bagul, Aarti and Ding, Daisy and Duan, Tony and Mehta, Hershel and Yang, Brandon and Zhu, Kaylie and Laird, Dillon and Ball, Robyn L and others},
  journal={arXiv preprint arXiv:1712.06957},
  year={2017}
}
"""


class Mura(tfds.core.GeneratorBasedBuilder):
  """MURA Image Dataset Class"""

  VERSION = tfds.core.Version('1.0.0',
                              experiments={tfds.core.Experiment.S3: False})

  def _info(self):
    """Define Dataset Info"""

    return tfds.core.DatasetInfo(
        builder=self,

        description=_DESCRIPTION,

        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(None, None, 3)),
            "label": tfds.features.ClassLabel(names=['positive', 'negative']),
            "type": tfds.features.Text(),
        }),

        supervised_keys=("image", "label"),

        urls="https://stanfordmlgroup.github.io/competitions/mura/",

        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    """Define Splits"""
    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name="train",
            num_shards=10,
            gen_kwargs={
                "data_dir_path": os.path.join(path, "train"),
            },
        ),
        tfds.core.SplitGenerator(
            name="valid",
            num_shards=10,
            gen_kwargs={
                "data_dir_path": os.path.join(path, "valid"),
            },
        ),
    ]

  def _generate_examples(self, data_dir_path):
    """Generate images and labels for splits"""

    for type_name_dir in tf.io.gfile.listdir(data_dir_path):
      type_name = type_name_dir.split("_")[1].lower()
      type_name_dir_path = os.path.join(data_dir_path, type_name_dir)
      for patient_dir in tf.io.gfile.listdir(type_name_dir_path):
        patient_dir_path = os.path.join(type_name_dir_path, patient_dir)
        for label_dir in tf.io.gfile.listdir(patient_dir_path):
          label = label_dir.split("_")[1]
          label_dir_path = os.path.join(patient_dir_path, label_dir)
          for image_file in tf.io.gfile.listdir(label_dir_path):
            image = os.path.join(label_dir_path, image_file)

            yield {
                "image": image,
                "label": label,
                "type": type_name,
            }
