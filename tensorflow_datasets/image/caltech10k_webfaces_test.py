import tensorflow as tf
from tensorflow_datasets.image import caltech10k_webfaces
import tensorflow_datasets.testing as tfds_test


class Caltech10K_WebFacesTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = caltech10k_webfaces.Caltech10K_WebFaces
  SPLITS = {  
    "train": 10,
  }
  

if __name__ == "__main__":
  tfds_test.test_main()