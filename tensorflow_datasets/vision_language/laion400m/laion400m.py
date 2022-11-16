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

"""LAION-400M image dataset."""
from typing import Dict, Tuple

from etils import epath

from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder
from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder_utils as laion400m_lib
import tensorflow_datasets.public_api as tfds


def _get_epaths(manual_dir: epath.Path,
                shard_idx: int) -> Tuple[epath.Path, epath.Path]:
  return (
      manual_dir / f'{shard_idx:05d}.tar',
      manual_dir / f'{shard_idx:05d}.parquet',
  )


class Laion400m(laion400m_dataset_builder.Laion400mDatasetBuilder):
  """DatasetBuilder for LAION-400M dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  SHARD_NUM = 41455  # total number of image tar files and metadata files
  MANUAL_DOWNLOAD_INSTRUCTIONS = f"""
  Refer to "Download Information" on {laion400m_lib.HOMEPAGE}
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info({
        'image': tfds.features.Image(doc='image'),
    })

  def _download_data(
      self, dl_manager: tfds.download.DownloadManager) -> Dict[str, epath.Path]:
    """Downloads data."""
    if not dl_manager.manual_dir.exists():
      raise AssertionError(
          'LAION-400M requires manual download of the images. Please download '
          f'the images and place them into: {dl_manager.manual_dir}')

    return {}

  def _generate_examples_one_shard(self,
                                   dl_manager: tfds.download.DownloadManager,
                                   file_name_to_dl_path: Dict[str, epath.Path],
                                   shard_idx: int):
    """Yields examples from a single shard."""
    pd = tfds.core.lazy_imports.pandas

    img_tar_epath, metadata_epath = _get_epaths(dl_manager.manual_dir,
                                                shard_idx)

    with metadata_epath.open('rb') as f:
      metadata_df = pd.read_parquet(f)

    for file_name, file_obj in dl_manager.iter_archive(img_tar_epath):
      file_epath = epath.Path(file_name)
      if file_epath.suffix in ('.json', '.txt'):
        continue

      row_idx = int(file_epath.stem)

      key = f'{shard_idx}_{row_idx}'
      example = {
          'image': file_obj.read(),
          **laion400m_lib.get_example_metadata(metadata_df.iloc[row_idx])
      }
      yield (key, example)
