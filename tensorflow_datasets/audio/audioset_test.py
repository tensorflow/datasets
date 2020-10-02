"""audioset dataset."""

import tensorflow_datasets as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.audio import audioset
import tensorflow_datasets.testing as tfds_test


class AudioSetTest(tfds_test.DatasetBuilderTestCase):
    
  DATASET_CLASS = audioset.Audioset
  SPLITS = {
      'train': 4,
  }

  DL_EXTRACT_RESULT = {
      'file_1' : '--PJHxphWEs.mp3',
      'file_2' : '-275_wTLm-4.mp3',
      'file_3' : '08u-jdwjM74.mp3',
      'file_4' : 'X-5UcZiOIhQ.mp3',
  }

if __name__ == "__main__":
  tfds_test.test_main()

