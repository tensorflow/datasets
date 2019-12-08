"""DIV2K dataset: DIVerse 2K resolution high quality images as used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import re

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """@InProceedings{Ignatov_2018_ECCV_Workshops,
author = {Ignatov, Andrey and Timofte, Radu and others},
title = {PIRM challenge on perceptual image enhancement on smartphones: report},
booktitle = {European Conference on Computer Vision (ECCV) Workshops},
url = "http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf",
month = {January},
year = {2019}
}
"""

_DESCRIPTION = """
DIV2K dataset: DIVerse 2K resolution high quality images as used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)
"""

_DL_URL = "https://data.vision.ee.ethz.ch/cvl/DIV2K/"

_DL_URLS = {
    "train_hr": _DL_URL + "DIV2K_train_HR.zip",
    "valid_hr": _DL_URL + "DIV2K_valid_HR.zip",
    "train_bicubic_x2": _DL_URL + "DIV2K_train_LR_bicubic_X2.zip",
    "train_unknown_x2": _DL_URL + "DIV2K_train_LR_unknown_X2.zip",
    "valid_bicubic_x2": _DL_URL + "DIV2K_valid_LR_bicubic_X2.zip",
    "valid_unknown_x2": _DL_URL + "DIV2K_valid_LR_unknown_X2.zip",
    "train_bicubic_x3": _DL_URL + "DIV2K_train_LR_bicubic_X3.zip",
    "train_unknown_x3": _DL_URL + "DIV2K_train_LR_unknown_X3.zip",
    "valid_bicubic_x3": _DL_URL + "DIV2K_valid_LR_bicubic_X3.zip",
    "valid_unknown_x3": _DL_URL + "DIV2K_valid_LR_unknown_X3.zip",
    "train_bicubic_x4": _DL_URL + "DIV2K_train_LR_bicubic_X4.zip",
    "train_unknown_x4": _DL_URL + "DIV2K_train_LR_unknown_X4.zip",
    "valid_bicubic_x4": _DL_URL + "DIV2K_valid_LR_bicubic_X4.zip",
    "valid_unknown_x4": _DL_URL + "DIV2K_valid_LR_unknown_X4.zip",
    "train_bicubic_x8": _DL_URL + "DIV2K_train_LR_x8.zip",
    "valid_bicubic_x8": _DL_URL + "DIV2K_valid_LR_x8.zip",
    "train_realistic_mild_x4": _DL_URL + "DIV2K_train_LR_mild.zip",
    "valid_realistic_mild_x4": _DL_URL + "DIV2K_valid_LR_mild.zip",
    "train_realistic_difficult_x4": _DL_URL + "DIV2K_train_LR_difficult.zip",
    "valid_realistic_difficult_x4": _DL_URL + "DIV2K_valid_LR_difficult.zip",
    "train_realistic_wild_x4": _DL_URL + "DIV2K_train_LR_wild.zip",
    "valid_realistic_wild_x4": _DL_URL + "DIV2K_valid_LR_wild.zip",
}

_DATA_OPTIONS = ["bicubic_x2", "bicubic_x3", "bicubic_x4", "bicubic_x8",
                 "unknown_x2", "unknown_x3", "unknown_x4",
                 "realistic_mild_x4", "realistic_difficult_x4",
                 "realistic_wild_x4"]

class Div2kConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Div2k."""

  def __init__(self, data, **kwargs):
    """Constructs a Div2kConfig."""
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    name = kwargs.get("name", data)
    kwargs["name"] = name

    description = kwargs.get("description", "Uses %s data." % data)
    kwargs["description"] = description

    super(Div2kConfig, self).__init__(**kwargs)
    self.data = data

  def download_urls():
    """Returns train and validation download urls for this config."""
    urls = {
        "train_lr_url": _DL_URLS["train_"+self.data],
        "valid_lr_url": _DL_URLS["valid_"+self.data],
        "train_hr_url": _DL_URLS["train_hr"],
        "valid_hr_url": _DL_URLS["valid_hr"],
    }
    return urls

def _make_builder_configs():
  configs = []
  for data in _DATA_OPTIONS:
    configs.append(Div2kConfig(
        version=tfds.core.Version("2.0.0"),
        data=data))
  return configs

class Div2k(tfds.core.GeneratorBasedBuilder):
  """DIV2K dataset: DIVerse 2K resolution high quality images"""

  BUILDER_CONFIGS = _make_builder_configs()
  VERSION = tfds.core.Version("2.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "lr": tfds.features.Image(),
            "hr": tfds.features.Image(),
        }),
        #homepage=_DL_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extracted_paths = dl_manager.download_and_extract(
        self.builder_config.download_urls)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "lr_path": extracted_paths["train_lr_url"],
                "hr_path": extracted_paths["train_hr_url"],
            }
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "lr_path": extracted_paths["valid_lr_url"],
                "hr_path": extracted_paths["valid_hr_url"],
            }
        ),
    ]

  def _generate_examples(self, lr_path, hr_path):
    """Yields examples."""
    if not tf.io.gfile.listdir(hr_path)[0].endswith(".png"):
      hr_path = os.path.join(hr_path, tf.io.gfile.listdir(hr_path)[0])

    for root, _, files in tf.io.gfile.walk(lr_path):
      if len(files):
        for file in files:
          yield root + file, {
              "lr": os.path.join(root, file),
              "hr": os.path.join(hr_path,
                                 re.search(r'\d{4}',
                                           str(file)).group(0) + ".png")
          }
