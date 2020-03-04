# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""RoboNet dataset.

RoboNet: Large-Scale Multi-Robot Learning

Sudeep Dasari, Frederik Ebert, Stephen Tian, Suraj Nair, Bernadette Bucher,
Karl Schmeckpeper, Siddharth Singh, Sergey Levine, Chelsea Finn

https://www.robonet.wiki/
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tempfile
import textwrap

import numpy as np
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds


DATA_URL = ('https://drive.google.com/uc?export=download&'
            'id=1YX2TgT8IKSn9V4wGCwdzbRnS53yicV2P')

STATES_DIM = 5
ACTIONS_DIM = 5

_CITATION = """\
@article{dasari2019robonet,
  title={RoboNet: Large-Scale Multi-Robot Learning},
  author={Dasari, Sudeep and Ebert, Frederik and Tian, Stephen and
  Nair, Suraj and Bucher, Bernadette and Schmeckpeper, Karl
  and Singh, Siddharth and Levine, Sergey and Finn, Chelsea},
  journal={arXiv preprint arXiv:1910.11215},
  year={2019}
}
"""


class RobonetConfig(tfds.core.BuilderConfig):
  """"Configuration for RoboNet video rescaling."""

  @tfds.core.disallow_positional_args
  def __init__(self, width=None, height=None, **kwargs):
    """The parameters specifying how the dataset will be processed.

    The dataset comes with three separate splits. You can specify which split
    you want in `split_number`. If `width` and `height` are set, the videos
    will be rescaled to have those heights and widths (using ffmpeg).

    Args:
      width: An integer with the width or None.
      height: An integer with the height or None.
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(RobonetConfig, self).__init__(
        version=tfds.core.Version('3.0.0'), **kwargs)
    if (width is None) ^ (height is None):
      raise ValueError('Either both dimensions should be set, or none of them')
    self.width = width
    self.height = height


class Robonet(tfds.core.GeneratorBasedBuilder):
  """RoboNet: Large-Scale Multi-Robot Learning."""

  BUILDER_CONFIGS = [
      RobonetConfig(
          name='robonet_64',
          description='64x64 RoboNet.',
          width=64,
          height=64,
      ),
  ]

  def _info(self):
    if self.builder_config.width is not None:
      if self.builder_config.height is None:
        raise ValueError('Provide either both height and width or none.')
      ffmpeg_extra_args = (
          '-vf', 'scale={}x{}'.format(self.builder_config.height,
                                      self.builder_config.width))
    else:
      ffmpeg_extra_args = []

    video_shape = (
        None, self.builder_config.height, self.builder_config.width, 3)

    features = tfds.features.FeaturesDict({
        # Video frames: uint8 [None, Time, Width, Height, Channels]
        'video': tfds.features.Video(
            video_shape,
            ffmpeg_extra_args=ffmpeg_extra_args,
            encoding_format='png'),
        # Robot actions: float32, [None, ACTIONS_DIM]
        'actions': tfds.features.Tensor(
            shape=(None, ACTIONS_DIM), dtype=tf.float32),
        # Robot states: float32, [None, STATE_DIM]
        # e Cartesian end-effector control action space
        # with restricted rotation, and a gripper joint
        'states': tfds.features.Tensor(
            shape=(None, STATES_DIM), dtype=tf.float32)
    })

    return tfds.core.DatasetInfo(
        builder=self,
        description=textwrap.dedent("""\
        RoboNet contains over 15 million video frames of robot-object
        interaction, taken from 113 unique camera viewpoints.

        *  The actions are deltas in position and rotation to the robot 
        end-effector with one additional dimension of the action vector 
        reserved for the gripper joint.

        * The states are cartesian end-effector control action space
        with restricted rotation, and a gripper joint"""),
        features=features,
        homepage='https://www.robonet.wiki/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    files = dl_manager.download_and_extract(DATA_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                'filedir': os.path.join(files, 'hdf5'),
            }),
    ]

  def _generate_examples(self, filedir):
    h5py = tfds.core.lazy_imports.h5py
    filenames = tf.io.gfile.glob(os.path.join(filedir, '*.hdf5'))
    with tempfile.TemporaryDirectory() as tmpdirname:
      for filename in filenames:
        hd5_path = filename
        with h5py.File(hd5_path) as hf:
          video_bytes = hf['env']['cam0_video']['frames'][:].tostring()
          video_path = os.path.join(tmpdirname, 'video.mp4')
          with tf.io.gfile.GFile(video_path, 'wb') as f:
            f.write(video_bytes)
          states = hf['env']['state'][:].astype(np.float32)
          states = np.pad(
              states, ((0, 0), (0, STATES_DIM-states.shape[1])), 'constant')
          actions = hf['policy']['actions'][:].astype(np.float32)
          actions = np.pad(
              actions, ((0, 0), (0, ACTIONS_DIM-actions.shape[1])), 'constant')

        features = {
            'video': video_path,
            'actions': actions,
            'states': states,
        }

        yield os.path.basename(filename), features


