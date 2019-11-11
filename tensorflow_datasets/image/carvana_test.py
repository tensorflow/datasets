import tensorflow as tf
from tensorflow_datasets import carvana
import tensorflow_datasets.testing as tfds_test

class CarvanaTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = carvana.Carvana