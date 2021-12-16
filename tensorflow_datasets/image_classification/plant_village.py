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

"""The PlantVillage dataset of healthy and unhealthy leaves."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{DBLP:journals/corr/HughesS15,
  author    = {David P. Hughes and
               Marcel Salath{\'{e}}},
  title     = {An open access repository of images on plant health to enable the
               development of mobile disease diagnostics through machine
               learning and crowdsourcing},
  journal   = {CoRR},
  volume    = {abs/1511.08060},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.08060},
  archivePrefix = {arXiv},
  eprint    = {1511.08060},
  timestamp = {Mon, 13 Aug 2018 16:48:21 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/HughesS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """
The PlantVillage dataset consists of 54303 healthy and unhealthy leaf images
divided into 38 categories by species and disease.

NOTE: The original dataset is not available from the original source
(plantvillage.org), therefore we get the unaugmented dataset from a paper that
used that dataset and republished it. Moreover, we dropped images with
Background_without_leaves label, because these were not present in the original
dataset.

Original paper URL: https://arxiv.org/abs/1511.08060
Dataset URL: https://data.mendeley.com/datasets/tywbtsjrjv/1
"""

_URL = "https://data.mendeley.com/public-files/datasets/tywbtsjrjv/files/d5652a28-c1d8-4b76-97f3-72fb80f94efc/file_downloaded"
_LABELS = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry___healthy",
    "Cherry___Powdery_mildew",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn___Common_rust",
    "Corn___healthy",
    "Corn___Northern_Leaf_Blight",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___healthy",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Potato___Late_blight",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___healthy",
    "Strawberry___Leaf_scorch",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___healthy",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
]


class PlantVillage(tfds.core.GeneratorBasedBuilder):
  """The PlantVillage dataset of healthy and unhealthy leaves."""

  VERSION = tfds.core.Version("1.0.2")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=_LABELS)
        }),
        supervised_keys=("image", "label"),
        homepage="https://arxiv.org/abs/1511.08060",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"datapath": path})
    ]

  def _generate_examples(self, datapath):
    """Yields examples."""
    for label in _LABELS:
      # The real dataset has spaces and commas in directories (label) names,
      # which causes issues with objfs and fig. The solution is to replace these
      # characters with underscores in fake data directories and then not care
      # whether it's an underscore or that character.
      fuzzy_label = label.replace(" ", "[_ ]").replace(",", "[_,]")
      glob_path = os.path.join(
          datapath, "Plant_leave_diseases_dataset_without_augmentation",
          fuzzy_label, "*.[jJ][pP][gG]")
      for fpath in tf.io.gfile.glob(glob_path):
        fname = os.path.basename(fpath)
        record = {
            "image": fpath,
            "image/filename": fname,
            "label": label,
        }
        yield "{}/{}".format(label, fname), record
