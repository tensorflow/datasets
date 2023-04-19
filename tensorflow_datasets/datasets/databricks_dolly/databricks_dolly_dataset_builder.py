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

"""databricks_dolly dataset."""
import json

from etils import epath
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for databricks_dolly dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'instruction': tfds.features.Text(),
            'context': tfds.features.Text(),
            'response': tfds.features.Text(),
            'category': tfds.features.Text(),
        }),
        homepage='https://github.com/databrickslabs/dolly',
        license='CC BY-SA 3.0',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    path = dl_manager.download(
        {
            'train': 'https://github.com/databrickslabs/dolly/raw/master/data/databricks-dolly-15k.jsonl'
        }
    )
    return {
        'train': self._generate_examples(path['train']),
    }

  def _generate_examples(self, path):
    with epath.Path(path).open() as f:
      for idx, line in enumerate(f):
        if not line:
          continue
        content = json.loads(line)
        yield idx, content
