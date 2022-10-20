# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Chexpert."""

import collections
import csv
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
CheXpert is a large dataset of chest X-rays and competition for automated chest 
x-ray interpretation, which features uncertainty labels and radiologist-labeled 
reference standard evaluation sets. It consists of 224,316 chest radiographs 
of 65,240 patients, where the chest radiographic examinations and the associated 
radiology reports were retrospectively collected from Stanford Hospital. Each 
report was labeled for the presence of 14 observations as positive, negative, 
or uncertain. We decided on the 14 observations based on the prevalence in the 
reports and clinical relevance.

The CheXpert dataset must be downloaded separately after reading and agreeing 
to a Research Use Agreement. To do so, please follow the instructions on the 
website, https://stanfordmlgroup.github.io/competitions/chexpert/.
"""

_CITATION = """\
@article{DBLP:journals/corr/abs-1901-07031,
  author    = {Jeremy Irvin and Pranav Rajpurkar and Michael Ko and Yifan Yu and Silviana Ciurea{-}Ilcus and Chris Chute and Henrik Marklund and Behzad Haghgoo and Robyn L. Ball and Katie Shpanskaya and Jayne Seekins and David A. Mong and Safwan S. Halabi and Jesse K. Sandberg and Ricky Jones and David B. Larson and Curtis P. Langlotz and Bhavik N. Patel and Matthew P. Lungren and Andrew Y. Ng},
  title     = {CheXpert: {A} Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison},
  journal   = {CoRR},
  volume    = {abs/1901.07031},
  year      = {2019},
  url       = {http://arxiv.org/abs/1901.07031},
  archivePrefix = {arXiv},
  eprint    = {1901.07031},
  timestamp = {Fri, 01 Feb 2019 13:39:59 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-07031},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

# Path to images and category labels in data dir
_DATA_DIR = "CheXpert-v1.0-small"
_TRAIN_DIR = os.path.join(_DATA_DIR, "train")
_VALIDATION_DIR = os.path.join(_DATA_DIR, "valid")
_TRAIN_LABELS_FNAME = os.path.join(_DATA_DIR, "train.csv")
_VALIDATION_LABELS_FNAME = os.path.join(_DATA_DIR, "valid.csv")

# Labels per category
_LABELS = collections.OrderedDict({
    "-1.0": "uncertain",
    "1.0": "positive",
    "0.0": "negative",
    "": "unmentioned",
})


class Chexpert(tfds.core.GeneratorBasedBuilder):
  """CheXpert 2019."""

  VERSION = tfds.core.Version("3.1.0")

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You must register and agree to user agreement on the dataset page:
  https://stanfordmlgroup.github.io/competitions/chexpert/
  Afterwards, you have to put the CheXpert-v1.0-small directory in the
  manual_dir. It should contain subdirectories: train/ and valid/ with images
  and also train.csv and valid.csv files.
  """

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "name":
                tfds.features.Text(),  # patient info
            "image":
                tfds.features.Image(),
            "label":
                tfds.features.Sequence(
                    tfds.features.ClassLabel(names=_LABELS.values())),
            "image_view":
                tfds.features.ClassLabel(names=["frontal", "lateral"]),
        }),
        supervised_keys=("image", "label"),
        homepage="https://stanfordmlgroup.github.io/competitions/chexpert/",
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.manual_dir
    train_path = os.path.join(path, _TRAIN_DIR)
    val_path = os.path.join(path, _VALIDATION_DIR)

    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      msg = ("You must download the dataset folder from CheXpert"
             "website manually and place it into %s." % path)
      raise AssertionError(msg)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "imgs_path": path,  # Relative img path is provided in csv
                "csv_path": os.path.join(path, _TRAIN_LABELS_FNAME)
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "imgs_path": path,
                "csv_path": os.path.join(path, _VALIDATION_LABELS_FNAME)
            },
        ),
    ]

  def _generate_examples(self, imgs_path, csv_path):
    """Yields examples."""
    with epath.Path(csv_path).open() as csv_f:
      reader = csv.DictReader(csv_f)
      # Get keys for each label from csv
      label_keys = reader.fieldnames[5:]
      for row in reader:
        # Get image based on indicated path in csv
        name = row["Path"]
        labels = [_LABELS[row[key]] for key in label_keys]
        image_view = row["Frontal/Lateral"].lower()
        yield name, {
            "name": name,
            "image": os.path.join(imgs_path, name),
            "label": labels,
            "image_view": image_view,
        }
