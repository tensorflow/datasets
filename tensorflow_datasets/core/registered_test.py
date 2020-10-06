# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

import abc
from unittest import mock

from tensorflow_datasets import testing
from tensorflow_datasets.core import load
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits
from tensorflow_datasets.core.utils import py_utils


class EmptyDatasetBuilder(registered.RegisteredDataset):

  def __init__(self, **kwargs):
    self.data_dir = "/some/path/to/dir"
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


class RegisteredTest(testing.TestCase):

  def test_registered(self):
    name = "empty_dataset_builder"
    self.assertEqual(name, EmptyDatasetBuilder.name)
    self.assertIsInstance(load.builder(name), EmptyDatasetBuilder)
    self.assertIn(name, load.list_builders())

    nonexistent = "nonexistent_foobar_dataset"
    with self.assertRaisesWithPredicateMatch(ValueError, "not found"):
      load.builder(nonexistent)
    # Prints registered datasets
    with self.assertRaisesWithPredicateMatch(ValueError, name):
      load.builder(nonexistent)

  def test_registered_cls(self):
    name = "empty_dataset_builder"
    self.assertIs(load.builder_cls(name), EmptyDatasetBuilder)

    nonexistent = "nonexistent_foobar_dataset"
    with self.assertRaisesWithPredicateMatch(ValueError, "not found"):
      load.builder_cls(nonexistent)

    with self.assertRaisesWithPredicateMatch(
        ValueError, "`builder_cls` only accept the `dataset_name`"):
      name_with_kwargs = "empty_dataset_builder/config:1.0.0"
      load.builder_cls(name_with_kwargs)

  def test_abstract(self):
    name = "unregistered_builder"
    self.assertEqual(name, UnregisteredBuilder.name)
    self.assertNotIn(name, load.list_builders())

    with self.assertRaisesWithPredicateMatch(ValueError, "an abstract class"):
      load.builder(name)

  def test_builder_with_kwargs(self):
    name = "empty_dataset_builder"
    name_with_kwargs = name + "/k1=1,k2=1.,k3=foo,k4=True,k5=False"
    builder = load.builder(name_with_kwargs, data_dir="bar")
    expectations = [("k1", 1), ("k2", 1.), ("k3", u"foo"), ("k4", True),
                    ("k5", False)]
    for k, v in expectations:
      self.assertEqual(type(builder.kwargs[k]), type(v))
      self.assertEqual(builder.kwargs[k], v)

  def test_builder_fullname(self):
    fullname = "empty_dataset_builder/conf1-attr:1.0.1/k1=1,k2=2"
    builder = load.builder(fullname, data_dir="bar")
    expected = {"k1": 1, "k2": 2, "version": "1.0.1",
                "config": "conf1-attr", "data_dir": "bar"}
    self.assertEqual(expected, builder.kwargs)

  def test_builder_camel_case(self):
    fullname = "EmptyDatasetBuilder"
    builder = load.builder(fullname)
    self.assertIsInstance(builder, EmptyDatasetBuilder)

  def test_load(self):
    name = "empty_dataset_builder/k1=1"
    data_dir = "foo"
    as_dataset_kwargs = dict(a=1, b=2)

    # EmptyDatasetBuilder returns self from as_dataset
    builder = load.load(
        name=name, split=splits.Split.TEST, data_dir=data_dir,
        download=False, as_dataset_kwargs=as_dataset_kwargs)
    self.assertTrue(builder.as_dataset_called)
    self.assertFalse(builder.download_called)
    self.assertEqual(splits.Split.TEST,
                     builder.as_dataset_kwargs.pop("split"))
    self.assertIsNone(builder.as_dataset_kwargs.pop("batch_size"))
    self.assertFalse(builder.as_dataset_kwargs.pop("as_supervised"))
    self.assertFalse(builder.as_dataset_kwargs.pop("decoders"))
    self.assertIsNone(builder.as_dataset_kwargs.pop("read_config"))
    self.assertFalse(builder.as_dataset_kwargs.pop("shuffle_files"))
    self.assertEqual(builder.as_dataset_kwargs, as_dataset_kwargs)
    self.assertEqual(dict(data_dir=data_dir, k1=1), builder.kwargs)

    builder = load.load(
        name, split=splits.Split.TRAIN, data_dir=data_dir,
        download=True, as_dataset_kwargs=as_dataset_kwargs)
    self.assertTrue(builder.as_dataset_called)
    self.assertTrue(builder.download_called)

    # Tests for different batch_size
    # By default batch_size=None
    builder = load.load(
        name=name, split=splits.Split.TEST, data_dir=data_dir)
    self.assertIsNone(builder.as_dataset_kwargs.pop("batch_size"))
    # Setting batch_size=1
    builder = load.load(
        name=name, split=splits.Split.TEST, data_dir=data_dir,
        batch_size=1)
    self.assertEqual(1, builder.as_dataset_kwargs.pop("batch_size"))

  def test_load_all_splits(self):
    name = "empty_dataset_builder"
    # EmptyDatasetBuilder returns self from as_dataset
    builder = load.load(name=name, data_dir="foo")
    self.assertTrue(builder.as_dataset_called)
    self.assertIsNone(builder.as_dataset_kwargs.pop("split"))

  def test_load_with_config(self):
    data_dir = "foo"
    name = "empty_dataset_builder/bar/k1=1"
    # EmptyDatasetBuilder returns self from as_dataset
    builder = load.load(name=name, split=splits.Split.TEST, data_dir=data_dir)
    expected = dict(data_dir=data_dir, k1=1, config="bar")
    self.assertEqual(expected, builder.kwargs)

    name = "empty_dataset_builder/bar"
    builder = load.load(name=name, split=splits.Split.TEST, data_dir=data_dir)
    self.assertEqual(dict(data_dir=data_dir, config="bar"), builder.kwargs)

  def test_notebook_overwrite_dataset(self):
    """Redefining the same builder twice is possible on colab."""

    with mock.patch.object(py_utils, "is_notebook", lambda: True):
      name = "colab_builder"
      self.assertNotIn(name, load.list_builders())

      class ColabBuilder(registered.RegisteredDataset):

        def __init__(self, **kwargs):
          del kwargs

      self.assertIn(name, load.list_builders())
      self.assertIsInstance(load.builder(name), ColabBuilder)
      old_colab_class = ColabBuilder

      class ColabBuilder(registered.RegisteredDataset):  # pylint: disable=function-redefined

        def __init__(self, **kwargs):
          del kwargs

      self.assertIsInstance(load.builder(name), ColabBuilder)
      self.assertNotIsInstance(load.builder(name), old_colab_class)

  def test_duplicate_dataset(self):
    """Redefining the same builder twice should raises error."""

    class DuplicateBuilder(registered.RegisteredDataset):  # pylint: disable=unused-variable
      pass

    with self.assertRaisesWithPredicateMatch(ValueError, "already registered"):
      class DuplicateBuilder(registered.RegisteredDataset):  # pylint: disable=function-redefined
        pass

  def test_is_full_name(self):
    """Test for `is_full_name`."""
    self.assertFalse(load.is_full_name("ds/config/1.0.2/other"))
    self.assertFalse(load.is_full_name("ds/config/1.0.2/"))
    self.assertFalse(load.is_full_name("ds/config/1.2"))
    self.assertFalse(load.is_full_name("ds/config"))
    self.assertFalse(load.is_full_name("ds/1.2.*"))

    self.assertTrue(load.is_full_name("ds/config/1.0.2"))
    self.assertTrue(load.is_full_name("ds/1.0.2"))
    self.assertTrue(load.is_full_name("ds_with_number123/1.0.2"))


def test_skip_regitration():
  """Test `skip_registration()`."""

  with registered.skip_registration():

    class SkipRegisteredDataset(registered.RegisteredDataset):
      pass

  name = "skip_registered_dataset"
  assert name == SkipRegisteredDataset.name
  assert name not in load.list_builders()


def test_skip_regitration_kwarg():
  """Test `class Dataset(..., skip_registration=True)`."""

  class SkipDataset(registered.RegisteredDataset, skip_registration=True):
    pass

  name = "skip_dataset"
  assert name == SkipDataset.name
  assert name not in load.list_builders()


def test_custom_name():
  """Tests that builder can have custom names."""

  class SomeCustomNameBuilder(registered.RegisteredDataset):
    name = "custom_name"

  assert "custom_name" == SomeCustomNameBuilder.name
  assert "custom_name" in load.list_builders()
