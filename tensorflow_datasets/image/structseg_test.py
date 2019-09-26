"""TODO(structseg): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import structseg


class StructsegTest(testing.DatasetBuilderTestCase):
  # TODO(structseg):
  DATASET_CLASS = structseg.Structseg
  SPLITS = {
      "train": 2,  # Number of fake train example
      #"test": 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      "name1": "/tensorflow_datasets//testing/test_data/fake_examples/structseg"  # Relative to fake_examples/my_dataset dir.
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  testing.test_main()

