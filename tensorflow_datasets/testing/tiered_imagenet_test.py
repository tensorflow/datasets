import tensorflow as tf
from tensorflow_datasets.image import tiered_imagenet
import tensorflow_datasets.testing as tfds_test


class TieredImagenetTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = tiered_imagenet.TieredImagenet
    SPLITS = {
        "train": 10,
        "validation": 3,
        "test": 4
    }


if __name__ == "__main__":
    tfds_test.test_main()
