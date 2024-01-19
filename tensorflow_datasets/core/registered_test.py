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

"""Tests for tensorflow_datasets.core.registered."""

import abc
import re

from unittest import mock
import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import load
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import py_utils
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.testing.dummy_config_based_datasets.dummy_ds_1 import dummy_ds_1_dataset_builder


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

  VERSION = utils.Version("1.0.0")
  BUILDER_CONFIGS = []
  builder_configs = {}


class UnregisteredBuilder(EmptyDatasetBuilder):

  @property
  @abc.abstractmethod
  def an_abstract_property(self):
    pass


class RegisteredTest(testing.TestCase):

  def test_registered(self):
    name = "empty_dataset_builder"
    self.assertEqual(name, EmptyDatasetBuilder.name)
    self.assertIsInstance(load.builder(name), EmptyDatasetBuilder)
    self.assertIn(name, load.list_builders())

    nonexistent = "nonexistent_foobar_dataset"
    with self.assertRaisesWithPredicateMatch(
        registered.DatasetNotFoundError, "not found"
    ):
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
        ValueError, "`builder_cls` only accept the `dataset_name`"
    ):
      name_with_kwargs = "empty_dataset_builder/config:1.0.0"
      load.builder_cls(name_with_kwargs)

  def test_abstract(self):
    name = "unregistered_builder"
    self.assertEqual(name, UnregisteredBuilder.name)
    self.assertNotIn(name, load.list_builders())

    with self.assertRaisesWithPredicateMatch(
        TypeError, "Can't instantiate abstract class"
    ):
      load.builder(name)

  def test_builder_with_kwargs(self):
    name = "empty_dataset_builder"
    name_with_kwargs = name + "/k1=1,k2=1.,k3=foo,k4=True,k5=False"
    builder = load.builder(name_with_kwargs, data_dir="bar")
    expectations = [
        ("k1", 1),
        ("k2", 1.0),
        ("k3", "foo"),
        ("k4", True),
        ("k5", False),
    ]
    for k, v in expectations:
      self.assertEqual(type(builder.kwargs[k]), type(v))
      self.assertEqual(builder.kwargs[k], v)

  def test_builder_fullname(self):
    fullname = "empty_dataset_builder/conf1-attr:1.0.1/k1=1,k2=2"
    builder = load.builder(fullname, data_dir="bar")
    expected = {
        "k1": 1,
        "k2": 2,
        "version": "1.0.1",
        "config": "conf1-attr",
        "data_dir": "bar",
    }
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
        name=name,
        split=splits.Split.TEST,
        data_dir=data_dir,
        download=False,
        as_dataset_kwargs=as_dataset_kwargs,
    )
    self.assertTrue(builder.as_dataset_called)
    self.assertFalse(builder.download_called)
    self.assertEqual(splits.Split.TEST, builder.as_dataset_kwargs.pop("split"))
    self.assertIsNone(builder.as_dataset_kwargs.pop("batch_size"))
    self.assertFalse(builder.as_dataset_kwargs.pop("as_supervised"))
    self.assertFalse(builder.as_dataset_kwargs.pop("decoders"))
    self.assertIsNone(builder.as_dataset_kwargs.pop("read_config"))
    self.assertFalse(builder.as_dataset_kwargs.pop("shuffle_files"))
    self.assertEqual(builder.as_dataset_kwargs, as_dataset_kwargs)
    self.assertEqual(dict(data_dir=data_dir, k1=1), builder.kwargs)

    builder = load.load(
        name,
        split=splits.Split.TRAIN,
        data_dir=data_dir,
        download=True,
        as_dataset_kwargs=as_dataset_kwargs,
    )
    self.assertTrue(builder.as_dataset_called)
    self.assertTrue(builder.download_called)

    # Tests for different batch_size
    # By default batch_size=None
    builder = load.load(name=name, split=splits.Split.TEST, data_dir=data_dir)
    self.assertIsNone(builder.as_dataset_kwargs.pop("batch_size"))
    # Setting batch_size=1
    builder = load.load(
        name=name, split=splits.Split.TEST, data_dir=data_dir, batch_size=1
    )
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

      class ColabBuilder(EmptyDatasetBuilder):
        pass

      self.assertIn(name, load.list_builders())
      self.assertIsInstance(load.builder(name), ColabBuilder)
      old_colab_class = ColabBuilder

      class ColabBuilder(EmptyDatasetBuilder):  # pylint: disable=function-redefined
        pass

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


def test_name_inferred_from_pkg():
  ds_builder = dummy_ds_1_dataset_builder.Builder()
  assert ds_builder.name == "dummy_ds_1"


def test_name_inferred_from_pkg_level0_fails():
  pkg_path = (
      tfds.core.tfds_path() / "testing/dummy_config_based_datasets/dummy_ds_2"
  )
  expected_msg = (
      "When using `Builder` as class name, the dataset builder name is "
      'inferred from module name if named "*_dataset_builder" or from '
      'package name, but there is no package in "dummy_builder".'
  )
  with tfds.core.utils.add_sys_path(pkg_path):
    with pytest.raises(AssertionError, match=re.escape(expected_msg)):
      tfds.core.community.builder_cls_from_module("dummy_builder")


@mock.patch.dict(registered._DATASET_REGISTRY, {})
def test_name_inferred_from_pkg_level1():
  pkg_path = tfds.core.tfds_path() / "testing/dummy_config_based_datasets"
  with tfds.core.utils.add_sys_path(pkg_path):
    ds_builder = tfds.core.community.builder_cls_from_module(
        "dummy_ds_2.dummy_builder"
    )
  assert ds_builder.name == "dummy_ds_2"


