"""
Mozilla CommonVoice Dataset Builder UnitTest
"""
import tensorflow_datasets.testing as tfds_test
from tensorflow_datasets.audio import commonvoice


class CommonVoiceTest(tfds_test.DatasetBuilderTestCase):
    """
    CommonVoice Tester Class
    """
    DATASET_CLASS = commonvoice.CommonVoice
    SPLITS = {"train":10, "test":10,"validation":10}
    DL_EXTRACT_RESULT = {"en":"."}
if __name__ == "__main__":
    tfds_test.test_main()
