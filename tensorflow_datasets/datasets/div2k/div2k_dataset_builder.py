# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""DIV2K dataset: DIVerse 2K resolution high quality images.

As used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018)
and @ PIRM (ECCV 2018)
"""

import os.path

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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

_DATA_OPTIONS = [
    "bicubic_x2",
    "bicubic_x3",
    "bicubic_x4",
    "bicubic_x8",
    "unknown_x2",
    "unknown_x3",
    "unknown_x4",
    "realistic_mild_x4",
    "realistic_difficult_x4",
    "realistic_wild_x4",
]


class Div2kConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Div2k."""

  def __init__(self, name, **kwargs):
    """Constructs a Div2kConfig."""
    if name not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    description = kwargs.get("description", "Uses %s data." % name)
    kwargs["description"] = description

    super(Div2kConfig, self).__init__(name=name, **kwargs)
    self.data = name
    self.download_urls = {
        "train_lr_url": _DL_URLS["train_" + self.data],
        "valid_lr_url": _DL_URLS["valid_" + self.data],
        "train_hr_url": _DL_URLS["train_hr"],
        "valid_hr_url": _DL_URLS["valid_hr"],
    }


def _make_builder_configs():
  configs = []
  for data in _DATA_OPTIONS:
    configs.append(Div2kConfig(version=tfds.core.Version("2.0.0"), name=data))
  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """DIV2K dataset: DIVerse 2K resolution high quality images."""

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "lr": tfds.features.Image(),
            "hr": tfds.features.Image(),
        }),
        supervised_keys=("lr", "hr"),
        homepage=_DL_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    print("EXTRACTING", self.builder_config.download_urls)
    extracted_paths = dl_manager.download_and_extract(
        self.builder_config.download_urls
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "lr_path": extracted_paths["train_lr_url"],
                "hr_path": os.path.join(
                    extracted_paths["train_hr_url"], "DIV2K_train_HR"
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "lr_path": extracted_paths["valid_lr_url"],
                "hr_path": os.path.join(
                    extracted_paths["valid_hr_url"], "DIV2K_valid_HR"
                ),
            },
        ),
    ]

  def _generate_examples(self, lr_path, hr_path):
    """Yields examples."""
    for root, _, files in tf.io.gfile.walk(lr_path):
      for file_path in files:
        # Select only png files.
        if file_path.endswith(".png"):
          yield file_path, {
              "lr": os.path.join(root, file_path),
              # Extract the image id from the filename: "0001x2.png"
              "hr": os.path.join(hr_path, file_path[:4] + ".png"),
          }
