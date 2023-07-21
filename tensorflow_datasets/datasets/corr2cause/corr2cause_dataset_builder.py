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

"""corr2cause dataset."""
import csv
from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds


_URL_PATH = 'https://huggingface.co/datasets/causalnlp/corr2cause/'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for corr2cause dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'input': tfds.features.Text(),
            'label': np.int64,
        }),
        supervised_keys=None,
        homepage='https://github.com/causalNLP/corr2cause/tree/main',
        license='https://github.com/causalNLP/corr2cause/blob/main/LICENSE',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    split_names = ['train', 'dev', 'test']

    data_dict = {
        'train': _URL_PATH + 'resolve/main/train.csv',
        'dev': _URL_PATH + 'raw/main/dev.csv',
        'test': _URL_PATH + 'raw/main/test.csv',
    }

    path = dl_manager.download_and_extract(data_dict)

    return {
        split: self._generate_examples(filepath=path[split])
        for split in split_names
    }

  def _generate_examples(self, filepath):
    """Yields examples."""
    with epath.Path(filepath).open() as csvfile:
      reader = csv.DictReader(csvfile)
      for i, row in enumerate(reader):
        yield i, {
            'input': row['input'],
            'label': row['label'],
        }
