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

"""Test utilities."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import os
import tempfile

import tensorflow as tf

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter


@contextlib.contextmanager
def tmp_dir(dirname=None):
  tmp = make_tmp_dir(dirname)
  yield tmp
  rm_tmp_dir(tmp)


def make_tmp_dir(dirname=None):
  if dirname and not tf.gfile.Exists(dirname):
    tf.gfile.MakeDirs(dirname)
  return tempfile.mkdtemp(dir=dirname)


def rm_tmp_dir(dirname):
  tf.gfile.DeleteRecursively(dirname)


class FeatureExpectationItem(object):
  """Test item of a FeatureExpectation."""

  def __init__(
      self,
      value,
      expected=None,
      expected_serialized=None,
      raise_cls=None,
      raise_msg=None):
    self.value = value
    self.expected = expected
    self.expected_serialized = expected_serialized
    self.raise_cls = raise_cls
    self.raise_msg = raise_msg


class FeatureExpectation(object):
  """Object defining a featureConnector test."""

  def __init__(
      self,
      name,
      feature,
      shape,
      dtype,
      tests,
      serialized_features=None):
    self.name = name
    self.feature = feature
    self.shape = shape
    self.dtype = dtype
    self.tests = tests
    self.serialized_features = serialized_features


class FeatureExpectationsTestCase(tf.test.TestCase):
  """Tests FeatureExpectations with full encode-decode."""

  @property
  def expectations(self):
    raise NotImplementedError

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    # Maybe should try to use metaclass instead and dynamically generate one
    # method per feature expectation.
    for exp in self.expectations:
      tf.logging.info("Testing feature %s", exp.name)

      # Check the shape/dtype
      self.assertEqual(exp.feature.shape, exp.shape)
      self.assertEqual(exp.feature.dtype, exp.dtype)

      # Check the serialized features
      if exp.serialized_features is not None:
        self.assertEqual(
            exp.serialized_features,
            exp.feature.get_serialized_features(),
        )

      # Create the feature dict
      fdict = features.FeaturesDict({exp.name: exp.feature})
      for test in exp.tests:
        input_value = {exp.name: test.value}

        if test.raise_cls is not None:
          if not test.raise_msg:
            raise ValueError(
                "test.raise_msg should be set with {}for test {}".format(
                    test.raise_cls, exp.name))
          with self.assertRaisesWithPredicateMatch(
              test.raise_cls, test.raise_msg):
            features_encode_decode(fdict, input_value)
        else:
          # Test the serialization only
          if test.expected_serialized is not None:
            self.assertEqual(
                test.expected_serialized,
                exp.feature.encode_sample(test.value),
            )

          # Test serialization + decoding from disk
          decoded_samples = features_encode_decode(fdict, input_value)
          self.assertAllEqual(test.expected, decoded_samples[exp.name])
          # TODO(rsepassi): test shape and dtype against exp.feature


def features_encode_decode(features_dict, sample):
  """Runs the full pipeline: encode > write > tmp files > read > decode."""
  # Encode sample
  encoded_sample = features_dict.encode_sample(sample)

  with tmp_dir() as tmp_dir_:
    tmp_filename = os.path.join(tmp_dir_, "tmp.tfrecord")

    # Read/write the file
    file_adapter = file_format_adapter.TFRecordExampleAdapter(
        features_dict.get_serialized_features())
    file_adapter.write_from_generator(
        generator_fn=lambda: [encoded_sample],
        output_files=[tmp_filename],
    )
    dataset = file_adapter.dataset_from_filename(tmp_filename)

    # Decode the sample
    dataset = dataset.map(features_dict.decode_sample)

    for el in dataset_utils.iterate_over_dataset(dataset):
      return el
