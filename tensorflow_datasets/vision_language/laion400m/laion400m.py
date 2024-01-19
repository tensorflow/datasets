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

"""LAION-400M image dataset."""
import functools
from typing import Dict, Tuple

from etils import epath
import numpy as np

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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

_HOMEPAGE = 'https://laion.ai/blog/laion-400-open-dataset/'
_EMBEDDINGS_URL = (
    'https://deploy.laion.ai/8f83b608504d46bb81708ec86e912220/embeddings/'
)

_CLIP_EMBEDDING_SHAPE = (512,)
_MISSING_SIMILARITY_VALUE = -1.0
_NSFW_MISSING_TAG = 'UNTAGGED'
_NSFW_TAGS = ('UNLIKELY', 'UNSURE', 'NSFW', _NSFW_MISSING_TAG)


def _get_example_metadata(metadata_df_row):
  """Returns example metadata."""
  nsfw_tag = metadata_df_row['NSFW']
  if nsfw_tag not in _NSFW_TAGS:
    nsfw_tag = _NSFW_MISSING_TAG

  return {
      'caption': metadata_df_row['caption'],
      'nsfw': nsfw_tag,
      'similarity': metadata_df_row['similarity'] or _MISSING_SIMILARITY_VALUE,
      'license': metadata_df_row['LICENSE'] or '',
      'url': metadata_df_row['url'],
      'original_width': metadata_df_row['original_width'],
      'original_height': metadata_df_row['original_height'],
  }


def _get_embeddings_file_names(shard_idx: int) -> Tuple[str, str, str]:
  return (
      f'img_emb_{shard_idx}.npy',
      f'text_emb_{shard_idx}.npy',
      f'metadata_{shard_idx}.parquet',
  )


class Laion400mConfig(tfds.core.BuilderConfig):
  """BuilderConfig for LAION-400M."""

  def __init__(self, *, num_shards: int, **kwargs):
    """BuilderConfig for LAION-400M.

    Args:
      num_shards: `int`, the number of shards in the dataset
      **kwargs: keyword arguments forwarded to super
    """
    super().__init__(**kwargs)
    self.num_shards = num_shards


LAION400M_IMAGES_CONFIG = Laion400mConfig(
    name='images',
    num_shards=41455,  # total number of image tar files and metadata files
)

LAION400M_EMBEDDINGS_CONFIG = Laion400mConfig(
    name='embeddings',
    num_shards=410,  # total number of embeddings and metadata files
)


