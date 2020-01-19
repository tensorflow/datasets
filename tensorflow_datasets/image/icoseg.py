"""CMU-Cornell iCoseg dataset for image segmentation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings {
title = {iCoseg: Interactive Co-segmentation with Intelligent Scribble Guidance},
author = {D. Batra and A. Kowdle and D. Parikh and J. Luo and T. Chen},
booktitle = {ECCV},
year = {2010} }
"""

_DESCRIPTION = """\
This is the CMU-Cornell iCoseg dataset for image segmentation. The dataset contains 38 different \
groups totalling 643 images. These images also have their respective pixel level groundtruth \
annotations. These groundtruths segment the images into two classes - the subject and the background.
"""

_URL = "http://chenlab.ece.cornell.edu/projects/touch-coseg/CMU_Cornell_iCoseg_dataset.zip"

_HOMEPAGE_URL = "http://chenlab.ece.cornell.edu/projects/touch-coseg/"

class Icoseg(tfds.core.GeneratorBasedBuilder):
  """iCoseg dataset for segmentation."""

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(None, None, 3), encoding_format="jpeg"),
        "label_png": tfds.features.Image(shape=(None, None, 1), encoding_format="png"),
      }),
      supervised_keys=("image", "label_png"),
      homepage=_HOMEPAGE_URL,
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_dir = dl_manager.download_and_extract(_URL)
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        num_shards=4,
        gen_kwargs={
          "imgs_dir_path": os.path.join(extracted_dir, "dataset_public", "images"),
          "labels_dir_path": os.path.join(extracted_dir, "dataset_public", "ground_truth"),
        }
      ),
    ]

  def _generate_examples(self, imgs_dir_path, labels_dir_path):
    for folder in tf.io.gfile.listdir(imgs_dir_path):
      img_dir_path = os.path.join(imgs_dir_path, folder)
      label_dir_path = os.path.join(labels_dir_path, folder)
      for img_name in tf.io.gfile.listdir(img_dir_path):
        if img_name != "Thumbs.db" and img_name != "DS.Store":
          img_path = os.path.join(img_dir_path, img_name)
          no_ext = os.path.splitext(img_name)
          label_img_name = no_ext[0] + ".png"
          label_img_path = os.path.join(label_dir_path, label_img_name)
          features = {
                "image": img_path,
                "label_png": label_img_path,
          }
          yield img_name, features
