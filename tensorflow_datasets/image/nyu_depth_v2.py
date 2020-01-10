"""NYU Depth V2 Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import h5py
import os
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds


_CITATION = """\
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}
@inproceedings{icra_2019_fastdepth,
  author    = {Wofk, Diana and Ma, Fangchang and Yang, Tien-Ju and Karaman, Sertac and Sze, Vivienne},
  title     = {FastDepth: Fast Monocular Depth Estimation on Embedded Systems},
  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2019}
}
"""


_DESCRIPTION = """\
The NYU-Depth V2 data set is comprised of video sequences from a variety of
indoor scenes as recorded by both the RGB and Depth cameras from the
Microsoft Kinect.
"""


_URL = 'http://datasets.lids.mit.edu/fastdepth/data/nyudepthv2.tar.gz'


class NyuDepthV2(tfds.core.GeneratorBasedBuilder):
  """NYU Depth V2 Dataset."""

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(480, 640, 3)),
            'depth': tfds.features.Tensor(shape=(480, 640), dtype=tf.float16),
        }),
        supervised_keys=('image', 'depth'),
        homepage='https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    base_path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'root_dir': os.path.join(base_path, 'nyudepthv2', 'train')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'root_dir': os.path.join(base_path, 'nyudepthv2', 'val')
            },
        ),
    ]

  def _generate_examples(self, root_dir):
    """Yields examples."""
    for dir in tf.io.gfile.listdir(root_dir):
      for file_name in tf.io.gfile.listdir(os.path.join(root_dir, dir)):
        with h5py.File(os.path.join(root_dir, dir, file_name), 'r') as file:
          yield dir + '_' + file_name, {
              'image': np.transpose(file["rgb"], (1, 2, 0)),
              'depth': file['depth'][:].astype('float16')
          }
