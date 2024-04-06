"""wake_vision dataset."""

import wake_vision_dataset_builder
import tensorflow_datasets.public_api as tfds

class WakeVisionTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for wake_vision dataset."""
  DATASET_CLASS = wake_vision_dataset_builder.Builder
  SPLITS = {
      'train_image': 16,  # Number of fake train image examples
      'train_bbox': 4,  # Number of fake train bbox examples
      'validation': 11,  # Number of fake validation examples
      'test': 10,  # Number of fake test examples
  }

  DL_EXTRACT_RESULT = {
      'train_images': ['wake-vision-train-dummy-1.tar.gz', 'wake-vision-train-dummy-2.tar.gz'],
      'validation_images': ['wake-vision-validation-dummy.tar.gz'],
      'test_images': ['wake-vision-test-dummy.tar.gz'],
      'train_image_metadata': 'wake_vision_train_image.csv',
      'train_bbox_metadata': 'wake_vision_train_bbox.csv',
      'validation_metadata': 'wake_vision_validation.csv',
      'test_metadata': 'wake_vision_test.csv',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
