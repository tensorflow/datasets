"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import covid_cxr

covid_cxr._IMAGE_SHAPE = (None, None, 3)

class CovidCxrTest(tfds.testing.DatasetBuilderTestCase):
    
  # TODO(covid_cxr):

    DATASET_CLASS = covid_cxr.CovidCxr
    BUILDER_CONFIG_NAMES_TO_TEST = ["224"]
    #_CONFIG = DATASET_CLASS.CovidCxrConfig
    SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 3,  # Number of fake test example
  }
    

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}

    DL_EXTRACT_RESULT = ['train.zip', 'test.zip']

if __name__ == "__main__":
  tfds.testing.test_main()

