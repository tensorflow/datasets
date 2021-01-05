# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import pytest

import tensorflow.compat.v2 as tf

# Import the final API to:
# * Register datasets
# * Make sure `tfds.load`, `tfds.builder` aliases works correctly after patching
import tensorflow_datasets as tfds


# TODO(pytest): Rather than `request.param` magic, should use
# `@pytest.mark.parametrize` once
# https://github.com/pytest-dev/pytest/issues/3960 is fixed
@pytest.fixture(
    params=[
        tfds.testing.MockPolicy.USE_FILES, tfds.testing.MockPolicy.USE_CODE
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
  assert (
      ds.element_spec['faces']['expression']
      == tf.TensorSpec(shape=(None,), dtype=tf.bool)
  )
  for ex in ds.take(2):
    assert ex['faces']['expression'].dtype == tf.bool


def test_custom_as_dataset(mock_data):
  def _as_dataset(self, *args, **kwargs):  # pylint: disable=unused-argument
    return tf.data.Dataset.from_generator(
        lambda: ({  # pylint: disable=g-long-lambda
            'text': t,
        } for t in ['some sentence', 'some other sentence']),
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
    assert [ex['label'].numpy() for ex in ds.take(5)] == [1, 9, 2, 5, 3]
    assert [ex['label'].numpy() for ex in ds.take(5)] == [1, 9, 2, 5, 3]


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


def test_mock_data_use_files(tmp_path):
  """Test `MockPolicy.USE_FILES` specific behavior."""
  with tfds.testing.mock_data(policy=tfds.testing.MockPolicy.USE_FILES):
    builder = tfds.builder('mnist')
    # Metadata should have been restored correctly.
    assert list(builder.info.splits.keys()) == ['test', 'train']

    # Unknown split should raise error
    # Currently, this error is accidentally triggered by
    # `info.splits[split].file_instructions` inside `_should_cache_ds`.
    # We could make the check more explicit.
    with pytest.raises(ValueError, match='Unknown split'):
      tfds.load('mnist', split='non_existent')

  with tfds.testing.mock_data(
      policy=tfds.testing.MockPolicy.USE_FILES,
      data_dir=tmp_path,
  ):
    with pytest.raises(ValueError, match='copy the real metadata files'):
      tfds.load('mnist')
