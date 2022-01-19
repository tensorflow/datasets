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

"""A parser for ranking-style LibSVM files.

Note that the LibSVM ranking file format does not have a formal specification.
This implementation supports the common formats that are available online and
will work with all the publically available LTR datasets such as MSLR-WEB,
Istella and Yahoo Webscope.
"""

import collections
import dataclasses
import re
from typing import Iterable, List, Mapping, Tuple

import numpy as np

# Type alias for a tuple representing a ranking example.
RankingExampleTuple = Tuple[str, Mapping[str, np.ndarray]]


@dataclasses.dataclass
class RankingExample:
  """Represents a parsed ranking example for a given query identifier.

  Attributes:
    qid: The query identifier.
    features: A mapping of feature name to feature values.
  """
  qid: str
  features: Mapping[str, List[float]]


class ParserError(Exception):
  """Raised when LibSVM-formatted contents cannot be parsed correctly."""

  def __init__(self, line_number: int, line: str, reason: str):
    """Initializes the instance.

    Args:
      line_number: The line number where the parser error occurred.
      line: The line where the parser error occurred.
      reason: An informative message about the nature of the parser error.
    """
    super().__init__(f"Unable to parse line {line_number} ('{line}'): {reason}")
    self.line_number = line_number
    self.line = line
    self.reason = reason


class LibSVMRankingParser(Iterable[RankingExampleTuple]):
  """A parser for LibSVM-formatted ranking files.

  This parser can parse an iterable of lines into an iterable of
  `RankingExampleTuple`s that contain the per-query labels and features.

  Example usage:
  >>> lines = ["1 qid:1 1:5.0 2:3.0", "2 qid:1 1:2.0 2:1.0"]
  >>> feature_names = {1: "bm25", 2: "tfidf"}
  >>> parser = LibSVMRankingParser(lines, feature_names)
  >>> for example in parser:
  ...   print(example[0])
  {'bm25': array([5., 2.]), 'tfidf': array([3., 1.]), 'label': array([1, 2])}

  The parser will raise a ParserError with an informative error message if the
  content being parsed does not match LibSVM ranking format.
  """

  def __init__(self,
               lines: Iterable[str],
               feature_names: Mapping[int, str],
               label_feature_name: str = "label",
               default_feature_value: float = 0.0):
    """Initializes the instance.

    Args:
      lines: The lines to parse.
      feature_names: A mapping from feature indices to feature names.
      label_feature_name: The name to assign to the label feature.
      default_feature_value: The default feature value to use when a feature is
        missing from the input.
    """
    self._lines = lines
    self._feature_names = feature_names
    self._label_feature_name = label_feature_name
    self._default_feature_value = default_feature_value
    self._current_example = None
    self._available_examples = collections.deque()

  def _parse_line(self, line_number: int, line: str):
    """Parses a single line of input from a LibSVM ranking file.

    This method will update the internal state of the parser and may produce a
    new item to be made available in `self._available_examples`.

    Args:
      line_number: The current line number. This may be used to generate more
        informative ParserError messages if such an error occurs.
      line: The line to parse.

    Raises:
      ParserError: If the parsing of given line failed.
    """
    # Remove comments and leading/trailing whitespace from line.
    line_clean, *_ = line.split("#", maxsplit=2)
    line_clean = line_clean.strip()

    # An empty line is allowed but should be skipped during parsing.
    if not line_clean:
      return

    # Split by space separators.
    try:
      label, qid, *features = re.split(r"\s+", line_clean)
    except ValueError as value_error:
      raise ParserError(
          line_number, line,
          "could not extract label, qid and features") from value_error

    # Convert relevance label to float.
    try:
      label = float(label)
    except ValueError as value_error:
      raise ParserError(
          line_number, line,
          f"label '{label}' could not be converted to a float") from value_error

    # Extract qid.
    if qid[:4] != "qid:":
      raise ParserError(line_number, line,
                        "line must contain a qid after the relevance label")
    qid = qid[4:]
    if not qid:
      raise ParserError(line_number, line, "qid can not be empty")

    # Construct a feature dict containing default values.
    feature_dict = {
        feature_name: self._default_feature_value
        for feature_name in self._feature_names.values()
    }

    # Parse all features and add them to the feature dict.
    for feature in features:
      try:
        index, value = feature.split(":", maxsplit=2)
        index = int(index)
        value = float(value)
        # Only add features if they map to a feature name in the
        # `_feature_names` dict. All other features are ignored.
        if index in self._feature_names:
          feature_dict[self._feature_names[index]] = value
      except ValueError as value_error:
        raise ParserError(
            line_number, line,
            f"failed to extract feature index and value from '{feature}'"
        ) from value_error

    # Add label to feature dict.
    feature_dict[self._label_feature_name] = label

    # Add the parsed qid and feature dictionary to the current example.
    self._add_to_current_example(qid, feature_dict)

  def _add_to_current_example(self, qid: str, feature_map: Mapping[str, float]):
    """Adds given qid and feature_map to the current example.

    If the qid matches the current example qid, this will add the features in
    given feature_map to the current example.
    If the qid does not match the current example qid, this will store the
    current example and then create a new one with given qid and feature_map.

    Args:
      qid: The query identifier.
      feature_map: A mapping of feature names to feature values.
    """
    if self._current_example is None:
      self._current_example = RankingExample(qid, collections.defaultdict(list))

    if self._current_example.qid != qid:
      self._store_current_example()
      self._current_example = RankingExample(qid, collections.defaultdict(list))

    for key, value in feature_map.items():
      self._current_example.features[key].append(value)

  def _store_current_example(self):
    """Store the current ranking example in numpy format.

    This method converts the current example to a RankingExampleTuple and stores
    it in `self._available_examples` so that it can be yielded by
    `self.__iter__`.
    """
    qid = self._current_example.qid
    np_features_dict = {
        key: np.array(value)
        for key, value in self._current_example.features.items()
    }
    self._available_examples.append((qid, np_features_dict))

  def _end_of_parse(self):
    """Signals the end of parsing has been reached.

    This method will store the item that is currently being parsed so it is
    available in `self._available_examples`.
    """
    if self._current_example is not None:
      self._store_current_example()
      self._current_example = None

  def __iter__(self):
    """Iterates over `RankingExampleTuple`s.

    Yields:
      `RankingExampleTuple` that represent a single query.

    Raises:
      ParserError: If parsing failed.
    """
    # Parse each line and yield the resulting examples as they become available.
    for line_number, line in enumerate(self._lines, start=1):
      self._parse_line(line_number, line)
      while self._available_examples:
        yield self._available_examples.popleft()

    # Signal the end has been reached and yield any remaining items.
    self._end_of_parse()
    while self._available_examples:
      yield self._available_examples.popleft()
