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

"""Tests for tensorflow_datasets.core.features.dataset_feature."""

# pylint: disable=g-complex-comprehension  # Comprehensions allow us to write more compact/readable tests in this file.

import pickle

from absl.testing import parameterized
import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import decode as decode_lib
from tensorflow_datasets.core import features as feature_lib


class IncrementDecoder(decode_lib.Decoder):
  """Basic decoder that just adds 1 to the encoded example."""

  def decode_example(self, serialized_example):
    return serialized_example + 1


class DatasetDictFeatureTest(
    parameterized.TestCase, testing.FeatureExpectationsTestCase
):

  @parameterized.parameters((np.int32), (tf.int32))
  def test_int(self, dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset({'int': dtype}),
        shape={'int': ()},  # shape of each element of the dataset
        dtype={'int': dtype},
        serialized_info={
            'int': feature_lib.TensorInfo(shape=(None,), dtype=dtype),
        },
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value=[{'int': 1}, {'int': 2}, {'int': 3}],
                expected=tf.data.Dataset.from_tensor_slices({'int': [1, 2, 3]}),
                # expected_np=Not implemented yet,
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'int': np.ones(shape=(3,), dtype=np.int32)}
                    )
                ),
                expected=tf.data.Dataset.from_tensor_slices({'int': [1, 1, 1]}),
                expected_np=[{'int': 1}] * 3,
            ),
            # Dataset length doesn't matter
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'int': np.ones(shape=(4,), dtype=np.int32)}
                    )
                ),
                expected=tf.data.Dataset.from_tensor_slices(
                    {'int': [1, 1, 1, 1]}
                ),
                expected_np=[{'int': 1}] * 4,
            ),
        ],
        test_attributes=dict(_length=None),
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_label(self, dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            {
                'label': feature_lib.ClassLabel(names=['left', 'right']),
            },
            length=None,
        ),
        shape={'label': ()},
        dtype={'label': dtype},
        serialized_info={
            'label': feature_lib.TensorInfo(shape=(None,), dtype=dtype),
        },
        tests=[
            testing.FeatureExpectationItem(
                value=[
                    {'label': 'right'},
                    {'label': 'left'},
                    {'label': 'left'},
                ],
                expected=tf.data.Dataset.from_tensor_slices(
                    {'label': [1, 0, 0]}
                ),
                # expected_np=Not implemented yet,
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices(
                        {'label': ['right', 'left', 'right', 'left']}
                    )
                ),
                expected=tf.data.Dataset.from_tensor_slices(
                    {'label': [1, 0, 1, 0]}
                ),
                expected_np=[
                    {'label': 1},
                    {'label': 0},
                    {'label': 1},
                    {'label': 0},
                ],
            ),
        ],
        test_attributes=dict(_length=None),
    )

  @parameterized.parameters(
      (np.object_, np.int32, np.uint8),
      (tf.string, tf.int32, tf.uint8),
  )
  def test_nested(self, a_dtype, bc_dtype, bd_dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            {
                'a': a_dtype,
                'b': {
                    'c': feature_lib.Tensor(shape=(4, 2), dtype=bc_dtype),
                    'd': bd_dtype,
                },
            },
            length=None,
        ),
        shape={
            'a': (),
            'b': {
                'c': (4, 2),
                'd': (),
            },
        },
        dtype={
            'a': np.object_,
            'b': {
                'c': np.int32,
                'd': np.uint8,
            },
        },
        tests=[
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices({
                        'a': ['aa', 'b', 'ccc'],
                        'b': {
                            'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                            'd': [1, 2, 3],
                        },
                    })
                ),
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(t) for t in ('aa', 'b', 'ccc')],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    },
                }),
                expected_np=[
                    {
                        'a': b'aa',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 1,
                        },
                    },
                    {
                        'a': b'b',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 2,
                        },
                    },
                    {
                        'a': b'ccc',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 3,
                        },
                    },
                ],
            ),
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices({
                        'a': [str(i) for i in range(100)],
                        'b': {  # pylint: disable=g-complex-comprehension
                            'c': [
                                np.ones(shape=(4, 2), dtype=np.int32)
                                for _ in range(100)
                            ],
                            'd': [5 for _ in range(100)],
                        },
                    })
                ),
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(str(i)) for i in range(100)],
                    'b': {
                        'c': np.ones(shape=(100, 4, 2), dtype=np.int32),
                        'd': [5] * 100,
                    },
                }),
                expected_np=[
                    {
                        'a': str(i).encode(),
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 5,
                        },
                    }
                    for i in range(100)
                ],
            ),
        ],
    )

  @parameterized.parameters(
      (np.object_, np.int32, np.uint8),
      (tf.string, tf.int32, tf.uint8),
  )
  def test_input_dict(self, a_dtype, bc_dtype, bd_dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            {
                'a': a_dtype,
                'b': {
                    'c': feature_lib.Tensor(shape=(4, 2), dtype=bc_dtype),
                    'd': bd_dtype,
                },
            },
            length=None,
        ),
        shape={
            'a': (),
            'b': {
                'c': (4, 2),
                'd': (),
            },
        },
        dtype={
            'a': np.object_,
            'b': {
                'c': np.int32,
                'd': np.uint8,
            },
        },
        tests=[
            testing.FeatureExpectationItem(
                value={
                    'a': ['aa', 'b', 'ccc'],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    },
                },
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(t) for t in ('aa', 'b', 'ccc')],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    },
                }),
                expected_np=[
                    {
                        'a': b'aa',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 1,
                        },
                    },
                    {
                        'a': b'b',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 2,
                        },
                    },
                    {
                        'a': b'ccc',
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 3,
                        },
                    },
                ],
            ),
            testing.FeatureExpectationItem(
                value={
                    'a': [str(i) for i in range(100)],
                    'b': {  # pylint: disable=g-complex-comprehension
                        'c': [
                            np.ones(shape=(4, 2), dtype=np.int32)
                            for _ in range(100)
                        ],
                        'd': [5 for _ in range(100)],
                    },
                },
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(str(i)) for i in range(100)],
                    'b': {
                        'c': np.ones(shape=(100, 4, 2), dtype=np.int32),
                        'd': [5] * 100,
                    },
                }),
                expected_np=[
                    {
                        'a': str(i).encode(),
                        'b': {
                            'c': np.ones(shape=(4, 2), dtype=np.int32),
                            'd': 5,
                        },
                    }
                    for i in range(100)
                ],
            ),
            # Wrong length in one of the lists.
            testing.FeatureExpectationItem(
                value={
                    'a': ['aa'],
                    'b': {
                        'c': np.ones(shape=(3, 4, 2), dtype=np.int32),
                        'd': [1, 2, 3],
                    },
                },
                raise_cls=ValueError,
                raise_cls_np=ValueError,
                raise_msg=(
                    'The length of all elements of one sequence should be the'
                    ' same.'
                ),
            ),
        ],
    )

  @parameterized.parameters(
      (np.object_, np.uint8),
      (tf.string, tf.uint8),
  )
  def test_decoding(self, a_dtype, bc_dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            {
                'a': a_dtype,
                'b': {
                    'c': bc_dtype,
                },
            },
            length=None,
        ),
        shape={
            'a': (),
            'b': {
                'c': (),
            },
        },
        dtype={
            'a': np.object_,
            'b': {
                'c': np.uint8,
            },
        },
        tests=[
            testing.FeatureExpectationItem(
                value=dataset_utils.as_numpy(
                    tf.data.Dataset.from_tensor_slices({
                        'a': ['aa', 'b', 'ccc'],
                        'b': {
                            'c': [1, 2, 3],
                        },
                    })
                ),
                decoders={
                    'b': {
                        'c': IncrementDecoder(),
                    },
                },
                expected=tf.data.Dataset.from_tensor_slices({
                    'a': [tf.compat.as_bytes(t) for t in ('aa', 'b', 'ccc')],
                    'b': {
                        'c': [2, 3, 4],
                    },
                }),
                expected_np=[
                    {
                        'a': b'aa',
                        'b': {
                            'c': 2,
                        },
                    },
                    {
                        'a': b'b',
                        'b': {
                            'c': 3,
                        },
                    },
                    {
                        'a': b'ccc',
                        'b': {
                            'c': 4,
                        },
                    },
                ],
            ),
        ],
    )


