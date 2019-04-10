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

"""Tests for tensorflow_datasets.core.dataset_info."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
import tempfile
import numpy as np
import tensorflow as tf
from tensorflow_data_validation.utils import test_util
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.image import mnist

from google.protobuf import text_format
from tensorflow_metadata.proto.v0 import schema_pb2
from tensorflow_metadata.proto.v0 import statistics_pb2

tf.compat.v1.enable_eager_execution()

_TFDS_DIR = py_utils.tfds_dir()
_INFO_DIR = os.path.join(_TFDS_DIR, "testing", "test_data", "dataset_info",
                         "mnist", "1.0.0")
_INFO_DIR_UNLABELED = os.path.join(_TFDS_DIR, "testing", "test_data",
                                   "dataset_info", "mnist_unlabeled", "1.0.0")
_NON_EXISTENT_DIR = os.path.join(_TFDS_DIR, "non_existent_dir")


DummyDatasetSharedGenerator = testing.DummyDatasetSharedGenerator


class RandomShapedImageGenerator(DummyDatasetSharedGenerator):

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"im": features.Image()}),
        supervised_keys=("im", "im"),
    )

  def _generate_examples(self):
    for _ in range(30):
      height = np.random.randint(5, high=10)
      width = np.random.randint(5, high=10)
      yield {
          "im":
              np.random.randint(
                  0, 255, size=(height, width, 3), dtype=np.uint8)
      }


class DatasetInfoTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetInfoTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls._builder = DummyDatasetSharedGenerator(data_dir=cls._tfds_tmp_dir)

  @classmethod
  def tearDownClass(cls):
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def test_undefined_dir(self):
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             "undefined dataset_info_dir"):
      info = dataset_info.DatasetInfo(builder=self._builder)
      info.read_from_directory(None)

  def test_non_existent_dir(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    with self.assertRaisesWithPredicateMatch(
        tf.errors.NotFoundError, "No such file or dir"):
      info.read_from_directory(_NON_EXISTENT_DIR)

  def test_reading(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR)

    # Assert that we read the file and initialized DatasetInfo.
    self.assertTrue(info.initialized)
    self.assertEqual("dummy_dataset_shared_generator", info.name)
    self.assertEqual("dummy_dataset_shared_generator/1.0.0", info.full_name)

    # Test splits are initialized properly.
    split_dict = info.splits

    # Assert they are the correct number.
    self.assertTrue(len(split_dict), 2)

    # Assert on what they are
    self.assertTrue("train" in split_dict)
    self.assertTrue("test" in split_dict)

    # Assert that this is computed correctly.
    self.assertEqual(70000, info.splits.total_num_examples)

    self.assertEqual("image", info.supervised_keys[0])
    self.assertEqual("label", info.supervised_keys[1])

  def test_reading_empty_properties(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR_UNLABELED)

    # Assert supervised_keys has not been set
    self.assertEqual(None, info.supervised_keys)

  def test_writing(self):
    # First read in stuff.
    mnist_builder = mnist.MNIST(
        data_dir=tempfile.mkdtemp(dir=self.get_temp_dir()))

    info = dataset_info.DatasetInfo(builder=mnist_builder)
    info.read_from_directory(_INFO_DIR)

    # Read the json file into a string.
    with tf.io.gfile.GFile(info._dataset_info_filename(_INFO_DIR)) as f:
      existing_json = json.load(f)

    # Now write to a temp directory.
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      info.write_to_directory(tmp_dir)

      # Read the newly written json file into a string.
      with tf.io.gfile.GFile(info._dataset_info_filename(tmp_dir)) as f:
        new_json = json.load(f)

      # Read the newly written LICENSE file into a string.
      with tf.io.gfile.GFile(info._license_filename(tmp_dir)) as f:
        license_ = f.read()

    # Assert what was read and then written and read again is the same.
    self.assertEqual(existing_json, new_json)

    # Assert correct license was written.
    self.assertEqual(existing_json["redistributionInfo"]["license"], license_)

  def test_restore_after_modification(self):
    # Create a DatasetInfo
    info = dataset_info.DatasetInfo(
        builder=self._builder,
        description="A description",
        supervised_keys=("input", "output"),
        urls=["some location"],
        citation="some citation",
        redistribution_info={"license": "some license"}
    )
    info.size_in_bytes = 456
    info.as_proto.schema.feature.add()
    info.as_proto.schema.feature.add()  # Add dynamic statistics
    info.download_checksums = {
        "url1": "some checksum",
        "url2": "some other checksum",
    }

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are not defined, then everything is restored from disk
      restored_info = dataset_info.DatasetInfo(builder=self._builder)
      restored_info.read_from_directory(tmp_dir)
      self.assertEqual(info.as_proto, restored_info.as_proto)

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are defined, then the code version is kept
      restored_info = dataset_info.DatasetInfo(
          builder=self._builder,
          supervised_keys=("input (new)", "output (new)"),
          urls=["some location (new)"],
          citation="some citation (new)",
          redistribution_info={"license": "some license (new)"}
      )
      restored_info.size_in_bytes = 789
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()  # Add dynamic statistics
      restored_info.download_checksums = {
          "url2": "some other checksum (new)",
          "url3": "some checksum (new)",
      }

      restored_info.read_from_directory(tmp_dir)

      # Even though restored_info has been restored, informations defined in
      # the code overwrite informations from the json file.
      self.assertEqual(restored_info.description, "A description")
      self.assertEqual(
          restored_info.supervised_keys, ("input (new)", "output (new)"))
      self.assertEqual(restored_info.urls, ["some location (new)"])
      self.assertEqual(restored_info.citation, "some citation (new)")
      self.assertEqual(restored_info.redistribution_info.license,
                       "some license (new)")
      self.assertEqual(restored_info.size_in_bytes, 789)
      self.assertEqual(len(restored_info.as_proto.schema.feature), 4)
      self.assertEqual(restored_info.download_checksums, {
          "url2": "some other checksum (new)",
          "url3": "some checksum (new)",
      })

  def test_reading_from_gcs_bucket(self):
    # The base TestCase prevents GCS access, so we explicitly ask it to restore
    # access here.
    with self.gcs_access():
      mnist_builder = mnist.MNIST(
          data_dir=tempfile.mkdtemp(dir=self.get_temp_dir()))
      info = dataset_info.DatasetInfo(builder=mnist_builder)
      info = mnist_builder.info

      # A nominal check to see if we read it.
      self.assertTrue(info.initialized)
      self.assertEqual(10000, info.splits["test"].num_examples)

  def test_str_smoke(self):
    info = mnist.MNIST(data_dir="/tmp/some_dummy_dir").info
    _ = str(info)

  @testing.run_in_graph_and_eager_modes()
  def test_statistics_generation(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()

      # Overall
      self.assertEqual(30, builder.info.splits.total_num_examples)

      # Per split.
      test_split = builder.info.splits["test"].get_proto()
      train_split = builder.info.splits["train"].get_proto()
      expected_train_stats = text_format.Parse("""
