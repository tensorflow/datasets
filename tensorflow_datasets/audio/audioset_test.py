"""audioset dataset."""

from tensorflow_datasets.audio import audioset
import tensorflow_datasets.testing as tfds_test

class AudioSetTest(tfds_test.DatasetBuilderTestCase):

  DATASET_CLASS = audioset.Audioset
  SPLITS = {
      "train": 4,
  }
  DL_EXTRACT_RESULT = None
  SKIP_CHECKSUMS = True

if __name__ == "__main__":
  tfds_test.test_main()
