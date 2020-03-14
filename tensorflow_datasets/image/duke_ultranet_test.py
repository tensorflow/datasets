"""TODO(duke_ultranet): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import duke_ultranet


class DukeUltranetTest(testing.DatasetBuilderTestCase):
  # TODO(duke_ultranet):
  DATASET_CLASS = duke_ultranet.DukeUltranet
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  testing.test_main()

