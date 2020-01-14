"""Database of character image features; try to identify the letter."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import letter_recognition

class LetterRecognitionTest(testing.DatasetBuilderTestCase):

  DATASET_CLASS = letter_recognition.LetterRecognition
  SPLITS = {

      "train": 1,

  }

  DL_EXTRACT_RESULT = {'letter-recognition.data'}

if __name__ == "__main__":
  testing.test_main()