num_examples: 20
features {
  name: "x"
  num_stats {
    common_stats {
      num_non_missing: 20
      min_num_values: 1
      max_num_values: 1
      avg_num_values: 1.0
      num_values_histogram {
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 2.0
        }
        type: QUANTILES
      }
      tot_num_values: 20
    }
    mean: 14.0
    std_dev: 8.63133825082
    num_zeros: 1
    median: 15.0
    max: 28.0
    histograms {
      buckets {
        high_value: 2.8
        sample_count: 1.998
      }
      buckets {
        low_value: 2.8
        high_value: 5.6
        sample_count: 1.998
      }
      buckets {
        low_value: 5.6
        high_value: 8.4
        sample_count: 1.998
      }
      buckets {
        low_value: 8.4
        high_value: 11.2
        sample_count: 1.998
      }
      buckets {
        low_value: 11.2
        high_value: 14.0
        sample_count: 1.998
      }
      buckets {
        low_value: 14.0
        high_value: 16.8
        sample_count: 1.998
      }
      buckets {
        low_value: 16.8
        high_value: 19.6
        sample_count: 1.998
      }
      buckets {
        low_value: 19.6
        high_value: 22.4
        sample_count: 1.998
      }
      buckets {
        low_value: 22.4
        high_value: 25.2
        sample_count: 1.998
      }
      buckets {
        low_value: 25.2
        high_value: 28.0
        sample_count: 2.018
      }
    }
    histograms {
      buckets {
        high_value: 3.0
        sample_count: 2.0
      }
      buckets {
        low_value: 3.0
        high_value: 6.0
        sample_count: 2.0
      }
      buckets {
        low_value: 6.0
        high_value: 9.0
        sample_count: 2.0
      }
      buckets {
        low_value: 9.0
        high_value: 12.0
        sample_count: 2.0
      }
      buckets {
        low_value: 12.0
        high_value: 15.0
        sample_count: 2.0
      }
      buckets {
        low_value: 15.0
        high_value: 18.0
        sample_count: 2.0
      }
      buckets {
        low_value: 18.0
        high_value: 21.0
        sample_count: 2.0
      }
      buckets {
        low_value: 21.0
        high_value: 24.0
        sample_count: 2.0
      }
      buckets {
        low_value: 24.0
        high_value: 27.0
        sample_count: 2.0
      }
      buckets {
        low_value: 27.0
        high_value: 28.0
        sample_count: 2.0
      }
      type: QUANTILES
    }
  }
}""", statistics_pb2.DatasetFeatureStatistics())
      expected_test_stats = text_format.Parse("""
