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

"""Tests for tensorflow_datasets.testing.mocking."""

import functools
import pickle

import numpy as np
import pytest
import tensorflow as tf
# Import the final API to:
# * Register datasets
# * Make sure `tfds.load`, `tfds.builder` aliases works correctly after patching
import tensorflow_datasets as tfds


# TODO(pytest): Rather than `request.param` magic, should use
# `@pytest.mark.parametrize` once
# https://github.com/pytest-dev/pytest/issues/3960 is fixed
@pytest.fixture(
    params=[
        tfds.testing.MockPolicy.USE_FILES,
        tfds.testing.MockPolicy.USE_CODE,
    ],
)
def mock_data(request):
  """Parametrized fixture to test both `USE_FILES` and `USE_CODE` policy."""
  return functools.partial(tfds.testing.mock_data, policy=request.param)


# pylint: disable=redefined-outer-name


@pytest.fixture
def apply_mock_data(mock_data):
  """Fixture which apply `tfds.testing.mock_data` to the test.

  Test which uses this fixture will be executed twice, once with `USE_FILES` and
  once with `USE_CODE`.

  Args:
    mock_data: `mock_data` fixture defined above.

  Yields:
    None
  """
  with mock_data():
    yield


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_imagenet():
  ds = tfds.load('imagenet2012', split='train')
  assert ds.element_spec == {
      'file_name': tf.TensorSpec(shape=(), dtype=tf.string),
      'image': tf.TensorSpec(shape=(None, None, 3), dtype=tf.uint8),
      'label': tf.TensorSpec(shape=(), dtype=tf.int64),
  }
  list(ds.take(3))  # Iteration should work


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_add_tfds_id():
  read_config = tfds.ReadConfig(add_tfds_id=True)
  ds = tfds.load('mnist', split='train', read_config=read_config)
  assert ds.element_spec == {
      'tfds_id': tf.TensorSpec(shape=(), dtype=tf.string),
      'image': tf.TensorSpec(shape=(28, 28, 1), dtype=tf.uint8),
      'label': tf.TensorSpec(shape=(), dtype=tf.int64),
  }
  train_examples = list(ds.take(3))  # Iteration should work
  ds = tfds.load('mnist', split='test', read_config=read_config)
  test_examples = list(ds.take(3))  # Iteration should work
  assert train_examples[0]['tfds_id'] != test_examples[0]['tfds_id']


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_partial_decoding():
  ds = tfds.load(
      'mnist',
      split='train',
      decoders=tfds.decode.PartialDecoding({
          'image': tfds.features.Image(shape=(None, None, 1)),
      }),
  )
  assert ds.element_spec == {
      'image': tf.TensorSpec(shape=(28, 28, 1), dtype=tf.uint8),
  }
  list(ds.take(3))  # Iteration should work


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_imagenet_decoders():
  """Test with SkipDecoding."""
  ds, ds_info = tfds.load(
      'imagenet2012',
      split='train',
      decoders={'image': tfds.decode.SkipDecoding()},
      with_info=True,
  )
  assert ds.element_spec == {
      'file_name': tf.TensorSpec(shape=(), dtype=tf.string),
      'image': tf.TensorSpec(shape=(), dtype=tf.string),  # Encoded images
      'label': tf.TensorSpec(shape=(), dtype=tf.int64),
  }
  for ex in ds.take(10):
    # Image decoding should works
    image = ds_info.features['image'].decode_example(ex['image'])
    image.shape.assert_is_compatible_with((None, None, 3))
    assert image.dtype == tf.uint8


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_wider_face():
  ds = tfds.load('wider_face', split='train')
  assert ds.element_spec['faces']['expression'] == tf.TensorSpec(
      shape=(None,), dtype=tf.bool
  )
  for ex in ds.take(2):
    assert ex['faces']['expression'].dtype == tf.bool


@pytest.mark.usefixtures('apply_mock_data')
def test_mocking_coco_captions():
  ds = tfds.load('coco_captions', split='train')
  assert ds.element_spec['captions']['text'] == tf.TensorSpec(
      shape=(None,), dtype=tf.string
  )
  for ex in ds.take(2):
    assert ex['captions']['text'].dtype == tf.string
    ex['captions']['text'].shape.assert_is_compatible_with((None,))


