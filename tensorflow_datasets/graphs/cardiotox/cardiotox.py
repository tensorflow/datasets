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

"""cardiotox dataset."""
import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Drug Cardiotoxicity dataset [1-2] is a molecule classification task to detect
cardiotoxicity caused by binding hERG target, a protein associated with heart
beat rhythm. The data covers over 9000 molecules with hERG activity.

Note:

1. The data is split into four splits: train, test-iid, test-ood1, test-ood2.

2. Each molecule in the dataset has 2D graph annotations which is designed to
facilitate graph neural network modeling. Nodes are the atoms of the molecule
and edges are the bonds. Each atom is represented as a vector encoding basic
atom information such as atom type. Similar logic applies to bonds.

3. We include Tanimoto fingerprint distance (to training data) for each molecule
in the test sets to facilitate research on distributional shift in graph domain.

For each example, the features include:
  atoms: a 2D tensor with shape (60, 27) storing node features. Molecules with
    less than 60 atoms are padded with zeros. Each atom has 27 atom features.
  pairs: a 3D tensor with shape (60, 60, 12) storing edge features. Each edge
    has 12 edge features.
  atom_mask: a 1D tensor with shape (60, ) storing node masks. 1 indicates the
    corresponding atom is real, othewise a padded one.
  pair_mask: a 2D tensor with shape (60, 60) storing edge masks. 1 indicates the
    corresponding edge is real, othewise a padded one.
  active: a one-hot vector indicating if the molecule is toxic or not. [0, 1]
    indicates it's toxic, otherwise [1, 0] non-toxic.


## References
[1]: V. B. Siramshetty et al. Critical Assessment of Artificial Intelligence
Methods for Prediction of hERG Channel Inhibition in the Big Data Era.
    JCIM, 2020. https://pubs.acs.org/doi/10.1021/acs.jcim.0c00884

[2]: K. Han et al. Reliable Graph Neural Networks for Drug Discovery Under
Distributional Shift.
    NeurIPS DistShift Workshop 2021. https://arxiv.org/abs/2111.12951
"""

_CITATION = """
@ARTICLE{Han2021-tu,
  title         = "Reliable Graph Neural Networks for Drug Discovery Under
                   Distributional Shift",
  author        = "Han, Kehang and Lakshminarayanan, Balaji and Liu, Jeremiah",
  month         =  nov,
  year          =  2021,
  archivePrefix = "arXiv",
  primaryClass  = "cs.LG",
  eprint        = "2111.12951"
}

"""

_LABEL_NAME = 'active'
_NODES_FEATURE_NAME = 'atoms'
_EDGES_FEATURE_NAME = 'pairs'
_NODE_MASK_FEATURE_NAME = 'atom_mask'
_EDGE_MASK_FEATURE_NAME = 'pair_mask'
_DISTANCE_TO_TRAIN_NAME = 'dist2topk_nbs'
_EXAMPLE_NAME = 'molecule_id'

_MAX_NODES = 60
_NODE_FEATURE_LENGTH = 27
_EDGE_FEATURE_LENGTH = 12
_NUM_CLASSES = 2

_DATA_URL = tfds.core.gcs_path('downloads/cardiotox')
_FILENAME_TRAIN = 'train_*.tfrecords*'
_FILENAME_VAL = 'test_iid.tfrecords'
_FILENAME_TEST = 'test_ood1.tfrecords'
_FILENAME_TEST2 = 'test_ood2.tfrecords'


class Cardiotox(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for cardiotox dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = {
        _LABEL_NAME: tfds.features.Tensor(shape=[_NUM_CLASSES], dtype=np.int64),
        _NODES_FEATURE_NAME: tfds.features.Tensor(
            shape=[_MAX_NODES, _NODE_FEATURE_LENGTH], dtype=np.float32
        ),
        _EDGES_FEATURE_NAME: tfds.features.Tensor(
            shape=[_MAX_NODES, _MAX_NODES, _EDGE_FEATURE_LENGTH],
            dtype=np.float32,
        ),
        _NODE_MASK_FEATURE_NAME: tfds.features.Tensor(
            shape=[_MAX_NODES], dtype=np.float32
        ),
        _EDGE_MASK_FEATURE_NAME: tfds.features.Tensor(
            shape=[_MAX_NODES, _MAX_NODES], dtype=np.float32
        ),
        _DISTANCE_TO_TRAIN_NAME: tfds.features.Tensor(
            shape=[1], dtype=np.float32
        ),
        _EXAMPLE_NAME: tfds.features.Tensor(shape=[], dtype=np.str_),
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=None,
        homepage='https://github.com/google/uncertainty-baselines/tree/main/baselines/drug_cardiotoxicity',
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(
            max_nodes=_MAX_NODES,
            node_features=_NODE_FEATURE_LENGTH,
            edge_features=_EDGE_FEATURE_LENGTH,
        ),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    return {
        tfds.Split.TRAIN: self._generate_examples(
            os.path.join(_DATA_URL, _FILENAME_TRAIN), is_training=True
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            os.path.join(_DATA_URL, _FILENAME_VAL), is_training=False
        ),
        tfds.Split.TEST: self._generate_examples(
            os.path.join(_DATA_URL, _FILENAME_TEST), is_training=False
        ),
        tfds.Split('test2'): self._generate_examples(
            os.path.join(_DATA_URL, _FILENAME_TEST2), is_training=False
        ),
    }

  def _generate_examples(self, path, is_training):
    """Yields examples."""
    cycle_len = 10 if is_training else 1
    dataset = tf.data.Dataset.list_files(path)
    dataset = dataset.interleave(
        tf.data.TFRecordDataset, cycle_length=cycle_len
    )
    dataset = dataset.map(
        self.info.features.deserialize_example,
        num_parallel_calls=tf.data.experimental.AUTOTUNE,
    )

    dataset = tfds.as_numpy(dataset)
    for example in dataset:
      yield example[_EXAMPLE_NAME], example
