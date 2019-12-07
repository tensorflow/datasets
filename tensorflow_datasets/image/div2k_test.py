"""Test for div2k dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import div2k

class Div2kTest_bicubic_x2(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["bicubic_x2"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_bicubic_X2",
    "valid_lr_url": "DIV2K_valid_LR_bicubic_X2",
  }

class Div2kTest_bicubic_x3(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["bicubic_x3"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_bicubic_X3",
    "valid_lr_url": "DIV2K_valid_LR_bicubic_X3",
  }

class Div2kTest_bicubic_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["bicubic_x4"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_bicubic_X4",
    "valid_lr_url": "DIV2K_valid_LR_bicubic_X4",
  }

class Div2kTest_bicubic_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["bicubic_x8"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_x8",
    "valid_lr_url": "DIV2K_valid_LR_x8",
  }

class Div2kTest_unknown_x2(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["unknown_x2"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_unknown_X2",
    "valid_lr_url": "DIV2K_valid_LR_unknown_X2",
  }

class Div2kTest_unknown_x3(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["unknown_x3"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_unknown_X3",
    "valid_lr_url": "DIV2K_valid_LR_unknown_X3",
  }

class Div2kTest_unknown_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["unknown_x4"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_unknown_X4",
    "valid_lr_url": "DIV2K_valid_LR_unknown_X4",
  }

class Div2kTest_realistic_mild_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["realistic_mild_x4"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_mild",
    "valid_lr_url": "DIV2K_valid_LR_mild",
  }

class Div2kTest_realistic_difficult_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["realistic_difficult_x4"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_difficult",
    "valid_lr_url": "DIV2K_valid_LR_difficult",
  }

class Div2kTest_realistic_wild_x4(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["realistic_wild_x4"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
    "train_hr_url": "DIV2K_train_HR",
    "valid_hr_url": "DIV2K_valid_HR",
    "train_lr_url": "DIV2K_train_LR_wild",
    "valid_lr_url": "DIV2K_valid_LR_wild",
  }

if __name__ == "__main__":
  testing.test_main()