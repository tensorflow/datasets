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

"""scitail dataset."""

import csv

from etils import epath
import tensorflow_datasets.public_api as tfds

_URL = 'http://data.allenai.org.s3.amazonaws.com/downloads/SciTailV1.1.zip'
_SCITAIL_DIR = 'SciTailV1.1'
_TSV_DIR = 'tsv_format'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for scitail dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # Specifies the tfds.core.DatasetInfo object
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'premise': tfds.features.Text(),
            'hypothesis': tfds.features.Text(),
            # Label indicates whether the premise entails or implies the
            # hypothesis.
            'label': tfds.features.ClassLabel(names=['entails', 'neutral']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://allenai.org/data/scitail',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Downloads the data and defines the splits
    data_dir = dl_manager.download_and_extract(_URL)

    # Returns the Dict[split names, Iterator[Key, Example]]
    return {
        tfds.Split.TRAIN: self._generate_examples(
            path=data_dir / _SCITAIL_DIR / _TSV_DIR / 'scitail_1.0_train.tsv'
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            path=data_dir / _SCITAIL_DIR / _TSV_DIR / 'scitail_1.0_dev.tsv'
        ),
        tfds.Split.TEST: self._generate_examples(
            path=data_dir / _SCITAIL_DIR / _TSV_DIR / 'scitail_1.0_test.tsv'
        ),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with epath.Path(path).open() as f:
      data = csv.reader(f, delimiter='\t')
      for id_, row in enumerate(data):
        yield id_, {'premise': row[0], 'hypothesis': row[1], 'label': row[2]}
