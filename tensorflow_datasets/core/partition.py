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

"""Functionality for partitioned datasets."""
from __future__ import annotations

import dataclasses
import datetime
import functools
import os
from typing import Any, Callable, List, Mapping, Optional, Tuple, Union


def parse_date(date_str: str) -> datetime.date:
  try:
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(date_str, "%Y%m%d").date()
  except ValueError:
    pass
  raise ValueError(f"Could not parse date from {date_str}")


def format_date(date: datetime.date, date_format: str = "%Y-%m-%d") -> str:
  return date.strftime(date_format)


def folder_as_name_value(value: str, name: str) -> str:
  return f"{name}={value}"


def folder_as_name_value_fn(name: str) -> Callable[[str], str]:
  return functools.partial(folder_as_name_value, name=name)


def folder_as_value(value: str) -> str:
  return value


def date_as_days_since_epoch(date: Union[str, datetime.date]) -> str:
  if isinstance(date, str):
    date = parse_date(date)
  unix_epoch = parse_date("1970-01-01")
  return str((date - unix_epoch).days)


class Partitioning:
  """How a dataset is partitioned along a single dimension."""

  def __init__(
      self,
      name: str,
      possible_values: Union[None, List[str], Callable[[], List[str]]] = None,
      folder_name_fn: Optional[Callable[[str], str]] = None,
  ):
    """Constructs a Partitioning for a single dimension.

    Arguments:
      name: the name of this partition.
      possible_values: the values that are allowed for this partition. For
        example, if the partitioning is for 'language`, then `possible_values`
        should be the list of languages that are allowed. A function can also be
        passed that returns the possible partition values. If `None`, then it is
        not known what the possible partition values are.
      folder_name_fn: the function that given a partition value returns the
        folder name for this partition. By default, it uses the partition value
        as the folder name.

    Returns:
      a Partitioning.
    """
    self.name = name
    self._possible_values = possible_values
    self._folder_name_fn = folder_name_fn or folder_as_value

  def folder_for(self, value: str) -> str:
    return self._folder_name_fn(value)

  @property
  @functools.lru_cache(maxsize=1)
  def possible_values(self) -> Optional[List[str]]:
    if self._possible_values is None:
      return None
    elif isinstance(self._possible_values, Callable):
      return self._possible_values()
    return self._possible_values


def create_date_partitioning(
    name: str,
    start_date: Union[str, datetime.date],
    end_date: Union[None, str, datetime.date] = None,
    days_between: int = 1,
    folder_name_fn: Optional[Callable[[str], str]] = None,
    date_format: str = "%Y-%m-%d",
) -> Partitioning:
  """Returns a partitioning by date with possible values between start and end.

  Arguments:
    name: name of this partition.
    start_date: the start of the date range.
    end_date: the end of the date range. If `None`, then today's date is used.
    days_between: the number of days between partitions. Default is 1 which
      corresponds to a daily partition. If `days_between` is 7, then there's a
      partition every week.
    folder_name_fn: optional function that formats a partition value into how it
      should be represented in a folder name.
    date_format: how to format dates.

  Returns:
    a partitioning by date with possible values between start and end.
  """
  if days_between < 1:
    raise ValueError(f"`days_between` should be >=1! Got: {days_between}.")

  if isinstance(start_date, str):
    start_date = parse_date(start_date)
  if isinstance(end_date, str):
    end_date = parse_date(end_date)
  if end_date is None:
    end_date = datetime.date.today()

  if start_date > end_date:
    raise ValueError(f"Begin date {start_date} is after end date {end_date}")

  possible_values = []
  current_date = start_date
  while current_date <= end_date:
    possible_values.append(format_date(current_date, date_format=date_format))
    current_date += datetime.timedelta(days_between)

  return Partitioning(
      name=name, possible_values=possible_values, folder_name_fn=folder_name_fn)


def create_tfx_date_partitioning(
    name: str,
    start_date: Union[str, datetime.date],
    end_date: Union[None, str, datetime.date] = None,
) -> Partitioning:
  return create_date_partitioning(
      name=name,
      start_date=start_date,
      end_date=end_date,
      folder_name_fn=date_as_days_since_epoch)


