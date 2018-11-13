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

import collections
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


class FeatureExpectation(
    collections.namedtuple('_FeatureExpectation',
                           ['name', 'feature', 'value', 'expected'])):
  pass


class FeatureExpectationsTestCase(tf.test.TestCase):
  """Tests FeatureExpectations with full encode-decode."""

  @property
  def expectations(self):
    raise NotImplementedError

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    expectations = self.expectations
    fdict = features.FeaturesDict(
        {exp.name: exp.feature for exp in expectations})

    decoded_sample = features_encode_decode(
        fdict, dict([(exp.name, exp.value) for exp in expectations]))

    for exp in expectations:
      self.assertAllEqual(decoded_sample[exp.name], exp.expected)
      # TODO(rsepassi): test shape and dtype against exp.feature


def features_encode_decode(features_dict, sample):
  """Runs the full pipeline: encode > write > tmp files > read > decode."""
  # Encode sample
  encoded_sample = features_dict.encode_sample(sample)

  with tmp_dir() as tmp_dir_:
    tmp_filename = os.path.join(tmp_dir_, 'tmp.tfrecord')

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
