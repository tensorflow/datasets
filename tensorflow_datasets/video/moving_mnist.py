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

"""MovingMNIST."""

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.video.moving_sequence import image_as_moving_sequence  # pylint: disable=unused-import

_OUT_RESOLUTION = (64, 64)
_SEQUENCE_LENGTH = 20
_URL = "http://www.cs.toronto.edu/~nitish/unsupervised_video/"
_CITATION = """\
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
_DESCRIPTION = """\
Moving variant of MNIST database of handwritten digits. This is the
data used by the authors for reporting model performance. See
`tfds.video.moving_mnist.image_as_moving_sequence`
for generating training/validation data from the MNIST dataset.
"""


class MovingMnist(tfds.core.GeneratorBasedBuilder):
  """MovingMnist."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image_sequence": tfds.features.Video(
                shape=(_SEQUENCE_LENGTH,) + _OUT_RESOLUTION + (1,))
        }),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    data_path = dl_manager.download(_URL + "mnist_test_seq.npy")

    # authors only provide test data.
    # See `tfds.video.moving_mnist.image_as_moving_sequence` for mapping
    # function to create training/validation dataset from MNIST.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(data_path=data_path)),
    ]

  def _generate_examples(self, data_path):
    """Generate MovingMnist sequences.

    Args:
      data_path (str): Path to the data file

    Yields:
      20 x 64 x 64 x 1 uint8 numpy arrays
    """
    with tf.io.gfile.GFile(data_path, "rb") as fp:
      images = np.load(fp)
    images = np.transpose(images, (1, 0, 2, 3))
    images = np.expand_dims(images, axis=-1)
    for i, sequence in enumerate(images):
      yield i, dict(image_sequence=sequence)
