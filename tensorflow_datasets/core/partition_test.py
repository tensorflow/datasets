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

"""Tests for partition."""
import functools

from absl.testing import parameterized
import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import partition as partition_lib

_SPEC_FOR_A_B = partition_lib.PartitionSpec.create_simple_spec(["a", "b"])


class PartitionInfoTest(parameterized.TestCase, testing.TestCase):

  def test_constructor(self):
    partition_spec = _SPEC_FOR_A_B
    partition_lib.PartitionInfo(
        spec=partition_spec, values={
            "a": "x",
            "b": "y"
        })
    with pytest.raises(
        ValueError, match="The following partitions were not specified:.+"):
      partition_lib.PartitionInfo(spec=partition_spec, values={})

  def test_relative_path_does_not_include_partition_name(self):
    partition_spec = _SPEC_FOR_A_B
    partition_info = partition_lib.PartitionInfo(
        spec=partition_spec, values={
            "a": "x",
            "b": "y"
        })
    assert partition_info.relative_path() == "x/y"

  def test_relative_path_include_partition_name(self):
    partition_spec = partition_lib.PartitionSpec(partitions=[
        partition_lib.Partitioning(
            name="a", folder_name_fn=partition_lib.folder_as_name_value_fn(
                "a")),
        partition_lib.Partitioning(
            name="b", folder_name_fn=partition_lib.folder_as_name_value_fn(
                "b")),
    ])
    partition_info = partition_lib.PartitionInfo(
        spec=partition_spec, values={
            "a": "x",
            "b": "y"
        })
    assert partition_info.relative_path() == "a=x/b=y"

  def test_missing_partition(self):
    partition_spec = _SPEC_FOR_A_B
    with pytest.raises(
        ValueError, match="The following partitions were not specified.+"):
      partition_lib.PartitionInfo(spec=partition_spec, values={"a": "x"})

  @parameterized.parameters([
      ("a=1,b=2", None, partition_lib.PartitionInfo(values={
          "a": "1",
          "b": "2"
      })),
      ("a=1,b=2", _SPEC_FOR_A_B,
       partition_lib.PartitionInfo(
           spec=_SPEC_FOR_A_B, values={
               "a": "1",
               "b": "2"
           })),
  ])
  def test_parse_tfds_partition_info(self, tfds_name, spec, expected):
    assert partition_lib.PartitionInfo.parse_tfds_partition_info(
        tfds_name, spec) == expected

  def test_parse_tfds_partition_info_missing_partition(self):
    with pytest.raises(
        ValueError, match="The following partitions were not specified:.+"):
      partition_lib.PartitionInfo.parse_tfds_partition_info(
          tfds_name="a=1", spec=_SPEC_FOR_A_B)

  def test_parse_tfds_partition_info_unknown_partition(self):
    with pytest.raises(
        ValueError,
        match="The following partitions got values, but are not in the spec: b"
    ):
      partition_lib.PartitionInfo.parse_tfds_partition_info(
          tfds_name="a=1,b=2",
          spec=partition_lib.PartitionSpec.create_simple_spec(["a"]))


class PartitioningTest(parameterized.TestCase, testing.TestCase):

  @parameterized.named_parameters([
      ("None", None, None),
      ("List", ["a", "b", "c"], ["a", "b", "c"]),
      ("Callable", lambda: ["a", "b", "c"], ["a", "b", "c"]),
  ])
  def test_possible_values(self, input_param, expected):
    partitioning = partition_lib.Partitioning(
        name="partition", possible_values=input_param)
    assert partitioning.possible_values == expected

  @parameterized.named_parameters([
      ("value", None, ["a"], "a", "a"),
      ("name=value",
       functools.partial(partition_lib.folder_as_name_value,
                         name="partition"), ["a"], "a", "partition=a"),
  ])
  def test_folder_for(self, folder_name_fn, possible_values, value, expected):
    partitioning = partition_lib.Partitioning(
        name="partition",
        possible_values=possible_values,
        folder_name_fn=folder_name_fn)
    assert partitioning.folder_for(value) == expected

  @parameterized.named_parameters([
      ("Daily", "2022-01-01", "2022-01-03", 1,
       ["2022-01-01", "2022-01-02", "2022-01-03"]),
      ("Weekly 1 week", "2022-01-01", "2022-01-03", 7, ["2022-01-01"]),
      ("Weekly multiple", "2022-01-01", "2022-01-15", 7,
       ["2022-01-01", "2022-01-08", "2022-01-15"]),
  ])
  def test_create_date_partitioning(self, start_date, end_date, days_between,
                                    expected):
    partitioning = partition_lib.create_date_partitioning(
        name="snapshot",
        start_date=start_date,
        end_date=end_date,
        days_between=days_between)
    assert partitioning.name == "snapshot"
    assert partitioning.possible_values == expected

  def test_tfx_spans(self):
    partitioning = partition_lib.create_tfx_date_partitioning(
        name="my_data", start_date="1970-01-01", end_date="1970-01-03")
    assert partitioning.possible_values == [
        "1970-01-01", "1970-01-02", "1970-01-03"
    ]
    actual_folder_names = [
        partitioning.folder_for(v) for v in partitioning.possible_values
    ]
    assert actual_folder_names == ["0", "1", "2"]


class PartitionSpecTest(parameterized.TestCase, testing.TestCase):

  def test_create_simple_spec(self):
    spec = partition_lib.PartitionSpec.create_simple_spec(
        ["a", ("b", ["b1", "b2"])])
    partition1 = spec.partitions[0]
    assert partition1.name == "a"
    assert partition1.possible_values is None

    partition2 = spec.partitions[1]
    assert partition2.name == "b"
    assert partition2.possible_values == ["b1", "b2"]

  def test_get_partition_infos(self):
    spec = partition_lib.PartitionSpec(partitions=[
        partition_lib.Partitioning(name="lower", possible_values=["a", "b"]),
        partition_lib.Partitioning(name="upper", possible_values=["A"]),
        partition_lib.Partitioning(name="number", possible_values=["1", "2"]),
    ])
    partition_infos = spec.get_partition_infos()
    partition_values = [info.values for info in partition_infos]
    for pv in partition_values:
      print(pv)
    assert partition_values == [
        {
            "lower": "a",
            "upper": "A",
            "number": "1"
        },
        {
            "lower": "b",
            "upper": "A",
            "number": "1"
        },
        {
            "lower": "a",
            "upper": "A",
            "number": "2"
        },
        {
            "lower": "b",
            "upper": "A",
            "number": "2"
        },
    ]
