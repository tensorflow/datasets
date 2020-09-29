"""audioset dataset."""

import tensorflow_datasets as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.audio import audioset

class AudiosetTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(audioset):
  DATASET_CLASS = audioset.Audioset
  SPLITS = {
      "train": 3,   # Number of fake train example
                    # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}

class AudioSetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = audioset.AudioSet
  SPLITS = {
      'train': 4,
  }

  DL_EXTRACT_RESULT = {
      'summary_table':
          'id2label.json',
      'all_files': [
          '--PJHxphWEs.mp3', '-275_wTLm-4.mp3',
          '08u-jdwjM74.mp3', 'X-5UcZiOIhQ.mp3',
      ]
  }

if __name__ == "__main__":
  tfds.testing.test_main()

