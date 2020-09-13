"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import covid_cxr
import tensorflow_datasets.testing as testing

class CovidCxrTest(tfds.testing.DatasetBuilderTestCase):
    
  # TODO(covid_cxr):
    
    DATASET_CLASS = covid_cxr.CovidCxr
    #assert isinstance(covid_cxr.supervised_keys, tuple)
    #assert len(covid_cxr.supervised_keys) == 2
    class CovidCxrOriginalTest(testing.DatasetBuilderTestCase):
          DATASET_CLASS = covid_cxr.CovidCxr
          BUILDER_CONFIG_NAMES_TO_TEST = ["original"]
          SPLITS = {
              "train": 3,
              "test": 3,
          }
           
            
          DL_EXTRACT_RESULT = {
                          "train": "original/train",  
                          "test": "original/test"
                                  }


    class CovidCxr224Test(testing.DatasetBuilderTestCase):
          DATASET_CLASS = covid_cxr.CovidCxr
          BUILDER_CONFIG_NAMES_TO_TEST = ["224"]
          SPLITS = {
              "train": 3,
              "test": 3,
          }
            
          DL_EXTRACT_RESULT = {
                          "train": "224/train", 
                          "test": "224/test"
                                  }


    class CovidCxr480Test(testing.DatasetBuilderTestCase):
          DATASET_CLASS = covid_cxr.CovidCxr
          BUILDER_CONFIG_NAMES_TO_TEST = ["480"]
          SPLITS = {
              "train": 3,
              "test": 3,}
            
          DL_EXTRACT_RESULT = {
                        "train": "480/train",  
                        "test": "480/test"
          }

if __name__ == "__main__":
      tfds.testing.test_main()

