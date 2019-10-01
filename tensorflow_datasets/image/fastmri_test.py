"""Test for single coil files from fastmri."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import fastmri

class FastMRITest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = fastmri.FastMRI
    SPLITS = {
      "train": 1,
      "test": 1
    }
    DL_EXTRACT_RESULT = ['extracted/singlecoil_train.tar.gz',
                         'extracted/singlecoil_test_v2.tar.gz']
    BUILDER_CONFIG_NAMES_TO_TEST = ["singlecoil"]

if __name__ == "__main__":
  testing.test_main()