def test_custom_as_dataset(mock_data):
  def _as_dataset(self, *args, **kwargs):  # pylint: disable=unused-argument
    return tf.data.Dataset.from_generator(
        lambda: (  # pylint: disable=g-long-lambda
            {'text': t} for t in ['some sentence', 'some other sentence']
        ),
        output_types=self.info.features.dtype,
        output_shapes=self.info.features.shape,
    )

  with mock_data(as_dataset_fn=_as_dataset):
    ds = tfds.load('librispeech_lm', split='train')
    out = [ex['text'] for ex in tfds.as_numpy(ds)]
    assert out == [b'some sentence', b'some other sentence']


def test_max_values(mock_data):
  with mock_data(num_examples=50):
    ds = tfds.load('mnist', split='train')
    assert ds.element_spec == {
        'image': tf.TensorSpec(shape=(28, 28, 1), dtype=tf.uint8),
        'label': tf.TensorSpec(shape=(), dtype=tf.int64),
    }
    for ex in ds.take(50):
      assert tf.math.reduce_max(ex['label']).numpy() < 10
    # Test determinism (iterating twice should yield the same samples)
    assert [ex['label'].numpy() for ex in ds.take(5)] == [8, 2, 9, 3, 1]
    assert [ex['label'].numpy() for ex in ds.take(5)] == [8, 2, 9, 3, 1]


def test_mock_data_auto(tmp_path):
  """Test `MockPolicy.AUTO` fallback to `USE_CODE`."""
  # By default, mock data should load metadata when present.
  with tfds.testing.mock_data():
    builder = tfds.builder('mnist')
    assert list(builder.info.splits.keys())  # Metadata should loaded.

  # When mock data unknown, fallback to `USE_CODE` mode.
  with tfds.testing.mock_data(data_dir=tmp_path):
    builder = tfds.builder('mnist')
    assert not list(builder.info.splits.keys())  # Metadata unknown.


def test_mock_data_use_code():
  """Test `MockPolicy.USE_CODE` specific behavior."""
  with tfds.testing.mock_data(policy=tfds.testing.MockPolicy.USE_CODE):
    builder = tfds.builder('mnist')
    # Dynamic metadata should be unknown.
    assert not list(builder.info.splits.keys())

    # As splits are unknown, any split can be loaded.
    ds = tfds.load('mnist', split='non_existent')
    assert set(ds.element_spec.keys()) == {'image', 'label'}

    ds = tfds.data_source('mnist', split='non_existent')
    assert len(ds) == 1
    assert set(ds[0].keys()) == {'image', 'label'}


def test_mock_data_use_files(tmp_path):
  """Test `MockPolicy.USE_FILES` specific behavior."""
  with tfds.testing.mock_data(policy=tfds.testing.MockPolicy.USE_FILES):
    builder = tfds.builder('mnist')
    # Metadata should have been restored correctly.
    assert builder.info.splits.keys() == {'test', 'train'}

    # Unknown split should raise error
    # Currently, this error is accidentally triggered by
    # `info.splits[split].file_instructions` inside `_should_cache_ds`.
    # We could make the check more explicit.
    with pytest.raises(ValueError, match='Unknown split'):
      tfds.load('mnist', split='non_existent')
    with pytest.raises(ValueError, match='Unknown split'):
      tfds.data_source('mnist', split='non_existent')

  with tfds.testing.mock_data(
      policy=tfds.testing.MockPolicy.USE_FILES,
      data_dir=tmp_path,
  ):
    with pytest.raises(ValueError, match='copy the real metadata files'):
      tfds.load('mnist')
    with pytest.raises(ValueError, match='copy the real metadata files'):
      tfds.data_source('mnist', split='non_existent')


def test_cardinality():
  with tfds.testing.mock_data(num_examples=8):
    ds = tfds.load('mnist', split='train')
    assert ds.cardinality().numpy().item() == 8

  with tfds.testing.mock_data(num_examples=15):
    ds = tfds.load('mnist', split='train')
    assert ds.cardinality().numpy().item() == 15


def test_mocking_rlu_nested_dataset():
  """Test of a nested dataset.

  In this test we use the dataset rlu_atari.
  The dataset has the following features:

    features=tfds.features.FeaturesDict({
      'episode_id': tf.int64,
      'checkpoint_id': tf.int64,
      'episode_return': tf.float32,
      'steps': tfds.features.Dataset({
          'action': tf.int64,
          'discount': tf.float32,
          'is_first': tf.bool,
          'is_last': tf.bool,
          'is_terminal': tf.bool,
          'observation': tfds.features.Image(shape=(84, 84, 1), dtype=tf.uint8),
          'reward': tf.float32,
      }),
    })
  """
  with tfds.testing.mock_data(
      num_examples=3, policy=tfds.testing.MockPolicy.USE_CODE
  ):
    ds = tfds.load('rlu_atari/Pong_run_1', split='train')

    steps = ds.element_spec['steps']
    assert isinstance(steps, tf.data.DatasetSpec)
    assert steps.element_spec['reward'] == tf.TensorSpec(
        shape=(), dtype=tf.float32
    )

    for ex in ds.take(3):
      ds_steps = ex['steps']
      assert isinstance(ds_steps, tf.data.Dataset)

      ds_steps_iter = iter(ds_steps)
      steps_ex = next(ds_steps_iter)
      assert set(steps_ex.keys()) == {
          'action',
          'discount',
          'is_first',
          'is_last',
          'is_terminal',
          'observation',
          'reward',
      }
      assert steps_ex['observation'].shape == (84, 84, 1)


