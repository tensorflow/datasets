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

"""Oxford 102 Category Flower Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_BASE_URL = "https://www.robots.ox.ac.uk/~vgg/data/flowers/102/"

_CITATION = """\
@InProceedings{Nilsback08,
   author = "Nilsback, M-E. and Zisserman, A.",
   title = "Automated Flower Classification over a Large Number of Classes",
   booktitle = "Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing",
   year = "2008",
   month = "Dec"
}
"""

_DESCRIPTION = """
The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly occurring
in the United Kingdom. Each class consists of between 40 and 258 images. The images have
large scale, pose and light variations. In addition, there are categories that have large
variations within the category and several very similar categories.

The dataset is divided into a training set, a validation set and a test set.
The training set and validation set each consist of 10 images per class (totalling 1030 images each).
The test set consist of the remaining 6129 images (minimum 20 per class).
"""


class OxfordFlowers102(tfds.core.GeneratorBasedBuilder):
  """Oxford 102 category flower dataset."""

  VERSION = tfds.core.Version("0.0.1")  # Version 1.1 of oxford flowers 102.

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(num_classes=102),
            "file_name": tfds.features.Text(),
        }),
        supervised_keys=("image", "label"),
        urls=[_BASE_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download images and annotations that come in separate archives.
    # Note, that the extension of archives is .tar.gz even though the actual
    # archives format is uncompressed tar.
    dl_paths = dl_manager.download_and_extract({
        "images": tfds.download.Resource(
            url=os.path.join(_BASE_URL, "102flowers.tgz"),
            extract_method=tfds.download.ExtractMethod.TAR),
        "labels": os.path.join(_BASE_URL, "imagelabels.mat"),
        "setid": os.path.join(_BASE_URL, "setid.mat"),
    })

    gen_kwargs = dict(
        images_dir_path=os.path.join(dl_paths["images"], "jpg"),
        labels_path=dl_paths["labels"],
        setid_path=dl_paths["setid"],
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs=dict(split_name="trnid", **gen_kwargs)),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(split_name="tstid", **gen_kwargs)),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs=dict(split_name="valid", **gen_kwargs)),
    ]

  def _generate_examples(self, images_dir_path, labels_path, setid_path,
                         split_name):
    """Yields examples."""
    with tf.io.gfile.GFile(labels_path, "rb") as f:
      labels = tfds.core.lazy_imports.scipy.io.loadmat(f)["labels"][0]
    with tf.io.gfile.GFile(setid_path, "rb") as f:
      examples = tfds.core.lazy_imports.scipy.io.loadmat(f)[split_name][0]

    for image_id in examples:
      file_name = "image_%05d.jpg" % image_id
      yield {
          "image": os.path.join(images_dir_path, file_name),
          "label": labels[image_id - 1] - 1,
          "file_name": file_name,
      }