class DatasetFeatureTest(
    parameterized.TestCase, testing.FeatureExpectationsTestCase
):

  @parameterized.parameters((np.int32), (tf.int32))
  def test_int(self, dtype):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(dtype, length=3),
        shape=(),
        dtype=np.int32,
        tests=[
            # Python array
            testing.FeatureExpectationItem(
                value=[1, 2, 3],
                expected=tf.data.Dataset.from_tensor_slices([1, 2, 3]),
                expected_np=[1, 2, 3],
            ),
            # Numpy array
            testing.FeatureExpectationItem(
                value=np.ones(shape=(3,), dtype=np.int32),
                expected=tf.data.Dataset.from_tensor_slices([1, 1, 1]),
                expected_np=[1, 1, 1],
            ),
            # Datasets with a different lenght will fail on encoding.
            testing.FeatureExpectationItem(
                value=np.ones(shape=(4,), dtype=np.int32),
                raise_cls=ValueError,
                raise_cls_np=ValueError,
                raise_msg='Error while serializing feature',
            ),
        ],
    )

  def test_label(self):
    self.assertFeatureEagerOnly(
        feature=feature_lib.Dataset(
            feature_lib.ClassLabel(names=['left', 'right']),
        ),
        shape=(),
        dtype=np.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=['right', 'left', 'left'],
                expected=tf.data.Dataset.from_tensor_slices([1, 0, 0]),
                expected_np=[1, 0, 0],
            ),
            # Variable sequence length
            testing.FeatureExpectationItem(
                value=['right', 'left', 'right', 'left'],
                expected=tf.data.Dataset.from_tensor_slices([1, 0, 1, 0]),
                expected_np=[1, 0, 1, 0],
            ),
            # Empty sequence length
            testing.FeatureExpectationItem(
                value=[],
                expected=[],
                expected_np=[],
            ),
        ],
    )

  def test_getattr(self):
    feature = feature_lib.Dataset(
        feature_lib.ClassLabel(names=['left', 'right']),
    )
    self.assertEqual(feature.names, ['left', 'right'])

    feature = feature_lib.Dataset(
        {
            'label': feature_lib.ClassLabel(names=['left', 'right']),
        }
    )
    self.assertEqual(feature['label'].names, ['left', 'right'])

  def test_metadata(self):
    feature = feature_lib.Dataset(feature_lib.ClassLabel(num_classes=2))
    feature.feature.names = ['left', 'right']
    with testing.tmp_dir() as tmp_dir:
      feature.save_metadata(data_dir=tmp_dir, feature_name='test')

      feature2 = feature_lib.Dataset(feature_lib.ClassLabel(num_classes=2))
      feature2.load_metadata(data_dir=tmp_dir, feature_name='test')
    self.assertEqual(feature2.feature.names, ['left', 'right'])


