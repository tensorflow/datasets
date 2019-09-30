"""Test for single coil files from fastmri."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import fastmri

class FastMRITest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = fastmri.fastMRI
    SPLITS = {
      "train": 1
    }
    DL_EXTRACT_RESULT = ['singlecoil_train.tar.gz']


if __name__ == "__main__":
  testing.test_main()
