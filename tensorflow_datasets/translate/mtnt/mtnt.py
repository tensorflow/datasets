# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""mtnt dataset."""
import csv
import dataclasses
import hashlib

from absl import logging
from etils import epath
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
MTNT: Machine Translation of Noisy Text
"""

_CITATION = """
@InProceedings{michel2018mtnt,
  author    = {Michel, Paul  and  Neubig, Graham},
  title     = {MTNT: A Testbed for Machine Translation of Noisy Text},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing}
}
"""

URL_1_1 = 'https://github.com/pmichel31415/mtnt/releases/download/v1.1/MTNT.1.1.tar.gz'


@dataclasses.dataclass
class MtntConfig(tfds.core.BuilderConfig):
  src_lang: str = ''
  dst_lang: str = ''


class Mtnt(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for mtnt dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      # pylint: disable=unexpected-keyword-arg
      MtntConfig(name='en-fr', src_lang='en', dst_lang='fr'),
      MtntConfig(name='en-ja', src_lang='en', dst_lang='ja'),
      MtntConfig(name='fr-en', src_lang='fr', dst_lang='en'),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(mtnt): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'src': tfds.features.Text(),
            'dst': tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('src', 'dst'),  # Set to `None` to disable
        homepage='https://pmichel31415.github.io/mtnt/index.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(URL_1_1)

    pair = f'{self.builder_config.src_lang}-{self.builder_config.dst_lang}'
    return {
        'train': self._generate_examples(path / f'MTNT/train/train.{pair}.tsv'),
        'test': self._generate_examples(path / f'MTNT/test/test.{pair}.tsv'),
        'valid': self._generate_examples(path / f'MTNT/valid/valid.{pair}.tsv'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with epath.Path(path).open() as f:
      reader = csv.reader(f, delimiter='\t')
      for row in reader:
        if len(row) < 3:
          logging.info('skipped row %s', row)
          continue
        key = hashlib.md5(','.join(row[0:3]).encode('utf-8')).hexdigest()
        yield key, {
            'src': row[1],
            'dst': row[2],
        }