def _get_steps(data, window_size=4):
  """Extract the steps dataset and create out of it a window dataset."""
  episode_ds = data['steps']
  # The line below creates a variant dataset
  return episode_ds.window(window_size, drop_remainder=True)


@pytest.mark.parametrize('num_sub_examples', [1, 36])
def test_mocking_rlu_nested_dataset_with_windows(
    num_sub_examples, num_examples=3, max_value=8, window_size=4
):
  """Test of a nested dataset with windows.

  In this test we use the dataset rlu_atari - see the docstring of
  test_mocking_rlu_nested_dataset for a full list of features.

  The test checks in particular that after application of the window method
  the number of elements in the dataset is

  num_examples * (num_sub_examples // window_size).

  Args:
    num_sub_examples: Number of examples to generate in a nested subdataset.
    num_examples: Number of examples to generate in the dataset.
    max_value: The maximum value present in generated tensors.
    window_size: The size of the sequence window.
  """
  with tfds.testing.mock_data(
      num_examples=num_examples,
      num_sub_examples=num_sub_examples,
      max_value=max_value,
      policy=tfds.testing.MockPolicy.USE_CODE,
  ):
    ds = tfds.load('rlu_atari/Pong_run_1', split='train')

    for ex in ds.take(3):
      ds_steps = ex['steps']
      assert ds_steps.cardinality().numpy().item() == num_sub_examples

      # the window method is applied in _get_steps
      ds_flat_steps = ds.flat_map(
          functools.partial(_get_steps, window_size=window_size)
      )
      ds_flat_steps = iter(ds_flat_steps)

      assert len(list(ds_flat_steps)) == num_examples * (
          num_sub_examples // window_size
      )

      for obs_rew_act in ds_flat_steps:
        assert obs_rew_act['observation'].element_spec == tf.TensorSpec(
            shape=(84, 84, 1), dtype=tf.uint8
        )
        assert (
            next(iter(tfds.as_numpy(obs_rew_act['observation']))) <= max_value
        ).all()
        assert (
            next(iter(tfds.as_numpy(obs_rew_act['action']))) <= max_value
        ).all()


def test_mock_data_source():
  with tfds.testing.mock_data(num_examples=10):
    data_source = tfds.data_source('imagenet2012')
    assert len(data_source['train']) == 10
    assert isinstance(data_source['train'][0], dict)

    data_source = tfds.data_source('imagenet2012', split='train')
    assert len(data_source) == 10
    assert isinstance(data_source[0], dict)

    data_source = tfds.data_source('imagenet2012', split='train[:50%]')
    assert len(data_source) == 10
    assert isinstance(data_source[0], dict)
    assert isinstance(data_source[0]['image'], np.ndarray)

    # Without decoding the images
    decoders = {'image': tfds.decode.SkipDecoding()}
    data_source = tfds.data_source(
        'imagenet2012', split='train[:50%]', decoders=decoders
    )
    assert isinstance(data_source[0]['image'], bytes)


def test_mock_multiple_data_source():
  with tfds.testing.mock_data(num_examples=10):
    imagenet = tfds.data_source('imagenet2012', split='train')
    librispeech = tfds.data_source('librispeech_lm', split='train')

    # Data sources of different element specs produce different elements.
    assert set(next(iter(imagenet)).keys()) != set(
        next(iter(librispeech)).keys()
    )


def test_as_data_source_fn():
  as_data_source_fn = lambda *args, **kwargs: ['foo', 'bar', 'baz']
  with tfds.testing.mock_data(as_data_source_fn=as_data_source_fn):
    imagenet = tfds.data_source('imagenet2012', split='train')
    assert len(imagenet) == 3
    assert imagenet[0] == 'foo'
    assert imagenet[1] == 'bar'
    assert imagenet[2] == 'baz'
