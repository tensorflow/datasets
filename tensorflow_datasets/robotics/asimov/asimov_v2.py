# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""Asimov 2.0 datasets."""

from tensorflow_datasets.robotics import dataset_importer_builder

ASIMOV_V2_CITATION = """"""

ASIMOV_V2_HOMEPAGE = 'https://asimov-benchmark.github.io/v2/'


class AsimovV2Injuries(dataset_importer_builder.TFDSDatasetImporterBuilder):
  """DatasetBuilder for `asimov_2_injuries` dataset."""

  def get_description(self):
    return 'Situations generated from real hospital injury reports.'

  def get_citation(self):
    return ASIMOV_V2_CITATION

  def get_homepage(self):
    return ASIMOV_V2_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_v2_injuries/0.1.0'


class AsimovV2Videos(dataset_importer_builder.TFDSDatasetImporterBuilder):
  """DatasetBuilder for `asimov_2_videos` dataset."""

  def get_description(self):
    return (
        'Photorealistic videos involving potential physical injury scenarios.'
    )

  def get_citation(self):
    return ASIMOV_V2_CITATION

  def get_homepage(self):
    return ASIMOV_V2_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_v2_videos/0.1.0'


class AsimovV2ConstraintsWithoutRationale(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_v2_constraints_without_rationale` dataset."""

  def get_description(self):
    return (
        'Dataset to evaluate the ability to reason and adhere to'
        ' physical safety constraints imposed by embodiment limitations.'
        ' No rationale for the answer needs to be provided.'
    )

  def get_citation(self):
    return ASIMOV_V2_CITATION

  def get_homepage(self):
    return ASIMOV_V2_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_v2_constraints_without_rationale/0.1.0'


class AsimovV2ConstraintsWithRationale(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_v2_constraints_with_rationale` dataset."""

  def get_description(self):
    return (
        'Dataset to evaluate the ability to reason and adhere to'
        ' physical safety constraints imposed by embodiment limitations.'
        ' Rationale for the answer needs to be provided.'
    )

  def get_citation(self):
    return ASIMOV_V2_CITATION

  def get_homepage(self):
    return ASIMOV_V2_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_v2_constraints_with_rationale/0.1.0'
