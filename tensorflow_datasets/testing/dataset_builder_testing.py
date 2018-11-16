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

"""Base TestCase to test a DatasetBuilder base class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import itertools
import os
import tempfile
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.utils import tf_utils


class TestCase(tf.test.TestCase):
  """Inherit this class to test your DatasetBuilder class.

  You must set the following class attributes:
    DATASET_CLASS: class object of DatasetBuilder you want to test.

  You may set the following class attributes:
    OVERLAPPING_SPLITS: `list[str]`, splits containing records from other splits
      (e.g. a "sample" split containing pictures from other splits).

  This test case will check for the following:
   - the dataset builder is correctly registered, i.e. `tfds.load(name)` works;
   - the dataset builder can read the fake samples stored in
       testing/test_data/fake_samples/${dataset_name};
   - the dataset builder can produce serialized data;
   - the dataset builder produces a valid Dataset object from serialized data
     - in eager mode;
     - in graph mode.
   - the produced Dataset records have the expected dimensions and types;
   - the produced Dataset has and the expected number of records;
   - a record is not part of two splits, or one of these splits is whitelisted
       in OVERLAPPING_SPLITS.
  """

  DATASET_CLASS = None
  OVERLAPPING_SPLITS = []

  @classmethod
  def setUpClass(cls):
    name = cls.__name__
    # Check class has the right attributes
    if cls.DATASET_CLASS is None or not callable(cls.DATASET_CLASS):
      raise AssertionError(
          "Assign your DatasetBuilder class to %s.DATASET_CLASS." % name)

  def setUp(self):
    # get_temp_dir is actually the same for all tests, so create a temp sub-dir.
    data_dir = tempfile.mkdtemp(dir=tf.test.get_temp_dir())
    self.builder = self.DATASET_CLASS(data_dir=data_dir)  # pylint: disable=not-callable
    self.sample_dir = os.path.join(
        os.path.dirname(__file__),
        "test_data/fake_samples/%s" % self.builder.name)

  def test_baseclass(self):
    self.assertIsInstance(
        self.builder, dataset_builder.DatasetBuilder,
        "Dataset class must inherit from `dataset_builder.DatasetBuilder`.")
    # Since class was instantiated and base class is ABCMeta, then we know
    # all needed methods were implemented.

  def test_registered(self):
    self.assertIn(self.builder.name, registered.list_builders(),
                  "Dataset was not registered.")

  def test_info(self):
    self.assertIsInstance(self.builder.info, dataset_info.DatasetInfo)

    info = self.builder.info
    self.assertEquals(self.builder.name, info.name)

  def _check_split(self, dataset):
    """Check given split has right types and shapes."""
    for component, (expected_type, expected_shapes) in self.SPEC.items():
      output_type = dataset.output_types[component]
      self.assertEqual(
          expected_type, output_type,
          "Component %s doesn't have type %s, but %s." %
          (component, expected_type, output_type))
      shapes = dataset.output_shapes[component]
      tf_utils.assert_shape_match(shapes, expected_shapes)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_download_and_prepare_as_dataset(self):
    dl_manager = tf.test.mock.Mock(spec_set=download_manager.DownloadManager)
    dl_manager.download_and_extract.return_value = self.sample_dir
    dl_manager.extract.return_value = self.sample_dir
    dl_manager.manual_dir = self.sample_dir
    self.builder.download_and_prepare(dl_manager=dl_manager,
                                      compute_stats=False)

    split_to_checksums = {}  # {"split": set(records_checksums)}
    for split_name, expected_records_number in self.SPLITS.items():
      dataset = self.builder.as_dataset(split=split_name)
      self._check_split(dataset)
      records = list(self.builder.numpy_iterator(split=split_name))
      split_to_checksums[split_name] = set(checksum(rec) for rec in records)
      self.assertEqual(len(records), expected_records_number)
    for (split1, hashes1), (split2, hashes2) in itertools.combinations(
        split_to_checksums.items(), 2):
      if split1 in self.OVERLAPPING_SPLITS or split2 in self.OVERLAPPING_SPLITS:
        continue
      self.assertFalse(
          hashes1.intersection(hashes2),
          ("Splits '%s' and '%s' are overlapping. Are you sure you want to have"
           " the same objects in those splits? If yes, add one one of them to "
           "OVERLAPPING_SPLITS class attribute.") % (split1, split2))


def checksum(record):
  hash_ = hashlib.md5()
  for key, val in sorted(record.items()):
    hash_.update(key.encode("utf-8"))
    hash_.update(val)
  return hash_.hexdigest()


main = tf.test.main