class DecodeExampleNpTest(testing.SubTestCase):

  def test_top_level_feature(self):
    feature = feature_lib.Dataset(
        {'feature_name': feature_lib.Tensor(dtype=np.uint8, shape=(4, 2))}
    )
    example = {'feature_name': np.ones(shape=(24,), dtype=np.int32)}
    expected = [{'feature_name': np.ones(shape=(4, 2), dtype=np.int32)}] * 3
    self.assertAllEqualNested(feature.decode_example_np(example), expected)

  def test_tensor_feature(self):
    feature = feature_lib.Dataset(
        feature_lib.Tensor(dtype=np.uint8, shape=(4, 2))
    )
    example = np.ones(shape=(24,), dtype=np.uint8)
    expected = [np.ones(shape=(4, 2), dtype=np.int32)] * 3
    self.assertAllEqualNested(feature.decode_example_np(example), expected)

  def test_nested_dict(self):
    feature = feature_lib.Dataset({'a': {'b': np.int32}, 'b': np.str_})
    example = {'a': {'b': [1, 2, 3]}, 'b': ['a', 'b', 'c']}
    expected = [
        {'a': {'b': 1}, 'b': 'a'},
        {'a': {'b': 2}, 'b': 'b'},
        {'a': {'b': 3}, 'b': 'c'},
    ]
    self.assertAllEqualNested(feature.decode_example_np(example), expected)

  def test_example_with_wrong_shape(self):
    feature = feature_lib.Dataset({'a': {'b': np.int32}, 'b': np.str_})
    example = {'a': {'b': [1, 2]}, 'b': ['a', 'b', 'c']}
    with self.assertRaisesWithPredicateMatch(ValueError, 'Got 2 and 3'):
      feature.decode_example_np(example)

  def test_decode_example_np_is_picklable(self):
    feature = feature_lib.Dataset(np.str_)
    example = [b'a']
    pickle.loads(pickle.dumps(feature.decode_example_np(example)))
    pickle.loads(pickle.dumps(feature.decode_example_np))
    pickle.loads(pickle.dumps(feature_lib.Dataset.decode_example_np))


if __name__ == '__main__':
  testing.test_main()