@mock.patch.dict(registered._DATASET_REGISTRY, {})
def test_name_inferred_from_pkg_level2():
  pkg_path = tfds.core.tfds_path() / "testing"
  with tfds.core.utils.add_sys_path(pkg_path):
    ds_builder = tfds.core.community.builder_cls_from_module(
        "dummy_config_based_datasets.dummy_ds_2.dummy_builder"
    )
  assert ds_builder.name == "dummy_ds_2"


@mock.patch.dict(registered._DATASET_REGISTRY, {})
def test_name_inferred_from_pkg_level3():
  pkg_path = tfds.core.tfds_path()
  with tfds.core.utils.add_sys_path(pkg_path):
    ds_builder = tfds.core.community.builder_cls_from_module(
        "testing.dummy_config_based_datasets.dummy_ds_2.dummy_builder"
    )
  assert ds_builder.name == "dummy_ds_2"


class ConfigBasedBuildersTest(testing.TestCase):

  def test__get_existing_dataset_packages(self):
    ds_packages = registered._get_existing_dataset_packages(
        "testing/dummy_config_based_datasets"
    )
    self.assertEqual(set(ds_packages.keys()), {"dummy_ds_1", "dummy_ds_2"})
    pkg_path, builder_module = ds_packages["dummy_ds_1"]
    self.assertEndsWith(
        str(pkg_path),
        "tensorflow_datasets/testing/dummy_config_based_datasets/dummy_ds_1",
    )
    self.assertEqual(
        builder_module,
        "tensorflow_datasets.testing.dummy_config_based_datasets.dummy_ds_1.dummy_ds_1_dataset_builder",
    )

  @mock.patch.object(
      constants, "DATASETS_TFDS_SRC_DIR", "testing/dummy_config_based_datasets"
  )
  def test_imported_builder_cls(self):
    builder = registered.imported_builder_cls("dummy_ds_1")
    self.assertEqual(builder.name, "dummy_ds_1")


# Tests for RegisteredDatasetCollection.


class EmptyDatasetCollectionBuilder(registered.RegisteredDatasetCollection):
  pass


class AbstractDatasetCollectionBuilder(registered.RegisteredDatasetCollection):

  @property
  @abc.abstractmethod
  def an_abstract_property(self):
    pass


def test_registered_dataset_collection():
  name = "empty_dataset_collection_builder"
  assert name == EmptyDatasetCollectionBuilder.name


def test_skip_dataset_collection_registration():
  with registered.skip_registration():

    class SkipCollectionBuilder(registered.RegisteredDatasetCollection):  # pylint: disable=unused-variable
      pass

  assert (
      "skip_collection_builder"
      not in registered.list_imported_dataset_collections()
  )


def test_duplicate_dataset_collection_builders():
  name = "duplicate_collection_builder"
  error_msg = f"DatasetCollection with name {name} already registered"

  class DuplicateCollectionBuilder(registered.RegisteredDatasetCollection):  # pylint: disable=unused-variable
    pass

  with pytest.raises(ValueError, match=error_msg):

    class DuplicateCollectionBuilder(registered.RegisteredDatasetCollection):  # pylint: disable=function-redefined
      pass


def test_duplicate_dataset_collections_on_notebooks():
  with mock.patch.object(py_utils, "is_notebook", lambda: True):
    name = "colab_dataset_collection_builder"
    assert name not in registered.list_imported_dataset_collections()

    class ColabDatasetCollectionBuilder(EmptyDatasetCollectionBuilder):  # pylint: disable=unused-variable
      pass

    assert name in registered.list_imported_dataset_collections()
    cls = registered.imported_dataset_collection_cls(name)
    assert isinstance(cls, type(ColabDatasetCollectionBuilder))
    old_colab_cls = ColabDatasetCollectionBuilder

    class ColabDatasetCollectionBuilder(EmptyDatasetBuilder):  # pylint: disable=function-redefined
      pass

    assert name in registered.list_imported_dataset_collections()
    assert isinstance(cls, type(ColabDatasetCollectionBuilder))
    assert not isinstance(cls, old_colab_cls)


def test_list_imported_dataset_collections():
  assert (
      "empty_dataset_collection_builder"
      in registered.list_imported_dataset_collections()
  )
  assert (
      "abstract_dataset_collection_builder"
      not in registered.list_imported_dataset_collections()
  )
  assert (
      "nonexistent_dc_builder"
      not in registered.list_imported_dataset_collections()
  )


def test_is_dataset_collection():
  assert registered.is_dataset_collection("empty_dataset_collection_builder")
  assert not registered.is_dataset_collection(
      "abstract_dataset_collection_builder"
  )
  assert not registered.is_dataset_collection("nonexistent_dc_builder")


def test_imported_dataset_collection_cls():
  existent = "empty_dataset_collection_builder"
  abstract = "abstract_dataset_collection_builder"
  nonexistent = "nonexistent_dataset_collection_builder"

  cls = registered.imported_dataset_collection_cls(existent)
  assert isinstance(cls, type(EmptyDatasetCollectionBuilder))

  error_msg = f"DatasetCollection {abstract} is an abstract class."
  with pytest.raises(AssertionError, match=error_msg):
    registered.imported_dataset_collection_cls(abstract)

  with pytest.raises(registered.DatasetCollectionNotFoundError):
    registered.imported_dataset_collection_cls(nonexistent)
