from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image \
    import B_ALL_White_Blood_Cancer_Microscopic_Image


class BAllWhiteBloodCancerMicroscopicImageTest(testing.DatasetBuilderTestCase):

    DATASET_CLASS = B_All_White_Blood_Cancer_Microscopic_Image.\
                                        BAllWhiteBloodCancerMicroscopicImage
    SPLITS = {
        'train': 2
    }

if __name__ == "__main__":
    testing.test_main()