num_examples: 10
features {
  name: "x"
  num_stats {
    common_stats {
      num_non_missing: 10
      min_num_values: 1
      max_num_values: 1
      avg_num_values: 1.0
      num_values_histogram {
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        buckets {
          low_value: 1.0
          high_value: 1.0
          sample_count: 1.0
        }
        type: QUANTILES
      }
      tot_num_values: 10
    }
    mean: 15.5
    std_dev: 8.61684396981
    min: 2.0
    median: 17.0
    max: 29.0
    histograms {
      buckets {
        low_value: 2.0
        high_value: 4.7
        sample_count: 0.999
      }
      buckets {
        low_value: 4.7
        high_value: 7.4
        sample_count: 0.999
      }
      buckets {
        low_value: 7.4
        high_value: 10.1
        sample_count: 0.999
      }
      buckets {
        low_value: 10.1
        high_value: 12.8
        sample_count: 0.999
      }
      buckets {
        low_value: 12.8
        high_value: 15.5
        sample_count: 0.999
      }
      buckets {
        low_value: 15.5
        high_value: 18.2
        sample_count: 0.999
      }
      buckets {
        low_value: 18.2
        high_value: 20.9
        sample_count: 0.999
      }
      buckets {
        low_value: 20.9
        high_value: 23.6
        sample_count: 0.999
      }
      buckets {
        low_value: 23.6
        high_value: 26.3
        sample_count: 0.999
      }
      buckets {
        low_value: 26.3
        high_value: 29.0
        sample_count: 1.009
      }
    }
    histograms {
      buckets {
        low_value: 2.0
        high_value: 5.0
        sample_count: 1.0
      }
      buckets {
        low_value: 5.0
        high_value: 8.0
        sample_count: 1.0
      }
      buckets {
        low_value: 8.0
        high_value: 11.0
        sample_count: 1.0
      }
      buckets {
        low_value: 11.0
        high_value: 14.0
        sample_count: 1.0
      }
      buckets {
        low_value: 14.0
        high_value: 17.0
        sample_count: 1.0
      }
      buckets {
        low_value: 17.0
        high_value: 20.0
        sample_count: 1.0
      }
      buckets {
        low_value: 20.0
        high_value: 23.0
        sample_count: 1.0
      }
      buckets {
        low_value: 23.0
        high_value: 26.0
        sample_count: 1.0
      }
      buckets {
        low_value: 26.0
        high_value: 29.0
        sample_count: 1.0
      }
      buckets {
        low_value: 29.0
        high_value: 29.0
        sample_count: 1.0
      }
      type: QUANTILES
    }
  }
}""", statistics_pb2.DatasetFeatureStatistics())
      expected_schema = text_format.Parse("""
feature {
  name: "x"
  type: INT
  presence {
    min_fraction: 1.0
    min_count: 1
  }
  shape {
    dim {
      size: 1
    }
  }
}""", schema_pb2.Schema())

      test_util.assert_dataset_feature_stats_proto_equal(
          self, train_split.statistics, expected_train_stats)
      test_util.assert_dataset_feature_stats_proto_equal(
          self, test_split.statistics, expected_test_stats)
      self.assertEqual(builder.info.as_proto.schema, expected_schema)

  @testing.run_in_graph_and_eager_modes()
  def test_schema_generation_variable_sizes(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = RandomShapedImageGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()

      expected_schema = text_format.Parse(
          """
feature {
  name: "im"
  type: BYTES
  presence {
    min_fraction: 1.0
    min_count: 1
  }
  shape {
    dim {
      size: -1
    }
    dim {
      size: -1
    }
    dim {
      size: 3
    }
  }
}""", schema_pb2.Schema())
      self.assertEqual(builder.info.as_proto.schema, expected_schema)

  def test_updates_on_bucket_info(self):

    info = dataset_info.DatasetInfo(builder=self._builder,
                                    description="won't be updated")
    # No statistics in the above.
    self.assertEqual(0, info.splits.total_num_examples)
    self.assertEqual(0, len(info.as_proto.schema.feature))

    # Partial update will happen here.
    info.read_from_directory(_INFO_DIR)

    # Assert that description (things specified in the code) didn't change
    # but statistics are updated.
    self.assertEqual("won't be updated", info.description)

    # These are dynamically computed, so will be updated.
    self.assertEqual(70000, info.splits.total_num_examples)
    self.assertEqual(2, len(info.as_proto.schema.feature))


if __name__ == "__main__":
  testing.test_main()
