# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
          'a': tfds.features.Scalar(
              dtype=tf.int64,
              doc=tfds.features.Documentation(
                  desc='a feature', value_range='From 1 to 10'
              ),
          ),
          'b': tfds.features.Text(doc='Some text'),
          'c': tfds.features.Image(
              shape=(None, None, 1), encoding_format='png'
          ),
          'd': tf.int64,
          'e': tfds.features.Sequence(tf.float32, doc='Floats'),
          'f': tfds.features.Sequence(tfds.features.Audio(), doc='Audio'),
          'g': tfds.features.Sequence(
              {
                  'a': tf.float32,
                  'b': tfds.features.Scalar(dtype=tf.int64, doc='b'),
              },
              doc='Nested',
          ),
          'h': tfds.features.Dataset(
              {
                  'a': tf.float32,
                  'b': tfds.features.Text(doc='Nested text'),
              },
              doc='Dataset of something',
          ),
      },
      doc='My test features',
  )
  section = dataset_markdown_builder.FeatureDocumentationSection()
  assert section._format_block(features.catalog_documentation()) == '\n'.join([
      'Feature | Class | Shape | Dtype | Description | Value range',
      ':------ | :---- | :---- | :---- | :---------- | :----------',
      ' | FeaturesDict |  |  | My test features | ',
      'a | Scalar |  | int64 | a feature | From 1 to 10',
      'b | Text |  | string | Some text | ',
      'c | Image | (None, None, 1) | uint8 |  | ',
      'd | Tensor |  | int64 |  | ',
      'e | Sequence(Tensor) | (None,) | float32 | Floats | ',
      'f | Sequence(Audio) | (None, None) | int64 | Audio | ',
      'g | Sequence |  |  | Nested | ',
      'g/a | Tensor |  | float32 |  | ',
      'g/b | Scalar |  | int64 | b | ',
      'h | Dataset |  |  | Dataset of something | ',
      'h/a | Tensor |  | float32 |  | ',
      'h/b | Text |  | string | Nested text | ',
  ])


def test_feature_documentation_section_missing_value_range():
  features = tfds.features.FeaturesDict(
      feature_dict={
          'a': tfds.features.Scalar(
              dtype=tf.int64, doc=tfds.features.Documentation(desc='a feature')
          ),
          'b': tfds.features.Text(doc='Some text'),
      },
      doc='My test features',
  )
  section = dataset_markdown_builder.FeatureDocumentationSection()
  assert section._format_block(features.catalog_documentation()) == '\n'.join([
      'Feature | Class | Shape | Dtype | Description',
      ':------ | :---- | :---- | :---- | :----------',
      ' | FeaturesDict |  |  | My test features',
      'a | Scalar |  | int64 | a feature',
      'b | Text |  | string | Some text',
  ])


def test_paperswithcode_section():
  tfds_to_pwc_links = {'dummy_dataset': 'https://paperswithcode/dummy_dataset'}
  pwc_section = dataset_markdown_builder.PapersWithCodeSection(
      tfds_to_pwc_links=tfds_to_pwc_links
  )

  dummy_builder = tfds.testing.DummyDataset()
  expected_output = f"""
        <a class="button button-with-icon" href="{tfds_to_pwc_links[dummy_builder.name]}">
          Explore on Papers With Code
          <span class="material-icons icon-after" aria-hidden="true">
            north_east
          </span>
        </a>
      """

  assert pwc_section.content(builder=dummy_builder) == expected_output
