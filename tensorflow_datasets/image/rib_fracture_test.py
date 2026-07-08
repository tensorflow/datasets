"""rib_fracture dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import rib_fracture


class RibFractureTest(tfds.testing.DatasetBuilderTestCase):
    # TODO(rib_fracture):
    DATASET_CLASS = rib_fracture.RibFracture
    SPLITS = {"train": 10}

    DL_EXTRACT_RESULT = {
        'image_slice': 'image.zip',
        'mask_slice': 'mask.zip'
    }


if __name__ == "__main__":
    tfds.testing.test_main()