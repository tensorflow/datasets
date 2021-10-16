# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
"""DIODE: A Dense Indoor and Outdoor Depth Dataset"""
import os

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{diode_dataset,
  title={{DIODE}: {A} {D}ense {I}ndoor and {O}utdoor {DE}pth {D}ataset},
  author={Igor Vasiljevic and Nick Kolkin and Shanyi Zhang and Ruotian Luo and
  Haochen Wang and Falcon Z. Dai and Andrea F. Daniele and Mohammadreza Mostajabi and
  Steven Basart and Matthew R. Walter and Gregory Shakhnarovich},
  journal={CoRR},
  volume={abs/1908.00463},
  year={2019},
  url={http://arxiv.org/abs/1908.00463}
}
"""

_DESCRIPTION = """
This is the dataset for DIODE(Dense Indoor/Outdoor DEpth).
It contains images as .png, depth information per pixel as .npy, and a depth mask as .npy.
The images are kept at their original dimensions(all are 768x1024).
"""


class DiodeDepth(tfds.core.BeamBasedBuilder):
  """DIODE dataset."""

  VERSION = tfds.core.Version("4.4.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict(
            {
                "image": tfds.features.Image(encoding_format="png"),
                "depth": tfds.features.Image(shape=(768, 1024, 1)),
                "depth_mask": tfds.features.Image(shape=(768, 1024, 1)),
            }
        ),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("image", "depth"),
        # Homepage of the dataset for documentation
        homepage="https://diode-dataset.org/",
        # Bibtex citation for the dataset
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    # Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    dl_paths = dl_manager.download_and_extract(
        {
            "train": "http://diode-dataset.s3.amazonaws.com/train.tar.gz",
            "validation": "http://diode-dataset.s3.amazonaws.com/val.tar.gz"
        }
    )

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_directory": dl_paths["train"],
                "indoors_outdoor_all": "all"
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "data_directory": dl_paths["validation"],
                "indoors_outdoor_all": "all"
            },
        ),
    ]

  def _generate_examples(self, data_directory, indoors_outdoor_all):
    image_paths = []
    if indoors_outdoor_all == "all":
      image_paths = tf.io.gfile.glob(
          os.path.join(data_directory, "*/*/*/*.png")
      )
    elif indoors_outdoor_all == "indoors":
      image_paths = tf.io.gfile.glob(
          os.path.join(data_directory, "indoors/*/*/*.png")
      )
    elif indoors_outdoor_all == "outdoor":
      image_paths = tf.io.gfile.glob(
          os.path.join(data_directory, "outdoor/*/*/*.png")
      )
    else:
      raise ValueError(
          f"{indoors_outdoor_all} is not a valid choice for `indoors_outdoor_all`. Choose `indoors`, `outdoor` or `all`."
      )

    for image_path in image_paths:
      depth_path = image_path.replace(".png", "_depth.npy")
      depth_mask_path = image_path.replace(".png", "_depth_mask.npy")
      yield image_path.replace(".png", ""), {
          "image": image_path,
          "depth": np.load(depth_path),
          "depth_mask": np.load(depth_mask_path)
      }
