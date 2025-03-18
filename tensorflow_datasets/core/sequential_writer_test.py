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

"""Tests for the sequential writer."""
import tempfile

from absl.testing import absltest
from absl.testing import parameterized
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import sequential_writer


def _generate_split(num_examples: int) -> tf.data.Dataset:
  data = {
      'a': list(range(num_examples)),
      'b': list(range(num_examples)),
  }
  return tf.data.Dataset.from_tensor_slices(data)


def _dataset_info(
    data_dir: str, name: str = 'test_dataset'
) -> dataset_info.DatasetInfo:
  return dataset_info.DatasetInfo(
      builder=dataset_info.DatasetIdentity(
          name=name,
          data_dir=data_dir,
          module_name='',
          version='1.0.0',
      ),
      description='Test builder',
      features=tfds.features.FeaturesDict({
          'a': tf.int32,
          'b': tf.int32,
      }),
  )


class SequentialWriterTest(parameterized.TestCase):

  @parameterized.named_parameters(
      {
          'testcase_name': 'uneven_shards',
          'num_examples': 5,
          'max_examples_per_shard': 3,
          'num_expected_shards': 2,
      },
      {
          'testcase_name': 'even_shards',
          'num_examples': 6,
          'max_examples_per_shard': 3,
          'num_expected_shards': 2,
      },
      {
          'testcase_name': 'one_full_shard',
          'num_examples': 3,
          'max_examples_per_shard': 3,
          'num_expected_shards': 1,
      },
      {
          'testcase_name': 'one_not_full_shard',
          'num_examples': 2,
          'max_examples_per_shard': 3,
          'num_expected_shards': 1,
      },
  )
  def test_generates_correct_shards(
      self, num_examples, max_examples_per_shard, num_expected_shards
  ):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=max_examples_per_shard,
    )
    writer.initialize_splits(['train'])
    for example in tfds.as_numpy(_generate_split(num_examples)):
      writer.add_examples({'train': [example]})
    writer.close_splits(['train'])

    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(
        ds_builder.info.splits['train'].num_shards, num_expected_shards
    )
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples)

  def test_writes_multiple_examples(self):
    num_examples = 5
    max_examples_per_shard = 3
    num_expected_shards = 2
    data_dir = tempfile.mkdtemp('data_dir')

    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=max_examples_per_shard,
    )
    writer.initialize_splits(['train'])
    writer.add_examples(
        {'train': list(tfds.as_numpy(_generate_split(num_examples)))}
    )
    writer.close_splits(['train'])

    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(
        ds_builder.info.splits['train'].num_shards, num_expected_shards
    )
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples)

  def test_writes_multiple_splits(self):
    num_examples_train = 5
    num_examples_eval = 7
    max_examples_per_shard = 3
    num_expected_shards_train = 2
    num_expected_shards_eval = 3

    data_dir = tempfile.mkdtemp('data_dir')

    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=max_examples_per_shard,
    )
    writer.initialize_splits(['train', 'eval'])
    writer.add_examples({
        'train': list(tfds.as_numpy(_generate_split(num_examples_train))),
        'eval': list(tfds.as_numpy(_generate_split(num_examples_eval))),
    })
    writer.close_splits(['train', 'eval'])
    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(
        ds_builder.info.splits['train'].num_shards, num_expected_shards_train
    )
    self.assertEqual(
        ds_builder.info.splits['eval'].num_shards, num_expected_shards_eval
    )
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_train)
    counter = (
        ds_builder.as_dataset(split='eval')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_eval)

  def test_closes_all(self):
    num_examples_train = 5
    num_examples_eval = 7
    max_examples_per_shard = 3
    num_expected_shards_train = 2
    num_expected_shards_eval = 3

    data_dir = tempfile.mkdtemp('data_dir')

    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=max_examples_per_shard,
    )
    writer.initialize_splits(['train', 'eval'])
    writer.add_examples({
        'train': list(tfds.as_numpy(_generate_split(num_examples_train))),
        'eval': list(tfds.as_numpy(_generate_split(num_examples_eval))),
    })
    writer.close_all()
    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(
        ds_builder.info.splits['train'].num_shards, num_expected_shards_train
    )
    self.assertEqual(
        ds_builder.info.splits['eval'].num_shards, num_expected_shards_eval
    )
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_train)
    counter = (
        ds_builder.as_dataset(split='eval')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_eval)

  def test_writes_multiple_splits_sequentially(self):
    num_examples_train = 5
    num_examples_eval = 7
    max_examples_per_shard = 3
    num_expected_shards_train = 2
    num_expected_shards_eval = 3

    data_dir = tempfile.mkdtemp('data_dir')

    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=max_examples_per_shard,
    )
    writer.initialize_splits(['train'])
    writer.add_examples(
        {
            'train': list(tfds.as_numpy(_generate_split(num_examples_train))),
        }
    )
    writer.close_splits(['train'])
    writer.initialize_splits(['eval'])
    writer.add_examples(
        {
            'eval': list(tfds.as_numpy(_generate_split(num_examples_eval))),
        }
    )
    writer.close_splits(['eval'])
    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(
        ds_builder.info.splits['train'].num_shards, num_expected_shards_train
    )
    self.assertEqual(
        ds_builder.info.splits['eval'].num_shards, num_expected_shards_eval
    )
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_train)
    counter = (
        ds_builder.as_dataset(split='eval')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, num_examples_eval)

  def test_fails_to_append_to_nonexisting_split(self):
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info('/unused/dir'), max_examples_per_shard=1
    )
    with self.assertRaises(KeyError):
      writer.add_examples(
          {
              'train': list(tfds.as_numpy(_generate_split(1))),
          }
      )

  def test_fails_to_close_a_nonexisting_split(self):
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info('/unused/dir'), max_examples_per_shard=1
    )
    with self.assertRaises(KeyError):
      writer.close_splits(['train'])

  def test_fails_to_initialize_same_split_twice(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir), max_examples_per_shard=1
    )
    writer.initialize_splits(['train'])
    with self.assertRaises(KeyError):
      writer.initialize_splits(['train'])

  def test_initializes_same_split_twice(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir), max_examples_per_shard=1
    )
    writer.initialize_splits(['train'])
    writer.initialize_splits(['train'], fail_if_exists=False)

  def test_fails_to_append_to_closed_split(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir), max_examples_per_shard=1
    )
    writer.initialize_splits(['train'])
    writer.close_splits(['train'])
    with self.assertRaises(ValueError):
      writer.add_examples(
          {
              'train': list(tfds.as_numpy(_generate_split(1))),
          }
      )

  def test_closing_a_closed_split_is_a_noop(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir), max_examples_per_shard=1
    )
    writer.initialize_splits(['train'])
    writer.close_splits(['train'])
    writer.close_splits(['train'])

  def test_append_to_different_dataset_fails(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir), max_examples_per_shard=3
    )
    writer.initialize_splits(['train'])
    writer.close_splits(['train'])
    with self.assertRaises(ValueError):
      sequential_writer.SequentialWriter(
          _dataset_info(data_dir, 'new_name'),
          max_examples_per_shard=3,
          overwrite=False,
      )

  def test_append_to_non_existent_works(self):
    data_dir = tempfile.mkdtemp('data_dir')
    writer = sequential_writer.SequentialWriter(
        ds_info=_dataset_info(data_dir),
        max_examples_per_shard=3,
        overwrite=False,
    )
    writer.initialize_splits(['train'])
    writer.close_splits(['train'])

  def test_append_to_existing_dataset_works(self):
    data_dir = tempfile.mkdtemp('data_dir')
    ds_info = _dataset_info(data_dir)
    writer = sequential_writer.SequentialWriter(
        ds_info=ds_info, max_examples_per_shard=3
    )
    writer.initialize_splits(['train'])
    writer.add_examples({'train': list(tfds.as_numpy(_generate_split(4)))})
    writer.close_splits(
        ['train']
    )  # The split should have 2 shards with 4 examples

    new_writer = sequential_writer.SequentialWriter(
        ds_info=ds_info, max_examples_per_shard=2, overwrite=False
    )
    new_writer.initialize_splits(['train'], fail_if_exists=False)
    new_writer.add_examples({'train': list(tfds.as_numpy(_generate_split(3)))})
    new_writer.close_splits(['train'])  # We added 2 shards with 3 examples

    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(ds_builder.info.splits['train'].num_shards, 4)
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, 7)

  def test_overwrites(self):
    data_dir = tempfile.mkdtemp('data_dir')
    ds_info = _dataset_info(data_dir)
    writer = sequential_writer.SequentialWriter(
        ds_info=ds_info, max_examples_per_shard=3
    )
    writer.initialize_splits(['train'])
    writer.add_examples({'train': list(tfds.as_numpy(_generate_split(4)))})
    writer.close_splits(
        ['train']
    )  # The split should have 2 shards with 4 examples

    new_writer = sequential_writer.SequentialWriter(
        ds_info=ds_info, max_examples_per_shard=2, overwrite=True
    )
    new_writer.initialize_splits(['train'], fail_if_exists=True)
    new_writer.add_examples({'train': list(tfds.as_numpy(_generate_split(3)))})
    new_writer.close_splits(['train'])  # We added 2 shards with 3 examples

    ds_builder = tfds.builder_from_directory(data_dir)
    self.assertEqual(ds_builder.info.splits['train'].num_shards, 2)
    counter = (
        ds_builder.as_dataset(split='train')
        .reduce(0, lambda v, _: v + 1)
        .numpy()
    )
    self.assertEqual(counter, 3)


if __name__ == '__main__':
  absltest.main()
