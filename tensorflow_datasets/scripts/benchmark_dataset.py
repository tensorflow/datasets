r"""Script to Benchmark dataset.

Standalone script to benchmark dataset.
The script by default runs in graph mode which gives us better performance.

Instructions:

```
python -m tensorflow_datasets.scripts.benchmark_dataset \
  --dataset dataset_name \
  --num_iterations 3
```

Use the `--help` flag for more options and details.

"""
import time
from typing import Dict, Tuple, Any

from absl import app
from absl import flags
from absl import logging
from packaging import version

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

NUM_ITERATIONS = 1
FLAGS = flags.FLAGS

flags.DEFINE_string('dataset', None, 'Dataset name')
flags.DEFINE_string(
    'data_dir', None,
    'Path to dataset directory (auto-computed). Dataset should already present')
flags.DEFINE_integer(
    'num_iterations', NUM_ITERATIONS,
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
    num_iterations: int,
    ds_size: int,
) -> Dict[str, Any]:
  """Benchmarks the dataset.

  Reports:
  - Total Execution time
  - Time taken per Epoch
  - Dataset elements per second
  """
  if version.parse(tf.__version__) >= version.parse('2.2.0'):
    ds = ds.apply(tf.data.experimental.assert_cardinality(ds_size))

  # Compute time taken by first iteration separately.
  start_time = time.perf_counter()
  time_per_iteration_list = []
  first_batch_time = 0
  with tfds.core.utils.async_tqdm(
      total=num_iterations,
      desc='Iterations completed...',
      unit=' iterations') as pbar:
    for _ in range(num_iterations):
      t1 = time.perf_counter()
      iter_ds = iter(ds)
      next(iter_ds)  # First warmup batch
      t2 = time.perf_counter()
      first_batch_time += t2 - t1
      for _ in iter_ds:  # Other batch
        pass
      pbar.update()
      time_per_iteration_list.append(time.perf_counter() - t1)
      # time_per_iteration_list.append(time.perf_counter() - t2) # exclude first batch

  total_time = time.perf_counter() - start_time
  time_per_iter = total_time / num_iterations
  time_per_example = total_time / ds_size
  avg_first_batch_time = first_batch_time / num_iterations
  print('\nSummary\n')
  print('Dataset size:', ds_size)
  print('Time taken for first batch of dataset:', avg_first_batch_time)
  print('Avg time per iteration:', time_per_iter)
  print('Element per second:', time_per_example)
  print('Total Execution Time:', total_time)

  return {
      'dataset_size': ds_size,
      'num_iterations': num_iterations,
      'total_time': total_time,
      'avg_first_batch_time': first_batch_time,
      'time_per_iteration': time_per_iter,
      'time_per_example': time_per_example,
      'iteration_duration': time_per_iteration_list
  }


def main(_):
  if FLAGS.enable_eager_exec:
    tf.config.experimental_run_functions_eagerly(True)
  else:
    tf.compat.v1.disable_eager_execution()

  status = 'Enabled' if tf.executing_eagerly() else 'Disabled'
  logging.info('Eager Execution: %s', status)

  ds_name = FLAGS.dataset
  data_dir = FLAGS.data_dir
  num_iterations = FLAGS.num_iterations

  if FLAGS.disable_tqdm:
    tfds.disable_progress_bar()

  ds, num_examples = _make_ds(ds_name, data_dir)

  print('Benchmarking\n')
  print(benchmark(ds, num_iterations, num_examples))


if __name__ == '__main__':
  app.run(main)
