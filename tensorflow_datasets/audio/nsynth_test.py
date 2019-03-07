"""
Nsynth Dataset Builder Unittest
"""
import tensorflow_datasets.testing as tfds_test
from tensorflow_datasets.audio import nsynth
import tensorflow_datasets as tfds

class NsynthTest(tfds_test.DatasetBuilderTestCase):
    """
    Nsynth Tester Class
    """
    DATASET_CLASS = nsynth.Nsynth
    SPLITS = {"train": 3, "test": 3, "valid": 3}
    DL_EXTRACT_RESULT = {"train": "nsynth-train.tfrecord",
                         "test": "nsynth-test.tfrecord",
                         "valid": "nsynth-valid.tfrecord",
                         "instrument_labels": "nsynth-instrument_labels.txt"}


if __name__ == "__main__":
    tfds_test.test_main()
