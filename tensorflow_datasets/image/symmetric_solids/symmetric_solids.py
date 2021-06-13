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

"""symmetric_solids dataset."""

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This is a pose estimation dataset, consisting of symmetric 3D shapes where 
multiple orientations are visually indistinguishable. 
The challenge is to predict all equivalent orientations when only one 
orientation is paired with each image during training (as is the scenario for 
most pose estimation datasets). In contrast to most pose estimation datasets, 
the full set of equivalent orientations is available for evaluation.

There are eight shapes total, each rendered from 50,000 viewpoints distributed 
uniformly at random over the full space of 3D rotations.
Five of the shapes are featureless -- tetrahedron, cube, icosahedron, cone, and 
cylinder.
Of those, the three Platonic solids (tetrahedron, cube, icosahedron) are 
annotated with their 12-, 24-, and 60-fold discrete symmetries, respectively.
The cone and cylinder are annotated with their continuous symmetries discretized
 at 1 degree intervals. These symmetries are provided for evaluation; the 
 intended supervision is only a single rotation with each image.

The remaining three shapes are marked with a distinguishing feature.
There is a tetrahedron with one red-colored face, a cylinder with an off-center 
dot, and a sphere with an X capped by a dot. Whether or not the distinguishing 
feature is visible, the space of possible orientations is reduced.  We do not 
provide the set of equivalent rotations for these shapes.

Each example contains of 

- the 224x224 RGB image
- a shape index so that the dataset may be filtered by shape.  
The indices correspond to: 

  - 0 = tetrahedron
  - 1 = cube
  - 2 = icosahedron
  - 3 = cone
  - 4 = cylinder
  - 5 = marked tetrahedron
  - 6 = marked cylinder
  - 7 = marked sphere
  
- the rotation used in the rendering process, represented as a 3x3 rotation matrix
- the set of known equivalent rotations under symmetry, for evaluation.  

In the case of the three marked shapes, this is only the rendering rotation.
"""

_CITATION = """\
@inproceedings{implicitpdf2021,
  title = {Implicit Representation of Probability Distributions on the Rotation 
  Manifold},
  author = {Murphy, Kieran and Esteves, Carlos and Jampani, Varun and 
  Ramalingam, Srikumar and Makadia, Ameesh}
  booktitle = {International Conference on Machine Learning}
  year = {2021}
}
"""
_DATA_PATH = 'https://storage.googleapis.com/gresearch/implicit-pdf/symsol_dataset.zip'
_IMAGE_DIMENSIONS = (224, 224, 3)
_SHAPE_NAMES = [
    'tet',
    'cube',
    'icosa',
    'cone',
    'cyl',
    'tetX',
    'cylO',
    'sphereX',
]


class SymmetricSolids(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for symmetric_solids dataset."""

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
            'image':
                tfds.features.Image(shape=_IMAGE_DIMENSIONS, dtype=tf.uint8),
            'label_shape':
                tfds.features.ClassLabel(names=_SHAPE_NAMES),
            'rotation':
                tfds.features.Tensor(shape=(3, 3), dtype=tf.float32),
            'rotations_equivalent':
                tfds.features.Tensor(shape=(None, 3, 3), dtype=tf.float32),
        }),
        # These are returned if `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'rotation'),
        homepage='https://implicit-pdf.github.io',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted_paths = dl_manager.download_and_extract(_DATA_PATH)
    return {
        'train':
            self._generate_examples(
                images_path=extracted_paths / 'train/images',
                rotations_path=extracted_paths / 'train/rotations.npz'),
        'test':
            self._generate_examples(
                images_path=extracted_paths / 'test/images',
                rotations_path=extracted_paths / 'test/rotations.npz'),
    }

  def _generate_examples(self, images_path, rotations_path):
    """Yields examples."""
    with rotations_path.open('rb') as f:
      rotations = dict(np.load(f))
    for key in rotations:
      rotations[key] = rotations[key].astype(np.float32)
    for image_path in images_path.glob('*.png'):
      fname = image_path.name
      shape_name, image_index = fname.split('_')
      image_index = int(image_index.split('.')[0])
      shape_id = _SHAPE_NAMES.index(shape_name)
      yield fname, {
          'image': image_path,
          'label_shape': shape_id,
          'rotation': rotations[shape_name][image_index, 0],
          'rotations_equivalent': rotations[shape_name][image_index],
      }
