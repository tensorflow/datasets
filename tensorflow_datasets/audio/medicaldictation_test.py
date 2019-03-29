"""
ezDI medical dictation Dataset Builder UnitTest
"""
import tensorflow_datasets.testing as tfds_test
from tensorflow_datasets.audio import medicaldictation


class MedicalDictationTest(tfds_test.DatasetBuilderTestCase):
  """
  MedicalDictation Tester Class
  """
  DATASET_CLASS = medicaldictation.MedicalDictation
  SPLITS = {"train": 5, "test": 5}


if __name__ == "__main__":
  tfds_test.test_main()
