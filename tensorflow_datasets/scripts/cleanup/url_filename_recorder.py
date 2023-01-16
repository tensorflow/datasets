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

r"""Update checksums to contain filename."""

from concurrent import futures
import dataclasses
import itertools
import typing
from typing import Dict, NewType, Optional
import urllib

from absl import app
from absl import logging
import requests
import tensorflow_datasets as tfds
from tensorflow_datasets.core.download import checksums
import tqdm

Url = NewType('Url', str)
Filename = NewType('Filename', Optional[str])

# pylint: disable=logging-format-interpolation


def _collect_path_to_url_infos() -> (
    Dict[tfds.core.Path, Dict[Url, checksums.UrlInfo]]
):
  """Collect checksums paths to url_infos."""
  # Collect legacy checksums paths
  url_info_paths = list(checksums._checksum_paths().values())  # pylint: disable=protected-access

  # Collect dataset-as-folder checksums path
  for name in tfds.list_builders(with_community_datasets=False):
    url_info_path = tfds.builder_cls(name)._checksums_path  # pylint: disable=protected-access
    if url_info_path.exists():
      url_info_paths.append(url_info_path)

  url_info_paths = [tfds.core.utils.to_write_path(p) for p in url_info_paths]
  return {
      path: typing.cast(
          Dict[Url, checksums.UrlInfo], checksums.load_url_infos(path)
      )
      for path in url_info_paths
  }


def _request_filename(
    url: Url,
    url_info: checksums.UrlInfo,
    tqdm_bar: tqdm.tqdm,
) -> Filename:
  """Get filename of dataset at `url`."""
  if url_info.filename:
    # tqdm_bar.update(1)
    return Filename(url_info.filename)
  # Uses `_open_url` for drive urls compatibility
  downloader = tfds.core.download.downloader
  try:
    with downloader._open_url(url, verify=True, timeout=10.0) as (response, _):  # pylint: disable=protected-access
      filename = downloader._get_filename(response)  # pylint: disable=protected-access
  except (
      requests.exceptions.RequestException,
      urllib.error.URLError,
      downloader.DownloadError,
  ) as e:
    tqdm.tqdm.write(f'Error for {url}: {e}')
    filename = None
  tqdm_bar.update(1)
  # logging.info(f'{url} -> {filename}')
  return Filename(filename)


def _update_url_info(
    url: Url,
    url_info: checksums.UrlInfo,
    new_filename: Filename,
) -> checksums.UrlInfo:
  """Update the `UrlInfo` with the filename."""
  old_filename = url_info.filename
  if new_filename is None:
    return url_info
  if old_filename and old_filename != new_filename:
    tqdm.tqdm.write(
        f'Filename for {url} already exist. Updating `{old_filename}` to '
        f'`{new_filename}`'
    )
  return dataclasses.replace(url_info, filename=new_filename)


def main(_):
  logging.info('Load all UrlInfo.')
  path_to_url_infos = _collect_path_to_url_infos()

  # Remove duplicate urls (merge all Dict[Url, UrlInfo] together)
  all_url_infos = dict(
      itertools.chain.from_iterable(
          d.items() for d in path_to_url_infos.values()
      )
  )

  logging.info('Start fetching filenames.')
  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Query all filenames in parallel
    iter_all_url_infos = tqdm.tqdm(all_url_infos.items(), desc='Urls sent')
    received_tqdm = tqdm.tqdm(
        desc='Filenames received', total=len(all_url_infos)
    )
    urls_to_filename = {
        url: executor.submit(_request_filename, url, url_info, received_tqdm)
        for url, url_info in iter_all_url_infos
    }
    # Update and save the new UrlInfo
    for path, url_infos in tqdm.tqdm(
        path_to_url_infos.items(), desc='Saving filenames'
    ):
      # Update the UrlInfo with the new filenames
      url_infos = {
          url: _update_url_info(url, url_info, urls_to_filename[url].result())
          for url, url_info in url_infos.items()
      }
      checksums.save_url_infos(path, url_infos)
  received_tqdm.close()
  tqdm.tqdm.write('Url infos updated.')


if __name__ == '__main__':
  app.run(main)
