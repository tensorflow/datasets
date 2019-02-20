"""Texture tiles from colorectal cancer histology."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds
import random

_URL = "https://zenodo.org/record/53169#.XGZemKwzbmG"
_TILES_DL_URL = "https://zenodo.org/record/53169/files/Kather_texture_2016_image_tiles_5000.zip?download=1"
_LARGE_DL_URL = "https://zenodo.org/record/53169/files/Kather_texture_2016_larger_images_10.zip?download=1"

_TILES_SUBDIR = "Kather_texture_2016_image_tiles_5000"
_LARGE_SUBDIR = "Kather_texture_2016_larger_images_10"

_CLASS_NAMES = (
    "tumor",
    "stroma",
    "complex",
    "lympho",
    "debris",
    "mucosa",
    "adipose",
    "empty",
)
_TILES_SIZE  = 150
_LARGE_SIZE = 5000

_CITATION = """\
@article{kather2016multi,
  title={Multi-class texture analysis in colorectal cancer histology},
  author={Kather, Jakob Nikolas and Weis, Cleo-Aron and Bianconi, Francesco and Melchers, Susanne M and Schad, Lothar R and Gaiser, Timo and Marx, Alexander and Z{\"o}llner, Frank Gerrit},
  journal={Scientific reports},
  volume={6},
  pages={27988},
  year={2016},
  publisher={Nature Publishing Group}
}
"""

def _class_subdir(class_index, class_name):
  return "%02d_%s" % (class_index + 1, class_name.upper())


def _load_tif(path):
  with tf.io.gfile.GFile(path, "rb") as fp:
    image = tfds.core.lazy_imports.PIL_Image.open(fp)
  return np.array(image)


class ColorectalHistology(tfds.core.GeneratorBasedBuilder):
  """Biological 8-class classification problem."""
  URL = _URL
  VERSION = tfds.core.Version("0.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
          "Classification of textures in colorectal cancer histology. "
          "Each example is a 150 x 150 x 3 RGB image of one of 8 classes."),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(_TILES_SIZE,)*2 + (3,)),
            "label": tfds.features.ClassLabel(
                names=_CLASS_NAMES),
            "filename": tfds.features.Text(),
        }),
        urls=[_URL],
        citation=_CITATION,
        supervised_keys=("image", "label"),
    )

  def _split_generators(self, dl_manager):
    folder = dl_manager.download_and_extract(_TILES_DL_URL)
    return [
      tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(root_dir=folder))
    ]

  def _generate_examples(self, root_dir):
    root_dir = os.path.join(root_dir, _TILES_SUBDIR)
    for i, class_name in enumerate(_CLASS_NAMES):
      class_dir = os.path.join(root_dir, _class_subdir(i, class_name))
      fns = tf.io.gfile.listdir(class_dir)
      random.shuffle(fns)
      n = len(fns)
      for fn in fns:
        image = _load_tif(os.path.join(class_dir, fn))
        yield {
            "image": image,
            "label": class_name,
            "filename": fn,
        }


class ColorectalHistologyLarge(tfds.core.GeneratorBasedBuilder):
  """10 Large 5000 x 5000 colorectal histology images without labels."""
  URL = _URL
  VERSION = tfds.core.Version("0.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "10 large 5000 x 5000 textured colorectal cancer histology images"),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(_LARGE_SIZE,)*2 + (3,)),
            "filename": tfds.features.Text(),
        }),
        urls=[_URL],
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    folder = dl_manager.download_and_extract(_LARGE_DL_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(folder=folder)
        )
    ]

  def _generate_examples(self, folder):
    folder = os.path.join(folder, _LARGE_SUBDIR)
    for fn in tf.io.gfile.listdir(folder):
      image = _load_tif(os.path.join(folder, fn))
      yield dict(image=image, filename=fn)
