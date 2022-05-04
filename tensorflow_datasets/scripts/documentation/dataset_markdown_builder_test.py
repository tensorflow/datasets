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

"""Tests for dataset_markdown_builder."""
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import dataset_markdown_builder


def test_feature_documentation_section():
  features = tfds.features.FeaturesDict(
      feature_dict={
          'a':
              tfds.features.Scalar(
                  dtype=tf.int64,
                  doc=tfds.features.Documentation(
                      desc='a feature', value_range='From 1 to 10')),
          'b':
              tfds.features.Text(doc='Some text'),
          'c':
              tfds.features.Image(shape=(None, None, 1), encoding_format='png'),
          'd':
              tf.int64,
          'e':
              tfds.features.Sequence(tf.float32, doc='Floats'),
          'f':
              tfds.features.Sequence(tfds.features.Audio(), doc='Audio'),
          'g':
              tfds.features.Sequence(
                  {
                      'a': tf.float32,
                      'b': tfds.features.Scalar(dtype=tf.int64, doc='b'),
                  },
                  doc='Nested'),
          'h':
              tfds.features.Dataset(
                  {
                      'a': tf.float32,
                      'b': tfds.features.Text(doc='Nested text'),
                  },
                  doc='Dataset of something'),
      },
      doc='My test features')
  section = dataset_markdown_builder.FeatureDocumentationSection()
  assert section._format_block(features.catalog_documentation()) == '\n'.join([
      'Feature | Class | Shape | Dtype | Description | Value range',
      ':------ | :---- | :---- | :---- | :---------- | :----------',
      ' | FeaturesDict |  |  | My test features | ',
      'a | Scalar |  | tf.int64 | a feature | From 1 to 10',
      'b | Text |  | tf.string | Some text | ',
      'c | Image | (None, None, 1) | tf.uint8 |  | ',
      'd | Tensor |  | tf.int64 |  | ',
      'e | Sequence(Tensor) | (None,) | tf.float32 | Floats | ',
      'f | Sequence(Audio) | (None, None) | tf.int64 | Audio | ',
      'g | Sequence |  |  | Nested | ',
      'g/a | Tensor |  | tf.float32 |  | ',
      'g/b | Scalar |  | tf.int64 | b | ',
      'h | Dataset |  |  | Dataset of something | ',
      'h/a | Tensor |  | tf.float32 |  | ',
      'h/b | Text |  | tf.string | Nested text | ',
  ])


def test_feature_documentation_section_missing_value_range():
  features = tfds.features.FeaturesDict(
      feature_dict={
          'a':
              tfds.features.Scalar(
                  dtype=tf.int64,
                  doc=tfds.features.Documentation(desc='a feature')),
          'b':
              tfds.features.Text(doc='Some text'),
      },
      doc='My test features')
  section = dataset_markdown_builder.FeatureDocumentationSection()
  assert section._format_block(features.catalog_documentation()) == '\n'.join([
      'Feature | Class | Shape | Dtype | Description',
      ':------ | :---- | :---- | :---- | :----------',
      ' | FeaturesDict |  |  | My test features',
      'a | Scalar |  | tf.int64 | a feature',
      'b | Text |  | tf.string | Some text',
  ])
