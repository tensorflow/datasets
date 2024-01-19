# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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
import tensorflow_datasets.public_api as tfds

_DATA_PATH = (
    'https://storage.googleapis.com/gresearch/implicit-pdf/symsol_dataset.zip'
)
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


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for symmetric_solids dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(
                shape=_IMAGE_DIMENSIONS, dtype=np.uint8
            ),
            'label_shape': tfds.features.ClassLabel(names=_SHAPE_NAMES),
            'rotation': tfds.features.Tensor(shape=(3, 3), dtype=np.float32),
            'rotations_equivalent': tfds.features.Tensor(
                shape=(None, 3, 3), dtype=np.float32
            ),
        }),
        # These are returned if `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'rotation'),
        homepage='https://implicit-pdf.github.io',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted_paths = dl_manager.download_and_extract(_DATA_PATH)
    return {
        'train': self._generate_examples(
            images_path=extracted_paths / 'train/images',
            rotations_path=extracted_paths / 'train/rotations.npz',
        ),
        'test': self._generate_examples(
            images_path=extracted_paths / 'test/images',
            rotations_path=extracted_paths / 'test/rotations.npz',
        ),
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
