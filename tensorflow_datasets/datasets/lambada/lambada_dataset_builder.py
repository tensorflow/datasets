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

"""LAMBADA dataset."""

import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_LAMBADA_DATASET_URL = (
    'https://zenodo.org/record/2630551/files/lambada-dataset.tar.gz?download=1'
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for lambada dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {
                'passage': tfds.features.Text(),
            }
        ),
        supervised_keys=None,
        homepage='https://zenodo.org/record/2630551#.X4Xzn5NKjUI',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    dl_dir = dl_manager.download_and_extract(_LAMBADA_DATASET_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filepath': os.path.join(
                    dl_dir, 'lambada_development_plain_text.txt'
                )
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'filepath': os.path.join(dl_dir, 'lambada_test_plain_text.txt')
            },
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with epath.Path(filepath).open() as f:
      for idx, line in enumerate(f):
        key = '%s_%d' % (os.path.basename(filepath), idx)
        yield key, {'passage': line}
