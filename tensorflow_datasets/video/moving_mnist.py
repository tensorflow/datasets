from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import functools
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image.mnist import _MNIST_IMAGE_SIZE

_OUT_RESOLUTION = (64, 64)
_TOTAL_PADDING = tuple(o - _MNIST_IMAGE_SIZE for o in _OUT_RESOLUTION) # 36, 36
_SEQUENCE_LENGTH = 20
_IMAGES_PER_SEQUENCE = 2

_citation = """
@article{DBLP:journals/corr/SrivastavaMS15,
  author    = {Nitish Srivastava and
               Elman Mansimov and
               Ruslan Salakhutdinov},
  title     = {Unsupervised Learning of Video Representations using LSTMs},
  journal   = {CoRR},
  volume    = {abs/1502.04681},
  year      = {2015},
  url       = {http://arxiv.org/abs/1502.04681},
  archivePrefix = {arXiv},
  eprint    = {1502.04681},
  timestamp = {Mon, 13 Aug 2018 16:47:05 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SrivastavaMS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


class MovingMnist(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    shape = (_SEQUENCE_LENGTH,) + _OUT_RESOLUTION + (1,)

    # as Image - doesn't work with 1 as final dim?
    # sequence = tfds.features.Image(shape=shape)

    # as video - doesn't work with 1 as final dim?
    # sequence = tfds.features.Video(shape=shape)

    # as base tensor - space inefficient??
    sequence = tfds.features.Tensor(shape=shape, dtype=tf.uint8)

    return tfds.core.DatasetInfo(
        builder=self,
        description=(
          "Moving variant of MNIST database of handwritten digits. This is the "
          "data used by the authors for reporting model performance. See "
          "`tfds.video.moving_sequence` for functions to generate training/"
          "validation data."),
        features=tfds.features.FeaturesDict(
          dict(image_sequence=sequence)),
        # supervised_keys=("inputs",),
        urls=["http://www.cs.toronto.edu/~nitish/unsupervised_video/"],
        citation=_citation,
        splits=[tfds.Split.TEST]
    )

  def _split_generators(self, dl_manager):
    data_path = dl_manager.download(
        "http://www.cs.toronto.edu/~nitish/unsupervised_video/"
        "mnist_test_seq.npy")

    # authors only provide test data. See `tfds.video.moving_sequence` for
    # approach based on creating sequences from existing datasets
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=5,
            gen_kwargs=dict(data_path=data_path)),
    ]

  def _generate_examples(self, data_path):
    """Generate MOVING_MNIST sequences as a single.

    Args:
      data_path (str): Path to the data file

    Returns:
      10000 x 20 x 64 x 64 x 1 uint8 numpy array
    """
    with tf.io.gfile.GFile(data_path, "r") as fp:
      images = np.load(fp)
    images = np.transpose(images, (1, 0, 2, 3))
    images = np.expand_dims(images, axis=-1)
    for sequence in images:
      yield dict(image_sequence=sequence)
