"""covid_cxr dataset."""

from tensorflow_datasets.image_classification import covid_cxr
import tensorflow_datasets.testing as tfds_test

class CovidCxrTest(tfds_test.DatasetBuilderTestCase):
    
    DATASET_CLASS = covid_cxr.CovidCxr
    BUILDER_CONFIG_NAMES_TO_TEST = ["224"]
    
    SPLITS = {"train": 3,
              "test": 3,}   
    
    DL_EXTRACT_RESULT = {'train': './train_224.zip', 
                         'test': './test_224.zip'}
    
if __name__ == "__main__":
    tfds_test.test_main()

'''
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
'''