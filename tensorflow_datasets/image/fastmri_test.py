"""TODO(my_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import fastmri

class FastMRITest(testing.DatasetBuilderTestCase):
    # TODO(fastmri):
    DATASET_CLASS = fastmri.fastMRI
    SPLITS = {
      "train": 6,  # Number of fake train example
      "test": 6,  # Number of fake test example
    }
    if challenge == 'singlecoil':
        DL_EXTRACT_RESULT = [
                            'singlecoil_train.tar.gz',
                            'singlecoil_test_v2.tar.gz'
                            ]
    else:
        DL_EXTRACT_RESULT = [
                             'multicoil_train.tar.gz',
                             'multicoil_test_v2.tar.gz'
                             ]


  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  testing.test_main()
