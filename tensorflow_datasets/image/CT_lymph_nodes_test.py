"""CT_lymph_nodes dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import CT_lymph_nodes


class CtLymphNodesTest(tfds.testing.DatasetBuilderTestCase):

  DATASET_CLASS = CT_lymph_nodes.CtLymphNodes
  SPLITS = {
      "train": 3,  # Number of fake train example
      
  }

  


if __name__ == "__main__":
  tfds.testing.test_main()

