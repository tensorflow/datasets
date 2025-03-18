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

"""ClassLabel feature."""

from collections.abc import Iterable
from typing import Optional, Union

from etils import epath
import numpy as np
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json


class ClassLabel(tensor_feature.Tensor):
  """`FeatureConnector` for integer class labels."""

  # If updating the signature here, LabeledImage should likely be updated too.
  def __init__(
      self,
      *,
      num_classes: int | None = None,
      names: Iterable[str] | None = None,
      names_file: epath.PathLike | None = None,
      doc: feature_lib.DocArg = None,
  ):
    """Constructs a ClassLabel FeatureConnector.

    There are 3 ways to define a ClassLabel, which correspond to the 3
    arguments:

     * `num_classes`: create 0 to (num_classes-1) labels
     * `names`: a list of label strings
     * `names_file`: a file containing the list of labels.

    Note: On python2, the strings are encoded as utf-8.

    Args:
      num_classes: Number of classes. All labels must be < num_classes.
      names: String names for the integer classes. The order in which the names
        are provided is kept.
      names_file: Path to a file with names for the integer classes, one per
        line.
      doc: Documentation of this feature (e.g. description).
    """
    super(ClassLabel, self).__init__(shape=(), dtype=np.int64, doc=doc)

    self._num_classes: Optional[int] = None
    self._str2int: Optional[dict[str, int]] = None
    self._int2str: Optional[list[str]] = None

    # The label is explicitly set as undefined (no label defined)
    if all(a is None for a in (num_classes, names, names_file)):
      return

    if sum(a is not None for a in (num_classes, names, names_file)) != 1:
      raise ValueError(
          "Only a single argument of ClassLabel() should be provided."
      )

    if num_classes is not None:
      self._num_classes = num_classes
    elif names is not None:
      self.names = list(names)
    elif names_file is not None:
      self.names = _load_names_from_file(epath.Path(names_file))

  @property
  def num_classes(self) -> Optional[int]:
    return self._num_classes

  @property
  def names(self) -> list[str]:
    if not self._int2str:
      return [str(i) for i in range(self._num_classes)]
    return self._int2str

  @names.setter
  def names(self, new_names: list[str]):
    int2str = new_names
    # Names can only be defined once
    if self._int2str is not None and self._int2str != int2str:
      raise ValueError(
          "Trying to overwrite already defined ClassLabel names. Previous: {} "
          ", new: {}".format(self._int2str, int2str)
      )

    # Set-up [new] names
    self._int2str = int2str
    self._str2int = {name: i for i, name in enumerate(self._int2str)}
    if len(self._int2str) != len(self._str2int):
      raise ValueError(
          "Some label names are duplicated. Each label name should be unique."
      )

    # If num_classes has been defined, ensure that num_classes and names match
    num_classes = len(self._str2int)
    if self._num_classes is None:
      self._num_classes = num_classes
    elif self._num_classes != num_classes:
      raise ValueError(
          "ClassLabel number of names do not match the defined num_classes. "
          "Got {} names VS {} num_classes".format(
              num_classes, self._num_classes
          )
      )

  def str2int(self, str_value: str) -> int:
    """Conversion class name string => integer."""
    if self._str2int:
      return self._str2int[str_value]

    # No names provided, try to integerize
    failed_parse = False
    try:
      int_value = int(str_value)
    except ValueError:
      failed_parse = True
    if failed_parse or not 0 <= int_value < self._num_classes:
      raise ValueError("Invalid string class label %s" % str_value)
    return int_value

  def int2str(self, int_value: int) -> str:
    """Conversion integer => class name string."""
    if self._int2str:
      # Maybe should support batched np array/eager tensors, to allow things
      # like
      # out_ids = model(inputs)
      # labels = cifar10.info.features['label'].int2str(out_ids)
      return self._int2str[int_value]

    # No names provided, return str(int)
    if not 0 <= int_value < self._num_classes:
      raise ValueError("Invalid integer class label %d" % int_value)
    return str(int_value)

  def encode_example(self, example_data):
    if self._num_classes is None:
      raise ValueError(
          "Trying to use ClassLabel feature with undefined number of class. "
          "Please set ClassLabel.names or num_classes."
      )

    # If a string is given, convert to associated integer
    if isinstance(example_data, str):
      example_data = self.str2int(example_data)
    elif isinstance(example_data, bytes):
      # Accept bytes if user yield `tensor.numpy()`
      # Python 3 doesn't interpret byte strings as strings directly.
      example_data = self.str2int(example_data.decode("utf-8"))

    # Allowing -1 to mean no label.
    if not -1 <= example_data < self._num_classes:
      raise ValueError(
          "Class label %d greater than configured num_classes %d"
          % (example_data, self._num_classes)
      )
    return example_data

  def save_metadata(self, data_dir, feature_name=None) -> None:
    """See base class for details."""
    # Save names if defined
    if self._str2int is not None:
      names_filepath = self.get_names_filepath(data_dir, feature_name)
      _write_names_to_file(names_filepath, self.names)

  def load_metadata(self, data_dir, feature_name=None) -> Optional[list[str]]:
    """See base class for details."""
    # Restore names if defined
    names_filepath = self.get_names_filepath(data_dir, feature_name)
    try:
      self.names = _load_names_from_file(names_filepath)
    except OSError:
      pass

  def _additional_repr_info(self) -> dict[str, int]:
    return {"num_classes": self.num_classes}  # pytype: disable=bad-return-type  # always-use-property-annotation

  def repr_html(self, ex: int) -> str:
    """Class labels are displayed with their name."""
    if ex == -1:
      return "-"
    elif not self._int2str:
      return str(ex)
    else:
      return f"{ex} ({self.int2str(ex)})"

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.ClassLabel]
  ) -> "ClassLabel":
    if isinstance(value, dict):
      return cls(**value)
    return cls(num_classes=value.num_classes)

  def to_json_content(self) -> feature_pb2.ClassLabel:  # pytype: disable=signature-mismatch  # overriding-return-type-checks
    return feature_pb2.ClassLabel(num_classes=self.num_classes)

  @classmethod
  def get_names_filepath(cls, data_dir, feature_name: str) -> epath.Path:
    return epath.Path(data_dir) / f"{feature_name}.labels.txt"


def _load_names_from_file(names_filepath: epath.Path) -> list[str]:
  return [
      name.strip()
      for name in names_filepath.read_text().split("\n")
      if name.strip()  # Filter empty names
  ]


def _write_names_to_file(
    names_filepath: epath.Path, names: Iterable[str]
) -> None:
  names_filepath.write_text("\n".join(names) + "\n")
