"""credit_card_fraud dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured import credit_card_fraud


class CreditCardFraudTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(credit_card_fraud):
  DATASET_CLASS = credit_card_fraud.CreditCardFraud
  SPLITS = {
      "train": 1,
  }

  DL_EXTRACT_RESULT = "credit_card_fraud.csv"
  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()
