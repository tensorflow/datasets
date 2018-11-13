# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""DatasetInfo records the information we know about a dataset.

This includes things that we know about the dataset statically, i.e.:
 - schema
 - description
 - canonical location
 - does it have validation and tests splits
 - size
 - etc.

This also includes the things that can and should be computed once we've
processed the dataset as well:
 - number of records (in each split)
 - feature statistics (in each split)
 - etc.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import splits

__all__ = [
    "DatasetInfo",
]

DATASET_INFO_FILENAME = "dataset_info.json"  # TODO(afrozm): Replace by proto


class DatasetInfo(object):
  """Structure defining the info of the dataset.

  Information on the datasets are available through the builder.info property.
  Properties:
    features (FeaturesDict): Information on the feature dict of the
      `tf.data.Dataset()` object from the `builder.as_dataset()` method.
    splits (SplitDict): Available Splits for this dataset

  Note that some of those fields are dynamically computed at data generation
  time (ex: num_samples) and will be updated by update_from_metadata_dir().

  """

  @api_utils.disallow_positional_args
  def __init__(self, features, supervised_keys=None):
    """Constructor of the DatasetInfo.

    Args:
      features: (`tfds.features.FeaturesDict`) Information on the feature dict
        of the `tf.data.Dataset()` object from the `builder.as_dataset()`
        method.
      supervised_keys: (`tuple`) Specifies the input feature and the
        label for supervised learning, if applicable for the dataset.
    """
    self._features = features
    self._splits = splits.SplitDict()
    self._supervised_keys = supervised_keys
    if supervised_keys is not None:
      assert isinstance(supervised_keys, tuple)
      assert len(supervised_keys) == 2
    # TODO(pierrot): Move SIZE here
    # TODO(afrozm): Should add other metadata here (num samples, hash,...)

  @property
  def features(self):
    return self._features

  @property
  def supervised_keys(self):
    return self._supervised_keys

  @property
  def splits(self):
    return self._splits

  # TODO(afrozm): Use proto instead
  def update_from_metadata_dir(self, metadata_dir):
    """Update the DatasetInfo properties from the metadata file.

    This function update all the dynamically generated fields (num_samples,
    hash, time of creation,...) of the DatasetInfo. This reads the metadata
    file on the dataset directory to extract the info and expose them.
    This function is called after the data has been generated in
    .download_and_prepare() and when the data is loaded and already exists.

    This will overwrite all previous metadata.

    Args:
      metadata_dir: (str) The directory containing the metadata file. This
        should be the root directory of a specific dataset version.
    """
    if not metadata_dir:
      raise ValueError(
          "Calling _refresh_metadata while metadata_dir hasn't been defined")

    # Load the metadata from disk
    # TODO(afrozm): Replace by proto
    with tf.gfile.Open(os.path.join(metadata_dir, DATASET_INFO_FILENAME)) as f:
      metadata = json.loads(f.read())

    # Restore the Splits
    self._splits.from_json_data(metadata["splits"])


