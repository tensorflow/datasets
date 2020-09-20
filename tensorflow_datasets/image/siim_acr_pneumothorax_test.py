"""siim_acr_pneumothorax dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import siim_acr_pneumothorax


class SiimAcrPneumothoraxTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(siim_acr_pneumothorax):
  DATASET_CLASS = siim_acr_pneumothorax.SiimAcrPneumothorax
  SPLITS = {
      "train": 3,
  }
  
#   DL_EXTRACT_RESULT = {
#       "1.2.276.0.7230010.3.1.4.8323329.300.1517875162.258081": "1.2.276.0.7230010.3.1.4.8323329.300.1517875162.258081.dcm", 
#       "1.2.276.0.7230010.3.1.4.8323329.301.1517875162.280319": "1.2.276.0.7230010.3.1.4.8323329.301.1517875162.280319.dcm",
#       "1.2.276.0.7230010.3.1.4.8323329.302.1517875162.286330": "1.2.276.0.7230010.3.1.4.8323329.302.1517875162.286330.dcm",
#       "mask": "train-rle.csv"
      
#   }
  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()

