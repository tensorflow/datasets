"""TODO(my_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing

import spineweb


class SpineWebTest(testing.DatasetBuilderTestCase):
    # TODO(my_dataset):
    DATASET_CLASS = spineweb.SpineWeb
    SPLITS = {
        "train": 2,  # Number of fake train example
        "test": 1,  # Number of fake test example
    }

    # If you are calling `download/download_and_extract` with a dict, like:
    #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
    # then the tests needs to provide the fake output paths relative to the
    # fake data directory
    # DL_EXTRACT_RESULT = {
    #     'train': "training_images",
    #     'train_csv': "training_angles.csv",
    #     'test': "test_images",
    #     'test_csv': "test_angles.csv"
    # }
    DL_EXTRACT_RESULT = {
        'train': '',
        'train_csv': '',
        'test': '',
        'test_csv': ''
    }


if __name__ == "__main__":
    testing.test_main()