class Laion400m(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for LAION-400M dataset."""

  BUILDER_CONFIGS = [LAION400M_IMAGES_CONFIG, LAION400M_EMBEDDINGS_CONFIG]

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = f"""
  Refer to "Download Information" section on {_HOMEPAGE}
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = {
        'caption': tfds.features.Text(doc='HTML alt-text attribute'),
        'nsfw': tfds.features.ClassLabel(
            names=_NSFW_TAGS,
            doc=(
                'NSFW tag (detected with CLIP). Incohesive and missing tags'
                f' are replaced with {_NSFW_MISSING_TAG}'
            ),
        ),
        'similarity': tfds.features.Scalar(
            tf.float64,
            doc=tfds.features.Documentation(
                desc=(
                    'cosine similarity score between the text and image '
                    'embedding. Missing values default to '
                    f'{_MISSING_SIMILARITY_VALUE}'
                ),
                value_range='[0.0, 1.0]',
            ),
        ),
        'license': tfds.features.Text(
            doc='type of Creative Commons license (if applicable)'
        ),
        'url': tfds.features.Text(doc='image URL'),
        'original_width': tfds.features.Scalar(
            tf.int32, doc='original width of the image'
        ),
        'original_height': tfds.features.Scalar(
            tf.int32, doc='original height of the image'
        ),
    }

    if self.builder_config.name == LAION400M_IMAGES_CONFIG.name:
      features.update(
          {
              'image': tfds.features.Image(doc='image'),
          }
      )
    else:
      features.update({
          'image_embedding': tfds.features.Tensor(
              shape=_CLIP_EMBEDDING_SHAPE,
              dtype=tf.float16,
              doc='CLIP image embedding',
          ),
          'text_embedding': tfds.features.Tensor(
              shape=_CLIP_EMBEDDING_SHAPE,
              dtype=tf.float16,
              doc='CLIP text embedding',
          ),
      })

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=None,
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _download_data(
      self, dl_manager: tfds.download.DownloadManager
  ) -> Dict[str, epath.Path]:
    """Downloads data."""
    if self.builder_config.name == LAION400M_IMAGES_CONFIG.name:
      if not dl_manager.manual_dir.exists():
        raise AssertionError(
            'LAION-400M requires manual download of the images. Please download'
            f' the images and place them into: {dl_manager.manual_dir}'
        )

      return {}
    else:
      file_name_to_url = {}
      for shard_idx in range(self.builder_config.num_shards):
        img_emb_file_name, text_emb_file_name, metadata_file_name = (
            _get_embeddings_file_names(shard_idx)
        )
        file_name_to_url[img_emb_file_name] = (
            f'{_EMBEDDINGS_URL}img_emb/{img_emb_file_name}'
        )
        file_name_to_url[text_emb_file_name] = (
            f'{_EMBEDDINGS_URL}text_emb/{text_emb_file_name}'
        )
        file_name_to_url[metadata_file_name] = (
            f'{_EMBEDDINGS_URL}metadata/{metadata_file_name}'
        )

      file_name_to_dl_path = dl_manager.download(file_name_to_url)

      return file_name_to_dl_path

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    file_name_to_dl_path = self._download_data(dl_manager)

    return {
        'train': self._generate_examples(dl_manager, file_name_to_dl_path),
    }

  def _generate_examples(
      self,
      dl_manager: tfds.download.DownloadManager,
      file_name_to_dl_path: Dict[str, epath.Path],
  ):
    beam = tfds.core.lazy_imports.apache_beam

    return (
        'Generate shard indices'
        >> beam.Create(list(range(self.builder_config.num_shards)))
        | 'Generate examples from a single shard'
        >> beam.FlatMap(
            functools.partial(
                self._generate_examples_one_shard,
                dl_manager,
                file_name_to_dl_path,
            )
        )
        # `self._generate_examples_one_shard` produces a large number of
        # outputs, so we want to make sure that the next transforms will be
        # run in parallel independently of this step
        | 'Prevent fusion of transforms' >> beam.Reshuffle()
    )

  def _generate_examples_one_shard(
      self,
      dl_manager: tfds.download.DownloadManager,
      file_name_to_dl_path: Dict[str, epath.Path],
      shard_idx: int,
  ):
    """Yields examples from a single shard."""
    pd = tfds.core.lazy_imports.pandas

    if self.builder_config.name == LAION400M_IMAGES_CONFIG.name:
      img_archive_path = dl_manager.manual_dir / f'{shard_idx:05d}.tar'
      metadata_path = dl_manager.manual_dir / f'{shard_idx:05d}.parquet'

      with metadata_path.open('rb') as f:
        metadata_df = pd.read_parquet(f)

      for file_name, file_obj in dl_manager.iter_archive(img_archive_path):
        file_path = epath.Path(file_name)
        if file_path.suffix in ('.json', '.txt'):
          continue

        row_idx = int(file_path.stem)

        key = f'{shard_idx}_{row_idx}'
        example = {
            'image': file_obj.read(),
            **_get_example_metadata(metadata_df.iloc[row_idx]),
        }
        yield (key, example)
    else:
      img_emb_file_name, text_emb_file_name, metadata_file_name = (
          _get_embeddings_file_names(shard_idx)
      )

      with file_name_to_dl_path[img_emb_file_name].open('rb') as f:
        img_emb_arr = np.load(f)

      with file_name_to_dl_path[text_emb_file_name].open('rb') as f:
        text_emb_arr = np.load(f)

      with file_name_to_dl_path[metadata_file_name].open('rb') as f:
        metadata_df = pd.read_parquet(f)

      for row_idx, row in metadata_df.iterrows():
        key = f'{shard_idx}_{row_idx}'
        example = {
            'image_embedding': img_emb_arr[row_idx],
            'text_embedding': text_emb_arr[row_idx],
            **_get_example_metadata(row),
        }
        yield (key, example)
