"""NYU Depth V2 Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import tensorflow as tf

import tensorflow_datasets as tfds


_CITATION = """\
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}
@article{Alhashim2018,
  author    = {Ibraheem Alhashim and Peter Wonka},
  title     = {High Quality Monocular Depth Estimation via Transfer Learning},
  journal   = {arXiv e-prints},
  volume    = {abs/1812.11941},
  year      = {2018},
  url       = {https://arxiv.org/abs/1812.11941},
  eid       = {arXiv:1812.11941},
  eprint    = {1812.11941}
}
"""


_DESCRIPTION = """\
The NYU-Depth V2 data set is comprised of video sequences from a variety of
indoor scenes as recorded by both the RGB and Depth cameras from the
Microsoft Kinect.
"""


_URL = 'https://s3-eu-west-1.amazonaws.com/densedepth/nyu_data.zip'


class NyuDepthV2(tfds.core.GeneratorBasedBuilder):
  """NYU Depth V2 Dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(480, 640, 3)),
            'depth': tfds.features.Image(shape=(480, 640, 1)),
        }),
        supervised_keys=('image', 'depth'),
        # Homepage of the dataset for documentation
        urls=['https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    base_path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'extracted_path': base_path,
                'file_list': os.path.join(base_path, 'data', 'nyu2_train.csv'),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'extracted_path': base_path,
                'file_list': os.path.join(base_path, 'data', 'nyu2_test.csv'),
            },
        ),
    ]

  def _generate_pairs(self, file_list):
    with tf.io.gfile.GFile(file_list) as f:
      return csv.reader(f, delimiter=',')

  def _generate_examples(self, extracted_path, file_list):
    """Yields examples."""
    for (image, depth) in self._generate_pairs(file_list):
      name, _ = os.path.splitext(image)
      yield name, {
          'image': os.path.join(extracted_path, image),
          'depth': os.path.join(extracted_path, depth)
      }
