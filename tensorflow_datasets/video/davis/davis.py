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

"""DAVIS 2017 dataset for video object segmentation."""

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = """
The DAVIS 2017 video object segmentation dataset.
"""

_URL = 'https://data.vision.ee.ethz.ch/csergi/share/davis/'

_CITATION = """\
@article{DBLP:journals/corr/Pont-TusetPCASG17,
  author    = {Jordi Pont{-}Tuset and
               Federico Perazzi and
               Sergi Caelles and
               Pablo Arbelaez and
               Alexander Sorkine{-}Hornung and
               Luc Van Gool},
  title     = {The 2017 {DAVIS} Challenge on Video Object Segmentation},
  journal   = {CoRR},
  volume    = {abs/1704.00675},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.00675},
  archivePrefix = {arXiv},
  eprint    = {1704.00675},
  timestamp = {Mon, 13 Aug 2018 16:48:55 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/Pont-TusetPCASG17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


def _read_annotation(annotation_path):
  """Read the image pixels of the annotation stored at annotations_path."""
  with tf.io.gfile.GFile(annotation_path, 'rb') as f:
    # Annotations are stored as index PNG so PIL returns directly the indices.
    image = tfds.core.lazy_imports.PIL_Image.open(f)
    image = np.asarray(image)
  return image[:, :, None]


class DavisConfig(tfds.core.BuilderConfig):
  """"Configuration for RoboNet video rescaling."""

  def __init__(
      self, *, full_resolution=False, **kwargs
  ):
    """The parameters specifying how the dataset will be processed.

    The dataset comes with two versions, 1080p and 480p video. Set
    full_resolution to True to load the 1080p version and to False to load the
    480p version.

    Args:
      full_resolution: bool, whether to load the 1080p version.
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(DavisConfig, self).__init__(**kwargs)
    self.full_resolution = full_resolution


class Davis(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for davis dataset."""
  BUILDER_CONFIGS = [
      DavisConfig(
          name='480p',
          description='The 480p version of the dataset',
          full_resolution=False,
      ),
      DavisConfig(
          name='full_resolution',
          description='The full resolution version of the dataset.',
          full_resolution=True,
      ),
  ]

  VERSION = tfds.core.Version('2.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '2.0.0': 'Change instance ids to be 0, 1, 2, ...',
      '2.1.0': 'Fix instance ids order.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # NOTE: Different videos have different resolutions.
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'video':
                tfds.features.Sequence({
                    'frames':
                        tfds.features.Image(shape=(None, None, 3)),
                    'segmentations':
                        tfds.features.Image(
                            shape=(None, None, 1),
                            use_colormap=True,
                        ),
                }),
            'metadata': {
                'num_frames': tf.int64,
                'video_name': tf.string,
            },
        }),
        supervised_keys=None,
        homepage='https://davischallenge.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    if self.builder_config.full_resolution:
      trainval_data = dl_manager.download_and_extract(
          _URL + 'DAVIS-2017-trainval-Full-Resolution.zip')
    else:
      trainval_data = dl_manager.download_and_extract(
          _URL + 'DAVIS-2017-trainval-480p.zip')

    train_files = trainval_data / 'DAVIS/ImageSets/2017/train.txt'
    val_files = trainval_data / 'DAVIS/ImageSets/2017/val.txt'

    return {
        tfds.Split.TRAIN:
            self._generate_examples(train_files),
        tfds.Split.VALIDATION:
            self._generate_examples(val_files)
    }

  def _generate_examples(self, path):
    """Yields examples in the form of key, dataset dictionary."""

    videos_to_include = path.read_text().splitlines()
    root_path = path.parent.parent.parent  # Move up three directories.
    resolution = 'Full-Resolution' if self.builder_config.full_resolution else '480p'
    for video in videos_to_include:
      images_path = root_path /'JPEGImages' / resolution / video
      annotations_path = root_path / 'Annotations' / resolution / video
      seq_len = len(list(images_path.iterdir()))
      images = []
      annotations = []
      for i in range(seq_len):
        image_path = images_path / f'{i:05d}.jpg'
        annotation_path = annotations_path / f'{i:05d}.png'
        annotation = _read_annotation(annotation_path)
        images.append(image_path)
        annotations.append(annotation)

      video_dict = {'frames': images, 'segmentations': annotations}
      metadata = {'num_frames': seq_len, 'video_name': video}
      key = video + resolution
      yield key, {'video': video_dict, 'metadata': metadata}

