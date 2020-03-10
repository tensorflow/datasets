# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""QMNIST."""


import codecs
import numpy as np
from six.moves import urllib
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_QMNIST_URL = "https://raw.githubusercontent.com/facebookresearch/qmnist/master/"
_QMNIST_TRAIN_DATA_FILENAME = "qmnist-train-images-idx3-ubyte.gz"
_QMNIST_TRAIN_LABELS_FILENAME = "qmnist-train-labels-idx2-int.gz"
_QMNIST_TEST_DATA_FILENAME = "qmnist-test-images-idx3-ubyte.gz"
_QMNIST_TEST_LABELS_FILENAME = "qmnist-test-labels-idx2-int.gz"
_QMNIST_IMAGE_SIZE = 28
QMNIST_IMAGE_SHAPE = (_QMNIST_IMAGE_SIZE, _QMNIST_IMAGE_SIZE, 1)
QMNIST_NUM_CLASSES = 10
_TRAIN_EXAMPLES = 60000
_TEST_EXAMPLES = 60000




_CITATION = """\
@article{DBLP:journals/corr/abs-1905-10498,
  author    = {Chhavi Yadav and
               L{\'{e}}on Bottou},
  title     = {Cold Case: The Lost {MNIST} Digits},
  journal   = {CoRR},
  volume    = {abs/1905.10498},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.10498},
  archivePrefix = {arXiv},
  eprint    = {1905.10498},
  timestamp = {Mon, 03 Jun 2019 13:42:33 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-10498.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """
The QMNIST dataset was generated from the original data found in the NIST Special Database 19
with the goal to match the MNIST preprocessing as closely as possible.
The exact preprocessing steps used to construct the MNIST dataset have long been lost. 
This leaves us with no reliable way to associate its characters with the ID of the writer 
and little hope to recover the full MNIST testing set that had 60K images but was never released. 
The official MNIST testing set only contains 10K randomly sampled images and is often considered too small 
to provide meaninful confidence intervals.
"""


class Qmnist(tfds.core.GeneratorBasedBuilder):
  """QMNIST."""

  URL = _QMNIST_URL
  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=QMNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=QMNIST_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/facebookresearch/qmnist/blob/master/README.md",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download the full QMNIST Database
    filenames = {
        "train_data": _QMNIST_TRAIN_DATA_FILENAME,
        "train_labels": _QMNIST_TRAIN_LABELS_FILENAME,
        "test_data": _QMNIST_TEST_DATA_FILENAME,
        "test_labels": _QMNIST_TEST_LABELS_FILENAME,
    }
    qmnist_files = dl_manager.download_and_extract(
        {k: urllib.parse.urljoin(self.URL, v) for k, v in filenames.items()})

    # QMNIST provides TRAIN and TEST splits, not a VALIDATION split, so we only
    # write the TRAIN and TEST splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                num_examples=_TRAIN_EXAMPLES,
                data_path=qmnist_files["train_data"],
                label_path=qmnist_files["train_labels"],
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                num_examples=_TEST_EXAMPLES,
                data_path=qmnist_files["test_data"],
                label_path=qmnist_files["test_labels"],
            )),
    ]

  def _generate_examples(self, num_examples, data_path, label_path):
    """Generate QMNIST examples as dicts.

    Args:
      num_examples (int): The number of example.
      data_path (str): Path to the data files
      label_path (str): Path to the labels

    Yields:
      Generator yielding the next examples
    """
    images = _extract_qmnist_images(data_path, num_examples)
    labels = _extract_qmnist_labels(label_path)
    data = list(zip(images, labels))

    # Using index as key since data is always loaded in same order.
    for index, (image, label) in enumerate(data):
      record = {"image": image, "label": label}
      yield index, record


def _extract_qmnist_images(image_filepath, num_images):
  with tf.io.gfile.GFile(image_filepath, "rb") as f:
    f.read(16)
    buf = f.read(_QMNIST_IMAGE_SIZE * _QMNIST_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf,
        dtype=np.uint8,
    ).reshape(num_images, _QMNIST_IMAGE_SIZE, _QMNIST_IMAGE_SIZE, 1)
    return data

def _extract_qmnist_labels(labels_filepath):
  with tf.io.gfile.GFile(labels_filepath, "rb") as f:
    data = f.read()
    assert get_int(data[:4]) == 12*256 + 2
    length = get_int(data[4:8])
    width = get_int(data[8:12])
    labels = np.frombuffer(data, dtype=np.dtype('>i4'), offset=12)
    labels = labels.reshape(length, width).astype(np.dtype('i4'))
    return labels[:, 0]

def get_int(b):
  return int(codecs.encode(b, 'hex'), 16)
