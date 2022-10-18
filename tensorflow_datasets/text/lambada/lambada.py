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

"""LAMBADA dataset."""

import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """The LAMBADA dataset evaluates the capabilities of computational
models for text understanding by means of a word prediction task. LAMBADA is a
collection of narrative passages sharing the characteristic that human subjects
are able to guess their last word if they are exposed to the whole passage, but
not if they only see the last sentence preceding the target word
"""

_CITATION = """@inproceedings{paperno-etal-2016-lambada,
    title = "The {LAMBADA} dataset: Word prediction requiring a broad discourse context",
    author = "Paperno, Denis  and
      Kruszewski, Germ{\'a}n  and
      Lazaridou, Angeliki  and
      Pham, Ngoc Quan  and
      Bernardi, Raffaella  and
      Pezzelle, Sandro  and
      Baroni, Marco  and
      Boleda, Gemma  and
      Fern{\'a}ndez, Raquel",
    booktitle = "Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2016",
    address = "Berlin, Germany",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P16-1144",
    doi = "10.18653/v1/P16-1144",
    pages = "1525--1534",
}
"""

_LAMBADA_DATASET_URL = 'https://zenodo.org/record/2630551/files/lambada-dataset.tar.gz?download=1'


class Lambada(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for lambada dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'passage': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://zenodo.org/record/2630551#.X4Xzn5NKjUI',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    dl_dir = dl_manager.download_and_extract(_LAMBADA_DATASET_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filepath':
                    os.path.join(dl_dir, 'lambada_development_plain_text.txt')
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
