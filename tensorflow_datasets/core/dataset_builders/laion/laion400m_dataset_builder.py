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

"""Format-specific dataset builders for LAION-400M datasets.

It contains a Laion400mDatasetBuilder which is used to initialize TFDS datasets
based on LAION-400M data.

Typical usage example:
class MyLaion400mDataset(tfds.dataset_builders.Laion400mDatasetBuilder):
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  SHARD_NUM = 410

  def _info(self) -> tfds.core.DatasetInfo:
    ...

  def _download_data(
      self, dl_manager: tfds.download.DownloadManager
  ) -> Dict[str, tfds.download.Url]:
    ...

  def _generate_examples_one_shard(
      self, dl_manager: tfds.download.DownloadManager,
      file_name_to_dl_path: Dict[str, tfds.download.Url], shard_idx: int):
    ...
"""
import functools
from typing import Dict

from etils import epath

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder_utils as laion400m_lib
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features.features_dict import FeaturesDict
from tensorflow_datasets.core.lazy_imports_lib import lazy_imports
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.core.utils.version import Version

_DESCRIPTION = """
The LAION-400M dataset is completely openly, freely accessible.

Check
[https://laion.ai/laion-400-open-dataset/](https://laion.ai/laion-400-open-dataset/)
for the full description of this dataset.

All images and texts in the LAION-400M dataset have been filtered with OpenAI‘s
CLIP by calculating the cosine similarity between the text and image embeddings
and dropping those with a similarity below 0.3. The threshold of 0.3 had been
determined through human evaluations and seemed to be a good heuristic for
estimating semantic image-text-content matching.

The image-text-pairs have been extracted from the Common Crawl web data dump and
are from random web pages crawled between 2014 and 2021.
"""

_CITATION = """
@article{DBLP:journals/corr/abs-2111-02114,
  author    = {Christoph Schuhmann and
               Richard Vencu and
               Romain Beaumont and
               Robert Kaczmarczyk and
               Clayton Mullis and
               Aarush Katta and
               Theo Coombes and
               Jenia Jitsev and
               Aran Komatsuzaki},
  title     = {{LAION-400M:} Open Dataset of CLIP-Filtered 400 Million Image-Text
               Pairs},
  journal   = {CoRR},
  volume    = {abs/2111.02114},
  year      = {2021},
  url       = {https://arxiv.org/abs/2111.02114},
  eprinttype = {arXiv},
  eprint    = {2111.02114},
  timestamp = {Fri, 05 Nov 2021 15:25:54 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2111-02114.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_NSFW_MISSING_TAG = 'UNTAGGED'
_NSFW_TAGS = ('UNLIKELY', 'UNSURE', 'NSFW', _NSFW_MISSING_TAG)
_MISSING_SIMILARITY_VALUE = -1.


class Laion400mDatasetBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True):
  """Base class for Laion datasets.

  It provides functionalities to ease the processing of Laion datasets.
  Users can overwrite `_generate_examples_one_shard` to customize the pipeline.
  """

  SHARD_NUM: int = 0  # override in derived builders

  def create_dataset_info(
      self, ordered_features: Dict[str, feature_lib.FeatureConnector]
  ) -> dataset_info.DatasetInfo:
    """Returns the dataset metadata."""
    ordered_features.update({
        'caption':
            features.Text(doc='HTML alt-text attribute'),
        'nsfw':
            features.ClassLabel(
                names=_NSFW_TAGS,
                doc='NSFW tag (detected with CLIP). Incohesive and missing tags'
                f' are replaced with {_NSFW_MISSING_TAG}'),
        'similarity':
            features.Scalar(
                tf.float64,
                doc=features.Documentation(
                    desc='cosine similarity score between the text and image '
                    'embedding. Missing values default to '
                    f'{_MISSING_SIMILARITY_VALUE}',
                    value_range='[0.0, 1.0]',
                ),
            ),
        'license':
            features.Text(doc='type of Creative Commons license (if applicable)'
                         ),
        'url':
            features.Text(doc='image URL'),
        'original_width':
            features.Scalar(tf.int32, doc='original width of the image'),
        'original_height':
            features.Scalar(tf.int32, doc='original height of the image'),
    })

    return dataset_info.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=FeaturesDict(ordered_features),
        supervised_keys=None,
        homepage=laion400m_lib.HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: download_manager.DownloadManager):
    """Returns SplitGenerators."""
    file_name_to_dl_path = self._download_data(dl_manager)

    return {
        'train': self._generate_examples(dl_manager, file_name_to_dl_path),
    }

  def _generate_examples(self, dl_manager: download_manager.DownloadManager,
                         file_name_to_dl_path: Dict[str, epath.Path]):
    beam = lazy_imports.apache_beam

    return (
        'Generate shard indices' >> beam.Create(list(range(self.SHARD_NUM)))
        | 'Generate examples from a single shard' >> beam.FlatMap(
            functools.partial(self._generate_examples_one_shard, dl_manager,
                              file_name_to_dl_path))
        | 'Prevent coupling' >> beam.Reshuffle())

  def _download_data(
      self,
      dl_manager: download_manager.DownloadManager) -> Dict[str, epath.Path]:
    """Downloads data."""
    raise NotImplementedError()

  def _generate_examples_one_shard(self,
                                   dl_manager: download_manager.DownloadManager,
                                   file_name_to_dl_path: Dict[str, epath.Path],
                                   shard_idx: int):
    """Yields examples from a single shard."""
    raise NotImplementedError()


class DummyLaion400mDataset(Laion400mDatasetBuilder):
  """Dummy class for tests."""
  VERSION = Version('1.0.0')
  RELEASE_NOTES = {'1.0.0': 'Dummy notes.'}
  SHARD_NUM = 1
  EXAMPLES_IN_SHARD = []  # overwrite in tests

  def _info(self) -> dataset_info.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        ordered_features={'dummy': features.Scalar(dtype=tf.int32)})

  def _download_data(
      self,
      dl_manager: download_manager.DownloadManager) -> Dict[str, epath.Path]:
    """Downloads data."""
    return {}

  def _generate_examples_one_shard(self,
                                   dl_manager: download_manager.DownloadManager,
                                   file_name_to_dl_path: Dict[str, epath.Path],
                                   shard_idx: int):
    """Yields examples from a single shard."""
    for idx, item in enumerate(self.EXAMPLES_IN_SHARD):
      key = str(idx)
      example = {
          'dummy': item,
          'caption': '',
          'nsfw': 'NSFW',
          'similarity': 0.0,
          'license': '',
          'url': '',
          'original_width': 0,
          'original_height': 0,
      }
      yield (key, example)
