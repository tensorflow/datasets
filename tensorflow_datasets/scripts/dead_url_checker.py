r"""Dump the list of all dead urls in a `.txt` file.

Instructions:

```sh
python tensorflow_datasets/scripts/dead_url_checker.py
```

"""
import os
import requests

from absl import app
from absl import flags

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

FLAGS = flags.FLAGS

flags.DEFINE_string('tfds_dir', tfds.core.utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')


def _is_dead_url(url: str) -> bool:
  return requests.head(url).status_code != 200


def main(_):
  dead_urls = []
  for url in tfds.core.utils.tqdm(
      tfds.core.download.checksums.get_all_url_infos()):
    if _is_dead_url(url):
      dead_urls.append(url)

  path = os.path.join(FLAGS.tfds_dir, 'dead_urls.txt')
  with tf.io.gfile.GFile(path, 'w') as f:
    f.write('\n'.join(dead_urls))
  print(f'Found {len(dead_urls)} dead urls.')


if __name__ == '__main__':
    app.run(main)
