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

"""UnifiedQA dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.unifiedqa import unifiedqa


class UnifiedQAAI2ScienceElementaryTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ai2_science_elementary."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['ai2_science_elementary']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'ai2_science_elementary/train.tsv',
      'validation': 'ai2_science_elementary/dev.tsv',
      'test': 'ai2_science_elementary/test.tsv',
  }


class UnifiedQAAI2ScienceMiddleTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ai2_science_middleai2_science_middle."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['ai2_science_middle']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'ai2_science_middle/train.tsv',
      'validation': 'ai2_science_middle/dev.tsv',
      'test': 'ai2_science_middle/test.tsv',
  }


class UnifiedQAAmbigQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ambigqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['ambigqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'ambigqa/train.tsv',
      'validation': 'ambigqa/dev.tsv',
  }


class UnifiedQAARCEasyTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_easy."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_easy']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_easy/train.tsv',
      'validation': 'arc_easy/dev.tsv',
      'test': 'arc_easy/test.tsv',
  }


class UnifiedQAARCEasyDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_easy_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_easy_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_easy_dev/train.tsv',
      'validation': 'arc_easy_dev/dev.tsv',
      'test': 'arc_easy_dev/test.tsv',
  }


class UnifiedQAARCEasyIRTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_easy_with_ir."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_easy_with_ir']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_easy_with_ir/train.tsv',
      'validation': 'arc_easy_with_ir/dev.tsv',
      'test': 'arc_easy_with_ir/test.tsv',
  }


class UnifiedQAARCEasyIRDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_easy_with_ir_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_easy_with_ir_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_easy_with_ir_dev/train.tsv',
      'validation': 'arc_easy_with_ir_dev/dev.tsv',
      'test': 'arc_easy_with_ir_dev/test.tsv',
  }


class UnifiedQAARCHardTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_hard."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_hard']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_hard/train.tsv',
      'validation': 'arc_hard/dev.tsv',
      'test': 'arc_hard/test.tsv',
  }


class UnifiedQAARCHardDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_hard_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_hard_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_hard_dev/train.tsv',
      'validation': 'arc_hard_dev/dev.tsv',
      'test': 'arc_hard_dev/test.tsv',
  }


class UnifiedQAARCHardIRTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_hard_with_ir."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_hard_with_ir']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_hard_with_ir/train.tsv',
      'validation': 'arc_hard_with_ir/dev.tsv',
      'test': 'arc_hard_with_ir/test.tsv',
  }


class UnifiedQAARCHardIRDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for arc_hard_with_ir_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['arc_hard_with_ir_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'arc_hard_with_ir_dev/train.tsv',
      'validation': 'arc_hard_with_ir_dev/dev.tsv',
      'test': 'arc_hard_with_ir_dev/test.tsv',
  }


class UnifiedQABoolQTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for boolq."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['boolq']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'boolq/train.tsv',
      'validation': 'boolq/dev.tsv',
  }


class UnifiedQABoolQNPTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for boolq_np."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['boolq_np']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'boolq_np/train.tsv',
      'validation': 'boolq_np/dev.tsv',
  }


class UnifiedQACQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for commonsenseqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['commonsenseqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'commonsenseqa/train.tsv',
      'validation': 'commonsenseqa/dev.tsv',
      'test': 'commonsenseqa/test.tsv',
  }


class UnifiedQACQATestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for commonsenseqa_test."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['commonsenseqa_test']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'commonsenseqa_test/train.tsv',
      'validation': 'commonsenseqa_test/dev.tsv',
      'test': 'commonsenseqa_test/test.tsv',
  }


class UnifiedQAContrastSetsBoolQTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for contrast_sets_boolq."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['contrast_sets_boolq']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'contrast_sets_boolq/train.tsv',
      'validation': 'contrast_sets_boolq/dev.tsv',
  }


class UnifiedQAContrastSetsDROPTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for contrast_sets_drop."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['contrast_sets_drop']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'contrast_sets_drop/train.tsv',
      'validation': 'contrast_sets_drop/dev.tsv',
  }


class UnifiedQAContrastSetsQuorefTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for contrast_sets_quoref."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['contrast_sets_quoref']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'contrast_sets_quoref/train.tsv',
      'validation': 'contrast_sets_quoref/dev.tsv',
  }


class UnifiedQAContrastSetsROPESTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for contrast_sets_ropes."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['contrast_sets_ropes']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'contrast_sets_ropes/train.tsv',
      'validation': 'contrast_sets_ropes/dev.tsv',
  }


class UnifiedQADROPTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for drop."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['drop']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'drop/train.tsv',
      'validation': 'drop/dev.tsv',
  }


class UnifiedQAMCTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for mctest."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['mctest']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'mctest/train.tsv',
      'validation': 'mctest/dev.tsv',
  }


class UnifiedQAMCTestCorrectedTheSeparatorTest(
    tfds.testing.DatasetBuilderTestCase
):
  """Tests for mctest_corrected_the_separator."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['mctest_corrected_the_separator']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'mctest_corrected_the_separator/train.tsv',
      'validation': 'mctest_corrected_the_separator/dev.tsv',
  }


class UnifiedQAMultiRCTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for multirc."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['multirc']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'multirc/train.tsv',
      'validation': 'multirc/dev.tsv',
  }


class UnifiedQANarrativeQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for narrativeqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['narrativeqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'narrativeqa/train.tsv',
      'validation': 'narrativeqa/dev.tsv',
      'test': 'narrativeqa/test.tsv',
  }


class UnifiedQANarrativeQADevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for narrativeqa_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['narrativeqa_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'narrativeqa_dev/train.tsv',
      'validation': 'narrativeqa_dev/dev.tsv',
      'test': 'narrativeqa_dev/test.tsv',
  }


class UnifiedQANatQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions/train.tsv',
      'validation': 'natural_questions/dev.tsv',
  }


class UnifiedQANatQADirectAnsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions_direct_ans."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions_direct_ans']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions_direct_ans/train.tsv',
      'validation': 'natural_questions_direct_ans/dev.tsv',
      'test': 'natural_questions_direct_ans/test.tsv',
  }


class UnifiedQANatQADirectAnsTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions_direct_ans_test."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions_direct_ans_test']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions_direct_ans_test/train.tsv',
      'validation': 'natural_questions_direct_ans_test/dev.tsv',
      'test': 'natural_questions_direct_ans_test/test.tsv',
  }


class UnifiedQANatQADPRParaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions_with_dpr_para."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions_with_dpr_para']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions_with_dpr_para/train.tsv',
      'validation': 'natural_questions_with_dpr_para/dev.tsv',
  }


class UnifiedQANatQADPRParaTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for natural_questions_with_dpr_para_test."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions_with_dpr_para_test']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'natural_questions_with_dpr_para_test/train.tsv',
      'test': 'natural_questions_with_dpr_para_test/test.tsv',
  }


class UnifiedQANewsQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for newsqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['newsqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'newsqa/train.tsv',
      'validation': 'newsqa/dev.tsv',
  }


class UnifiedQAOBQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for openbookqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['openbookqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'openbookqa/train.tsv',
      'validation': 'openbookqa/dev.tsv',
      'test': 'openbookqa/test.tsv',
  }


class UnifiedQAOBQADevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for openbookqa_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['openbookqa_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'openbookqa_dev/train.tsv',
      'validation': 'openbookqa_dev/dev.tsv',
      'test': 'openbookqa_dev/test.tsv',
  }


class UnifiedQAOBQAIRTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for openbookqa_with_ir."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['openbookqa_with_ir']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'openbookqa_with_ir/train.tsv',
      'validation': 'openbookqa_with_ir/dev.tsv',
      'test': 'openbookqa_with_ir/test.tsv',
  }


class UnifiedQAOBQAIRDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for openbookqa_with_ir_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['openbookqa_with_ir_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'openbookqa_with_ir_dev/train.tsv',
      'validation': 'openbookqa_with_ir_dev/dev.tsv',
      'test': 'openbookqa_with_ir_dev/test.tsv',
  }


class UnifiedQAPIQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for physical_iqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['physical_iqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'physical_iqa/train.tsv',
      'validation': 'physical_iqa/dev.tsv',
  }


class UnifiedQAQASCTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for qasc."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['qasc']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'qasc/train.tsv',
      'validation': 'qasc/dev.tsv',
      'test': 'qasc/test.tsv',
  }


class UnifiedQAQASCTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for qasc_test."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['qasc_test']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'qasc_test/train.tsv',
      'validation': 'qasc_test/dev.tsv',
      'test': 'qasc_test/test.tsv',
  }


class UnifiedQAQASCIRTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for qasc_with_ir."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['qasc_with_ir']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'qasc_with_ir/train.tsv',
      'validation': 'qasc_with_ir/dev.tsv',
      'test': 'qasc_with_ir/test.tsv',
  }


class UnifiedQAQASCIRTestTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for qasc_with_ir_test."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['qasc_with_ir_test']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'qasc_with_ir_test/train.tsv',
      'validation': 'qasc_with_ir_test/dev.tsv',
      'test': 'qasc_with_ir_test/test.tsv',
  }


class UnifiedQAQuorefTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for quoref."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['quoref']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'quoref/train.tsv',
      'validation': 'quoref/dev.tsv',
  }


class UnifiedQARACEStringDevTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for race_string_dev."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['race_string_dev']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'race_string_dev/train.tsv',
      'validation': 'race_string_dev/dev.tsv',
      'test': 'race_string_dev/test.tsv',
  }


class UnifiedQARACEStringTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for race_string."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['race_string']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'race_string/train.tsv',
      'validation': 'race_string/dev.tsv',
      'test': 'race_string/test.tsv',
  }


class UnifiedQAROPESTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ropes."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['ropes']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'ropes/train.tsv',
      'validation': 'ropes/dev.tsv',
  }


class UnifiedQASIQATest(tfds.testing.DatasetBuilderTestCase):
  """Tests for social_iqa."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['social_iqa']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'social_iqa/train.tsv',
      'validation': 'social_iqa/dev.tsv',
  }


class UnifiedQASQuAD11Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for squad1_1."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['squad1_1']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'squad1_1/train.tsv',
      'validation': 'squad1_1/dev.tsv',
  }


class UnifiedQASQuAD20Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for squad2."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['squad2']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'squad2/train.tsv',
      'validation': 'squad2/dev.tsv',
  }


class UnifiedQAWGLTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for winogrande_l."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['winogrande_l']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'winogrande_l/train.tsv',
      'validation': 'winogrande_l/dev.tsv',
  }


class UnifiedQAWGMTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for winogrande_m."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['winogrande_m']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      'train': 'winogrande_m/train.tsv',
      'validation': 'winogrande_m/dev.tsv',
  }


class UnifiedQAWGSTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for winogrande_s."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['winogrande_s']
  DATASET_CLASS = unifiedqa.UnifiedQA
  SPLITS = {
      'train': 3,  # Number of fake train example
      'validation': 1,  # Number of fake validation example
      'test': 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      'train': 'winogrande_s/train.tsv',
      'validation': 'winogrande_s/dev.tsv',
      'test': 'winogrande_s/test.tsv',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
