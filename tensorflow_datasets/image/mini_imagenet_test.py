import tensorflow as tf
from tensorflow_datasets.image import mini_imagenet
import tensorflow_datasets.testing as tfds_test


class MiniImagenetTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = mini_imagenet.MiniImagenet
    SPLITS = {
        "train": 6,
        "validation": 4,
        "test": 4
    }


if __name__ == "__main__":
    tfds_test.test_main()
