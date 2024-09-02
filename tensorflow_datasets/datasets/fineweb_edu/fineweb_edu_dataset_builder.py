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

"""FineWeb-Edu dataset."""

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq
import tensorflow_datasets.public_api as tfds

_URL_TEMPLATE = 'https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu/resolve/refs%2Fconvert%2Fparquet/default/train/{shard_idx:04d}.parquet'
_NUM_SHARDS = 1630


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for FineWeb-Edu dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'text': tfds.features.Text(),
            'id': tfds.features.Text(),
            'dump': tfds.features.Text(),
            'url': tfds.features.Text(),
            'file_path': tfds.features.Text(),
            'language': tfds.features.Text(),
            'language_score': tfds.features.Scalar(dtype=np.float64),
            'token_count': tfds.features.Scalar(dtype=np.int64),
            'score': tfds.features.Scalar(dtype=np.float64),
            'int_score': tfds.features.Scalar(dtype=np.int64),
        }),
        supervised_keys=None,
        homepage='https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    shard_url_by_shard_idx = {
        shard_idx: _URL_TEMPLATE.format(shard_idx=shard_idx)
        for shard_idx in range(_NUM_SHARDS)
    }
    shard_filepath_by_shard_idx = dl_manager.download(shard_url_by_shard_idx)

    return {
        'train': self._generate_examples(shard_filepath_by_shard_idx),
    }

  def _generate_examples(self, shard_filepath_by_shard_idx):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    shard_filepaths_with_offsets: list[tuple[epath.Path, int]] = []
    offset = 0

    for shard_idx in range(_NUM_SHARDS):
      shard_filepath = shard_filepath_by_shard_idx[shard_idx]
      shard_filepaths_with_offsets.append((shard_filepath, offset))

      parquet_file = pq.ParquetFile(shard_filepath)
      offset += parquet_file.metadata.num_rows

    def _process_shard(shard_filepath: epath.Path, offset: int):
      parquet_file = pq.ParquetFile(shard_filepath)

      for batch in parquet_file.iter_batches():
        df = batch.to_pandas()

        for row_idx, row in enumerate(df.itertuples()):
          yield offset + row_idx, {
              'text': row.text,
              'id': row.id,
              'dump': row.dump,
              'url': row.url,
              'file_path': row.file_path,
              'language': row.language,
              'language_score': row.language_score,
              'token_count': row.token_count,
              'score': row.score,
              'int_score': row.int_score,
          }

    return beam.Create(shard_filepaths_with_offsets) | beam.FlatMapTuple(
        _process_shard
    )
