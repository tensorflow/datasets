"""Test for Opinosis Opinion Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.summarization import opinosis


class OpinosisTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = opinosis.Opinosis
  SPLITS = {
      "test": 2,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = ""


if __name__ == "__main__":
  testing.test_main()
