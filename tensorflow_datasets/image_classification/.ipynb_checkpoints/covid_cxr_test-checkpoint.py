"""covid_cxr dataset."""

from tensorflow_datasets.image_classification import covid_cxr
import tensorflow_datasets.testing as tfds_test

class CovidCxr224Test(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = covid_cxr.CovidCxr
    BUILDER_CONFIG_NAMES_TO_TEST = ['224']
    
    SPLITS = {'train': 3,
              'test': 3,}   
        
    DL_EXTRACT_RESULT = ['train_224.zip', 'test_224.zip']
        
class CovidCxr480Test(tfds_test.DatasetBuilderTestCase):
    
    DATASET_CLASS = covid_cxr.CovidCxr
    BUILDER_CONFIG_NAMES_TO_TEST = ['480']
    
    SPLITS = {"train": 3,
              "test": 3,}   
        
    DL_EXTRACT_RESULT = ['train_480.zip', 'test_480.zip']

class CovidCxrOriginalTest(tfds_test.DatasetBuilderTestCase):
    
    DATASET_CLASS = covid_cxr.CovidCxr
    BUILDER_CONFIG_NAMES_TO_TEST = ["original"]
    
    SPLITS = {"train": 3,
              "test": 3,}   
        
    DL_EXTRACT_RESULT = ['train_original.zip', 'test_original.zip']
    
if __name__ == "__main__":
    tfds_test.test_main()