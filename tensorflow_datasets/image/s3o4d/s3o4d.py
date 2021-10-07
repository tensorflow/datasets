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

"""Stanford 3D Objects for Disentangling (S3O4D) dataset."""

import itertools
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = r"""
The dataset first described in the "Stanford 3D Objects"
section of the paper [Disentangling by Subspace Diffusion](https://arxiv.org/abs/2006.12982).
The data consists of 100,000 renderings each of the Bunny and Dragon objects
from the [Stanford 3D Scanning Repository](http://graphics.stanford.edu/data/3Dscanrep/).
More objects may be added in the future, but only the Bunny and Dragon are used
in the paper. Each object is rendered with a uniformly sampled illumination from
a point on the 2-sphere, and a uniformly sampled 3D rotation. The true latent
states are provided as NumPy arrays along with the images. The lighting is given
as a 3-vector with unit norm, while the rotation is provided both as a
quaternion and a 3x3 orthogonal matrix.

There are many similarities between S3O4D and existing ML benchmark datasets
like [NORB](https://cs.nyu.edu/~ylclab/data/norb-v1.0/),
[3D Chairs](https://github.com/mathieuaubry/seeing3Dchairs),
[3D Shapes](https://github.com/deepmind/3d-shapes) and many others, which also
include renderings of a set of objects under different pose and illumination
conditions. However, none of these existing datasets include the *full manifold*
of rotations in 3D - most include only a subset of changes to elevation and
azimuth. S3O4D images are sampled uniformly and independently from the full space
of rotations and illuminations, meaning the dataset contains objects that are
upside down and illuminated from behind or underneath. We believe that this
makes S3O4D uniquely suited for research on generative models where the latent
space has non-trivial topology, as well as for general manifold learning
methods where the curvature of the manifold is important.
"""

_CITATION = r"""
@article{pfau2020disentangling,
  title={Disentangling by Subspace Diffusion},
  author={Pfau, David and Higgins, Irina and Botev, Aleksandar and Racani\`ere,
  S{\'e}bastian},
  journal={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2020}
}
"""


class S3o4d(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for s3o4d dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(256, 256, 3)),
            'label': tfds.features.ClassLabel(names=['bunny', 'dragon']),
            'illumination': tfds.features.Tensor(shape=(3,), dtype=tf.float32),
            'pose_quat': tfds.features.Tensor(shape=(4,), dtype=tf.float32),
            'pose_mat': tfds.features.Tensor(shape=(3, 3), dtype=tf.float32),
        }),
        supervised_keys=None,
        homepage='https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    suffices = {'img': 'images.zip', 'latent': 'latents.npz'}
    prod = itertools.product(['bunny', 'dragon'], ['train', 'test'],
                             ['img', 'latent'])
    path_dict = dict([
        ('_'.join([a, b, c]),
         f'https://storage.googleapis.com/dm_s3o4d/{a}/{b}_{suffices[c]}')
        for a, b, c in prod
    ])
    paths = dl_manager.download(path_dict)

    return dict([
        (  # pylint: disable=g-complex-comprehension
            '_'.join([a, b]),
            self._generate_examples(dl_manager, paths['_'.join([a, b, 'img'])],
                                    paths['_'.join([a, b, 'latent'])], a))
        for a, b in itertools.product(['bunny', 'dragon'], ['train', 'test'])
    ])

  def _generate_examples(self, dl_manager: tfds.download.DownloadManager,
                         img_path, latent_path, label):
    """Yields examples."""
    with tf.io.gfile.GFile(latent_path, 'rb') as f:
      latents = dict(np.load(f))
    for key in latents:
      latents[key] = latents[key].astype(np.float32)
    for fname, fobj in dl_manager.iter_archive(img_path):
      idx = int(fname[-9:-4]) % 80000
      yield label + '_' + fname[-9:-4], {
          'image': fobj,
          'label': label,
          'illumination': latents['illumination'][idx],
          'pose_mat': latents['pose_mat'][idx],
          'pose_quat': latents['pose_quat'][idx],
      }
