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

"""Tests for tensorflow_datasets.core.registered."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import six
import tensorflow as tf

from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits


@six.add_metaclass(registered.RegisteredDataset)
class EmptyDatasetBuilder(object):

  def __init__(self, **kwargs):
    self.kwargs = kwargs
    self.download_called = False
    self.as_dataset_called = False

  def download_and_prepare(self, **kwargs):
    self.download_called = True
    self.download_kwargs = kwargs

  def as_dataset(self, **kwargs):
    self.as_dataset_called = True
    self.as_dataset_kwargs = kwargs
    return self


class UnregisteredBuilder(EmptyDatasetBuilder):

  @abc.abstractproperty
  def an_abstract_property(self):
    pass


class RegisteredTest(tf.test.TestCase):

  def test_registered(self):
    name = "empty_dataset_builder"
    self.assertEqual(name, EmptyDatasetBuilder.name)
    self.assertIsInstance(registered.builder(name), EmptyDatasetBuilder)
    self.assertIn(name, registered.list_builders())
    self.assertNotIn("unregistered_builder", registered.list_builders())

    nonexistent = "nonexistent_foobar_dataset"
    with self.assertRaisesWithPredicateMatch(ValueError, "not found"):
      registered.builder(nonexistent)
    # Prints registered datasets
    with self.assertRaisesWithPredicateMatch(ValueError, name):
      registered.builder(nonexistent)

  def test_builder_with_kwargs(self):
    name = "empty_dataset_builder"
    name_with_kwargs = name + "/k1=1,k2=1.,k3=foo,k4=True,k5=False"
    builder = registered.builder(name_with_kwargs, data_dir="bar")
    expectations = [("k1", 1), ("k2", 1.), ("k3", u"foo"), ("k4", True),
                    ("k5", False)]
    for k, v in expectations:
      self.assertEqual(type(builder.kwargs[k]), type(v))
      self.assertEqual(builder.kwargs[k], v)

  def test_load(self):
    name = "empty_dataset_builder/k1=1"
    data_dir = "foo"
    as_dataset_kwargs = dict(a=1, b=2)

    # EmptyDatasetBuilder returns self from as_dataset
    builder = registered.load(
        name=name, split=splits.Split.TEST, data_dir=data_dir,
        download=False, as_dataset_kwargs=as_dataset_kwargs)
    self.assertTrue(builder.as_dataset_called)
    self.assertFalse(builder.download_called)
    self.assertEqual(splits.Split.TEST,
                     builder.as_dataset_kwargs.pop("split"))
    self.assertFalse(builder.as_dataset_kwargs.pop("as_supervised"))
    self.assertEqual(builder.as_dataset_kwargs, as_dataset_kwargs)
    self.assertEqual(dict(data_dir=data_dir, k1=1), builder.kwargs)

    builder = registered.load(
        name, split=splits.Split.TRAIN, data_dir=data_dir,
        download=True, as_dataset_kwargs=as_dataset_kwargs)
    self.assertTrue(builder.as_dataset_called)
    self.assertTrue(builder.download_called)


if __name__ == "__main__":
  tf.test.main()
