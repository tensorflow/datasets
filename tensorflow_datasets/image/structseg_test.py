'''
Structure Segmentation unit test
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import structseg


class StructsegTest(testing.DatasetBuilderTestCase):
    '''
    Structure Segmentation unit test
    '''
    DATASET_CLASS = structseg.Structseg
    SPLITS = {
        "train": 1,  # Number of fake train example
    }

if __name__ == "__main__":
    testing.test_main()
