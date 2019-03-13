import tensorflow_datasets.testing as tfds_test
from tensorflow_datasets.image import stanford_online_products


class StanfordOnlineProductsTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = stanford_online_products.StanfordOnlineProducts
  SPLITS = {"train": 3, "test": 3}


if __name__ == "__main__":
  tfds_test.test_main()
