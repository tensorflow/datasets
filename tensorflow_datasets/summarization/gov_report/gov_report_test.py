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

"""gov_report dataset."""

import json

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.summarization.gov_report import gov_report

_REPORT = r"""
{
  "section_title":"",
  "paragraphs":[
  ],
  "subsections":[
    {
      "section_title":"Introduction",
      "paragraphs":[
        "p1",
        "p2"
      ],
      "subsections":[
        {
          "section_title":"Background",
          "paragraphs":[
            "p3"
          ],
          "subsections":[
          ]
        }
      ]
    },
    {
      "section_title":"Conclusion",
      "paragraphs":[
        "p6"
      ],
      "subsections":[
      ]
    }
  ]
}
"""


class GovReportTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for gov_report dataset."""
  DATASET_CLASS = gov_report.GovReport
  SPLITS = {
      tfds.Split.TRAIN: 1,
      tfds.Split.VALIDATION: 1,
      tfds.Split.TEST: 1,
  }

  def test_flatten_structures_whitespace(self):
    self.assertEqual(
        gov_report._flatten_structure(json.loads(_REPORT), " ", 1, False),
        " Introduction p1 p2 Background p3 Conclusion p6")

  def test_flatten_structures_html(self):
    self.assertEqual(
        gov_report._flatten_structure(json.loads(_REPORT), "\n", 1, True),
        "<h1></h1>\n<h2>Introduction</h2>\np1\np2\n<h3>Background</h3>\np3\n<h2>Conclusion</h2>\np6"
    )


if __name__ == "__main__":
  tfds.testing.test_main()
