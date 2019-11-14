import tensorflow as tf
from tensorflow_datasets.image import carvana
import tensorflow_datasets.testing as tfds_test

class CarvanaTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = carvana.Carvana

    # TODO

if __name__ == '__main__':
    tfds_test.test_main()