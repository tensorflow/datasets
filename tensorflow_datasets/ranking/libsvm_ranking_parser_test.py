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

"""Tests for libsvm_ranking_parser."""

from tensorflow_datasets import testing
from tensorflow_datasets.ranking.libsvm_ranking_parser import LibSVMRankingParser
from tensorflow_datasets.ranking.libsvm_ranking_parser import ParserError

# The following is a test dataset that exhibits some of the LibSVM edge cases
# which should be appropriately handled by the parser.
_TEST_DATASET = """
3 qid:1 1:1 2:1 3:0 4:0.2 5:0  # Line-comments should be ignored.
1 qid:1 1:0 2:0 3:1 4:0.1 5:1
0  qid:1  \t 1:0   2:1   3:0   4:0.4   5:0  # Extra spacing in a line is fine.
0 qid:1 1:0 2:0 3:1 4:0.3 5:0
0 qid:2 1:0 2:0 3:1 4:0.2 5:0  # Feature values after comment should be ignored:
1 qid:2 1:1 2:0 3:1 4:0.4 5:0  # 1:10 2:20 3:30 4:40 5:50
# just a comment, this entire line should be ignored by the parser.
# empty lines should also be ignored:

0 qid:2 1:0 2:0 3:1 4:0.1 5:0
0 qid:2 1:0 2:0 3:1 4:0.2 5:0

# feature 6 on the next line will be ignored if it is not specified in the
# feature_names map of the parser (see first unit test):
1 qid:2 1:0 2:0 3:1 4:0.1 5:1 6:2
   # Leading and trailing white space should be ignored:
   2 qid:2 1:1 2:1 3:0 4:0.3 5:0  \t
3 qid:3 1:1         4:0.4 5:1  # missing features should have default value (0)
0 qid:3 1:0 2:1 3:1 4:0.5 5:0
"""


class LibSVMRankingParserTest(testing.TestCase):

  def test_parses_a_libsvm_ranking_dataset(self):

    results = iter(
        LibSVMRankingParser(
            _TEST_DATASET.split("\n"),
            feature_names={
                1: "bm25",
                2: "tfidf",
                3: "querylen",
                4: "doclen",
                5: "qualityscore"
            }))

    qid, features = next(results)
    self.assertEqual(qid, "1")
    self.assertAllEqual(features["label"], [3., 1., 0., 0.])
    self.assertAllEqual(features["bm25"], [1., 0., 0., 0.])
    self.assertAllEqual(features["tfidf"], [1., 0., 1., 0.])
    self.assertAllEqual(features["querylen"], [0., 1., 0., 1.])
    self.assertAllEqual(features["doclen"], [0.2, 0.1, 0.4, 0.3])
    self.assertAllEqual(features["qualityscore"], [0., 1., 0., 0])

    qid, features = next(results)
    self.assertEqual(qid, "2")
    self.assertAllEqual(features["label"], [0., 1., 0., 0., 1., 2.])
    self.assertAllEqual(features["bm25"], [0., 1., 0., 0., 0., 1.])
    self.assertAllEqual(features["tfidf"], [0., 0., 0., 0., 0., 1.])
    self.assertAllEqual(features["querylen"], [1., 1., 1., 1., 1., 0.])
    self.assertAllEqual(features["doclen"], [0.2, 0.4, 0.1, 0.2, 0.1, 0.3])
    self.assertAllEqual(features["qualityscore"], [0., 0., 0., 0., 1., 0.])

    qid, features = next(results)
    self.assertEqual(qid, "3")
    self.assertAllEqual(features["label"], [3., 0.])
    self.assertAllEqual(features["bm25"], [1., 0.])
    self.assertAllEqual(features["tfidf"], [0., 1.])
    self.assertAllEqual(features["querylen"], [0., 1.])
    self.assertAllEqual(features["doclen"], [0.4, 0.5])
    self.assertAllEqual(features["qualityscore"], [1., 0.])

    # Assert that the end of the file has been reached.
    with self.assertRaises(StopIteration):
      next(results)

  def test_raises_error_if_line_only_contains_label(self):
    contents = ["1"]
    with self.assertRaisesRegex(ParserError,
                                "could not extract label, qid and features"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_label_is_not_a_number(self):
    contents = ["abc qid:1 2:0.0 3:0.0"]
    with self.assertRaisesRegex(
        ParserError, "label 'abc' could not be converted to a float"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_qid_is_missing(self):
    contents = ["0 2:0.0 3:0.0"]
    with self.assertRaisesRegex(
        ParserError, "line must contain a qid after the relevance label"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_qid_is_malformatted(self):
    contents = ["1 qid: 2:0.0 3:0.0"]
    with self.assertRaisesRegex(ParserError, "qid can not be empty"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_feature_index_is_malformatted(self):
    contents = ["1 qid:1 2:0.0 _12_:0.0"]
    with self.assertRaisesRegex(
        ParserError,
        "failed to extract feature index and value from '_12_:0.0'"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_feature_value_is_malformatted(self):
    contents = ["1 qid:1 2:0.0 3:0.00.1 4:10.0"]
    with self.assertRaisesRegex(
        ParserError,
        "failed to extract feature index and value from '3:0.00.1'"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_if_feature_is_not_separated_by_colon(self):
    contents = ["1 qid:1 2:0.0 3=0.1 4:10.0"]
    with self.assertRaisesRegex(
        ParserError, "failed to extract feature index and value from '3=0.1'"):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_with_offending_line_number(self):
    contents = ["1 qid:1 2:0.0", "malformatted line", "1 qid:1 2:0.0"]
    with self.assertRaisesWithPredicateMatch(
        ParserError, lambda error: error.line_number == 2):
      for _ in LibSVMRankingParser(contents, {}):
        pass

  def test_raises_error_with_offending_line(self):
    contents = ["1 qid:1 2:1000.0", "2 qid:1 9:9.9", "malformatted line"]
    with self.assertRaisesWithPredicateMatch(
        ParserError, lambda error: error.line == "malformatted line"):
      for _ in LibSVMRankingParser(contents, {}):
        pass


if __name__ == "__main__":
  testing.test_main()
