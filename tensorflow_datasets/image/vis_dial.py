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

"""Visual Dialog Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
import re
import fnmatch
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{visdial,
  title={{V}isual {D}ialog},
  author={Abhishek Das and Satwik Kottur and Khushi Gupta and Avi Singh
    and Deshraj Yadav and Jos\'e M.F. Moura and Devi Parikh and Dhruv Batra},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2017}
}
"""

_Train_Dialogs = "https://dl.dropboxusercontent.com/s/ix8keeudqrd8hn8/visdial_1.0_train.zip"
_Train_Images = "http://images.cocodataset.org/zips/train2014.zip"
_Validation_Dialogs = "https://dl.dropboxusercontent.com/s/ibs3a0zhw74zisc/visdial_1.0_val.zip"
_Validation_Images = "https://dl.dropboxusercontent.com/s/twmtutniktom7tu/VisualDialog_val2018.zip"
_Test_Dialogs = "https://dl.dropboxusercontent.com/s/o7mucbre2zm7i5n/visdial_1.0_test.zip"
_Test_Images = "https://dl.dropboxusercontent.com/s/mwlrg31hx0430mt/VisualDialog_test2018.zip"


class VisualDialog(tfds.core.GeneratorBasedBuilder):
    """Visual Dialog Dataset"""

    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder = self,
            description="A large set of Images and Dialogs",
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(encoding_format="jpeg"),
                "label": tfds.features.Text(),
            }),
            urls=["https://visualdialog.org/"],
            citation=_CITATION
        )


    def _split_generators(self, dl_manager):

        extracted_json = dl_manager.download_and_extract({
            "Train_Dialogs": _Train_Dialogs,
            "Validation_Dialogs": _Validation_Dialogs,
            "Test_Dialogs": _Test_Dialogs,
        })
        extracted_images = dl_manager.download_and_extract({
            "Train_Images": _Train_Images,
            "Validation_Images": _Validation_Images,
            "Test_Images": _Test_Images,
        })

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=10,
                gen_kwargs={
                    "image": extracted_images,
                    "dialog": extracted_json,
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=10,
                gen_kwargs={
                    "image": extracted_images,
                    "dialog": extracted_json,
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=10,
                gen_kwargs={
                    "image": extracted_images,
                    "dialog": extracted_json,
                }),
        ]

    def _generate_examples(self, image, dialog):
        """Generate examples as dicts.

        Args:
        image: `str`, directory containing the images folder
        dialog: `str`, directory containing dialogs json

        Yields:
        Generator yielding the next samples
        """

        def find(pattern, path):
            result = []
            for root, dirs, files in os.walk(path):
                for name in files:
                    if fnmatch.fnmatch(name, pattern):
                        result.append(os.path.join(root, name))
            return result

        image_filedir = os.path.join(image["Train_Images"],"VisualDialog_train2018")
        dialog_filedir = os.path.join(dialog["Train_Dialogs"],"visdial_1.0_train.json")

        with open(dialog_filedir) as data_file:
            data_f = json.load(data_file)
            for details in data_f["data"]["dialogs"]:
                pattern = '*'+ str(details["image_id"]) + '.jpg'
                image_ = find(pattern, image_filedir.format(details["image_id"]))
                dialog_ = details["dialog"]
                yield {
                    "image": image_,
                    "label": dialog_
                }
