# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for cbis_ddsm dataset module."""
from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import cbis_ddsm


class CuratedBreastImagingDDSMOriginalCalcTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cbis_ddsm.CuratedBreastImagingDDSM
  BUILDER_CONFIG_NAMES_TO_TEST = ['original-calc']
  SPLITS = {
      'train': 3,  # Abnormalities: 7
      'test': 2,  # Abnormalities: 4
  }
  DL_EXTRACT_RESULT = {
      'test': 'calc_case_description_test_set.csv',
      'train': 'calc_case_description_train_set.csv',
  }


class CuratedBreastImagingDDSMOriginalMassTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cbis_ddsm.CuratedBreastImagingDDSM
  BUILDER_CONFIG_NAMES_TO_TEST = ['original-mass']
  SPLITS = {
      'train': 3,  # Abnormalities: 10
      'test': 2,  # Abnormalities: 4
  }
  DL_EXTRACT_RESULT = {
      'test': 'mass_case_description_test_set.csv',
      'train': 'mass_case_description_train_set.csv',
  }


class CuratedBreastImagingDDSMPatchesTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cbis_ddsm.CuratedBreastImagingDDSM
  BUILDER_CONFIG_NAMES_TO_TEST = ['patches']
  SPLITS = {
      # Total patches = [(10 + 4 + 7 + 4) + (3 + 2 + 3 + 2)] * 10
      'train': 280,
      'validation': 40,
      'test': 30,
  }
  DL_EXTRACT_RESULT = {
      'calc-test': 'calc_case_description_test_set.csv',
      'calc-train': 'calc_case_description_train_set.csv',
      'mass-test': 'mass_case_description_test_set.csv',
      'mass-train': 'mass_case_description_train_set.csv',
  }


if __name__ == '__main__':
  testing.test_main()
