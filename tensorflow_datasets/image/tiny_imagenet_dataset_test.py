"""TODO(tiny_imagenet_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import tiny_imagenet_dataset


class TinyImagenetDatasetTest(testing.DatasetBuilderTestCase):
  # TODO(tiny_imagenet_dataset):
  DATASET_CLASS = tiny_imagenet_dataset.TinyImagenetDataset
  SPLITS = {
      "train": 4,  # Number of fake train example
      "validation": 2,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = ""
  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  testing.test_main()

