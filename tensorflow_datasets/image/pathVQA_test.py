"""pathVQA dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import pathVQA


class PathvqaTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(pathVQA):
  DATASET_CLASS = pathVQA.Pathvqa
  SPLITS = {
      "train": 4,
      "test": 4,
  }

  DL_EXTRACT_RESULT = {
      "train": "train",
      "test": "test",
  }


if __name__ == "__main__":
  tfds.testing.test_main()

