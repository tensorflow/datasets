##structure segmentation test script 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import structseg


class StructsegTest(testing.DatasetBuilderTestCase):
  
  DATASET_CLASS = structseg.Structseg
  SPLITS = {
      "train": 1,  # Number of fake train example
  }


  DL_EXTRACT_RESULT = {
      "name1": "/tensorflow_datasets/testing/test_data/fake_examples/structseg"  
  }



if __name__ == "__main__":
  testing.test_main()

