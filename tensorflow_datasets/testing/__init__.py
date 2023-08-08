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

"""Testing utilities."""

import importlib
import typing
from typing import Any, List

from tensorflow_datasets.core import registered

# pylint: disable=g-import-not-at-top,g-importing-member
if typing.TYPE_CHECKING:
  # We import testing namespace but without registering the tests datasets
  # (e.g. DummyMnist,...).
  # LINT.IfChange(pydeps)
  from tensorflow_datasets.testing.dataset_builder_testing import DatasetBuilderTestCase
  from tensorflow_datasets.testing.feature_test_case import FeatureExpectationItem
  from tensorflow_datasets.testing.feature_test_case import FeatureExpectationsTestCase
  from tensorflow_datasets.testing.feature_test_case import RaggedConstant
  from tensorflow_datasets.testing.feature_test_case import SubTestCase
  from tensorflow_datasets.testing.mocking import mock_data
  from tensorflow_datasets.testing.mocking import MockPolicy
  from tensorflow_datasets.testing.mocking import PickableDataSourceMock
  from tensorflow_datasets.testing.test_case import TestCase
  from tensorflow_datasets.testing.test_utils import assert_features_equal
  from tensorflow_datasets.testing.test_utils import DummyBeamDataset
  from tensorflow_datasets.testing.test_utils import DummyDataset
  from tensorflow_datasets.testing.test_utils import DummyDatasetCollection
  from tensorflow_datasets.testing.test_utils import DummyDatasetSharedGenerator
  from tensorflow_datasets.testing.test_utils import DummyMnist
  from tensorflow_datasets.testing.test_utils import DummyParser
  from tensorflow_datasets.testing.test_utils import DummySerializer
  from tensorflow_datasets.testing.test_utils import fake_examples_dir
  from tensorflow_datasets.testing.test_utils import make_tmp_dir
  from tensorflow_datasets.testing.test_utils import mock_kaggle_api
  from tensorflow_datasets.testing.test_utils import MockFs
  from tensorflow_datasets.testing.test_utils import rm_tmp_dir
  from tensorflow_datasets.testing.test_utils import run_in_graph_and_eager_modes
  from tensorflow_datasets.testing.test_utils import test_main
  from tensorflow_datasets.testing.test_utils import tmp_dir
  # LINT.ThenChange(:deps)
# pylint: enable=g-import-not-at-top,g-importing-member

_API = {
    # LINT.IfChange(deps)
    "assert_features_equal": "tensorflow_datasets.testing.test_utils",
    "DatasetBuilderTestCase": (
        "tensorflow_datasets.testing.dataset_builder_testing"
    ),
    "DummyBeamDataset": "tensorflow_datasets.testing.test_utils",
    "DummyDataset": "tensorflow_datasets.testing.test_utils",
    "DummyDatasetCollection": "tensorflow_datasets.testing.test_utils",
    "DummyDatasetSharedGenerator": "tensorflow_datasets.testing.test_utils",
    "DummyMnist": "tensorflow_datasets.testing.test_utils",
    "DummyParser": "tensorflow_datasets.testing.test_utils",
    "DummySerializer": "tensorflow_datasets.testing.test_utils",
    "fake_examples_dir": "tensorflow_datasets.testing.test_utils",
    "FeatureExpectationItem": "tensorflow_datasets.testing.feature_test_case",
    "FeatureExpectationsTestCase": (
        "tensorflow_datasets.testing.feature_test_case"
    ),
    # TODO(afrozm): rm from here and add as methods to TestCase
    "make_tmp_dir": "tensorflow_datasets.testing.test_utils",
    "mock_data": "tensorflow_datasets.testing.mocking",
    "mock_kaggle_api": "tensorflow_datasets.testing.test_utils",
    "MockFs": "tensorflow_datasets.testing.test_utils",
    "MockPolicy": "tensorflow_datasets.testing.mocking",
    "PickableDataSourceMock": "tensorflow_datasets.testing.mocking",
    "RaggedConstant": "tensorflow_datasets.testing.feature_test_case",
    # TODO(afrozm): rm from here and add as methods to TestCase
    "rm_tmp_dir": "tensorflow_datasets.testing.test_utils",
    "run_in_graph_and_eager_modes": "tensorflow_datasets.testing.test_utils",
    "SubTestCase": "tensorflow_datasets.testing.feature_test_case",
    "test_main": "tensorflow_datasets.testing.test_utils",
    "TestCase": "tensorflow_datasets.testing.test_case",
    # TODO(afrozm): rm from here and add as methods to TestCase
    "tmp_dir": "tensorflow_datasets.testing.test_utils",
    # LINT.ThenChange(:pydeps)
}

__all__ = list(_API)


def __dir__() -> List[str]:  # pylint: disable=invalid-name
  return __all__


def __getattr__(name: str) -> Any:  # pylint: disable=invalid-name
  if name in _API:
    module_name = _API[name]
    with registered.skip_registration():
      module = importlib.import_module(module_name)
    return getattr(module, name)
  else:
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
