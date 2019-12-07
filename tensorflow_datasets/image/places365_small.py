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

"""Dataset class for Places365-Standard small(256x256) dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import csv
import os
import six
import six.moves.urllib as urllib
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "http://data.csail.mit.edu/places/places365/"
_TRAIN_URL = "train_256_places365standard.tar"
_TEST_URL = "test_256.tar"
_VALID_URL = "val_256.tar"
_FILE_ANNOTATION_URL = "filelist_places365-standard.tar"

_IMAGE_SHAPE = (256, 256, 3)

_DESCRIPTION = (
    "The Places365-Standard dataset contains 1.8 million train images from 365"
    " scene categories,which are used to train the Places365 CNNs.There are 50"
    " images per category in the validation set and 900 images per category in"
    " the testing set.")

_LABELS_FNAME = "image/categories_places365.txt"

_CITATION = """\

 @article{zhou2017places,
  title={Places: A 10 million Image Database for Scene Recognition},
  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2017},
  publisher={IEEE}
}

"""


class Places365Small(tfds.core.GeneratorBasedBuilder):
  """Places365 Images dataset."""

  VERSION = tfds.core.Version("2.0.0")

  def _info(self):
    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        supervised_keys=("image", "label"),
        homepage="http://places2.csail.mit.edu/",
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    output_files = dl_manager.download_and_extract({
        "train": urllib.parse.urljoin(_BASE_URL, _TRAIN_URL),
        "test": urllib.parse.urljoin(_BASE_URL, _TEST_URL),
        "validation": urllib.parse.urljoin(_BASE_URL, _VALID_URL),
        "annotation": urllib.parse.urljoin(_BASE_URL, _FILE_ANNOTATION_URL),
    })

    return [
        tfds.core.SplitGenerator(
            name="train",
            gen_kwargs={
                "data_dir_path":
                    os.path.join(output_files["train"], "data_256"),
                "annotation_path":
                    os.path.join(output_files["annotation"],
                                 "places365_train_standard.txt"),
                "split_name":
                    "train",
            },
        ),
        tfds.core.SplitGenerator(
            name="test",
            gen_kwargs={
                "data_dir_path":
                    os.path.join(output_files["test"], "test_256"),
                "annotation_path":
                    os.path.join(output_files["annotation"],
                                 "places365_test.txt"),
                "split_name":
                    "test",
            },
        ),
        tfds.core.SplitGenerator(
            name="validation",
            gen_kwargs={
                "data_dir_path":
                    os.path.join(output_files["validation"], "val_256"),
                "annotation_path":
                    os.path.join(output_files["annotation"],
                                 "places365_val.txt"),
                "split_name":
                    "validation",
            },
        ),
    ]

  def _generate_examples(self, data_dir_path, split_name, annotation_path):
    with tf.io.gfile.GFile(annotation_path) as f:
      if split_name == "test":
        # test split doesn't have labels assigned.
        file_to_class = {x[0]: -1 for x in csv.reader(f, delimiter=" ")}
      else:
        file_to_class = {x[0]: int(x[1]) for x in csv.reader(f, delimiter=" ")}

    for filepath, class_id in six.iteritems(file_to_class):
      yield filepath, {
          # it is a "+" instead of os.path.join on purpose.
          # as some annotation file entries contain paths starting with "/"
          "image": os.path.normpath(data_dir_path + "/" + filepath),
          "label": class_id
      }
