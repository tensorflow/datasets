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

from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_metadata
from tensorflow_datasets.core.utils import resource_utils


class DatasetMetadataTest(testing.TestCase):

  def test_load(self):
    datadir_path = resource_utils.tfds_path(
        "testing/dummy_config_based_datasets/dummy_ds_1"
    )
    metadata = dataset_metadata.load(datadir_path)
    self.assertEqual(
        metadata.description,
        "Description of `dummy_ds_1` dummy config-based dataset.\n",
    )
    self.assertEqual(
        metadata.citation,
        """@Article{google22tfds,
author = "The TFDS team",
title = "TFDS: a collection of ready-to-use datasets for use with TensorFlow, Jax, and other Machine Learning frameworks.",
journal = "ML gazette",
year = "2022"
}""",
    )
    self.assertEqual(metadata.tags, ["content.data-type.image"])

  def test_valid_tags(self):
    valid_tags = dataset_metadata.valid_tags()
    self.assertIn("content.data-type.image", valid_tags)

  def test_valid_tags_with_comments(self):
    text = dataset_metadata.valid_tags_with_comments()
    self.assertIn("content.data-type.image # Contains image data.", text)


if __name__ == "__main__":
  testing.main()
