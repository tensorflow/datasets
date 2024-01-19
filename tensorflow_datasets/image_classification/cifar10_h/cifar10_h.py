# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""CIFAR10-H dataset."""

import collections
import os
from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import pandas as pd
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_CIFAR_IMAGE_SIZE = 32
_CIFAR_IMAGE_SHAPE = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)

_DESCRIPTION = """A re-labeled version of CIFAR-10's test set with soft-labels
coming from real human annotators. For every pair (image, label) in the
original CIFAR-10 test set, it provides several additional labels given by real
human annotators as well as the average soft-label. The training set is
identical to the one of the original dataset.
"""

_CITATION = """
@inproceedings{wei2022learning,
  title={Human uncertainty makes classification more robust},
  author={Joshua C. Peterson and Ruairidh M. Battleday and Thomas L. Griffiths
  and Olga Russakovsky},
  booktitle={IEEE International Conference on Computer Vision and Pattern
  Recognition (CVPR)},
  year={2019}
}
"""


class Cifar10H(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for CIFAR-10H dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {"1.0.0": "Initial release."}

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "image": tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
            "soft_label": tfds.features.Tensor(shape=(10,), dtype=np.float32),
            "human_labels": tfds.features.Sequence(
                feature=tfds.features.ClassLabel(num_classes=10)
            ),
            "trial_indices": tfds.features.Sequence(
                feature=tfds.features.Scalar(dtype=np.int32)
            ),
            "annotator_ids": tfds.features.Sequence(
                feature=tfds.features.Scalar(dtype=np.int32)
            ),
            "reaction_times": tfds.features.Sequence(
                feature=tfds.features.Scalar(dtype=np.float32)
            ),
        }),
        supervised_keys=None,
        homepage="https://github.com/jcpeterson/cifar-10h",
        citation=_CITATION,
    )

  @property
  def _cifar_info(self):
    return Cifar10HInfo(
        name=self.name,
        url="https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz",
        human_annotations_url="https://github.com/jcpeterson/cifar-10h/raw/master/data/cifar10h-raw.zip",
        train_files=[
            "data_batch_1.bin",
            "data_batch_2.bin",
            "data_batch_3.bin",
            "data_batch_4.bin",
            "data_batch_5.bin",
        ],
        test_files=["test_batch.bin"],
        prefix="cifar-10-batches-bin/",
        label_files=["batches.meta.txt"],
        label_keys=["label"],
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info

    cifar_path = os.path.join(cifar_path, cifar_info.prefix)

    human_annotations_path = dl_manager.download_and_extract(
        self._cifar_info.human_annotations_url
    )
    human_annotations_file = os.path.join(
        human_annotations_path, "cifar10h-raw.csv"
    )

    # Load the label names
    for label_key, label_file in zip(
        cifar_info.label_keys, cifar_info.label_files
    ):
      labels_path = os.path.join(cifar_path, label_file)
      with epath.Path(labels_path).open() as label_f:
        label_names = [name for name in label_f.read().split("\n") if name]
      self.info.features[label_key].names = label_names

    # Define the splits
    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(cifar_path, f)

    return {
        "train": self._generate_examples(
            "train_",
            gen_filenames(cifar_info.train_files),
            human_annotations_file,
        ),
        "test": self._generate_examples(
            "test_",
            gen_filenames(cifar_info.test_files),
            human_annotations_file,
        ),
    }

  def _generate_examples(self, split_prefix, filepaths, human_annotations_path):
    """Generate CIFAR-10H examples as dicts.

    Uses self._cifar_info as configuration.

    Args:
      split_prefix (str): Prefix that identifies the split (e.g. "train" or
        "test").
      filepaths (list[str]): The files to use to generate the data.
      human_annotations_path (str): Path to human labels and metadata.

    Yields:
      The cifar examples, as defined in the dataset info features.
    """
    label_keys = self._cifar_info.label_keys
    index = 0  # Using index as key since data is always loaded in same order.

    human_annotations = None
    if "test" in split_prefix:
      human_annotations = _load_human_annotations(human_annotations_path)

    for path in filepaths:
      for labels, np_image in _load_data(path, len(label_keys)):
        record = dict(zip(label_keys, labels))
        # Note: "id" is only provided for the user convenience. To shuffle the
        # dataset we use `index`, so that the sharding is compatible with
        # earlier versions.
        record["id"] = "{}{:05d}".format(split_prefix, index)
        record["image"] = np_image

        if "test" in split_prefix:
          record["human_labels"] = _get_field_for_example(
              human_annotations, index, "chosen_label"
          )
          record["reaction_times"] = _get_field_for_example(
              human_annotations, index, "reaction_time"
          )
          record["trial_indices"] = _get_field_for_example(
              human_annotations, index, "trial_index"
          )
          record["annotator_ids"] = _get_field_for_example(
              human_annotations, index, "annotator_id"
          )
          record["soft_label"] = tf.reduce_mean(
              tf.one_hot(record["human_labels"], 10, dtype=np.float32), axis=0
          ).numpy()

        else:
          # There is no annotator data for the train split
          record["human_labels"] = []
          record["reaction_times"] = []
          record["trial_indices"] = []
          record["annotator_ids"] = []
          record["soft_label"] = tf.one_hot(
              record["label"], 10, dtype=np.float32
          ).numpy()

        yield index, record
        index += 1


class Cifar10HInfo(
    collections.namedtuple(
        "_Cifar10HInfo",
        [
            "name",
            "url",
            "human_annotations_url",
            "prefix",
            "train_files",
            "test_files",
            "label_files",
            "label_keys",
        ],
    )
):
  """Contains the information necessary to generate a CIFAR dataset.

  Attributes:
    name (str): name of dataset.
    url (str): data URL.
    human_annotations_url (str): URL of human annotations.
    prefix (str): path prefix within the downloaded and extracted file to look
      for `train_files` and `test_files`.
    train_files (list<str>): name of training files within `prefix`.
    test_files (list<str>): name of test files within `prefix`.
    label_files (list<str>): names of the label files in the data.
    label_keys (list<str>): names of the label keys in the data.
  """


def _load_data(path, labels_number=1):
  """Yields (labels, np_image) tuples."""
  with tf.io.gfile.GFile(path, "rb") as f:
    data = f.read()
  offset = 0
  max_offset = len(data) - 1
  while offset < max_offset:
    labels = np.frombuffer(
        data, dtype=np.uint8, count=labels_number, offset=offset
    ).reshape((labels_number,))
    # 1 byte per label, 1024 * 3 = 3072 bytes for the image.
    offset += labels_number
    img = (
        np.frombuffer(data, dtype=np.uint8, count=3072, offset=offset)
        .reshape((3, _CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE))
        .transpose((1, 2, 0))
    )
    offset += 3072
    yield labels, img


def _load_human_annotations(path):
  """Loads human annotations from a CSV file."""
  data = pd.read_csv(path)
  return data


def _get_field_for_example(data, example_id, field):
  """Loads the values of `field` from all the rows in a pandas dataframe where `cifar10_test_test_idx` is equal to `example_id`."""
  matches_id = data["cifar10_test_test_idx"] == example_id
  return data[matches_id][field].values
