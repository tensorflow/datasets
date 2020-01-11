
"""
CMU-Cornell iCoseg dataset
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
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
groups totalling 643 images. These images also have there respective pixel level groundtruth \
annotations. These groundtruths segment the images into two classes - the subject and the background.
"""


class Icoseg(tfds.core.GeneratorBasedBuilder):
  """iCoseg dataset for segmentation."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(None, None, 3), encoding_format="jpeg"),
        "label_png": tfds.features.Image(shape=(None, None, 1), encoding_format="png"),
      }),
      supervised_keys=("image", "label_png"),
      homepage="http://chenlab.ece.cornell.edu/projects/touch-coseg/",
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_dir = dl_manager.download_and_extract({
      "iCoseg_dir_path": "http://chenlab.ece.cornell.edu/projects/touch-coseg/CMU_Cornell_iCoseg_dataset.zip"
    })
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        num_shards=4,
        gen_kwargs={
          "imgs_dir_path": os.path.join(extracted_dir["iCoseg_dir_path"], "dataset_public", "images"),
          "label_path": os.path.join(extracted_dir["iCoseg_dir_path"], "dataset_public", "ground_truth"),
        }
      ),
    ]

  def _generate_examples(self, imgs_dir_path, label_path):
    for dir in sorted(os.listdir(imgs_dir_path)):
      img_dir_path = os.path.join(imgs_dir_path, dir)
      label_dir_path = os.path.join(label_path, dir)
      for img_name in sorted(os.listdir(img_dir_path)):
        if str(img_name) == "Thumbs.db" or str(img_name) == "DS.Store":
      	  break
        img_path = os.path.join(img_dir_path, img_name)
        no_ext = os.path.splitext(img_name)
        png = no_ext[0] + ".png"
        png_path = os.path.join(label_dir_path, png)
        features = {
              "image": img_path,
              "label_png": png_path,
        }
        yield img_name, features
