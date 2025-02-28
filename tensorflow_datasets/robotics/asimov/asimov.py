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

"""Asimov datasets."""

from tensorflow_datasets.robotics import dataset_importer_builder


class AsimovDilemmasAutoVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_auto_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_dilemmas_auto_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_auto_val/0.1.0'


class AsimovDilemmasManualVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_manual_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_dilemmas_manual_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_manual_val/0.1.0'


class AsimovDilemmasScifiTrain(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_scifi_train` dataset."""

  def get_description(self):
    return 'Asimov asimov_dilemmas_scifi_train dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_scifi_train/0.1.0'


class AsimovDilemmasScifiVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_scifi_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_dilemmas_scifi_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_scifi_val/0.1.0'


class AsimovInjuryVal(dataset_importer_builder.TFDSDatasetImporterBuilder):
  """DatasetBuilder for `asimov_injury_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_injury_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_injury_val/0.1.0'


class AsimovMultimodalAutoVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_multimodal_auto_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_multimodal_auto_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_multimodal_auto_val/0.1.0'


class AsimovMultimodalManualVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_multimodal_manual_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_multimodal_manual_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_multimodal_manual_val/0.1.0'


class AsimovMultimodalRobopairVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_multimodal_robopair_val` dataset."""

  def get_description(self):
    return 'Asimov asimov_multimodal_robopair_val dataset'

  def get_citation(self):
    return 'citation here'

  def get_homepage(self):
    return 'todo here'

  def get_relative_dataset_location(self):
    return 'asimov_multimodal_robopair_val/0.1.0'
