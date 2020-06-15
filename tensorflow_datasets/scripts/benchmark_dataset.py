r"""Benchmark dataset.

python -m tensorflow_datasets.scripts.benchmark_dataset \
  --dataset dataset_name

"""
import time

from absl import app
from absl import flags

import tensorflow_datasets as tfds

# DEFAULT_DATA_DIR = os.path.expanduser(os.path.join("~", "tensorflow_datasets"))

EPOCHS = 1

FLAGS = flags.FLAGS

flags.DEFINE_string('dataset', None, 'Dataset name')
flags.DEFINE_string(
    'data_dir', None,
    'Path to dataset directory (auto-computed). Dataset should already present')
flags.DEFINE_integer('epochs', EPOCHS, 'No. of iterations over the dataset')


def benchmark(dataset, data_dir, epochs):
  start_time = time.perf_counter()
  ds = tfds.load(dataset, data_dir=data_dir) # TODO: Exclude dataset download time
  for epoch_num in range(epochs):
    for split in ds:
      for _ in ds[split]:
        pass
    print('Epoch {} completed at Time: {}'
          .format(epoch_num, time.perf_counter() - start_time))

  print('Total Execution Time: ', time.perf_counter() - start_time)


def main(_):
  ds_name = FLAGS.dataset
  data_dir = FLAGS.data_dir
  epochs = FLAGS.epochs
  benchmark(ds_name, data_dir, epochs)


if __name__ == '__main__':
  app.run(main)
