# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Dump the list of all dead urls in a `.txt` file.

Instructions:

```sh
python tensorflow_datasets/scripts/dead_url_checker.py
```

"""
from concurrent import futures

from absl import app
import requests

import tensorflow_datasets as tfds


def _get_status_code(url: str) -> int:
  try:
    return requests.head(url, timeout=10).status_code
  except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
    return -1


def main(_):
  # Legacy datasets
  urls = set(tfds.core.download.checksums.get_all_url_infos().keys())

  # Dataset-as-folder datasets
  # Could keep track of the dataset name, so the report clearly indicates which
  # dataset should be updated.
  url_infos = {
      name: tfds.builder_cls(name).url_infos
      for name in tfds.list_builders(with_community_datasets=False)
  }
  for url_info in url_infos.values():
    if url_info:
      urls |= url_info.keys()

  urls = sorted(urls)

  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    all_codes = executor.map(_get_status_code, urls)

  print('\n************ Summary ************\n')
  total_errors = 0
  for url, code in zip(urls, all_codes):
    if code == requests.codes.ok:
      continue
    total_errors += 1
    print(f'{url} - status code: {code}')
  print(f'{total_errors} URLs had issues')


if __name__ == '__main__':
  app.run(main)
