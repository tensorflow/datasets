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

"""LAION-400M CLIP embeddings dataset."""

from typing import Dict, Tuple

from etils import epath
import numpy as np

from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder
from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder_utils as laion400m_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = 'https://deploy.laion.ai/8f83b608504d46bb81708ec86e912220/embeddings/'
_CLIP_EMBEDDING_SHAPE = (512,)


def _get_file_names(shard_idx: int) -> Tuple[str, str, str]:
  return (
      f'img_emb_{shard_idx}.npy',
      f'text_emb_{shard_idx}.npy',
      f'metadata_{shard_idx}.parquet',
  )


def _get_epaths(file_name_to_dl_path: Dict[str, epath.Path],
                shard_idx: int) -> Tuple[epath.Path, epath.Path, epath.Path]:
  img_emb_file_name, text_emb_file_name, metadata_file_name = _get_file_names(
      shard_idx)

  return (file_name_to_dl_path[img_emb_file_name],
          file_name_to_dl_path[text_emb_file_name],
          file_name_to_dl_path[metadata_file_name])


class Laion400mEmb(laion400m_dataset_builder.Laion400mDatasetBuilder):
  """DatasetBuilder for LAION-400M CLIP embeddings dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  SHARD_NUM = 410  # total number of embeddings and metadata files

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info({
        'image_embedding':
            tfds.features.Tensor(
                shape=_CLIP_EMBEDDING_SHAPE,
                dtype=tf.float16,
                doc='CLIP image embedding'),
        'text_embedding':
            tfds.features.Tensor(
                shape=_CLIP_EMBEDDING_SHAPE,
                dtype=tf.float16,
                doc='CLIP text embedding'),
    })

  def _download_data(
      self, dl_manager: tfds.download.DownloadManager) -> Dict[str, epath.Path]:
    """Downloads data."""
    file_name_to_url = {}
    for shard_idx in range(self.SHARD_NUM):
      img_emb_file_name, text_emb_file_name, metadata_file_name = _get_file_names(
          shard_idx)
      file_name_to_url[img_emb_file_name] = f'{_URL}img_emb/{img_emb_file_name}'
      file_name_to_url[
          text_emb_file_name] = f'{_URL}text_emb/{text_emb_file_name}'
      file_name_to_url[
          metadata_file_name] = f'{_URL}metadata/{metadata_file_name}'

    file_name_to_dl_path = dl_manager.download(file_name_to_url)

    return file_name_to_dl_path

  def _generate_examples_one_shard(self,
                                   dl_manager: tfds.download.DownloadManager,
                                   file_name_to_dl_path: Dict[str, epath.Path],
                                   shard_idx: int):
    """Yields examples from a single shard."""
    pd = tfds.core.lazy_imports.pandas

    img_emb_epath, text_emb_epath, metadata_epath = _get_epaths(
        file_name_to_dl_path, shard_idx)

    with img_emb_epath.open('rb') as f:
      img_emb_arr = np.load(f)

    with text_emb_epath.open('rb') as f:
      text_emb_arr = np.load(f)

    with metadata_epath.open('rb') as f:
      metadata_df = pd.read_parquet(f)

    for row_idx, row in metadata_df.iterrows():
      key = f'{shard_idx}_{row_idx}'
      example = {
          'image_embedding': img_emb_arr[row_idx],
          'text_embedding': text_emb_arr[row_idx],
          **laion400m_lib.get_example_metadata(row)
      }
      yield (key, example)
