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

"""Tests for XTREME-S Benchmark."""
import tensorflow as tf
from tensorflow_datasets.audio.xtreme_s import xtreme_s
import tensorflow_datasets.public_api as tfds


class FleursTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for FLEURS dataset with af_za."""
  DATASET_CLASS = xtreme_s.XtremeS
  BUILDER_CONFIG_NAMES_TO_TEST = ['fleurs.af_za']
  SKIP_CHECKSUMS = True
  SPLITS = {
      'train': 3,  # Number of fake train examples
      'validation': 1,  # Number of fake dev examples
      'test': 2,  # Number of fake test examples
  }
  DL_EXTRACT_RESULT = {'af_za': 'fleurs'}

  def _download_and_prepare_as_dataset(self, builder):
    super()._download_and_prepare_as_dataset(builder)
    if not tf.executing_eagerly():  # Only test the following in eager mode.
      return

    def get_sorted_data(builder, split):
      splits = builder.as_dataset()
      data = list(tfds.as_numpy(splits[split]))
      return sorted(data, key=lambda x: x['path'])

    # Get the first example per split, sorting by path for consistency.
    train_ex = get_sorted_data(builder, tfds.Split.TRAIN)[0]
    dev_ex = get_sorted_data(builder, tfds.Split.VALIDATION)[0]
    test_ex = get_sorted_data(builder, tfds.Split.TEST)[0]
    # Check Train
    self.assertEqual(1348, train_ex['id'])
    self.assertIn(b'dummy_data/fleurs/af_za/audio/train/train_1.wav',
                  train_ex['path'])
    self.assertEqual('Boot ritte.'.encode(), train_ex['raw_transcription'])
    self.assertEqual('boot ritte'.encode(), train_ex['transcription'])
    self.assertEqual(32000, train_ex['num_samples'])
    self.assertEqual(1, train_ex['gender'])
    self.assertEqual(0, train_ex['lang_id'])
    self.assertEqual('Afrikaans'.encode(), train_ex['language'])
    self.assertEqual(3, train_ex['lang_group_id'])
    self.assertEqual((32000,), train_ex['audio'].shape)
    self.assertCountEqual([
        'id', 'path', 'audio', 'raw_transcription', 'transcription',
        'num_samples', 'gender', 'lang_id', 'language', 'lang_group_id'
    ], train_ex.keys())
    # Check Dev
    self.assertEqual(305, dev_ex['id'])
    self.assertIn(b'dummy_data/fleurs/af_za/audio/dev/dev_1.wav',
                  dev_ex['path'])
    self.assertEqual('In die 1960s'.encode(), dev_ex['raw_transcription'])
    self.assertEqual('in die 1960s'.encode(), dev_ex['transcription'])
    self.assertEqual(32000, dev_ex['num_samples'])
    self.assertEqual(0, dev_ex['gender'])
    self.assertEqual(0, dev_ex['lang_id'])
    self.assertEqual('Afrikaans'.encode(), dev_ex['language'])
    self.assertEqual(3, dev_ex['lang_group_id'])
    self.assertEqual((32000,), dev_ex['audio'].shape)
    self.assertCountEqual([
        'id', 'path', 'audio', 'raw_transcription', 'transcription',
        'num_samples', 'gender', 'lang_id', 'language', 'lang_group_id'
    ], dev_ex.keys())
    # Check Test
    self.assertEqual(5, test_ex['id'])
    self.assertIn(b'dummy_data/fleurs/af_za/audio/test/test_1.wav',
                  test_ex['path'])
    self.assertEqual('Boot.'.encode(), test_ex['raw_transcription'])
    self.assertEqual('boot'.encode(), test_ex['transcription'])
    self.assertEqual(32000, test_ex['num_samples'])
    self.assertEqual(1, test_ex['gender'])
    self.assertEqual(0, test_ex['lang_id'])
    self.assertEqual('Afrikaans'.encode(), dev_ex['language'])
    self.assertEqual(3, test_ex['lang_group_id'])
    self.assertEqual((32000,), test_ex['audio'].shape)
    self.assertCountEqual([
        'id', 'path', 'audio', 'raw_transcription', 'transcription',
        'num_samples', 'gender', 'lang_id', 'language', 'lang_group_id'
    ], test_ex.keys())


if __name__ == '__main__':
  tfds.testing.test_main()
