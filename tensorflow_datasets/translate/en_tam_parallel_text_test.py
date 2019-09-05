"""Tests for English-Tamil parallel dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.translate import en_tam_parallel_text


class EnTamParallelTextTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = en_tam_parallel_text.EnTamParallelText
  SPLITS = {"train": 2, "validation": 2, "test": 2}
if __name__ == "__main__":
  testing.test_main()