# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""smartwatch_gestures dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The **SmartWatch Gestures Dataset** has been collected to evaluate several gesture recognition algorithms for interacting with mobile applications using arm gestures.

Eight different users performed twenty repetitions of twenty different gestures, for a total of 3200 sequences.
Each sequence contains acceleration data from the 3-axis accelerometer of a first generation Sony SmartWatch™, as well as timestamps from the different clock sources available on an Android device.
The smartwatch was worn on the user's right wrist.
The gestures have been manually segmented by the users performing them by tapping the smartwatch screen at the beginning and at the end of every repetition.
"""

_CITATION = """
@INPROCEEDINGS{
  6952946,
  author={Costante, Gabriele and Porzi, Lorenzo and Lanz, Oswald and Valigi, Paolo and Ricci, Elisa},
  booktitle={2014 22nd European Signal Processing Conference (EUSIPCO)},
  title={Personalizing a smartwatch-based gesture interface with transfer learning},
  year={2014},
  volume={},
  number={},
  pages={2530-2534},
  doi={}}
"""


class SmartwatchGestures(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for smartwatch_gestures dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    class_label = tfds.features.ClassLabel(
        names_file=tfds.core.tfds_path(
            'time_series/smartwatch_gestures/class_labels.txt'))
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'features':
                tfds.features.Sequence({
                    'time_millis': tf.uint64,
                    'time_nanos': tf.uint64,
                    'time_event': tf.uint64,
                    'accel_x': tf.float64,
                    'accel_y': tf.float64,
                    'accel_z': tf.float64,
                }),
            'participant':
                tf.uint8,
            'attempt':
                tf.uint8,
            'gesture':
                class_label
        }),
        supervised_keys=('features', 'gesture'),
        homepage='https://tev.fbk.eu/resources/smartwatch',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        'https://drive.google.com/uc?export=download&'
        'id=1nEs-JlAQv6xpuSIqahTKK68TgK37GirP')

    # There are no predefined train/val/test split for this dataset.
    # (smartwatch_gestures): Returns the Dict['train', Iterator[Key, Example]].
    return {
        'train': self._generate_examples(path / 'gestures-dataset'),
    }

  def _generate_examples(self, path):
    """Yields examples."""

    pd = tfds.core.lazy_imports.pandas

    for f in path.glob('*/*/*.txt'):

      table = pd.read_table(
          f,
          sep=' ',
          header=None,
          names=[
              'time_millis', 'time_nanos', 'time_event', 'accel_x', 'accel_y',
              'accel_z'
          ])

      # Create a unique key for each recorded gesture.
      participant_numstr = f.parent.parent.name[1:]  # Drop the "U".
      gesture_numstr = f.parent.name
      attempt_numstr = f.stem
      k = int(''.join([participant_numstr, gesture_numstr, attempt_numstr]))

      yield k, {
          'features': {
              'time_millis': table['time_millis'].to_numpy(),
              'time_nanos': table['time_nanos'].to_numpy(),
              'time_event': table['time_event'].to_numpy(),
              'accel_x': table['accel_x'].to_numpy(),
              'accel_y': table['accel_y'].to_numpy(),
              'accel_z': table['accel_z'].to_numpy(),
          },
          'participant': int(participant_numstr),
          'attempt': int(attempt_numstr),
          'gesture': int(gesture_numstr) - 1
      }
