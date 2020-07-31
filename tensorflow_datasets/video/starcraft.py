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

"""SCV dataset from http://arxiv.org/abs/1812.01717 ."""

from absl import logging
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

DATA_URL_DIR = "https://storage.googleapis.com/scv_dataset/data/"
_CITATION = """\
@article{DBLP:journals/corr/abs-1812-01717,
  author    = {Thomas Unterthiner and
               Sjoerd van Steenkiste and
               Karol Kurach and
               Rapha{\"{e}}l Marinier and
               Marcin Michalski and
               Sylvain Gelly},
  title     = {Towards Accurate Generative Models of Video: {A} New Metric and
               Challenges},
  journal   = {CoRR},
  volume    = {abs/1812.01717},
  year      = {2018},
  url       = {http://arxiv.org/abs/1812.01717},
  archivePrefix = {arXiv},
  eprint    = {1812.01717},
  timestamp = {Tue, 01 Jan 2019 15:01:25 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1812-01717},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


class StarcraftVideoConfig(tfds.core.BuilderConfig):
  """Config for StarcraftVideo dataset."""

  def __init__(self, *, map_name, resolution, size_in_gb, **kwargs):
    super(StarcraftVideoConfig, self).__init__(
        version=tfds.core.Version(
            "1.0.0", "New split API (https://tensorflow.org/datasets/splits)"),
        **kwargs)
    self.map_name = map_name
    self.resolution = resolution
    self.size_in_gb = size_in_gb


class StarcraftVideo(tfds.core.GeneratorBasedBuilder):
  """Starcraft video datasets."""

  BUILDER_CONFIGS = [
      StarcraftVideoConfig(
          name="brawl_64",
          description="Brawl map with 64x64 resolution.",
          map_name="Brawl",
          resolution=64,
          size_in_gb=6.3,
      ),
      StarcraftVideoConfig(
          name="brawl_128",
          description="Brawl map with 128x128 resolution.",
          map_name="Brawl",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="collect_mineral_shards_64",
          description="CollectMineralShards map with 64x64 resolution.",
          map_name="CollectMineralShards",
          resolution=64,
          size_in_gb=6.3,
      ),
      StarcraftVideoConfig(
          name="collect_mineral_shards_128",
          description="CollectMineralShards map with 128x128 resolution.",
          map_name="CollectMineralShards",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="move_unit_to_border_64",
          description="MoveUnitToBorder map with 64x64 resolution.",
          map_name="MoveUnitToBorder",
          resolution=64,
          size_in_gb=5.8,
      ),
      StarcraftVideoConfig(
          name="move_unit_to_border_128",
          description="MoveUnitToBorder map with 128x128 resolution.",
          map_name="MoveUnitToBorder",
          resolution=128,
          size_in_gb=20.7,
      ),
      StarcraftVideoConfig(
          name="road_trip_with_medivac_64",
          description="RoadTripWithMedivac map with 64x64 resolution.",
          map_name="RoadTripWithMedivac",
          resolution=64,
          size_in_gb=2.4,
      ),
      StarcraftVideoConfig(
          name="road_trip_with_medivac_128",
          description="RoadTripWithMedivac map with 128x128 resolution.",
          map_name="RoadTripWithMedivac",
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
        homepage="https://storage.googleapis.com/scv_dataset/README.html",
        citation=_CITATION,
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
            gen_kwargs={
                "files": [
                    download for name, download in downloaded_urls.items()
                    if "train" in name
                ]
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"files": [downloaded_urls["test"]]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
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
        "game_duration_loops": tf.io.FixedLenFeature([1], tf.int64),
        "game_duration_seconds": tf.io.FixedLenFeature([1], tf.float32),
        "n_steps": tf.io.FixedLenFeature([1], tf.int64),
        "screen_size": tf.io.FixedLenFeature([2], tf.int64),
    }

    sequence_features = {
        "rgb_screen": tf.io.FixedLenSequenceFeature([], tf.string),
    }

    _, seq_feat = tf.io.parse_single_sequence_example(
        example_proto,
        context_features=context_features,
        sequence_features=sequence_features)

    video_frames = tf.map_fn(
        tf.image.decode_png, seq_feat["rgb_screen"], dtype=tf.uint8)
    return video_frames

  def _generate_examples(self, files):
    logging.info("Reading data from %s.", ",".join(files))
    with tf.Graph().as_default():
      ds = tf.data.TFRecordDataset(sorted(files))
      ds = ds.map(
          self._parse_single_video,
          num_parallel_calls=tf.data.experimental.AUTOTUNE)
      iterator = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
      with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        try:
          i = 0
          while True:
            video = sess.run(iterator)
            yield i, {"rgb_screen": video}
            i += 1

        except tf.errors.OutOfRangeError:
          # End of file.
          return
