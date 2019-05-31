# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""PatchCAMELYON."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six.moves.urllib as urllib

import tensorflow_datasets.public_api as tfds

# MNIST constants
_PCAM_URL = "https://github.com/basveeling/pcam"
_CAM_URL = "https://camelyon17.grand-challenge.org/"
_PCAM_TRAIN_DATA_FILENAME = "camelyonpatch_level_2_split_train_x.h5.gz"
_PCAM_TRAIN_LABELS_FILENAME = "camelyonpatch_level_2_split_train_y.h5.gz"
_PCAM_VALID_DATA_FILENAME = "camelyonpatch_level_2_split_valid_x.h5.gz"
_PCAM_VALID_LABELS_FILENAME = "camelyonpatch_level_2_split_valid_y.h5.gz"
_PCAM_TEST_DATA_FILENAME = "camelyonpatch_level_2_split_test_x.h5.gz"
_PCAM_TEST_LABELS_FILENAME = "camelyonpatch_level_2_split_test_y.h5.gz"
_PCAM_IMAGE_SIZE = 96
_PCAM_IMAGE_SHAPE = (_PCAM_IMAGE_SIZE, _PCAM_IMAGE_SIZE, 3)
_TRAIN_EXAMPLES = 262144
_VALID_EXAMPLES = 32768
_TEST_EXAMPLES = 32768

_PCAM_CITATION = """\
@ARTICLE{Veeling2018-qh,
  title         = "Rotation Equivariant {CNNs} for Digital Pathology",
  author        = "Veeling, Bastiaan S and Linmans, Jasper and Winkens, Jim and
                   Cohen, Taco and Welling, Max",
  month         =  jun,
  year          =  2018,
  archivePrefix = "arXiv",
  primaryClass  = "cs.CV",
  eprint        = "1806.03962"
}
"""

_CAM_CITATION = """\
@article{Litjens2018,
    author = {Litjens, G. and Bándi, P. and Ehteshami Bejnordi, B. and Geessink, O. and Balkenhol, M. and Bult, P. and Halilovic, A. and Hermsen, M. and van de Loo, R. and Vogels, R. and Manson, Q.F. and Stathonikos, N. and Baidoshvili, A. and van Diest, P. and Wauters, C. and van Dijk, M. and van der Laak, J.},
    title = {1399 H&E-stained sentinel lymph node sections of breast cancer patients: the CAMELYON dataset},
    journal = {GigaScience},
    volume = {7},
    number = {6},
    year = {2018},
    month = {05},
    issn = {2047-217X},
    doi = {10.1093/gigascience/giy065},
    url = {https://dx.doi.org/10.1093/gigascience/giy065},
    eprint = {http://oup.prod.sis.lan/gigascience/article-pdf/7/6/giy065/25045131/giy065.pdf},
}
"""


class PatchCAMELYON(tfds.core.GeneratorBasedBuilder):
    """PatchCAMELYON"""
    URL = _PCAM_URL
    ZENODO_URL = "https://zenodo.org/record/2546921/files/"

    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=("The PatchCAMELYON dataset for identification of breast cancer metastases in lymph nodes. "
                         "This dataset has been extracted from the larger CAMELYON dataset of 1399 whole-slide images, "
                         "which created for the CAMELYON challenges at ISBI 2016 and 2017."
                         "It contains 96x96 RGB patches of normal lymph node and tumor tissue in a roughly 50/50 "
                         "distributions. It packs the clinically-relevant task of metastasis detection into a "
                         "straight-forward image classification task, akin to CIFAR-10 and MNIST. This increases the "
                         "ease of use by removing the complexity of handling large whole-slide images."),
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(shape=_PCAM_IMAGE_SHAPE),
                "label": tfds.features.ClassLabel(num_classes=2),
            }),
            supervised_keys=("image", "label"),
            urls=[_PCAM_URL, _CAM_URL],
            citation=_PCAM_CITATION + _CAM_CITATION,
        )

    def _split_generators(self, dl_manager):
        # Download the full MNist Database
        filenames = {
            "train_data": _PCAM_TRAIN_DATA_FILENAME,
            "train_labels": _PCAM_TRAIN_LABELS_FILENAME,
            "valid_data": _PCAM_VALID_DATA_FILENAME,
            "valid_labels": _PCAM_VALID_LABELS_FILENAME,
            "test_data": _PCAM_TEST_DATA_FILENAME,
            "test_labels": _PCAM_TEST_LABELS_FILENAME,
        }
        pcam_files = dl_manager.download_and_extract({
            k: urllib.parse.urljoin(self.ZENODO_URL, v) for k, v in filenames.items()
        })

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=32,
                gen_kwargs=dict(
                    data_path=pcam_files["train_data"],
                    label_path=pcam_files["train_labels"],
                )),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=4,
                gen_kwargs=dict(
                    data_path=pcam_files["valid_data"],
                    label_path=pcam_files["valid_labels"],
                )),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=4,
                gen_kwargs=dict(
                    data_path=pcam_files["test_data"],
                    label_path=pcam_files["test_labels"],
                )),
        ]

    def _generate_examples(self, data_path, label_path):
        """Generate PCAM examples as dicts.

        Args:
          data_path (str): Path to the data files
          label_path (str): Path to the labels

        Yields:
          Generator yielding the next examples
        """
        with tfds.core.lazy_imports.h5py.File(data_path) as f_x:
            imgs = f_x['x']
            with tfds.core.lazy_imports.h5py.File(label_path) as f_y:
                lbls = f_y['y'][:,0,0,0]
                data = zip(imgs, lbls)
                for image, label in data:
                    yield {
                        "image": image,
                        "label": label.flatten()[0],
                    }
