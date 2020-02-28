

"""Tests for qmnist dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import qmnist

# testing/qmnist.py generates fake input data

qmnist._TRAIN_EXAMPLES = 10  # pylint: disable=protected-access
qmnist._TEST_EXAMPLES = 2  # pylint: disable=protected-access

class QmnistTest(testing.DatasetBuilderTestCase):
  # TODO(qmnist):
  DATASET_CLASS = qmnist.QMNIST
  SPLITS = {
      "train": 10,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "train-image",
      "train_labels": "train-label",
      "test_data": "test-image",
      "test_labels": "test-label",
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  testing.test_main()

