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

ASIMOV_CITATION = """
@article{sermanet2025asimov,
  author    = {Pierre Sermanet and Anirudha Majumdar and Alex Irpan and Dmitry Kalashnikov and Vikas Sindhwani},
  title     = {Generating Robot Constitutions & Benchmarks for Semantic Safety},
  journal   = {arXiv preprint arXiv:2503.08663},
  url       = {https://arxiv.org/abs/2503.08663},
  year      = {2025},
}
"""

ASIMOV_HOMEPAGE = 'https://asimov-benchmark.github.io/'


class AsimovDilemmasAutoVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_auto_val` dataset."""

  def get_description(self):
    return (
        'Binary dilemma questions generated from counterfactual situations used'
        ' to auto-amend generated constitutions (validation set).'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_auto_val/0.1.0'


class AsimovDilemmasScifiTrain(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_scifi_train` dataset."""

  def get_description(self):
    return (
        'Multiple-choice ethical questions (with desirable and undesirable'
        ' answers) based on situations inspired from Science Fiction literature'
        ' (training set).'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_scifi_train/0.1.0'


class AsimovDilemmasScifiVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_dilemmas_scifi_val` dataset."""

  def get_description(self):
    return (
        'Multiple-choice ethical questions (with desirable and undesirable'
        ' answers) based on situations inspired from Science Fiction literature'
        ' (validation set).'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_dilemmas_scifi_val/0.1.0'


class AsimovInjuryVal(dataset_importer_builder.TFDSDatasetImporterBuilder):
  """DatasetBuilder for `asimov_injury_val` dataset."""

  def get_description(self):
    return (
        'Situations generated from real hospital injury reports (validation'
        ' set).'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_injury_val/0.1.0'


class AsimovMultimodalAutoVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_multimodal_auto_val` dataset."""

  def get_description(self):
    return (
        '(Image, context, instruction) triplets generated from real images'
        ' (from RoboVQA dataset) which are modified to contain undesirable'
        ' elements, generated instructions can be desirable or undesirable'
        ' (validation set).'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_multimodal_auto_val/0.1.0'


class AsimovMultimodalManualVal(
    dataset_importer_builder.TFDSDatasetImporterBuilder
):
  """DatasetBuilder for `asimov_multimodal_manual_val` dataset."""

  def get_description(self):
    return (
        '(Image, context, instruction) triplets manually taken and written by'
        ' humans while ensuring that the instruction desirability can only be'
        ' determined by looking at the image (validation set)'
    )

  def get_citation(self):
    return ASIMOV_CITATION

  def get_homepage(self):
    return ASIMOV_HOMEPAGE

  def get_relative_dataset_location(self):
    return 'asimov_multimodal_manual_val/0.1.0'
