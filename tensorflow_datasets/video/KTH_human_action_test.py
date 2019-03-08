import tensorflow as tf
from tensorflow_datasets import my_dataset
import tensorflow_datasets.testing as tfds_test


class KTH_human_actionTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = my_dataset.KTH_human_action
  SPLITS = {  # Expected number of examples on each split from fake example.
      "train": 8,
      "test": 8,
      "validation":8
  }
  # If dataset `download_and_extract`s more than one resource:
  DL_EXTRACT_RESULT = {
      "walking": "/walking",  # Relative to fake_examples/my_dataset dir.
      "jogging":"/jogging",
      "running":"/running",
      "boxing":"/boxing",
      "handwaving":"/handwaving",
      "handclapping":"/handclapping"
  }

if __name__ == "__main__":
  tfds_test.test_main()
