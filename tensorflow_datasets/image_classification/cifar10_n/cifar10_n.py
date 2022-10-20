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

"""CIFAR10-N dataset."""

from __future__ import annotations

import collections
import os

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_CIFAR_IMAGE_SIZE = 32
_CIFAR_IMAGE_SHAPE = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)

_DESCRIPTION_10 = """
A re-labeled version of CIFAR-10 with real human annotation errors. For every 
pair (image, label) in the original CIFAR-10 train set, it provides several 
additional labels given by real human annotators. 
"""

_CITATION = """
@inproceedings{wei2022learning,
  title={Learning with Noisy Labels Revisited: A Study Using Real-World Human 
  Annotations},
  author={Jiaheng Wei and Zhaowei Zhu and Hao Cheng and Tongliang Liu and Gang 
  Niu and Yang Liu},
  booktitle={International Conference on Learning Representations},
  year={2022},
  url={https://openreview.net/forum?id=TBWA6PLJZQm}
}
"""


class Cifar10N(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for CIFAR-10N dataset."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Download 'side_info_cifar10N.csv', 'CIFAR-10_human_ordered.npy' and 
  'image_order_c10.npy' from https://github.com/UCSC-REAL/cifar-10-100n.

  Then convert 'CIFAR-10_human_ordered.npy' into a CSV file 
  'CIFAR-10_human_annotations.csv'. This can be done with the following code:

  ```
  import numpy as np
  import pandas as pd
  from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

  human_labels_np_path = '<local_path>/CIFAR-10_human_ordered.npy'
  human_labels_csv_path = '<local_path>/CIFAR-10_human_annotations.csv'

  with tf.io.gfile.GFile(human_labels_np_path, "rb") as f:
    human_annotations = np.load(f, allow_pickle=True)

  df = pd.DataFrame(human_annotations[()])

  with tf.io.gfile.GFile(human_labels_csv_path, "w") as f:
    df.to_csv(f, index=False)
  ```
  """

  VERSION = tfds.core.Version('1.0.4')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.0.1': 'Fixed typo in `worse_label` key.',
      '1.0.2': 'Fixed correspondence between annotations and images.',
      '1.0.3': 'Fixed files in `MANUAL_DIR`.',
      '1.0.4': 'Fixed loading of side information.'
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION_10,
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'image': tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            'label': tfds.features.ClassLabel(num_classes=10),
            'worse_label': tfds.features.ClassLabel(num_classes=10),
            'aggre_label': tfds.features.ClassLabel(num_classes=10),
            'random_label1': tfds.features.ClassLabel(num_classes=10),
            'random_label2': tfds.features.ClassLabel(num_classes=10),
            'random_label3': tfds.features.ClassLabel(num_classes=10),
            'worker1_id': tf.int64,
            'worker1_time': tf.float32,
            'worker2_id': tf.int64,
            'worker2_time': tf.float32,
            'worker3_id': tf.int64,
            'worker3_time': tf.float32,
        }),
        supervised_keys=None,
        homepage='https://ucsc-real.soe.ucsc.edu:1995/Home.html/',
        citation=_CITATION,
    )

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url='https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz',
        train_files=[
            'data_batch_1.bin', 'data_batch_2.bin', 'data_batch_3.bin',
            'data_batch_4.bin', 'data_batch_5.bin'
        ],
        test_files=['test_batch.bin'],
        prefix='cifar-10-batches-bin/',
        label_files=['batches.meta.txt'],
        label_keys=['label'],
        human_label_path='CIFAR-10_human_annotations.csv',
        side_info_path='side_info_cifar10N.csv',
        annotations_order_path='image_order_c10.npy')

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info

    cifar_path = os.path.join(cifar_path, cifar_info.prefix)

    dl_paths = {
        'human_labels':
            dl_manager.manual_dir / cifar_info.human_label_path,
        'side_info':
            dl_manager.manual_dir / cifar_info.side_info_path,
        'annotations_order':
            dl_manager.manual_dir / cifar_info.annotations_order_path,
    }

    # Load the label names
    for label_key, label_file in zip(cifar_info.label_keys,
                                     cifar_info.label_files):
      labels_path = os.path.join(cifar_path, label_file)
      with epath.Path(labels_path).open() as label_f:
        label_names = [name for name in label_f.read().split('\n') if name]
      self.info.features[label_key].names = label_names

    # Define the splits
    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(cifar_path, f)

    return {
        'train':
            self._generate_examples('train_',
                                    gen_filenames(cifar_info.train_files),
                                    dl_paths),
        'test':
            self._generate_examples('test_',
                                    gen_filenames(cifar_info.test_files),
                                    dl_paths),
    }

  def _generate_examples(self, split_prefix, filepaths, dl_paths):
    """Generate CIFAR-10N examples as dicts.

    Uses self._cifar_info as configuration.

    Args:
      split_prefix (str): Prefix that identifies the split (e.g. "tr" or "te").
      filepaths (list[str]): The files to use to generate the data.
      dl_paths (dict[str, str]): Paths to human_labels and side_info

    Yields:
      The cifar examples, as defined in the dataset info features.
    """
    label_keys = self._cifar_info.label_keys
    index = 0  # Using index as key since data is always loaded in same order.

    if 'train' in split_prefix:
      human_labels = _load_human_labels(dl_paths['human_labels'])
      worse_label = human_labels['worse_label']
      aggre_label = human_labels['aggre_label']
      random_label1 = human_labels['random_label1']
      random_label2 = human_labels['random_label2']
      random_label3 = human_labels['random_label3']

      side_info = _load_side_info(dl_paths['side_info'])
      worker1_id = side_info['worker1_id']
      worker1_time = side_info['worker1_time']
      worker2_id = side_info['worker2_id']
      worker2_time = side_info['worker2_time']
      worker3_id = side_info['worker3_id']
      worker3_time = side_info['worker3_time']

      annotations_order = _load_annotations_order(dl_paths['annotations_order'])

    for path in filepaths:
      for labels, np_image in _load_data(path, len(label_keys)):
        record = dict(zip(label_keys, labels))
        # Note: "id" is only provided for the user convenience. To shuffle the
        # dataset we use `index`, so that the sharding is compatible with
        # earlier versions.
        record['id'] = '{}{:05d}'.format(split_prefix, index)
        record['image'] = np_image

        if 'train' in split_prefix:
          # Note: The human labels are provided according to default shuffling
          # of 'cifar10'. We need to invert the shuffling to assign the right
          # human label to each example.
          annotations_index = np.where(annotations_order == index)[0][0]

          record['worse_label'] = worse_label[annotations_index]
          record['aggre_label'] = aggre_label[annotations_index]
          record['random_label1'] = random_label1[annotations_index]
          record['random_label2'] = random_label2[annotations_index]
          record['random_label3'] = random_label3[annotations_index]

          # Worker metadata is shared every 10 samples
          record['worker1_id'] = worker1_id[index // 10]
          record['worker1_time'] = worker1_time[index // 10]
          record['worker2_id'] = worker2_id[index // 10]
          record['worker2_time'] = worker2_time[index // 10]
          record['worker3_id'] = worker3_id[index // 10]
          record['worker3_time'] = worker3_time[index // 10]
        else:
          # There is no annotator metadata for test split
          record['worse_label'] = -1
          record['aggre_label'] = -1
          record['random_label1'] = -1
          record['random_label2'] = -1
          record['random_label3'] = -1

          record['worker1_id'] = -1
          record['worker1_time'] = -1
          record['worker2_id'] = -1
          record['worker2_time'] = -1
          record['worker3_id'] = -1
          record['worker3_time'] = -1

        yield index, record
        index += 1


class CifarInfo(
    collections.namedtuple('_CifarInfo', [
        'name', 'url', 'prefix', 'train_files', 'test_files', 'label_files',
        'label_keys', 'human_label_path', 'side_info_path',
        'annotations_order_path'
    ])):
  """Contains the information necessary to generate a CIFAR dataset.

  Attributes:
    name (str): name of dataset.
    url (str): data URL.
    prefix (str): path prefix within the downloaded and extracted file to look
      for `train_files` and `test_files`.
    train_files (list<str>): name of training files within `prefix`.
    test_files (list<str>): name of test files within `prefix`.
    label_files (list<str>): names of the label files in the data.
    label_keys (list<str>): names of the label keys in the data.
    human_label_path (str): path to human annotations.
    side_info_path (str): path to metadata about annotations.
    annotations_order_path (str): path to annotation-image order correspondence.
  """


def _load_data(path, labels_number=1):
  """Yields (labels, np_image) tuples."""
  with tf.io.gfile.GFile(path, 'rb') as f:
    data = f.read()
  offset = 0
  max_offset = len(data) - 1
  while offset < max_offset:
    labels = np.frombuffer(
        data, dtype=np.uint8, count=labels_number, offset=offset).reshape(
            (labels_number,))
    # 1 byte per label, 1024 * 3 = 3072 bytes for the image.
    offset += labels_number
    img = (
        np.frombuffer(data, dtype=np.uint8, count=3072, offset=offset).reshape(
            (3, _CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE)).transpose((1, 2, 0)))
    offset += 3072
    yield labels, img


def _load_side_info(path):
  """Loads information from side_info_cifar10N.csv."""
  side_info_key_map = {
      1: 'worker1_id',
      2: 'worker1_time',
      3: 'worker2_id',
      4: 'worker2_time',
      5: 'worker3_id',
      6: 'worker3_time'
  }
  side_info_array = np.genfromtxt(
      tf.io.gfile.GFile(path), delimiter=',', skip_header=1)
  side_info = {}
  for key in side_info_key_map:
    side_info[side_info_key_map[key]] = side_info_array[:, key]
  return side_info


def _load_annotations_order(path):
  """Loads index mapping between the annotation files and the CIFAR10 binaries."""
  with tf.io.gfile.GFile(path, 'rb') as f:
    annotations_order = np.load(f)
  return annotations_order


def _load_human_labels(path):
  """Loads information from side_info_cifar10N.csv."""
  human_labels_key_map = {
      1: 'aggre_label',
      2: 'worse_label',
      3: 'random_label1',
      4: 'random_label2',
      5: 'random_label3',
  }
  with tf.io.gfile.GFile(path, 'r') as f:
    human_labels_array = np.genfromtxt(f, delimiter=',', skip_header=1)
  human_labels = {}
  for key in human_labels_key_map:
    human_labels[human_labels_key_map[key]] = human_labels_array[:, key]
  return human_labels
