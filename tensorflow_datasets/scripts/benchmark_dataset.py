r"""Script to Benchmark dataset.

Standalone script to benchmark dataset.
The script by default runs in graph mode which gives us better performance.

Instructions:

```
python -m tensorflow_datasets.scripts.benchmark_dataset \
  --dataset dataset_name \
  --epochs 3
```

Use the `--help` flag for more options and details.

"""
import time
from typing import Dict, Tuple

from absl import app
from absl import flags
from absl import logging
from packaging import version

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

NUM_EXECUTIONS = 1
FLAGS = flags.FLAGS

flags.DEFINE_string('dataset', None, 'Dataset name')
flags.DEFINE_string(
    'data_dir', None,
    'Path to dataset directory (auto-computed). Dataset should already present')
flags.DEFINE_integer(
    'epochs', NUM_EXECUTIONS,
    'No. of iterations over the dataset to average out performance')
flags.DEFINE_integer(
    'num_examples', None,
    'No. of examples of Dataset to be used for Benchmarking Dataset.'
    'Defaults to size of Train split')
flags.DEFINE_boolean('disable_tqdm', False, 'If True, disable progress bar.')
flags.DEFINE_boolean('enable_eager_exec', False,
                     'If True, enable eager execution.')


def _make_ds(
    name: str,
    data_dir: str,
) -> Tuple[Dict[str, tf.data.Dataset], int]:
  """Download, prepare and preprocess Dataset"""

  builder = tfds.builder(name, data_dir=data_dir)

  if FLAGS.num_examples is None or (
      FLAGS.num_examples >= builder.info.splits['train'].num_examples):
    num_examples = builder.info.splits['train'].num_examples
  else:
    num_examples = FLAGS.num_examples

  # Exclude dataset download time
  builder.download_and_prepare()

  percentage = int(
      num_examples * 100 / builder.info.splits['train'].num_examples)
  start_time = time.perf_counter()
  ds = builder.as_dataset(split=f'train[:{percentage}%]')
  print('\nTime taken to preprocess {} dataset: {}\n'
        .format(name, time.perf_counter() - start_time))

  return ds, num_examples

@tf.function
def benchmark(
    ds: tf.data.Dataset,
    epochs: int,
    ds_size: int,
) -> None:
  """Benchmarks the dataset.

  Reports:
  - Total Execution time
  - Time taken per Epoch
  - Dataset elements per second
  """
  if version.parse(tf.__version__) >= version.parse('2.2.0'):
    ds = ds.apply(tf.data.experimental.assert_cardinality(ds_size))

  start_time = time.perf_counter()
  epoch_start_time = [start_time] # Can be used to plot a graph
  with tfds.core.utils.async_tqdm(
      total=epochs, desc='Iterations completed...', unit=' epochs') as pbar:
    for _ in range(epochs):
      for _ in ds:
        pass
      pbar.update()
      epoch_start_time.append(time.perf_counter())

  print('\nSummary\n')
  total_time = time.perf_counter() - start_time
  first_iter_time = epoch_start_time[1] - epoch_start_time[0]
  remaining_time = total_time - first_iter_time
  print('Dataset size:', ds_size)
  print('Time taken for first iteration:', first_iter_time)
  print('Avg time per Epoch (excluding first iteration):',
        remaining_time / (epochs-1))
  print('Element per second:', remaining_time / (epochs-1) / ds_size)
  print('Total Execution Time:', total_time)


def main(_):
  if FLAGS.enable_eager_exec:
    tf.config.experimental_run_functions_eagerly(True)
  else:
    tf.compat.v1.disable_eager_execution()

  status = 'Enabled' if tf.executing_eagerly() else 'Disabled'
  logging.info('Eager Execution: %s', status)

  ds_name = FLAGS.dataset
  data_dir = FLAGS.data_dir
  epochs = FLAGS.epochs

  if FLAGS.disable_tqdm:
    tfds.disable_progress_bar()

  ds, num_examples = _make_ds(ds_name, data_dir)

  print('Benchmarking\n')
  benchmark(ds, epochs, num_examples)


if __name__ == '__main__':
  app.run(main)
