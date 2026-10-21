"""mrnet dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import mrnet

mrnet._IMAGE_SHAPE = (256, 256, 1)


class MrnetTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(mrnet):
  DATASET_CLASS = mrnet.Mrnet
  SPLITS = {
      "train": 60,  # Number of fake train example
      "test": 15,
  }

  DL_EXTRACT_RESULT = {
      "image": "train",
      "label": "train_labels.csv",
  }


if __name__ == "__main__":
  tfds.testing.test_main()
