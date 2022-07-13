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

"""mt_opt dataset."""

import os
from typing import Any, Dict, Generator, Tuple

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = """
Datasets for the [MT-Opt paper](https://arxiv.org/abs/2104.08212).
"""

_CITATION = """
@misc{kalashnikov2021mtopt,
      title={MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale},
      author={Dmitry Kalashnikov and Jacob Varley and Yevgen Chebotar and Benjamin Swanson and Rico Jonschkowski and Chelsea Finn and Sergey Levine and Karol Hausman},
      year={2021},
      eprint={2104.08212},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
"""

_BUILDER_CONFIGS = [
    tfds.core.BuilderConfig(
        name='rlds',
        description=(
            'This dataset contains task episodes collected across a'
            'fleet of real robots. It follows the [RLDS format](https://github.com/google-research/rlds)'
            'to represent steps and episodes.')),
    tfds.core.BuilderConfig(
        name='sd',
        description='The success detectors dataset that contains human curated definitions of tasks completion.'
    )
]

_STEPS_FEATURES = tfds.features.FeaturesDict({
    'action':
        tfds.features.FeaturesDict({
            'close_gripper':
                tf.bool,
            'open_gripper':
                tf.bool,
            'target_pose':
                tfds.features.Tensor(
                    shape=(7,),
                    dtype=tf.float32,
                    encoding=tfds.features.Encoding.ZLIB),
            'terminate':
                tf.bool,
        }),
    'is_first':
        tf.bool,
    'is_last':
        tf.bool,
    'is_terminal':
        tf.bool,
    'observation':
        tfds.features.FeaturesDict({
            'gripper_closed':
                tf.bool,
            'height_to_bottom':
                tf.float32,
            'image':
                tfds.features.Image(shape=(512, 640, 3), dtype=tf.uint8),
            'state_dense':
                tfds.features.Tensor(
                    shape=(7,),
                    dtype=tf.float32,
                    encoding=tfds.features.Encoding.ZLIB),
        }),
})

_NAME_TO_FEATURES = {
    'rlds':
        tfds.features.FeaturesDict({
            'episode_id': tf.string,
            'skill': tf.uint8,
            'steps': tfds.features.Dataset(_STEPS_FEATURES),
            'task_code': tf.string,
        }),
    'sd':
        tfds.features.FeaturesDict({
            'image_0': tfds.features.Image(shape=(512, 640, 3), dtype=tf.uint8),
            'image_1': tfds.features.Image(shape=(480, 640, 3), dtype=tf.uint8),
            'image_2': tfds.features.Image(shape=(480, 640, 3), dtype=tf.uint8),
            'success': tf.bool,
            'task_code': tf.string,
        }),
}

# To encode, we use sequence instead of nested dataset. Otherwise, Beam has
# issues calculating the size of the yielded examples (b/219881125)
_NAME_TO_FEATURES_ENCODE = {
    'rlds':
        tfds.features.FeaturesDict({
            'episode_id': tf.string,
            'skill': tf.uint8,
            'steps': tfds.features.Sequence(_STEPS_FEATURES),
            'task_code': tf.string,
        }),
    'sd':
        tfds.features.FeaturesDict({
            'image_0': tfds.features.Image(shape=(512, 640, 3), dtype=tf.uint8),
            'image_1': tfds.features.Image(shape=(480, 640, 3), dtype=tf.uint8),
            'image_2': tfds.features.Image(shape=(480, 640, 3), dtype=tf.uint8),
            'success': tf.bool,
            'task_code': tf.string,
        }),
}

_NAME_TO_SPLITS = {
    'sd': {
        'train': 1024,
        'test': 256,
    },
    'rlds': {
        'train': 2048,
    },
}


def _filename(prefix: str, num_shards: int, shard_id: int):
  return os.fspath(
      tfds.core.Path(f'{prefix}-{shard_id:05d}-of-{num_shards:05d}'))


def _get_files(prefix: str, ds_name: str, split: str, num_shards: int):
  prefix = f'{prefix}/mt_opt_{ds_name}/1.0.0/mt_opt_{ds_name}-{split}.tfrecord'
  return [_filename(prefix, num_shards, i) for i in range(num_shards)]


class MtOpt(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for mt_opt datasets."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = _BUILDER_CONFIGS
  _INPUT_FILE_PREFIX = 'gs://gresearch/robotics/'


  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=_NAME_TO_FEATURES[self.builder_config.name],
        supervised_keys=None,
        homepage='https://karolhausman.github.io/mt-opt/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_name = self.builder_config.name
    splits = {}
    for split, shards in _NAME_TO_SPLITS[ds_name].items():
      paths = {
          'file_paths':
              _get_files(self._INPUT_FILE_PREFIX, ds_name, split, shards)
      }
      splits[split] = self._generate_examples(paths)
    return splits

  def _generate_examples_one_file(
      self, path) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    """Yields examples from one file."""
    # Dataset of tf.Examples containing full episodes.
    example_ds = tf.data.TFRecordDataset(filenames=str(path))

    example_features = _NAME_TO_FEATURES_ENCODE[self.builder_config.name]
    example_specs = example_features.get_serialized_info()
    parser = tfds.core.example_parser.ExampleParser(example_specs)

    parsed_examples = example_ds.map(parser.parse_example)
    decoded_examples = parsed_examples.map(example_features.decode_example)

    for index, example in enumerate(tfds.as_numpy(decoded_examples)):
      if self.builder_config.name == 'rlds':
        id_key = 'episode_id'
      else:
        id_key = 'task_code'
      example_id = str(index) + str(example[id_key]) + str(hash(path))
      yield example_id, example

  def _generate_examples(self, paths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    file_paths = paths['file_paths']

    return beam.Create(file_paths) | beam.FlatMap(
        self._generate_examples_one_file)
