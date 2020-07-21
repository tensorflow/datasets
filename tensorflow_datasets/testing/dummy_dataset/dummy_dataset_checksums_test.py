import os

from tensorflow_datasets import testing
from dummy_dataset_checksums import DummyDatasetChecksums


class DummyDatasetChecksumTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = DummyDatasetChecksums
  SPLITS = {
      'train': 20,
  }


if __name__ == "__main__":
  testing.test_main()
