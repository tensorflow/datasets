r"""CLI for Tensorflow Datasets

Instructions:

```
tfds new my_dataset
```

This command will generator dataset files needed for adding a new dataset
to tfds

```
my_dataset/
    fake_examples/
    __init__.py
    dataset.py
    dataset_test.py
    fake_data_generator.py
    checksum.txt
```

"""

import argparse
from absl import app
from absl.flags import argparse_flags

import tensorflow_datasets as tfds


def _parse_flags(_=None) -> argparse.Namespace:
  parser = argparse_flags.ArgumentParser(
      description='Tensorflow Datasets CLI tool',
  )
  parser.add_argument(
      '--version',
      action='version',
      version='Tensorflow Datasets: ' + tfds.__version__
  )
  return parser.parse_args()


def main(args: argparse.Namespace = None):
  args = args or _parse_flags()


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