@dataclasses.dataclass()
class PartitionSpec:
  """Specification of the partitions for a dataset.

  A dataset could have 0, 1, or multiple partitions.

  Attributes:
    partitions: the specified partitions. The ordering is important, because it
      is used how to store the data.
  """
  partitions: List[Partitioning]

  def get_partition_names(self) -> List[str]:
    return [p.name for p in self.partitions]

  def get_partition(self, name: str) -> Partitioning:
    for partition in self.partitions:
      if partition.name == name:
        return partition
    raise ValueError(f"There was no partition with name '{name}'! "
                     "Available partition names: " +
                     ", ".join(self.get_partition_names()))

  def get_partition_infos(self) -> List[PartitionInfo]:
    """Returns all the partition infos based on the possible values."""
    current_values = []
    for partition in self.partitions:
      if partition.possible_values is None:
        raise ValueError(
            f"Cannot get partition infos because partition '{partition.name}' "
            "doesn't specify the possible values.")

      new_values = []
      for value in partition.possible_values:
        if not current_values:
          new_values.append({partition.name: value})
          continue

        for old_value in current_values:
          new_value = old_value.copy()
          new_value[partition.name] = value
          new_values.append(new_value)

      current_values = new_values

    return [PartitionInfo(values=value, spec=self) for value in current_values]

  @classmethod
  def create_simple_spec(
      cls,
      partitions: List[Union[str, Tuple[str, List[str]]]],
  ) -> PartitionSpec:
    """Creates a `PartitionSpec` for a list of simple partitions.

    Arguments:
      partitions: a list whose elements are either a string or a tuple. If the
        element is a string, then a `Partitioning` with that name and
        unspecified `possible_values` is created. If it's a tuple, then a
        `Partitioning` with as name the first element in the tuple, and as
        `possible_values` the second element of the tuple.

    Returns:
      a `PartitionSpec` with th
    """
    partitionings = []
    for partition in partitions:
      if isinstance(partition, str):
        partitionings.append(Partitioning(name=partition))
      elif isinstance(partition, tuple):
        name, possible_values = partition
        partitionings.append(
            Partitioning(name=name, possible_values=possible_values))
      else:
        raise ValueError(
            f"Partition spec of type {type(partition)} is not supported!")
    return PartitionSpec(partitions=partitionings)


@dataclasses.dataclass()
class PartitionInfo:
  """Information about one specific partition.

  For example, if the dataset has partitions `language` and `snapshot`, then
  `{'language': 'en', 'snapshot': '2022-11-22'}` would be a single partition.

  Attributes:
    values: the value per partition name.
    spec: optional partition specification that contains all the partition names
      amongst others.
  """
  values: Mapping[str, str]
  spec: Optional[PartitionSpec] = None

  def __post_init__(self):
    if self.spec is not None:
      spec_partition_names = {spec.name for spec in self.spec.partitions}
      missing_partition_names = spec_partition_names - set(self.values.keys())
      if missing_partition_names:
        raise ValueError("The following partitions were not specified: " +
                         ", ".join(missing_partition_names))
      unspecified_partitions = set(self.values.keys()) - spec_partition_names
      if unspecified_partitions:
        raise ValueError("The following partitions got values, "
                         "but are not in the spec: " +
                         ", ".join(unspecified_partitions))

  def replace(self, **kwargs: Any) -> PartitionInfo:
    """Returns a copy with updated attributes."""
    return dataclasses.replace(self, **kwargs)

  def partition_value(self, name: str) -> str:
    return self.values[name]

  def relative_path(self) -> str:
    """Returns the relative path where this partition should be stored."""
    if self.spec is None:
      parts = [self.values[name] for name in sorted(self.values)]
    else:
      parts = []
      for partition in self.spec.partitions:
        if partition.name not in self.values:
          raise ValueError(
              "Could not construct relative path "
              f"because the value for {partition.name} is missing!")
        parts.append(partition.folder_for(self.values[partition.name]))
    return os.path.join("", *parts)

  def config_name(self) -> str:
    parts = []
    for partition_name in sorted(self.values):
      parts.append(f"{partition_name}={self.values[partition_name]}")
    return "/".join(parts)

  @classmethod
  def parse_tfds_partition_info(
      cls,
      tfds_name: str,
      spec: Optional[PartitionSpec] = None,
  ) -> PartitionInfo:
    """Returns the `PartitionInfo` corresponding to the given `tfds_name` and `spec`."""
    parts = tfds_name.split(",")
    if not parts:
      raise ValueError(f"Could not parse `{tfds_name}`!")
    partitions = {}
    for part in parts:
      name, value = part.split("=")
      partitions[name] = value
    return PartitionInfo(values=partitions, spec=spec)
