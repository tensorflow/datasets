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

"""Dolma dataset."""

import gzip
import json

from etils import epath
import tensorflow_datasets.public_api as tfds

_URL = (
    'https://huggingface.co/datasets/allenai/dolma/resolve/main/urls/v1_7.txt'
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Dolma dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'text': tfds.features.Text(),
            'added': tfds.features.Text(),
            'created': tfds.features.Text(),
            'source': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://github.com/allenai/dolma',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    urls_filepath = dl_manager.download_and_extract(_URL)
    urls = epath.Path(urls_filepath).read_text().splitlines()
    filepaths = dl_manager.download(urls)

    return {
        'train': self._generate_examples(filepaths),
    }

  def _generate_examples(self, filepaths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_file(file_idx, filepath):
      with epath.Path(filepath).open('rb') as gz_file, gzip.open(gz_file) as f:
        for line_idx, line in enumerate(f):
          row = json.loads(line)
          yield f'{file_idx}_{line_idx}', {
              # Note: there are duplicate ids
              'id': row['id'],
              'text': row['text'],
              'added': str(row.get('added', '')),
              'created': str(row.get('created', '')),
              'source': row.get('source', ''),
          }

    return beam.Create(enumerate(filepaths)) | beam.FlatMapTuple(_process_file)
