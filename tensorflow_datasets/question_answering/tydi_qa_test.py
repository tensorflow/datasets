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

"""Tests for tydi_qa dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.question_answering import tydi_qa


class TydiQATest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = tydi_qa.TydiQA

  DL_EXTRACT_RESULT = {
      "train": "train-v1.1.json",
      "validation": "dev-v1.1.json",
      "lang-validation": "",
  }
  DL_EXTRACT_RESULT.update(
      {
          f"translate-train-{lang}": f"tydiqa.translate.train.en-{lang}.json"
          for lang in tydi_qa.LANGUAGES
      }
  )

  SPLITS = {"train": 3, "validation": 2}
  SPLITS.update({f"validation-{lang}": 1 for lang in tydi_qa.LANGUAGES})
  SPLITS.update(
      {
          f"translate-train-{lang}": 1
          for lang in tydi_qa.LANGUAGES
          if lang != "en"
      }
  )


if __name__ == "__main__":
  testing.test_main()
