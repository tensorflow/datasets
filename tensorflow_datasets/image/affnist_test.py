from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing

class AffnistTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = affnist.Affnist
  SPLITS = {
      "train": 8,
      "validation": 1,
      "test": 1,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "training_batches",
      "validation_data": "validation_batches",
      "test_data": "test_batches",
  }

if __name__ == "__main__":
  testing.test_main()
