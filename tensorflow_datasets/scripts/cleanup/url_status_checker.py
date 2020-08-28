r"""Dump the list of all dead urls in a `.txt` file.

Instructions:

```sh
python tensorflow_datasets/scripts/dead_url_checker.py
```

"""
from concurrent import futures
import requests

from absl import app

import tensorflow_datasets as tfds


def _get_status_code(url: str) -> int:
  try:
    return requests.head(url, timeout=10).status_code
  except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
    return -1


def main(_):
  urls = tfds.core.download.checksums.get_all_url_infos().keys()
  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    update_needed = {(url, code)
      for (url, code) in zip(urls, executor.map(_get_status_code, urls))
      if code != requests.codes.ok}


  print('\n************ Summary ************\n')
  print(f'{len(update_needed)} URLs need update.')
  for url, code in update_needed:
    print(f'HTTP Status code: {code}, URL: {url}')


if __name__ == '__main__':
    app.run(main)
