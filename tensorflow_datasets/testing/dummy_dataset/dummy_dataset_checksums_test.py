import os
from tensorflow_datasets import testing
from dummy_dataset_checksums import DummyDatasetChecksums
from tensorflow_datasets.image_classification import cats_vs_dogs


cats_vs_dogs._NUM_CORRUPT_IMAGES = 0  # pylint: disable=protected-access

class DummyDatasetChecksumTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = DummyDatasetChecksums
  EXAMPLE_DIR = os.path.join(DummyDatasetChecksums.code_dir, "fake_example")
  SPLITS = {
      'train': 4
  }
  DL_EXTRACT_RESULT = 'cats_vs_dogs.zip'

if __name__ == "__main__":
  testing.test_main()
