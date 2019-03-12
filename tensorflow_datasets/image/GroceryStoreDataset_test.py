from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import GroceryStoreDataset

num_classes=len(GroceryStoreDataset._CLASS_NAMES)

class GroceryStore(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = GroceryStoreDataset.GroceryStore
  SPLITS = {  
      "train": 2*num_classes,
      "test": 2*num_classes,
  }
  
 

if __name__ == "__main__":
  testing.test_main()