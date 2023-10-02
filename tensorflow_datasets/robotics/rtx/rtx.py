# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Open X-Embodiment datasets."""


from tensorflow_datasets.robotics import dataset_importer_builder


class UtokyoPr2TabletopManipulationConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'PR2 tabletop manipulation (folding cloth, picking)'

  def get_citation(self):
    return """@misc{oh2023pr2utokyodatasets,
  author={Jihoon Oh and Naoaki Kanazawa and Kento Kawaharazuka},
  title={X-Embodiment U-Tokyo PR2 Datasets},
  year={2023},
  url={https://github.com/ojh6404/rlds_dataset_builder},
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds/0.1.0'
