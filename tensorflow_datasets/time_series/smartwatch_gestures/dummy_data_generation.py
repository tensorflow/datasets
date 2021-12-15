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

"""smartwatch_gestures dummy data generator."""
import pathlib
import random

from absl import app

import tensorflow as tf
import tensorflow_datasets as tfds

# In TF 2.0, eager execution is enabled by default.
tf.compat.v1.disable_eager_execution()

NUMBER_OF_EXAMPLES = 3


def _output_dir():
  return tfds.core.tfds_path(
  ) / 'time_series' / 'smartwatch_gestures' / 'dummy_data' / 'gestures-dataset'


def _dummy_file(participant: int, gesture: int, attempt: int) -> pathlib.Path:
  """Return path to fake data file."""
  participant = f'U{participant:02}'
  gesture = f'{gesture:02}'
  attempt = f'{attempt:02}.txt'
  return _output_dir() / participant / gesture / attempt


def _init_time(num_digits: int) -> int:
  """Return rand time int."""
  return random.randint(0, (10**num_digits) - 1)


def _init_accel() -> float:
  """Return random accel float."""
  sign = 1 if random.random() < 0.5 else -1
  return sign * random.random() * 13


def _inc_time(t: int, type_str: str = 'nano') -> int:
  """Increment time at aprrox rate of 10Hz."""
  return int(t + 1e8) if type_str == 'nano' else t + 100


def _inc_accel(x: float) -> float:
  sign = 1 if random.random() < 0.5 else -1
  return x + sign * random.random() * 2


def _generate_data():
  """Generate dummy data."""
  for i in range(NUMBER_OF_EXAMPLES):
    fpath = _dummy_file(99, 1, i)
    if not fpath.exists():
      fpath.parent.mkdir(parents=True, exist_ok=True)
    else:
      fpath.unlink()

    t_milli = _init_time(13)
    t_nanos = _init_time(14)
    t_event = _init_time(13)
    accel_x = _init_accel()
    accel_y = _init_accel()
    accel_z = _init_accel()

    with fpath.open('w') as f:
      f.write(f'{t_milli:013} {t_nanos:014} {t_event:013}'
              f' {accel_x:.6f} {accel_y:.6f} {accel_z:.6f}\n')

      for _ in range(random.randint(11, 51)):
        t_milli = _inc_time(t_milli, 'milli')
        t_nanos = _inc_time(t_nanos)
        t_event = _inc_time(t_event)
        accel_x = _inc_accel(accel_x)
        accel_y = _inc_accel(accel_y)
        accel_z = _inc_accel(accel_z)

        f.write(f'{t_milli:013} {t_nanos:014} {t_event:013}'
                f' {accel_x:.6f} {accel_y:.6f} {accel_z:.6f}\n')


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  _generate_data()


if __name__ == '__main__':
  app.run(main)
