# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""SCV dataset from http://arxiv.org/abs/1812.01717 ."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

DATA_URL_DIR = "https://storage.googleapis.com/scv_dataset/data/"


class StarcraftVideoConfig(tfds.core.BuilderConfig):

  @api_utils.disallow_positional_args
  def __init__(self, map_name, resolution, size_in_gb, **kwargs):
    super(StarcraftVideoConfig, self).__init__(**kwargs)
    self.map_name = map_name
    self.resolution = resolution
    self.size_in_gb = size_in_gb


class StarcraftVideo(tfds.core.GeneratorBasedBuilder):
  """Abstract class Starcraft video datasets."""

  BUILDER_CONFIGS = [
      StarcraftVideoConfig(
          name="brawl_64",
          description="Brawl map with 64x64 resolution.",
          map_name="Brawl",
          version="0.1.0",
          resolution=64,
          size_in_gb=6.3,
      ),
      StarcraftVideoConfig(
          name="brawl_128",
          description="Brawl map with 128x128 resolution.",
          map_name="Brawl",
          version="0.1.0",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="collect_mineral_shards_64",
          description="CollectMineralShards map with 64x64 resolution.",
          map_name="CollectMineralShards",
          version="0.1.0",
          resolution=64,
          size_in_gb=6.3,
      ),
      StarcraftVideoConfig(
          name="collect_mineral_shards_128",
          description="CollectMineralShards map with 128x128 resolution.",
          map_name="CollectMineralShards",
          version="0.1.0",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="move_unit_to_border_64",
          description="MoveUnitToBorder map with 64x64 resolution.",
          map_name="MoveUnitToBorder",
          version="0.1.0",
          resolution=64,
          size_in_gb=5.8,
      ),
      StarcraftVideoConfig(
          name="move_unit_to_border_128",
          description="MoveUnitToBorder map with 128x128 resolution.",
          map_name="MoveUnitToBorder",
          version="0.1.0",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="road_trip_with_medivac_64",
          description="RoadTripWithMedivac map with 64x64 resolution.",
          map_name="RoadTripWithMedivac",
          version="0.1.0",
          resolution=64,
          size_in_gb=2.4,
      ),
      StarcraftVideoConfig(
          name="road_trip_with_medivac_128",
          description="RoadTripWithMedivac map with 128x128 resolution.",
          map_name="RoadTripWithMedivac",
          version="0.1.0",
          resolution=128,
          size_in_gb=7.9,
      ),
  ]

  def _info(self):
    features = tfds.features.FeaturesDict({
        "rgb_screen":
            tfds.features.Video(
                shape=(None, self.builder_config.resolution,
                       self.builder_config.resolution, 3)),
    })
    return tfds.core.DatasetInfo(
        builder=self,
        description="This data set contains videos generated from Starcraft.",
        features=features,
        urls=["https://storage.googleapis.com/scv_dataset/README.html"],
        citation=("Towards Accurate Generative Models of Video: "
                  "New Metrics & Challenges"),
    )

  def _split_generators(self, dl_manager):
    url = DATA_URL_DIR + "%s_%dx%d_png/" % (self.builder_config.map_name,
                                            self.builder_config.resolution,
                                            self.builder_config.resolution)

    urls_to_download = {
        "train_%d" % i: url + "train-0000%d-of-00010.tfrecords" % i
        for i in range(10)
    }
    urls_to_download["valid"] = url + "valid-00000-of-00001.tfrecords"
    urls_to_download["test"] = url + "test-00000-of-00001.tfrecords"

    downloaded_urls = dl_manager.download_and_extract(urls_to_download)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "files": [
                    download for name, download in downloaded_urls.items()
                    if "train" in name
                ]
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={"files": [downloaded_urls["test"]]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={"files": [downloaded_urls["valid"]]}),
    ]

  def _parse_single_video(self, example_proto):
    """Parses single video from the input tfrecords.

    Args:
      example_proto: tfExample proto with a single video.

    Returns:
      dict with all frames, positions and actions.
    """
    context_features = {
        "game_duration_loops": tf.FixedLenFeature([1], tf.int64),
        "game_duration_seconds": tf.FixedLenFeature([1], tf.float32),
        "n_steps": tf.FixedLenFeature([1], tf.int64),
        "screen_size": tf.FixedLenFeature([2], tf.int64),
    }

    sequence_features = {
        "rgb_screen": tf.FixedLenSequenceFeature([], tf.string),
    }

    _, seq_feat = tf.parse_single_sequence_example(
        example_proto,
        context_features=context_features,
        sequence_features=sequence_features)

    video_frames = tf.map_fn(
        tf.image.decode_png, seq_feat["rgb_screen"], dtype=tf.uint8)
    return video_frames

  def _generate_examples(self, files):
    tf.logging.info("Reading data from %s.", ",".join(files))
    with tf.Graph().as_default():
      ds = tf.data.TFRecordDataset(files)
      ds = ds.map(
          self._parse_single_video,
          num_parallel_calls=tf.data.experimental.AUTOTUNE)
      iterator = ds.make_one_shot_iterator().get_next()
      with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        try:
          while True:
            video = sess.run(iterator)
            yield self.info.features.encode_example({"rgb_screen": video})

        except tf.errors.OutOfRangeError:
          # End of file.
          return
