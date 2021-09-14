
from pathlib import Path
import random

from absl import app
from absl import flags

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

# In TF 2.0, eager execution is enabled by default
tf.compat.v1.disable_eager_execution()

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

NUMBER_OF_EXAMPLES = 3

def _output_dir():
  return Path(FLAGS.tfds_dir) / 'smartwatch_gestures_dataset' / 'dummy_data'

def _dummy_file():
  """return path to fake data file"""
  participant = f'U{random.int(1,99):02}'
  gesture = f'{random.int(1,20):02}'
  attempt = f'{random.int(1,99):02}.txt'

  return _output_dir() / participant / gesture / attempt

def _generate_data():
  for _ in range(NUMBER_OF_EXAMPLES):
    print(_dummy_file())


