r"""Benchmark dataset.

python -m tensorflow_datasets.scripts.benchmark_dataset \
  --dataset dataset_name

"""
import time
from typing import Dict

from absl import app
from absl import flags

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

# DEFAULT_DATA_DIR = os.path.expanduser(os.path.join("~", "tensorflow_datasets"))

EPOCHS = 1

FLAGS = flags.FLAGS

flags.DEFINE_string('dataset', None, 'Dataset name')
flags.DEFINE_string(
    'data_dir', None,
    'Path to dataset directory (auto-computed). Dataset should already present')
flags.DEFINE_integer('epochs', EPOCHS, 'No. of iterations over the dataset')


def _preprocess(
    name: str,
    data_dir: str,
) -> Dict[str, tf.data.Dataset]:

  # Exclude dataset download time
  builder = tfds.builder(name, data_dir=data_dir)
  builder.download_and_prepare()

  start_time = time.perf_counter()
  ds = builder.as_dataset()
  print('\nTime taken to preprocess {} dataset: {}\n'
        .format(name, time.perf_counter() - start_time))

  return ds


def benchmark(
    dataset: tf.data.Dataset,
    epochs: int,
) -> None:
  """Benchmarks the dataset.

  Reports:
  - Total Execution time
  - Time taken per Epoch
  - Dataset elements per second
  """

  num_examples = tf.data.experimental.cardinality(dataset)
  if num_examples == tf.data.experimental.UNKNOWN_CARDINALITY:
    num_examples = sum(1 for _ in dataset)
  elif num_examples == tf.data.experimental.INFINITE_CARDINALITY:
    raise RuntimeError('Dataset is of INFINITE_CARDINALITY')
  else:
    num_examples = num_examples.numpy()

  start_time = time.perf_counter()
  epoch_start_time = [start_time]

  for epoch_num in range(1, epochs+1):
    for _ in dataset:
      pass
    time_taken = time.perf_counter() - epoch_start_time[epoch_num - 1]
    print('Epoch {} duration: {}'.format(epoch_num, time_taken))
    print('Example per sec:', time_taken / num_examples)
    epoch_start_time.append(time.perf_counter())

  print('\nSummary\n')
  total_time = time.perf_counter() - start_time
  print('Dataset size:', num_examples)
  print('Total Execution Time:', total_time)
  print('Avg time per Epoch:', total_time / epochs)
  print('Avg Dataset element per second:', total_time / epochs / num_examples)
  print('\n')


def main(_):
  ds_name = FLAGS.dataset
  data_dir = FLAGS.data_dir
  epochs = FLAGS.epochs

  ds = _preprocess(ds_name, data_dir)

  for split in ds:
    print('Benchmarking split:', split)
    print('\n')
    benchmark(ds[split], epochs)


if __name__ == '__main__':
  app.run(main)
