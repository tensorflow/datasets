"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import covid_cxr
import tensorflow_datasets.testing as testing

class CovidCxrTest(tfds.testing.DatasetBuilderTestCase):
    
  # TODO(covid_cxr):
    DATASET_CLASS = covid_cxr.CovidCxr
    supervised_keys = ('image', 'label')
    class CovidCxrOriginalTest(testing.DatasetBuilderTestCase): 
                  covid_cxr._IMAGE_SHAPE = (None, None, 3)
                  DATASET_CLASS = covid_cxr.CovidCxr
                  BUILDER_CONFIG_NAMES_TO_TEST = ["original"]
                  SPLITS = {"train": 3, "test": 3,}
                  DL_EXTRACT_RESULT = {
                              "image": "original",  
                              "label": "original"
                                      }


    class CovidCxr224Test(testing.DatasetBuilderTestCase):
                  covid_cxr._IMAGE_SHAPE = (224, 224, 3)
                  DATASET_CLASS = covid_cxr.CovidCxr
                  BUILDER_CONFIG_NAMES_TO_TEST = ["224"]
                  SPLITS = { "train": 3,"test": 3,}
                  DL_EXTRACT_RESULT = {
                                  "image": "224", 
                                  "label": "224"
                                          }


    class CovidCxr480Test(testing.DatasetBuilderTestCase):
                  covid_cxr._IMAGE_SHAPE = (480, 480, 3)
                  DATASET_CLASS = covid_cxr.CovidCxr
                  BUILDER_CONFIG_NAMES_TO_TEST = ["480"]
                  SPLITS = {
                      "train": 3,
                      "test": 3,}

                  DL_EXTRACT_RESULT = {
                                "image": "480",  
                                "label": "480"
                  }

if __name__ == "__main__":
      tfds.testing.test_main()

