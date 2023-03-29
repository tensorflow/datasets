# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""UCF-101 dataset from https://www.crcv.ucf.edu/data/UCF101.php."""

import os

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

UCF_101_URL = 'https://storage.googleapis.com/thumos14_files/UCF101_videos.zip'
SPLITS_URL = (
    'https://www.crcv.ucf.edu/data/UCF101/'
    'UCF101TrainTestSplits-RecognitionTask.zip'
)

_CITATION = """\
@article{DBLP:journals/corr/abs-1212-0402,
  author    = {Khurram Soomro and
               Amir Roshan Zamir and
               Mubarak Shah},
  title     = {{UCF101:} {A} Dataset of 101 Human Actions Classes From Videos in
               The Wild},
  journal   = {CoRR},
  volume    = {abs/1212.0402},
  year      = {2012},
  url       = {http://arxiv.org/abs/1212.0402},
  archivePrefix = {arXiv},
  eprint    = {1212.0402},
  timestamp = {Mon, 13 Aug 2018 16:47:45 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1212-0402},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_LABELS_FNAME = 'video/ucf101_labels.txt'


class Ucf101Config(tfds.core.BuilderConfig):
  """ "Configuration for UCF101 split and possible video rescaling."""

  def __init__(self, *, split_number, width=None, height=None, **kwargs):
    """The parameters specifying how the dataset will be processed.

    The dataset comes with three separate splits. You can specify which split
    you want in `split_number`. If `width` and `height` are set, the videos
    will be rescaled to have those heights and widths (using ffmpeg).

    Args:
      split_number: The split number, one of (1, 2, 3)
      width: An integer with the width or None.
      height: An integer with the height or None.
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(Ucf101Config, self).__init__(
        version=tfds.core.Version('2.0.0'),
        release_notes={
            '2.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
        },
        **kwargs,
    )
    if (width is None) ^ (height is None):
      raise ValueError('Either both dimensions should be set, or none of them')
    self.width = width
    self.height = height
    if split_number not in (1, 2, 3):
      raise ValueError(
          'Unknown split number {}, should be 1, 2 or 3'.format(split_number)
      )
    self.split_number = split_number


class Ucf101(tfds.core.GeneratorBasedBuilder):
  """Ucf101 action recognition dataset.

  Note that in contrast to the labels provided in the original dataset, here the
  labels start at zero, not at one.
  """

  BUILDER_CONFIGS = [
      Ucf101Config(
          name='ucf101_1_256',
          description='256x256 UCF with the first action recognition split.',
          width=256,
          height=256,
          split_number=1,
      ),
      Ucf101Config(
          name='ucf101_1',
          description='UCF with the action recognition split #1.',
          width=None,
          height=None,
          split_number=1,
      ),
      Ucf101Config(
          name='ucf101_2',
          description='UCF with the action recognition split #2.',
          width=None,
          height=None,
          split_number=2,
      ),
      Ucf101Config(
          name='ucf101_3',
          description='UCF with the action recognition split #3.',
          width=None,
          height=None,
          split_number=3,
      ),
  ]

  def _info(self):
    if self.builder_config.width is not None:
      if self.builder_config.height is None:
        raise ValueError('Provide either both height and width or none.')
      ffmpeg_extra_args = (
          '-vf',
          'scale={}x{}'.format(
              self.builder_config.height, self.builder_config.width
          ),
      )
    else:
      ffmpeg_extra_args = []

    video_shape = (
        None,
        self.builder_config.height,
        self.builder_config.width,
        3,
    )
    labels_names_file = tfds.core.tfds_path(_LABELS_FNAME)
    features = tfds.features.FeaturesDict({
        'video': tfds.features.Video(
            video_shape,
            ffmpeg_extra_args=ffmpeg_extra_args,
            encoding_format='jpeg',
        ),  # pytype: disable=wrong-arg-types  # gen-stub-imports
        'label': tfds.features.ClassLabel(names_file=labels_names_file),
    })
    return tfds.core.DatasetInfo(
        builder=self,
        description='A 101-label video classification dataset.',
        features=features,
        homepage='https://www.crcv.ucf.edu/data-sets/ucf101/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    splits_folder = 'ucfTrainTestlist'

    urls_to_download = {
        'videos': UCF_101_URL,
        'splits': SPLITS_URL,
    }
    downloaded_urls = dl_manager.download_and_extract(urls_to_download)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'videos_dir': downloaded_urls['videos'],
                'splits_dir': downloaded_urls['splits'],
                'data_list': '{}/trainlist{:02d}.txt'.format(
                    splits_folder, self.builder_config.split_number
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'videos_dir': downloaded_urls['videos'],
                'splits_dir': downloaded_urls['splits'],
                'data_list': '{}/testlist{:02d}.txt'.format(
                    splits_folder, self.builder_config.split_number
                ),
            },
        ),
    ]

  def _generate_examples(self, videos_dir, splits_dir, data_list):
    data_list_path_path = os.path.join(splits_dir, data_list)
    with tf.io.gfile.GFile(data_list_path_path, 'r') as data_list_file:
      labels_and_paths = data_list_file.readlines()
    for label_and_path in sorted(labels_and_paths):
      # The train splits contain not only the filename, but also a digit
      # encoding the label separated by a space, which we ignore.
      label_and_path = label_and_path.strip().split(' ')[0]
      label, path = os.path.split(label_and_path)
      # Fix an inconsistency between the names in the list and in the zip file.
      path = path.replace('HandStandPushups', 'HandstandPushups')
      video_path = os.path.join(videos_dir, 'UCF101', path)
      if not tf.io.gfile.exists(video_path):
        logging.error('Example %s not found', video_path)
        continue
      # We extract the label from the filename.
      yield path, {'video': video_path, 'label': label}
